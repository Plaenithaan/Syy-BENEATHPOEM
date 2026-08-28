import fontforge
import unicodedata

font = fontforge.activeFont()

if font is None:
    raise RuntimeError("No font is open")


# ============================================================
# CONFIG
# ============================================================

RANGES = [
    # Latin
    (0x0080, 0x00FF),
    (0x0100, 0x017F),
    (0x0180, 0x024F),

    # Greek
    (0x0370, 0x03FF),

    # Cyrillic
    (0x0400, 0x04FF),
    (0x0500, 0x052F),
    (0x2DE0, 0x2DFF),
    (0xA640, 0xA69F),
    (0x1C80, 0x1C8F),
]

CELL_WIDTH = 512

ACCENT_DOWN = 128

ACCENT_UP = 0 # Syy UDT
# ACCENT_UP = 64 # Syy UDS

BLWM_DOWN = 192


# ============================================================
# SPECIAL LATIN BASES
# ============================================================

DOTLESS_I = 0x0131
DOTLESS_J = 0x0237


# ============================================================
# LOWERCASE BASES THAT KEEP NORMAL ACCENT HEIGHT
# ============================================================

NO_ACCENT_LOWER = {
    0x0062,  # b
    0x0064,  # d
    0x0066,  # f
    0x0068,  # h
    0x006B,  # k
    0x006C,  # l
    0x0074,  # t
}


# ============================================================
# LOWERCASE BASES THAT ALWAYS USE LOWER BLWM
# ============================================================

BLWM_LOWER = {
    0x0067,  # g
    0x006A,  # j
    0x0070,  # p
    0x0071,  # q
    0x0079,  # y
    0x01B7,
    0x0292,
    0x0443,
    0x04E0,
    0x04E1,
}


# ============================================================
# FONTFORGE TRANSFORMS
# ============================================================

IDENTITY = (
    1, 0,
    0, 1,
    0, 0
)

# Mark:
# +512 X
# 0 Y

SHIFT_RIGHT = (
    1, 0,
    0, 1,
    512, 0
)

# Lowercase above mark:
# +512 X
# -128 Y

SHIFT_RIGHT_DOWN = (
    1, 0,
    0, 1,
    512, -ACCENT_DOWN
)

# Capital above mark:
# +512 X
# +64 Y

SHIFT_RIGHT_UP = (
    1, 0,
    0, 1,
    512, ACCENT_UP
)


# ============================================================
# HELPERS
# ============================================================

def get_glyph(cp):
    try:
        return font[cp]
    except Exception:
        return None


def get_width(cp):
    """
    Return the EXACT existing width of the base glyph.
    CELL_WIDTH is used as fallback.
    """

    glyph = get_glyph(cp)

    if glyph is not None:
        try:
            return glyph.width
        except Exception:
            pass

    return CELL_WIDTH


def is_blank(glyph):
    """
    True only if the glyph is genuinely empty.
    """

    try:
        if glyph.isWorthOutputting():
            return False
    except Exception:
        pass

    try:
        if glyph.references:
            return False
    except Exception:
        pass

    try:
        return glyph.foreground.isEmpty()
    except Exception:
        return True


def full_nfd_decomposition(cp):
    return [
        ord(ch)
        for ch in unicodedata.normalize(
            "NFD",
            chr(cp)
        )
    ]


def is_above_mark(cp):
    return unicodedata.combining(chr(cp)) in (
        230,
        232,
        233,
        234,
    )


def is_below_mark(cp):
    """
    Includes attached-below marks such as:

        U+0328 COMBINING OGONEK
        U+0327 COMBINING CEDILLA
    """

    return unicodedata.combining(chr(cp)) in (
        202,
        220,
        221,
        222,
        224,
    )


def replace_special_base(base_cp, marks):

    if not marks:
        return base_cp

    if not any(
        is_above_mark(mark_cp)
        for mark_cp in marks
    ):
        return base_cp

    if base_cp == 0x0069:
        return DOTLESS_I

    if base_cp == 0x006A:
        return DOTLESS_J

    return base_cp


def should_lower_above_mark(base_cp, marks):

    if not any(
        is_above_mark(mark_cp)
        for mark_cp in marks
    ):
        return False

    if unicodedata.category(chr(base_cp)) != "Ll":
        return False

    if base_cp in NO_ACCENT_LOWER:
        return False

    return True


# ============================================================
# GPOS
# ============================================================

def add_gpos_anchors(glyph, base_cp, marks):

    has_above = any(
        is_above_mark(mark_cp)
        for mark_cp in marks
    )

    has_below = any(
        is_below_mark(mark_cp)
        for mark_cp in marks
    )

    category = unicodedata.category(
        chr(base_cp)
    )

    # IMPORTANT:
    # GPOS X is always 512.
    #
    # Glyph width does NOT affect anchor X.
    # The mark reference is still positioned at +512.
    anchor_x = 512

    # --------------------------------------------------------
    # ABVM
    # --------------------------------------------------------

    if category == "Lu":

        if has_above:
            abvm_y = 832
        else:
            abvm_y = 640

    elif category == "Ll":

        if (
            has_above
            or base_cp in NO_ACCENT_LOWER
        ):
            abvm_y = 768
        else:
            abvm_y = 576

    else:

        abvm_y = 640

    # --------------------------------------------------------
    # BLWM
    # --------------------------------------------------------

    if (
        base_cp in BLWM_LOWER
        or has_below
    ):
        blwm_y = -BLWM_DOWN
    else:
        blwm_y = 0

    glyph.addAnchorPoint(
        "abvm",
        "base",
        anchor_x,
        abvm_y
    )

    glyph.addAnchorPoint(
        "blwm",
        "base",
        anchor_x,
        blwm_y
    )


# ============================================================
# BUILD
# ============================================================

built = []
skipped_nonblank = []
skipped_nodecomp = []
skipped_stacked = []
skipped_missing = []

for range_start, range_end in RANGES:

    for cp in range(range_start, range_end + 1):

        # ----------------------------------------------------
        # NFD
        # ----------------------------------------------------

        decomposition = full_nfd_decomposition(cp)

        if len(decomposition) <= 1:
            skipped_nodecomp.append(cp)
            continue

        original_base_cp = decomposition[0]
        marks = decomposition[1:]

        # ----------------------------------------------------
        # STACKED
        # ----------------------------------------------------

        if len(marks) > 1:
            skipped_stacked.append(cp)
            continue

        # ----------------------------------------------------
        # SPECIAL BASE
        #
        # i + above -> dotless i
        # j + above -> dotless j
        # ----------------------------------------------------

        base_cp = replace_special_base(
            original_base_cp,
            marks
        )

        # ----------------------------------------------------
        # ABOVE POSITION
        # ----------------------------------------------------

        lower_above = should_lower_above_mark(
            original_base_cp,
            marks
        )

        # ----------------------------------------------------
        # TARGET
        # ----------------------------------------------------

        glyph = get_glyph(cp)

        if glyph is None:
            glyph = font.createChar(cp)

        # ----------------------------------------------------
        # NEVER OVERWRITE
        # ----------------------------------------------------

        if not is_blank(glyph):
            skipped_nonblank.append(cp)
            continue

        # ----------------------------------------------------
        # COMPONENTS
        # ----------------------------------------------------

        component_cps = [base_cp] + marks

        components = []
        missing = False

        for component_cp in component_cps:

            component = get_glyph(component_cp)

            if component is None:
                missing = True
                break

            components.append(component)

        if missing:
            skipped_missing.append(cp)
            continue

        # ----------------------------------------------------
        # WIDTH
        # ----------------------------------------------------

        base_width = get_width(base_cp)

        # ----------------------------------------------------
        # REFERENCES
        #
        # BASE:
        #   no movement
        #
        # MARK:
        #   ALWAYS +512 X
        #
        # WIDTH DOES NOT CHANGE REFERENCE POSITION.
        # ----------------------------------------------------

        for index, component in enumerate(components):

            if index == 0:

                glyph.addReference(
                    component.glyphname,
                    IDENTITY
                )

                continue

            mark_cp = component_cps[index]

            # ------------------------------------------------
            # BELOW MARK
            #
            # Reference itself stays at Y=0.
            # GPOS BLWM controls the mark positioning.
            # ------------------------------------------------

            if is_below_mark(mark_cp):

                transform = SHIFT_RIGHT

            # ------------------------------------------------
            # LOWERCASE ABOVE
            # ------------------------------------------------

            elif lower_above:

                transform = SHIFT_RIGHT_DOWN

            # ------------------------------------------------
            # CAPITAL ABOVE
            # ------------------------------------------------

            elif (
                unicodedata.category(
                    chr(original_base_cp)
                ) == "Lu"
                and is_above_mark(mark_cp)
            ):

                transform = SHIFT_RIGHT_UP

            # ------------------------------------------------
            # NORMAL
            # ------------------------------------------------

            else:

                transform = SHIFT_RIGHT

            glyph.addReference(
                component.glyphname,
                transform
            )

        # ----------------------------------------------------
        # SET EXACT BASE WIDTH
        # ----------------------------------------------------

        glyph.width = base_width

        # ----------------------------------------------------
        # GPOS
        # ----------------------------------------------------

        add_gpos_anchors(
            glyph,
            original_base_cp,
            marks
        )

        built.append(cp)


# ============================================================
# REPORT
# ============================================================

print("")
print("========================================")
print("Accented Glyph Generation")
print("========================================")
print("")

print("Built:              %d" % len(built))
print("Skipped non-blank:  %d" % len(skipped_nonblank))
print("No decomposition:   %d" % len(skipped_nodecomp))
print("Skipped stacked:    %d" % len(skipped_stacked))
print("Missing components: %d" % len(skipped_missing))


# ============================================================
# BUILT
# ============================================================

if built:

    print("")
    print("Built:")

    for cp in built:
        print("U+%04X" % cp)


# ============================================================
# SKIPPED STACKED
# ============================================================

if skipped_stacked:

    print("")
    print("Skipped stacked accents:")

    for cp in skipped_stacked:

        decomposition = full_nfd_decomposition(cp)

        print(
            "U+%04X: %s"
            % (
                cp,
                " + ".join(
                    "U+%04X" % x
                    for x in decomposition
                )
            )
        )


# ============================================================
# MISSING COMPONENTS
# ============================================================

if skipped_missing:

    print("")
    print("Missing components:")

    for cp in skipped_missing:

        decomposition = full_nfd_decomposition(cp)

        print(
            "U+%04X: %s"
            % (
                cp,
                " + ".join(
                    "U+%04X" % x
                    for x in decomposition
                )
            )
        )


print("")
print("Done.")