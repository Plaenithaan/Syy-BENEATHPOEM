## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[2] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-consistent-family-name">opentype/family/consistent_family_name</a></summary>
    <div>







* 🔥 **FAIL** <p>3 different Font Family names were found:</p>
<ul>
<li>
<p>'Syy UDT' was found in:</p>
<ul>
<li>SyyUDT-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Syy UDS' was found in:</p>
<ul>
<li>SyyUDS-Regular.ttf (nameID 1)</li>
</ul>
</li>
<li>
<p>'Syy Flowey' was found in:</p>
<ul>
<li>SyyFlowey-Bold.ttf (nameID 1)</li>
</ul>
</li>
</ul>
 [code: inconsistent-family-name]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Each font in a family must have the same set of vertical metrics values. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-vertical-metrics">family/vertical_metrics</a></summary>
    <div>







* 🔥 **FAIL** <p>sTypoAscender is not the same across the family:
Syy UDT: 960
Syy UDS: 960
Syy Flowey Bold: 896</p>
 [code: sTypoAscender-mismatch]



* 🔥 **FAIL** <p>sTypoDescender is not the same across the family:
Syy UDT: -256
Syy UDS: -256
Syy Flowey Bold: -384</p>
 [code: sTypoDescender-mismatch]



* 🔥 **FAIL** <p>usWinAscent is not the same across the family:
Syy UDT: 960
Syy UDS: 960
Syy Flowey Bold: 896</p>
 [code: usWinAscent-mismatch]



* 🔥 **FAIL** <p>usWinDescent is not the same across the family:
Syy UDT: 256
Syy UDS: 256
Syy Flowey Bold: 384</p>
 [code: usWinDescent-mismatch]



* 🔥 **FAIL** <p>ascent is not the same across the family:
Syy UDT: 960
Syy UDS: 960
Syy Flowey Bold: 896</p>
 [code: ascent-mismatch]



* 🔥 **FAIL** <p>descent is not the same across the family:
Syy UDT: -256
Syy UDS: -256
Syy Flowey Bold: -384</p>
 [code: descent-mismatch]



</div>
</details>
</div>
</details>

<details><summary>[21] SyyUDT-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font. Please set PANOSE Proportion to 9 (monospaced)</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1912 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 626 glyphs (32.71%) have a different width. You should check the widths of: ['exclam', 'quotedbl', 'quotesingle', 'parenleft', 'parenright', 'comma', 'period', 'colon', 'semicolon', 'M', 'W', 'underscore', 'grave', 'm', 'w', 'braceleft', 'bar', 'braceright', 'exclamdown', 'acute', 'periodcentered', 'cedilla', 'AE', 'ae', 'OE', 'oe', 'Wcircumflex', 'wcircumflex', 'uni01C0', 'uni01C1', 'uni01E2', 'uni01E3', 'AEacute', 'aeacute', 'uni02B9', 'quoteleft', 'quoteright', 'quotereversed', 'uni0402', 'uni0409', 'uni040A', 'uni040B', 'uni0416', 'uni0424', 'uni0428', 'uni0429', 'uni042B', 'uni042E', 'uni0436', 'uni043C', 'uni0444', 'uni0448', 'uni0449', 'uni044B', 'uni044E', 'uni0452', 'uni0459', 'uni045A', 'uni045B', 'uni0496', 'uni0497', 'uni04C1', 'uni04C2', 'uni04DC', 'uni04DD', 'uni04F8', 'uni04F9', 'uni0E0C', 'uni0E0D', 'uni0E12', 'uni0E13', 'uni0E40', 'uni0E46', 'uni0E86', 'uni0E8E', 'uni0E91', 'uni0E92', 'uni0E93', 'uni0E97', 'uni0E9E', 'uni0E9F', 'uni0EA4', 'uni0EAB', 'uni0EC0', 'uni0EC6', 'uni0EDC', 'uni0EDD', 'uni1E3E', 'uni1E3F', 'uni1E40', 'uni1E41', 'uni1E42', 'uni1E43', 'Wgrave', 'wgrave', 'Wacute', 'wacute', 'Wdieresis', 'wdieresis', 'uni1E86', 'uni1E87', 'uni1E88', 'uni1E89', 'uni1E98', 'uni2001', 'uni2003', 'uni2004', 'uni2005', 'uni2006', 'uni2008', 'uni2009', 'uni200A', 'emdash', 'uni2015', 'uni2016', 'quotesinglbase', 'quotedblleft', 'quotedblright', 'quotedblbase', 'uni201F', 'twodotenleader', 'minute', 'uni2034', 'uni203B', 'uni203E', 'uni2103', 'uni210F', 'uni2113', 'uni212B', 'aleph', 'arrowleft', 'arrowup', 'arrowright', 'arrowdown', 'arrowboth', 'arrowupdn', 'uni2196', 'uni2197', 'uni2198', 'uni2199', 'uni21A9', 'uni21AA', 'carriagereturn', 'uni21C4', 'arrowdblleft', 'arrowdblup', 'arrowdblright', 'arrowdbldown', 'arrowdblboth', 'uni21D5', 'uni21D6', 'uni21D7', 'uni21D8', 'uni21D9', 'uni21E5', 'uni21E6', 'uni21E7', 'uni21E8', 'uni21E9', 'uni21EA', 'uni21EB', 'uni21EC', 'uni21ED', 'uni21EE', 'uni21EF', 'uni21F0', 'uni21F1', 'uni21F2', 'uni21F3', 'universal', 'existential', 'emptyset', 'gradient', 'element', 'notelement', 'suchthat', 'uni2213', 'proportional', 'infinity', 'angle', 'uni2225', 'uni2226', 'logicaland', 'logicalor', 'intersection', 'union', 'uni222C', 'therefore', 'uni2235', 'uni223D', 'uni2243', 'congruent', 'approxequal', 'uni2252', 'equivalence', 'uni2262', 'uni2266', 'uni2267', 'uni226A', 'uni226B', 'uni2276', 'uni2277', 'propersubset', 'propersuperset', 'notsubset', 'uni2285', 'reflexsubset', 'reflexsuperset', 'uni228A', 'uni228B', 'circleplus', 'uni2296', 'circlemultiply', 'perpendicular', 'uni2305', 'uni2306', 'uni2312', 'uni2318', 'uni2325', 'uni232B', 'uni2387', 'uni23CE', 'filledbox', 'H22073', 'triagup', 'uni25B3', 'uni25B6', 'uni25B7', 'triagdn', 'uni25BD', 'uni25C0', 'uni25C1', 'uni25C6', 'uni25C7', 'uni25C9', 'circle', 'uni25CE', 'H18533', 'uni25EF', 'uni2605', 'uni2606', 'female', 'male', 'uni2661', 'heart', 'uni2669', 'musicalnote', 'musicalnotedbl', 'uni266C', 'uni266D', 'uni266E', 'uni266F', 'uni26A0', 'uni2726', 'uni2727', 'uni2764', 'uni2765', 'uni2934', 'uni2935', 'uni29BF', 'uni29FA', 'uni29FB', 'uni3000', 'uni3001', 'uni3002', 'uni3003', 'uni3005', 'uni3006', 'uni3007', 'uni3008', 'uni3009', 'uni300A', 'uni300B', 'uni300C', 'uni300D', 'uni300E', 'uni300F', 'uni3010', 'uni3011', 'uni3012', 'uni3013', 'uni3014', 'uni3015', 'uni3016', 'uni3017', 'uni3018', 'uni3019', 'uni301C', 'uni301D', 'uni301E', 'uni301F', 'uni3033', 'uni3034', 'uni3035', 'uni303B', 'uni303C', 'uni303D', 'uni3041', 'uni3042', 'uni3043', 'uni3044', 'uni3045', 'uni3046', 'uni3047', 'uni3048', 'uni3049', 'uni304A', 'uni304B', 'uni304C', 'uni304D', 'uni304E', 'uni304F', 'uni3050', 'uni3051', 'uni3052', 'uni3053', 'uni3054', 'uni3055', 'uni3056', 'uni3057', 'uni3058', 'uni3059', 'uni305A', 'uni305B', 'uni305C', 'uni305D', 'uni305E', 'uni305F', 'uni3060', 'uni3061', 'uni3062', 'uni3063', 'uni3064', 'uni3065', 'uni3066', 'uni3067', 'uni3068', 'uni3069', 'uni306A', 'uni306B', 'uni306C', 'uni306D', 'uni306E', 'uni306F', 'uni3070', 'uni3071', 'uni3072', 'uni3073', 'uni3074', 'uni3075', 'uni3076', 'uni3077', 'uni3078', 'uni3079', 'uni307A', 'uni307B', 'uni307C', 'uni307D', 'uni307E', 'uni307F', 'uni3080', 'uni3081', 'uni3082', 'uni3083', 'uni3084', 'uni3085', 'uni3086', 'uni3087', 'uni3088', 'uni3089', 'uni308A', 'uni308B', 'uni308C', 'uni308D', 'uni308E', 'uni308F', 'uni3090', 'uni3091', 'uni3092', 'uni3093', 'uni3094', 'uni3095', 'uni3096', 'uni309B', 'uni309C', 'uni309D', 'uni309E', 'uni309F', 'uni30A0', 'uni30A1', 'uni30A2', 'uni30A3', 'uni30A4', 'uni30A5', 'uni30A6', 'uni30A7', 'uni30A8', 'uni30A9', 'uni30AA', 'uni30AB', 'uni30AC', 'uni30AD', 'uni30AE', 'uni30AF', 'uni30B0', 'uni30B1', 'uni30B2', 'uni30B3', 'uni30B4', 'uni30B5', 'uni30B6', 'uni30B7', 'uni30B8', 'uni30B9', 'uni30BA', 'uni30BB', 'uni30BC', 'uni30BD', 'uni30BE', 'uni30BF', 'uni30C0', 'uni30C1', 'uni30C2', 'uni30C3', 'uni30C4', 'uni30C5', 'uni30C6', 'uni30C7', 'uni30C8', 'uni30C9', 'uni30CA', 'uni30CB', 'uni30CC', 'uni30CD', 'uni30CE', 'uni30CF', 'uni30D0', 'uni30D1', 'uni30D2', 'uni30D3', 'uni30D4', 'uni30D5', 'uni30D6', 'uni30D7', 'uni30D8', 'uni30D9', 'uni30DA', 'uni30DB', 'uni30DC', 'uni30DD', 'uni30DE', 'uni30DF', 'uni30E0', 'uni30E1', 'uni30E2', 'uni30E3', 'uni30E4', 'uni30E5', 'uni30E6', 'uni30E7', 'uni30E8', 'uni30E9', 'uni30EA', 'uni30EB', 'uni30EC', 'uni30ED', 'uni30EE', 'uni30EF', 'uni30F0', 'uni30F1', 'uni30F2', 'uni30F3', 'uni30F4', 'uni30F5', 'uni30F6', 'uni30F7', 'uni30F8', 'uni30F9', 'uni30FA', 'uni30FB', 'uni30FC', 'uni30FD', 'uni30FE', 'uni30FF', 'uni31F0', 'uni31F1', 'uni31F2', 'uni31F3', 'uni31F4', 'uni31F5', 'uni31F6', 'uni31F7', 'uni31F8', 'uni31F9', 'uni31FA', 'uni31FB', 'uni31FC', 'uni31FD', 'uni31FE', 'uni31FF', 'uni33CB', 'uni4EDD', 'uniE133', 'uniE134', 'uniE139', 'uni0E0D.descless', 'uni0E24_uni0E45', 'uni0E26_uni0E45', 'uniFB00', 'uniFB01', 'uniFB02', 'uniFB03', 'uniFB04', 'uniFE45', 'uniFE46', 'uniFF01', 'uniFF02', 'uniFF03', 'uniFF04', 'uniFF05', 'uniFF06', 'uniFF07', 'uniFF08', 'uniFF09', 'uniFF0A', 'uniFF0B', 'uniFF0C', 'uniFF0D', 'uniFF0E', 'uniFF0F', 'uniFF10', 'uniFF11', 'uniFF12', 'uniFF13', 'uniFF14', 'uniFF15', 'uniFF16', 'uniFF17', 'uniFF18', 'uniFF19', 'uniFF1A', 'uniFF1B', 'uniFF1C', 'uniFF1D', 'uniFF1E', 'uniFF1F', 'uniFF20', 'uniFF21', 'uniFF22', 'uniFF23', 'uniFF24', 'uniFF25', 'uniFF26', 'uniFF27', 'uniFF28', 'uniFF29', 'uniFF2A', 'uniFF2B', 'uniFF2C', 'uniFF2D', 'uniFF2E', 'uniFF2F', 'uniFF30', 'uniFF31', 'uniFF32', 'uniFF33', 'uniFF34', 'uniFF35', 'uniFF36', 'uniFF37', 'uniFF38', 'uniFF39', 'uniFF3A', 'uniFF3B', 'uniFF3C', 'uniFF3D', 'uniFF3E', 'uniFF3F', 'uniFF40', 'uniFF41', 'uniFF42', 'uniFF43', 'uniFF44', 'uniFF45', 'uniFF46', 'uniFF47', 'uniFF48', 'uniFF49', 'uniFF4A', 'uniFF4B', 'uniFF4C', 'uniFF4D', 'uniFF4E', 'uniFF4F', 'uniFF50', 'uniFF51', 'uniFF52', 'uniFF53', 'uniFF54', 'uniFF55', 'uniFF56', 'uniFF57', 'uniFF58', 'uniFF59', 'uniFF5A', 'uniFF5B', 'uniFF5C', 'uniFF5D', 'uniFF5E', 'uniFF5F', 'uniFF60', 'uniFFE0', 'uniFFE1', 'uniFFE2', 'uniFFE3', 'uniFFE4', 'uniFFE5', 'uniFFE6', 'uniFFE9', 'uniFFEA', 'uniFFEB', 'uniFFEC', 'u1F494', 'u1FBB0', 'u1FBB2', 'u1FBB3']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>







* 🔥 **FAIL** <p>dcaron uses component uni030C.</p>
 [code: wrong-mark]



* 🔥 **FAIL** <p>tcaron uses component uni030C.</p>
 [code: wrong-mark]



* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0182: LATIN CAPITAL LETTER B WITH TOPBAR</td>
<td align="left">U+0183: LATIN SMALL LETTER B WITH TOPBAR</td>
</tr>
<tr>
<td align="left">U+026A: LATIN LETTER SMALL CAPITAL I</td>
<td align="left">U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I</td>
</tr>
<tr>
<td align="left">U+028A: LATIN SMALL LETTER UPSILON</td>
<td align="left">U+01B1: LATIN CAPITAL LETTER UPSILON</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to J when shaping the text 'ÍJ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to j when shaping the text 'íj́'</td>
<td align="left">nl_Latn (Dutch)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҷ, ҳ</td>
<td align="left">tg_Cyrl (Tajik) and tg_Cyrl (Tajik)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҳ</td>
<td align="left">uz_Cyrl (Uzbek (Cyrillic)) and uz_Cyrl (Uzbek (Cyrillic))</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ɲ, ɲ</td>
<td align="left">bm_Latn (Bambara) and dyu_Latn (Dyula)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ƴ, Ƴ</td>
<td align="left">ff_Latn (Fulah)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ƙ, Ƴ, ƴ, Ƙ</td>
<td align="left">ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EB9 when shaping the text 'ẹ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EB8 when shaping the text 'Ẹ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EB9 when shaping the text 'ẹ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EB8 when shaping the text 'Ẹ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECD when shaping the text 'ọ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECC when shaping the text 'Ọ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECD when shaping the text 'ọ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECC when shaping the text 'Ọ̀'</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҙ, ҙ, Ҫ, ҡ, ҫ, Ҡ</td>
<td align="left">ba_Cyrl (Bashkir)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҫ, Ҫ</td>
<td align="left">cv_Cyrl (Chuvash)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҝ, ҹ</td>
<td align="left">az_Cyrl (Azerbaijani (Cyrillic))</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ӏ, ӏ</td>
<td align="left">kbd_Cyrl (Kabardian), av_Cyrl (Avaric) and inh_Cyrl (Ingush)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: гӏ, чӏ, пӏ, кӏ, рхӏ, тӏ, хӏ, цӏ</td>
<td align="left">ce_Cyrl (Chechen)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҥ, ҥ</td>
<td align="left">chm_Cyrl (Mari)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҳ, ҳ</td>
<td align="left">kaa_Cyrl (Kara-Kalpak)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҕ, ҥ</td>
<td align="left">sah_Cyrl (Sakha)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ӏ, Ӏ</td>
<td align="left">ady_Cyrl (Adyghe), dar_Cyrl (Dargwa) and lez_Cyrl (Lezghian)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǥ</td>
<td align="left">fi_Latn (Finnish)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Aogonek when shaping the text 'Ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Aogonek when shaping the text 'Ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Eogonek when shaping the text 'Ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Eogonek when shaping the text 'Ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to Iogonek when shaping the text 'Į́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to Iogonek when shaping the text 'Į̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to Iogonek when shaping the text 'Į̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to J when shaping the text 'J̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to J when shaping the text 'J̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to L when shaping the text 'L̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to i when shaping the text 'i̇́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to i when shaping the text 'i̇̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to i when shaping the text 'i̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to j when shaping the text 'j̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0307 to j when shaping the text 'j̇̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to l when shaping the text 'l̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to a when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to e when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to o when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to y when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to a when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to e when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to i when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to o when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to y when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to a when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to e when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to i when shaping the text 'і́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to o when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to y when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to a when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to o when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to y when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to a when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to e when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to o when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to y when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἀ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὰ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὲ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἠ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὴ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἰ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἴ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἲ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὸ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὺ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὼ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to R when shaping the text 'R̃'</td>
<td align="left">ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECA when shaping the text 'Ị́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECA when shaping the text 'Ị̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECD when shaping the text 'ọ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECC when shaping the text 'Ọ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECD when shaping the text 'ọ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECC when shaping the text 'Ọ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EE5 when shaping the text 'ụ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EE4 when shaping the text 'Ụ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EE5 when shaping the text 'ụ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EE4 when shaping the text 'Ụ̀'</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030C to uni1EB9 when shaping the text 'ẹ̌'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030C to uni1EB8 when shaping the text 'Ẹ̌'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030C to uni1ECD when shaping the text 'ọ̌'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030C to uni1ECC when shaping the text 'Ọ̌'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to e when shaping the text 'e̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to E when shaping the text 'E̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to eacute when shaping the text 'é̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Eacute when shaping the text 'É̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to egrave when shaping the text 'è̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Egrave when shaping the text 'È̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to ecircumflex when shaping the text 'ê̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Ecircumflex when shaping the text 'Ê̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to ecaron when shaping the text 'ě̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Ecaron when shaping the text 'Ě̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to o when shaping the text 'o̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to O when shaping the text 'O̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to oacute when shaping the text 'ó̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Oacute when shaping the text 'Ó̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to ograve when shaping the text 'ò̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Ograve when shaping the text 'Ò̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to ocircumflex when shaping the text 'ô̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Ocircumflex when shaping the text 'Ô̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to uni01D2 when shaping the text 'ǒ̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to uni01D1 when shaping the text 'Ǒ̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to s when shaping the text 's̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to S when shaping the text 'S̩'</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Name table entries should not contain line-breaks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-line-breaks">googlefonts/name/line_breaks</a></summary>
    <div>







* 🔥 **FAIL** <p>Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break.</p>
 [code: line-break]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2026 the syy beneathpoem project authors (<a href="https://github.com/plaenithaan/syy-beneathpoem">https://github.com/plaenithaan/syy-beneathpoem</a>)&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font follows the Google Fonts CJK vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics">googlefonts/cjk_vertical_metrics</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2 fsSelection bit 7 must be disabled</p>
 [code: bad-fselection-bit7]



* 🔥 **FAIL** <p>OS/2.sTypoAscender is &quot;960&quot; it should be 901</p>
 [code: bad-OS/2.sTypoAscender]



* 🔥 **FAIL** <p>OS/2.sTypoDescender is &quot;-256&quot; it should be -123</p>
 [code: bad-OS/2.sTypoDescender]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0334 (U+0334), uni0335 (U+0335), uni0336 (U+0336), uni0337 (U+0337), uni0338 (U+0338), uni0358 (U+0358), uni3099 (U+3099) and uni309A (U+309A)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain chws and vchw features? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-chws-feature">cjk_chws_feature</a></summary>
    <div>







* ⚠️ **WARN** <p>chws feature not found in font. Use chws_tool (<a href="https://github.com/googlefonts/chws_tool">https://github.com/googlefonts/chws_tool</a>) to add it.</p>
 [code: missing-chws-feature]



* ⚠️ **WARN** <p>vchw feature not found in font. Use chws_tool (<a href="https://github.com/googlefonts/chws_tool">https://github.com/googlefonts/chws_tool</a>) to add it.</p>
 [code: missing-vchw-feature]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 14	Expected: 4 or 5

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: at	Contours detected: 1	Expected: 2

- Glyph name: W	Contours detected: 3	Expected: 1 or 2

- Glyph name: k	Contours detected: 3	Expected: 1 or 2

- Glyph name: w	Contours detected: 3	Expected: 1

- Glyph name: copyright	Contours detected: 12	Expected: 3

- Glyph name: registered	Contours detected: 9	Expected: 3 or 4

- Glyph name: onequarter	Contours detected: 8	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 8	Expected: 3

- Glyph name: threequarters	Contours detected: 13	Expected: 3 or 4

- Glyph name: Ntilde	Contours detected: 3	Expected: 2

- Glyph name: eth	Contours detected: 4	Expected: 2

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: uni0137	Contours detected: 4	Expected: 2 or 3

- Glyph name: kgreenlandic	Contours detected: 3	Expected: 1 or 2

- Glyph name: Lcaron	Contours detected: 3	Expected: 2

- Glyph name: lcaron	Contours detected: 3	Expected: 2

- Glyph name: Lslash	Contours detected: 3	Expected: 1

- Glyph name: lslash	Contours detected: 3	Expected: 1

- Glyph name: Nacute	Contours detected: 3	Expected: 2

- Glyph name: uni0145	Contours detected: 3	Expected: 2

- Glyph name: Ncaron	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: Wcircumflex	Contours detected: 4	Expected: 2

- Glyph name: wcircumflex	Contours detected: 4	Expected: 2

- Glyph name: uni01E3	Contours detected: 2	Expected: 4

- Glyph name: uni01E9	Contours detected: 4	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: uni01EE	Contours detected: 3	Expected: 2

- Glyph name: uni01F8	Contours detected: 3	Expected: 2

- Glyph name: aeacute	Contours detected: 2	Expected: 4

- Glyph name: uni0228	Contours detected: 2	Expected: 1

- Glyph name: uni0229	Contours detected: 3	Expected: 2

- Glyph name: uni0312	Contours detected: 2	Expected: 1

- Glyph name: uni0313	Contours detected: 2	Expected: 1

- Glyph name: uni031B	Contours detected: 2	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: N	Contours detected: 2	Expected: 1

- Glyph name: delta	Contours detected: 1	Expected: 2

- Glyph name: kappa	Contours detected: 3	Expected: 1

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

- Glyph name: phi	Contours detected: 1	Expected: 2 or 3

- Glyph name: chi	Contours detected: 3	Expected: 1

- Glyph name: omega	Contours detected: 3	Expected: 1

- Glyph name: omegatonos	Contours detected: 4	Expected: 2

- Glyph name: uni040D	Contours detected: 3	Expected: 2

- Glyph name: uni0418	Contours detected: 2	Expected: 1

- Glyph name: uni0419	Contours detected: 3	Expected: 2

- Glyph name: uni042B	Contours detected: 2	Expected: 3

- Glyph name: uni0436	Contours detected: 5	Expected: 1

- Glyph name: uni0438	Contours detected: 2	Expected: 1

- Glyph name: uni0439	Contours detected: 3	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044B	Contours detected: 2	Expected: 3

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni045D	Contours detected: 3	Expected: 2

- Glyph name: uni0497	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni04C2	Contours detected: 6	Expected: 2

- Glyph name: ae	Contours detected: 1	Expected: 3

- Glyph name: uni04DD	Contours detected: 7	Expected: 3

- Glyph name: uni01B7	Contours detected: 2	Expected: 1

- Glyph name: uni04E2	Contours detected: 3	Expected: 2

- Glyph name: uni04E3	Contours detected: 3	Expected: 2

- Glyph name: uni04E4	Contours detected: 4	Expected: 3

- Glyph name: uni04E5	Contours detected: 4	Expected: 3

- Glyph name: uni04F8	Contours detected: 4	Expected: 5

- Glyph name: uni04F9	Contours detected: 4	Expected: 5

- Glyph name: uni0E0D	Contours detected: 2	Expected: 1 or 4

- Glyph name: uni0E10	Contours detected: 2	Expected: 1 or 5

- Glyph name: uni0E1E	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E1F	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E47	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E4F	Contours detected: 3	Expected: 4

- Glyph name: uni0E55	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E5B	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni1E44	Contours detected: 3	Expected: 2

- Glyph name: uni1E46	Contours detected: 3	Expected: 2

- Glyph name: uni1E48	Contours detected: 3	Expected: 2

- Glyph name: Wgrave	Contours detected: 4	Expected: 2

- Glyph name: wgrave	Contours detected: 4	Expected: 2

- Glyph name: Wacute	Contours detected: 4	Expected: 2

- Glyph name: wacute	Contours detected: 4	Expected: 2

- Glyph name: Wdieresis	Contours detected: 5	Expected: 3

- Glyph name: wdieresis	Contours detected: 5	Expected: 3

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: perthousand	Contours detected: 18	Expected: 6 or 7

- Glyph name: fraction	Contours detected: 8	Expected: 1

- Glyph name: uni2076	Contours detected: 3	Expected: 2

- Glyph name: uni2079	Contours detected: 3	Expected: 2

- Glyph name: uni2086	Contours detected: 3	Expected: 2

- Glyph name: uni2089	Contours detected: 3	Expected: 2

- Glyph name: trademark	Contours detected: 3	Expected: 2

- Glyph name: arrowleft	Contours detected: 3	Expected: 1

- Glyph name: arrowup	Contours detected: 5	Expected: 1

- Glyph name: arrowright	Contours detected: 5	Expected: 1

- Glyph name: arrowdown	Contours detected: 5	Expected: 1

- Glyph name: arrowboth	Contours detected: 9	Expected: 1

- Glyph name: arrowupdn	Contours detected: 9	Expected: 1

- Glyph name: uni2196	Contours detected: 13	Expected: 1

- Glyph name: uni2197	Contours detected: 13	Expected: 1

- Glyph name: uni2198	Contours detected: 13	Expected: 1

- Glyph name: uni2199	Contours detected: 13	Expected: 1

- Glyph name: arrowdblright	Contours detected: 7	Expected: 1

- Glyph name: arrowdblboth	Contours detected: 12	Expected: 2

- Glyph name: uni21E5	Contours detected: 6	Expected: 2

- Glyph name: universal	Contours detected: 7	Expected: 2

- Glyph name: partialdiff	Contours detected: 6	Expected: 2

- Glyph name: emptyset	Contours detected: 8	Expected: 3

- Glyph name: Delta	Contours detected: 4	Expected: 2

- Glyph name: gradient	Contours detected: 3	Expected: 2

- Glyph name: element	Contours detected: 7	Expected: 1

- Glyph name: notelement	Contours detected: 5	Expected: 3

- Glyph name: suchthat	Contours detected: 7	Expected: 1

- Glyph name: summation	Contours detected: 8	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 6	Expected: 1

- Glyph name: proportional	Contours detected: 10	Expected: 2

- Glyph name: infinity	Contours detected: 7	Expected: 3

- Glyph name: angle	Contours detected: 9	Expected: 1

- Glyph name: uni2226	Contours detected: 4	Expected: 1

- Glyph name: logicaland	Contours detected: 7	Expected: 1

- Glyph name: logicalor	Contours detected: 9	Expected: 1

- Glyph name: intersection	Contours detected: 5	Expected: 1

- Glyph name: union	Contours detected: 7	Expected: 1

- Glyph name: integral	Contours detected: 8	Expected: 1

- Glyph name: uni222C	Contours detected: 16	Expected: 2

- Glyph name: uni223D	Contours detected: 10	Expected: 1

- Glyph name: uni2243	Contours detected: 9	Expected: 2

- Glyph name: congruent	Contours detected: 10	Expected: 3

- Glyph name: approxequal	Contours detected: 16	Expected: 2

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: uni2262	Contours detected: 3	Expected: 1

- Glyph name: lessequal	Contours detected: 9	Expected: 2

- Glyph name: greaterequal	Contours detected: 9	Expected: 2

- Glyph name: uni226A	Contours detected: 22	Expected: 2

- Glyph name: uni226B	Contours detected: 22	Expected: 2

- Glyph name: propersubset	Contours detected: 7	Expected: 1

- Glyph name: propersuperset	Contours detected: 7	Expected: 1

- Glyph name: notsubset	Contours detected: 9	Expected: 2

- Glyph name: uni2285	Contours detected: 7	Expected: 2

- Glyph name: reflexsubset	Contours detected: 6	Expected: 2

- Glyph name: reflexsuperset	Contours detected: 6	Expected: 2

- Glyph name: circleplus	Contours detected: 11	Expected: 3

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 8	Expected: 1

- Glyph name: uni2572	Contours detected: 8	Expected: 1

- Glyph name: uni2573	Contours detected: 13	Expected: 1

- Glyph name: uni25B3	Contours detected: 10	Expected: 2

- Glyph name: uni25B7	Contours detected: 12	Expected: 2

- Glyph name: uni25BD	Contours detected: 6	Expected: 2

- Glyph name: uni25C1	Contours detected: 12	Expected: 2

- Glyph name: uni25C7	Contours detected: 15	Expected: 2

- Glyph name: uni25C9	Contours detected: 9	Expected: 3

- Glyph name: circle	Contours detected: 3	Expected: 2

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: musicalnote	Contours detected: 3	Expected: 1

- Glyph name: uniFFFC	Contours detected: 25	Expected: 22

- Glyph name: Eng	Contours detected: 2	Expected: 1

- Glyph name: Lcaron	Contours detected: 3	Expected: 2

- Glyph name: Lslash	Contours detected: 3	Expected: 1

- Glyph name: N	Contours detected: 2	Expected: 1

- Glyph name: Nacute	Contours detected: 3	Expected: 2

- Glyph name: Ncaron	Contours detected: 3	Expected: 2

- Glyph name: Ntilde	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: W	Contours detected: 3	Expected: 1 or 2

- Glyph name: Wacute	Contours detected: 4	Expected: 2

- Glyph name: Wcircumflex	Contours detected: 4	Expected: 2

- Glyph name: Wdieresis	Contours detected: 5	Expected: 3

- Glyph name: Wgrave	Contours detected: 4	Expected: 2

- Glyph name: ae	Contours detected: 1	Expected: 3

- Glyph name: aeacute	Contours detected: 2	Expected: 4

- Glyph name: angle	Contours detected: 9	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: approxequal	Contours detected: 16	Expected: 2

- Glyph name: arrowboth	Contours detected: 9	Expected: 1

- Glyph name: arrowdblboth	Contours detected: 12	Expected: 2

- Glyph name: arrowdblright	Contours detected: 7	Expected: 1

- Glyph name: arrowdown	Contours detected: 5	Expected: 1

- Glyph name: arrowup	Contours detected: 5	Expected: 1

- Glyph name: arrowupdn	Contours detected: 9	Expected: 1

- Glyph name: at	Contours detected: 1	Expected: 2

- Glyph name: chi	Contours detected: 3	Expected: 1

- Glyph name: circle	Contours detected: 3	Expected: 2

- Glyph name: circleplus	Contours detected: 11	Expected: 3

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: congruent	Contours detected: 10	Expected: 3

- Glyph name: copyright	Contours detected: 12	Expected: 3

- Glyph name: delta	Contours detected: 1	Expected: 2

- Glyph name: element	Contours detected: 7	Expected: 1

- Glyph name: emptyset	Contours detected: 8	Expected: 3

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: eth	Contours detected: 4	Expected: 2

- Glyph name: fraction	Contours detected: 8	Expected: 1

- Glyph name: gradient	Contours detected: 3	Expected: 2

- Glyph name: greaterequal	Contours detected: 9	Expected: 2

- Glyph name: infinity	Contours detected: 7	Expected: 3

- Glyph name: integral	Contours detected: 8	Expected: 1

- Glyph name: intersection	Contours detected: 5	Expected: 1

- Glyph name: k	Contours detected: 3	Expected: 1 or 2

- Glyph name: kappa	Contours detected: 3	Expected: 1

- Glyph name: kgreenlandic	Contours detected: 3	Expected: 1 or 2

- Glyph name: lcaron	Contours detected: 3	Expected: 2

- Glyph name: lessequal	Contours detected: 9	Expected: 2

- Glyph name: logicaland	Contours detected: 7	Expected: 1

- Glyph name: logicalor	Contours detected: 9	Expected: 1

- Glyph name: lslash	Contours detected: 3	Expected: 1

- Glyph name: musicalnote	Contours detected: 3	Expected: 1

- Glyph name: notelement	Contours detected: 5	Expected: 3

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: notsubset	Contours detected: 9	Expected: 2

- Glyph name: omega	Contours detected: 3	Expected: 1

- Glyph name: omegatonos	Contours detected: 4	Expected: 2

- Glyph name: onehalf	Contours detected: 8	Expected: 3

- Glyph name: onequarter	Contours detected: 8	Expected: 3 or 4

- Glyph name: partialdiff	Contours detected: 6	Expected: 2

- Glyph name: percent	Contours detected: 14	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 18	Expected: 6 or 7

- Glyph name: phi	Contours detected: 1	Expected: 2 or 3

- Glyph name: propersubset	Contours detected: 7	Expected: 1

- Glyph name: propersuperset	Contours detected: 7	Expected: 1

- Glyph name: proportional	Contours detected: 10	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: radical	Contours detected: 6	Expected: 1

- Glyph name: reflexsubset	Contours detected: 6	Expected: 2

- Glyph name: reflexsuperset	Contours detected: 6	Expected: 2

- Glyph name: registered	Contours detected: 9	Expected: 3 or 4

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: suchthat	Contours detected: 7	Expected: 1

- Glyph name: summation	Contours detected: 8	Expected: 1

- Glyph name: threequarters	Contours detected: 13	Expected: 3 or 4

- Glyph name: trademark	Contours detected: 3	Expected: 2

- Glyph name: uni0137	Contours detected: 4	Expected: 2 or 3

- Glyph name: uni0145	Contours detected: 3	Expected: 2

- Glyph name: uni01B7	Contours detected: 2	Expected: 1

- Glyph name: uni01E3	Contours detected: 2	Expected: 4

- Glyph name: uni01E9	Contours detected: 4	Expected: 2

- Glyph name: uni01EE	Contours detected: 3	Expected: 2

- Glyph name: uni01F8	Contours detected: 3	Expected: 2

- Glyph name: uni0228	Contours detected: 2	Expected: 1

- Glyph name: uni0229	Contours detected: 3	Expected: 2

- Glyph name: uni0312	Contours detected: 2	Expected: 1

- Glyph name: uni0313	Contours detected: 2	Expected: 1

- Glyph name: uni031B	Contours detected: 2	Expected: 1

- Glyph name: uni03BC	Contours detected: 2	Expected: 1

- Glyph name: uni040D	Contours detected: 3	Expected: 2

- Glyph name: uni0418	Contours detected: 2	Expected: 1

- Glyph name: uni0419	Contours detected: 3	Expected: 2

- Glyph name: uni042B	Contours detected: 2	Expected: 3

- Glyph name: uni0436	Contours detected: 5	Expected: 1

- Glyph name: uni0438	Contours detected: 2	Expected: 1

- Glyph name: uni0439	Contours detected: 3	Expected: 2

- Glyph name: uni043A	Contours detected: 3	Expected: 1

- Glyph name: uni044B	Contours detected: 2	Expected: 3

- Glyph name: uni045C	Contours detected: 4	Expected: 2

- Glyph name: uni045D	Contours detected: 3	Expected: 2

- Glyph name: uni0497	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni04C2	Contours detected: 6	Expected: 2

- Glyph name: uni04DD	Contours detected: 7	Expected: 3

- Glyph name: uni04E2	Contours detected: 3	Expected: 2

- Glyph name: uni04E3	Contours detected: 3	Expected: 2

- Glyph name: uni04E4	Contours detected: 4	Expected: 3

- Glyph name: uni04E5	Contours detected: 4	Expected: 3

- Glyph name: uni04F8	Contours detected: 4	Expected: 5

- Glyph name: uni04F9	Contours detected: 4	Expected: 5

- Glyph name: uni0E0D	Contours detected: 2	Expected: 1 or 4

- Glyph name: uni0E10	Contours detected: 2	Expected: 1 or 5

- Glyph name: uni0E1E	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E1F	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E47	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E4F	Contours detected: 3	Expected: 4

- Glyph name: uni0E55	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E5B	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni1E44	Contours detected: 3	Expected: 2

- Glyph name: uni1E46	Contours detected: 3	Expected: 2

- Glyph name: uni1E48	Contours detected: 3	Expected: 2

- Glyph name: uni2196	Contours detected: 13	Expected: 1

- Glyph name: uni2197	Contours detected: 13	Expected: 1

- Glyph name: uni2198	Contours detected: 13	Expected: 1

- Glyph name: uni2199	Contours detected: 13	Expected: 1

- Glyph name: uni21E5	Contours detected: 6	Expected: 2

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni2226	Contours detected: 4	Expected: 1

- Glyph name: uni222C	Contours detected: 16	Expected: 2

- Glyph name: uni223D	Contours detected: 10	Expected: 1

- Glyph name: uni2243	Contours detected: 9	Expected: 2

- Glyph name: uni2262	Contours detected: 3	Expected: 1

- Glyph name: uni226A	Contours detected: 22	Expected: 2

- Glyph name: uni226B	Contours detected: 22	Expected: 2

- Glyph name: uni2285	Contours detected: 7	Expected: 2

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 8	Expected: 1

- Glyph name: uni2572	Contours detected: 8	Expected: 1

- Glyph name: uni2573	Contours detected: 13	Expected: 1

- Glyph name: uni25B3	Contours detected: 10	Expected: 2

- Glyph name: uni25B7	Contours detected: 12	Expected: 2

- Glyph name: uni25BD	Contours detected: 6	Expected: 2

- Glyph name: uni25C1	Contours detected: 12	Expected: 2

- Glyph name: uni25C7	Contours detected: 15	Expected: 2

- Glyph name: uni25C9	Contours detected: 9	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uniFFFC	Contours detected: 25	Expected: 22

- Glyph name: union	Contours detected: 7	Expected: 1

- Glyph name: universal	Contours detected: 7	Expected: 2

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: w	Contours detected: 3	Expected: 1

- Glyph name: wacute	Contours detected: 4	Expected: 2

- Glyph name: wcircumflex	Contours detected: 4	Expected: 2

- Glyph name: wdieresis	Contours detected: 5	Expected: 3

- Glyph name: wgrave	Contours detected: 4	Expected: 2
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos-kerning-info">gpos_kerning_info</a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 1024 among a set of 29 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 512:
logicalnot, notequal, less, greaterequal, divide, plus, greater, multiply, lessequal, equal, minus, plusminus</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* Aogonek (U+0104): L&lt;&lt;448.0,0.0&gt;--&lt;320.0,0.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- NULL

- nonmarkingreturn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, cherokee, math</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: elbasan, glagolitic, coptic, gothic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, old-permic, canadian-aboriginal, tifinagh, coptic, malayalam, tai-le, todhri, math, duployan, syriac</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030E COMBINING DOUBLE VERTICAL LINE ABOVE: try adding ethiopic</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: todhri, coptic</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0314 COMBINING REVERSED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031A COMBINING LEFT ANGLE ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032A COMBINING BRIDGE BELOW: not included in any glyphset definition</li>
<li>U+032B COMBINING INVERTED DOUBLE ARCH BELOW: not included in any glyphset definition</li>
<li>U+032C COMBINING CARON BELOW: try adding math</li>
<li>U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding one of: syriac, sunuwar</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, cherokee, math</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0E83 : not included in any glyphset definition</li>
<li>U+0E85 : not included in any glyphset definition</li>
<li>U+0EA4 : not included in any glyphset definition</li>
<li>U+0EA6 : not included in any glyphset definition</li>
<li>U+2003 EM SPACE: try adding nushu</li>
<li>U+2010 HYPHEN: try adding one of: hebrew, kayah-li, syloti-nagri, sundanese, coptic, kaithi, sora-sompeng, kharoshthi, lisu, arabic, armenian, cham, yi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2034 TRIPLE PRIME: try adding math</li>
<li>U+203B REFERENCE MARK: not included in any glyphset definition</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2103 DEGREE CELSIUS: try adding math</li>
<li>U+210F PLANCK CONSTANT OVER TWO PI: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2127 INVERTED OHM SIGN: try adding math</li>
<li>U+212B ANGSTROM SIGN: try adding math</li>
<li>U+2135 ALEF SYMBOL: try adding math</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math</li>
<li>U+21C4 RIGHTWARDS ARROW OVER LEFTWARDS ARROW: try adding math</li>
<li>U+21D0 LEFTWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D1 UPWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D2 RIGHTWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D3 DOWNWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D4 LEFT RIGHT DOUBLE ARROW: try adding math</li>
<li>U+21D5 UP DOWN DOUBLE ARROW: try adding math</li>
<li>U+21D6 NORTH WEST DOUBLE ARROW: try adding math</li>
<li>U+21D7 NORTH EAST DOUBLE ARROW: try adding math</li>
<li>U+21D8 SOUTH EAST DOUBLE ARROW: try adding math</li>
<li>U+21D9 SOUTH WEST DOUBLE ARROW: try adding math</li>
<li>U+21E5 RIGHTWARDS ARROW TO BAR: try adding math</li>
<li>U+21E6 LEFTWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E8 RIGHTWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E9 DOWNWARDS WHITE ARROW: try adding symbols</li>
<li>U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols</li>
<li>U+21EB UPWARDS WHITE ARROW ON PEDESTAL: try adding symbols</li>
<li>U+21EC UPWARDS WHITE ARROW ON PEDESTAL WITH HORIZONTAL BAR: try adding symbols</li>
<li>U+21ED UPWARDS WHITE ARROW ON PEDESTAL WITH VERTICAL BAR: try adding symbols</li>
<li>U+21EE UPWARDS WHITE DOUBLE ARROW: try adding symbols</li>
<li>U+21EF UPWARDS WHITE DOUBLE ARROW ON PEDESTAL: try adding symbols</li>
<li>U+21F0 RIGHTWARDS WHITE ARROW FROM WALL: try adding symbols</li>
<li>U+21F1 NORTH WEST ARROW TO CORNER: try adding math</li>
<li>U+21F2 SOUTH EAST ARROW TO CORNER: try adding math</li>
<li>U+21F3 UP DOWN WHITE ARROW: try adding symbols</li>
<li>U+2200 FOR ALL: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2203 THERE EXISTS: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+2207 NABLA: try adding math</li>
<li>U+2208 ELEMENT OF: try adding math</li>
<li>U+2209 NOT AN ELEMENT OF: try adding math</li>
<li>U+220B CONTAINS AS MEMBER: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2213 MINUS-OR-PLUS SIGN: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, tai-tham, yi, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221D PROPORTIONAL TO: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2220 ANGLE: try adding math</li>
<li>U+2225 PARALLEL TO: try adding math</li>
<li>U+2226 NOT PARALLEL TO: try adding math</li>
<li>U+2227 LOGICAL AND: try adding math</li>
<li>U+2228 LOGICAL OR: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+222C DOUBLE INTEGRAL: try adding math</li>
<li>U+2234 THEREFORE: try adding math</li>
<li>U+2235 BECAUSE: try adding math</li>
<li>U+223D REVERSED TILDE: try adding math</li>
<li>U+2243 ASYMPTOTICALLY EQUAL TO: try adding math</li>
<li>U+2245 APPROXIMATELY EQUAL TO: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2252 APPROXIMATELY EQUAL TO OR THE IMAGE OF: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2262 NOT IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2266 LESS-THAN OVER EQUAL TO: try adding math</li>
<li>U+2267 GREATER-THAN OVER EQUAL TO: try adding math</li>
<li>U+226A MUCH LESS-THAN: try adding math</li>
<li>U+226B MUCH GREATER-THAN: try adding math</li>
<li>U+2276 LESS-THAN OR GREATER-THAN: try adding math</li>
<li>U+2277 GREATER-THAN OR LESS-THAN: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+2284 NOT A SUBSET OF: try adding math</li>
<li>U+2285 NOT A SUPERSET OF: try adding math</li>
<li>U+2286 SUBSET OF OR EQUAL TO: try adding math</li>
<li>U+2287 SUPERSET OF OR EQUAL TO: try adding math</li>
<li>U+228A SUBSET OF WITH NOT EQUAL TO: try adding math</li>
<li>U+228B SUPERSET OF WITH NOT EQUAL TO: try adding math</li>
<li>U+2295 CIRCLED PLUS: try adding math</li>
<li>U+2296 CIRCLED MINUS: try adding math</li>
<li>U+2297 CIRCLED TIMES: try adding math</li>
<li>U+22A5 UP TACK: try adding math</li>
<li>U+2305 PROJECTIVE: try adding symbols</li>
<li>U+2306 PERSPECTIVE: try adding symbols</li>
<li>U+2312 ARC: try adding symbols</li>
<li>U+2318 PLACE OF INTEREST SIGN: try adding symbols</li>
<li>U+2325 OPTION KEY: try adding symbols</li>
<li>U+232B ERASE TO THE LEFT: try adding symbols</li>
<li>U+2387 ALTERNATIVE KEY SYMBOL: try adding symbols</li>
<li>U+23CE RETURN SYMBOL: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25C9 FISHEYE: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E1 LOWER HALF CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+25EF LARGE CIRCLE: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2669 QUARTER NOTE: try adding one of: music, symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
<li>U+266B BEAMED EIGHTH NOTES: try adding one of: music, symbols</li>
<li>U+266C BEAMED SIXTEENTH NOTES: try adding one of: music, symbols</li>
<li>U+266D MUSIC FLAT SIGN: try adding one of: music, symbols, math</li>
<li>U+266E MUSIC NATURAL SIGN: try adding one of: music, symbols, math</li>
<li>U+266F MUSIC SHARP SIGN: try adding one of: music, symbols, math</li>
<li>U+26A0 WARNING SIGN: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2765 ROTATED HEAVY BLACK HEART BULLET: try adding symbols</li>
<li>U+2919 LEFTWARDS ARROW-TAIL: try adding math</li>
<li>U+2934 ARROW POINTING RIGHTWARDS THEN CURVING UPWARDS: try adding math</li>
<li>U+2935 ARROW POINTING RIGHTWARDS THEN CURVING DOWNWARDS: try adding math</li>
<li>U+29BF CIRCLED BULLET: try adding one of: symbols, math</li>
<li>U+29FA DOUBLE PLUS: try adding math</li>
<li>U+29FB TRIPLE PLUS: try adding math</li>
<li>U+3000 IDEOGRAPHIC SPACE: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, nushu, yi</li>
<li>U+3001 IDEOGRAPHIC COMMA: try adding one of: japanese, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3002 IDEOGRAPHIC FULL STOP: try adding one of: japanese, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, nushu, yi</li>
<li>U+3003 DITTO MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3005 IDEOGRAPHIC ITERATION MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3006 IDEOGRAPHIC CLOSING MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+3007 IDEOGRAPHIC NUMBER ZERO: try adding one of: phags-pa, chinese-simplified, japanese</li>
<li>U+3008 LEFT ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3009 RIGHT ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300A LEFT DOUBLE ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, lisu, phags-pa, yi</li>
<li>U+300B RIGHT DOUBLE ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, lisu, phags-pa, yi</li>
<li>U+300C LEFT CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300D RIGHT CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300E LEFT WHITE CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300F RIGHT WHITE CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3010 LEFT BLACK LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3011 RIGHT BLACK LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3012 POSTAL MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3013 GETA MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3014 LEFT TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3015 RIGHT TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3016 LEFT WHITE LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3017 RIGHT WHITE LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3018 LEFT WHITE TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3019 RIGHT WHITE TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+301C WAVE DASH: try adding japanese</li>
<li>U+301D REVERSED DOUBLE PRIME QUOTATION MARK: try adding one of: chinese-traditional, chinese-simplified, chinese-hongkong</li>
<li>U+301E DOUBLE PRIME QUOTATION MARK: try adding one of: chinese-traditional, chinese-simplified, chinese-hongkong</li>
<li>U+301F LOW DOUBLE PRIME QUOTATION MARK: not included in any glyphset definition</li>
<li>U+3033 VERTICAL KANA REPEAT MARK UPPER HALF: not included in any glyphset definition</li>
<li>U+3034 VERTICAL KANA REPEAT WITH VOICED SOUND MARK UPPER HALF: not included in any glyphset definition</li>
<li>U+3035 VERTICAL KANA REPEAT MARK LOWER HALF: not included in any glyphset definition</li>
<li>U+303B VERTICAL IDEOGRAPHIC ITERATION MARK: not included in any glyphset definition</li>
<li>U+303C MASU MARK: not included in any glyphset definition</li>
<li>U+303D PART ALTERNATION MARK: not included in any glyphset definition</li>
<li>U+3041 HIRAGANA LETTER SMALL A: try adding one of: chinese-simplified, japanese</li>
<li>U+3042 HIRAGANA LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+3043 HIRAGANA LETTER SMALL I: try adding one of: chinese-simplified, japanese</li>
<li>U+3044 HIRAGANA LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+3045 HIRAGANA LETTER SMALL U: try adding one of: chinese-simplified, japanese</li>
<li>U+3046 HIRAGANA LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+3047 HIRAGANA LETTER SMALL E: try adding one of: chinese-simplified, japanese</li>
<li>U+3048 HIRAGANA LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+3049 HIRAGANA LETTER SMALL O: try adding one of: chinese-simplified, japanese</li>
<li>U+304A HIRAGANA LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+304B HIRAGANA LETTER KA: try adding one of: chinese-simplified, japanese</li>
<li>U+304C HIRAGANA LETTER GA: try adding one of: chinese-simplified, japanese</li>
<li>U+304D HIRAGANA LETTER KI: try adding one of: chinese-simplified, japanese</li>
<li>U+304E HIRAGANA LETTER GI: try adding one of: chinese-simplified, japanese</li>
<li>U+304F HIRAGANA LETTER KU: try adding one of: chinese-simplified, japanese</li>
<li>U+3050 HIRAGANA LETTER GU: try adding one of: chinese-simplified, japanese</li>
<li>U+3051 HIRAGANA LETTER KE: try adding one of: chinese-simplified, japanese</li>
<li>U+3052 HIRAGANA LETTER GE: try adding one of: chinese-simplified, japanese</li>
<li>U+3053 HIRAGANA LETTER KO: try adding one of: chinese-simplified, japanese</li>
<li>U+3054 HIRAGANA LETTER GO: try adding one of: chinese-simplified, japanese</li>
<li>U+3055 HIRAGANA LETTER SA: try adding one of: chinese-simplified, japanese</li>
<li>U+3056 HIRAGANA LETTER ZA: try adding one of: chinese-simplified, japanese</li>
<li>U+3057 HIRAGANA LETTER SI: try adding one of: chinese-simplified, japanese</li>
<li>U+3058 HIRAGANA LETTER ZI: try adding one of: chinese-simplified, japanese</li>
<li>U+3059 HIRAGANA LETTER SU: try adding one of: chinese-simplified, japanese</li>
<li>U+305A HIRAGANA LETTER ZU: try adding one of: chinese-simplified, japanese</li>
<li>U+305B HIRAGANA LETTER SE: try adding one of: chinese-simplified, japanese</li>
<li>U+305C HIRAGANA LETTER ZE: try adding one of: chinese-simplified, japanese</li>
<li>U+305D HIRAGANA LETTER SO: try adding one of: chinese-simplified, japanese</li>
<li>U+305E HIRAGANA LETTER ZO: try adding one of: chinese-simplified, japanese</li>
<li>U+305F HIRAGANA LETTER TA: try adding one of: chinese-simplified, japanese</li>
<li>U+3060 HIRAGANA LETTER DA: try adding one of: chinese-simplified, japanese</li>
<li>U+3061 HIRAGANA LETTER TI: try adding one of: chinese-simplified, japanese</li>
<li>U+3062 HIRAGANA LETTER DI: try adding one of: chinese-simplified, japanese</li>
<li>U+3063 HIRAGANA LETTER SMALL TU: try adding one of: chinese-simplified, japanese</li>
<li>U+3064 HIRAGANA LETTER TU: try adding one of: chinese-simplified, japanese</li>
<li>U+3065 HIRAGANA LETTER DU: try adding one of: chinese-simplified, japanese</li>
<li>U+3066 HIRAGANA LETTER TE: try adding one of: chinese-simplified, japanese</li>
<li>U+3067 HIRAGANA LETTER DE: try adding one of: chinese-simplified, japanese</li>
<li>U+3068 HIRAGANA LETTER TO: try adding one of: chinese-simplified, japanese</li>
<li>U+3069 HIRAGANA LETTER DO: try adding one of: chinese-simplified, japanese</li>
<li>U+306A HIRAGANA LETTER NA: try adding one of: chinese-simplified, japanese</li>
<li>U+306B HIRAGANA LETTER NI: try adding one of: chinese-simplified, japanese</li>
<li>U+306C HIRAGANA LETTER NU: try adding one of: chinese-simplified, japanese</li>
<li>U+306D HIRAGANA LETTER NE: try adding one of: chinese-simplified, japanese</li>
<li>U+306E HIRAGANA LETTER NO: try adding one of: chinese-simplified, japanese</li>
<li>U+306F HIRAGANA LETTER HA: try adding one of: chinese-simplified, japanese</li>
<li>U+3070 HIRAGANA LETTER BA: try adding one of: chinese-simplified, japanese</li>
<li>U+3071 HIRAGANA LETTER PA: try adding one of: chinese-simplified, japanese</li>
<li>U+3072 HIRAGANA LETTER HI: try adding one of: chinese-simplified, japanese</li>
<li>U+3073 HIRAGANA LETTER BI: try adding one of: chinese-simplified, japanese</li>
<li>U+3074 HIRAGANA LETTER PI: try adding one of: chinese-simplified, japanese</li>
<li>U+3075 HIRAGANA LETTER HU: try adding one of: chinese-simplified, japanese</li>
<li>U+3076 HIRAGANA LETTER BU: try adding one of: chinese-simplified, japanese</li>
<li>U+3077 HIRAGANA LETTER PU: try adding one of: chinese-simplified, japanese</li>
<li>U+3078 HIRAGANA LETTER HE: try adding one of: chinese-simplified, japanese</li>
<li>U+3079 HIRAGANA LETTER BE: try adding one of: chinese-simplified, japanese</li>
<li>U+307A HIRAGANA LETTER PE: try adding one of: chinese-simplified, japanese</li>
<li>U+307B HIRAGANA LETTER HO: try adding one of: chinese-simplified, japanese</li>
<li>U+307C HIRAGANA LETTER BO: try adding one of: chinese-simplified, japanese</li>
<li>U+307D HIRAGANA LETTER PO: try adding one of: chinese-simplified, japanese</li>
<li>U+307E HIRAGANA LETTER MA: try adding one of: chinese-simplified, japanese</li>
<li>U+307F HIRAGANA LETTER MI: try adding one of: chinese-simplified, japanese</li>
<li>U+3080 HIRAGANA LETTER MU: try adding one of: chinese-simplified, japanese</li>
<li>U+3081 HIRAGANA LETTER ME: try adding one of: chinese-simplified, japanese</li>
<li>U+3082 HIRAGANA LETTER MO: try adding one of: chinese-simplified, japanese</li>
<li>U+3083 HIRAGANA LETTER SMALL YA: try adding one of: chinese-simplified, japanese</li>
<li>U+3084 HIRAGANA LETTER YA: try adding one of: chinese-simplified, japanese</li>
<li>U+3085 HIRAGANA LETTER SMALL YU: try adding one of: chinese-simplified, japanese</li>
<li>U+3086 HIRAGANA LETTER YU: try adding one of: chinese-simplified, japanese</li>
<li>U+3087 HIRAGANA LETTER SMALL YO: try adding one of: chinese-simplified, japanese</li>
<li>U+3088 HIRAGANA LETTER YO: try adding one of: chinese-simplified, japanese</li>
<li>U+3089 HIRAGANA LETTER RA: try adding one of: chinese-simplified, japanese</li>
<li>U+308A HIRAGANA LETTER RI: try adding one of: chinese-simplified, japanese</li>
<li>U+308B HIRAGANA LETTER RU: try adding one of: chinese-simplified, japanese</li>
<li>U+308C HIRAGANA LETTER RE: try adding one of: chinese-simplified, japanese</li>
<li>U+308D HIRAGANA LETTER RO: try adding one of: chinese-simplified, japanese</li>
<li>U+308E HIRAGANA LETTER SMALL WA: try adding one of: chinese-simplified, japanese</li>
<li>U+308F HIRAGANA LETTER WA: try adding one of: chinese-simplified, japanese</li>
<li>U+3090 HIRAGANA LETTER WI: try adding one of: chinese-simplified, japanese</li>
<li>U+3091 HIRAGANA LETTER WE: try adding one of: chinese-simplified, japanese</li>
<li>U+3092 HIRAGANA LETTER WO: try adding one of: chinese-simplified, japanese</li>
<li>U+3093 HIRAGANA LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+3094 HIRAGANA LETTER VU: try adding one of: chinese-simplified, japanese</li>
<li>U+3095 HIRAGANA LETTER SMALL KA: try adding one of: chinese-simplified, japanese</li>
<li>U+3096 HIRAGANA LETTER SMALL KE: try adding one of: chinese-simplified, japanese</li>
<li>U+3099 COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309A COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309B KATAKANA-HIRAGANA VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309C KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309D HIRAGANA ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+309E HIRAGANA VOICED ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+309F HIRAGANA DIGRAPH YORI: try adding one of: chinese-simplified, japanese</li>
<li>U+30A0 KATAKANA-HIRAGANA DOUBLE HYPHEN: try adding one of: chinese-simplified, japanese</li>
<li>U+30A1 KATAKANA LETTER SMALL A: try adding one of: chinese-simplified, japanese</li>
<li>U+30A2 KATAKANA LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+30A3 KATAKANA LETTER SMALL I: try adding one of: chinese-simplified, japanese</li>
<li>U+30A4 KATAKANA LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+30A5 KATAKANA LETTER SMALL U: try adding one of: chinese-simplified, japanese</li>
<li>U+30A6 KATAKANA LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+30A7 KATAKANA LETTER SMALL E: try adding one of: chinese-simplified, japanese</li>
<li>U+30A8 KATAKANA LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+30A9 KATAKANA LETTER SMALL O: try adding one of: chinese-simplified, japanese</li>
<li>U+30AA KATAKANA LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+30AB KATAKANA LETTER KA: try adding one of: chinese-simplified, japanese</li>
<li>U+30AC KATAKANA LETTER GA: try adding one of: chinese-simplified, japanese</li>
<li>U+30AD KATAKANA LETTER KI: try adding one of: chinese-simplified, japanese</li>
<li>U+30AE KATAKANA LETTER GI: try adding one of: chinese-simplified, japanese</li>
<li>U+30AF KATAKANA LETTER KU: try adding one of: chinese-simplified, japanese</li>
<li>U+30B0 KATAKANA LETTER GU: try adding one of: chinese-simplified, japanese</li>
<li>U+30B1 KATAKANA LETTER KE: try adding one of: chinese-simplified, japanese</li>
<li>U+30B2 KATAKANA LETTER GE: try adding one of: chinese-simplified, japanese</li>
<li>U+30B3 KATAKANA LETTER KO: try adding one of: chinese-simplified, japanese</li>
<li>U+30B4 KATAKANA LETTER GO: try adding one of: chinese-simplified, japanese</li>
<li>U+30B5 KATAKANA LETTER SA: try adding one of: chinese-simplified, japanese</li>
<li>U+30B6 KATAKANA LETTER ZA: try adding one of: chinese-simplified, japanese</li>
<li>U+30B7 KATAKANA LETTER SI: try adding one of: chinese-simplified, japanese</li>
<li>U+30B8 KATAKANA LETTER ZI: try adding one of: chinese-simplified, japanese</li>
<li>U+30B9 KATAKANA LETTER SU: try adding one of: chinese-simplified, japanese</li>
<li>U+30BA KATAKANA LETTER ZU: try adding one of: chinese-simplified, japanese</li>
<li>U+30BB KATAKANA LETTER SE: try adding one of: chinese-simplified, japanese</li>
<li>U+30BC KATAKANA LETTER ZE: try adding one of: chinese-simplified, japanese</li>
<li>U+30BD KATAKANA LETTER SO: try adding one of: chinese-simplified, japanese</li>
<li>U+30BE KATAKANA LETTER ZO: try adding one of: chinese-simplified, japanese</li>
<li>U+30BF KATAKANA LETTER TA: try adding one of: chinese-simplified, japanese</li>
<li>U+30C0 KATAKANA LETTER DA: try adding one of: chinese-simplified, japanese</li>
<li>U+30C1 KATAKANA LETTER TI: try adding one of: chinese-simplified, japanese</li>
<li>U+30C2 KATAKANA LETTER DI: try adding one of: chinese-simplified, japanese</li>
<li>U+30C3 KATAKANA LETTER SMALL TU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C4 KATAKANA LETTER TU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C5 KATAKANA LETTER DU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C6 KATAKANA LETTER TE: try adding one of: chinese-simplified, japanese</li>
<li>U+30C7 KATAKANA LETTER DE: try adding one of: chinese-simplified, japanese</li>
<li>U+30C8 KATAKANA LETTER TO: try adding one of: chinese-simplified, japanese</li>
<li>U+30C9 KATAKANA LETTER DO: try adding one of: chinese-simplified, japanese</li>
<li>U+30CA KATAKANA LETTER NA: try adding one of: chinese-simplified, japanese</li>
<li>U+30CB KATAKANA LETTER NI: try adding one of: chinese-simplified, japanese</li>
<li>U+30CC KATAKANA LETTER NU: try adding one of: chinese-simplified, japanese</li>
<li>U+30CD KATAKANA LETTER NE: try adding one of: chinese-simplified, japanese</li>
<li>U+30CE KATAKANA LETTER NO: try adding one of: chinese-simplified, japanese</li>
<li>U+30CF KATAKANA LETTER HA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D0 KATAKANA LETTER BA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D1 KATAKANA LETTER PA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D2 KATAKANA LETTER HI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D3 KATAKANA LETTER BI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D4 KATAKANA LETTER PI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D5 KATAKANA LETTER HU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D6 KATAKANA LETTER BU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D7 KATAKANA LETTER PU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D8 KATAKANA LETTER HE: try adding one of: chinese-simplified, japanese</li>
<li>U+30D9 KATAKANA LETTER BE: try adding one of: chinese-simplified, japanese</li>
<li>U+30DA KATAKANA LETTER PE: try adding one of: chinese-simplified, japanese</li>
<li>U+30DB KATAKANA LETTER HO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DC KATAKANA LETTER BO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DD KATAKANA LETTER PO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DE KATAKANA LETTER MA: try adding one of: chinese-simplified, japanese</li>
<li>U+30DF KATAKANA LETTER MI: try adding one of: chinese-simplified, japanese</li>
<li>U+30E0 KATAKANA LETTER MU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E1 KATAKANA LETTER ME: try adding one of: chinese-simplified, japanese</li>
<li>U+30E2 KATAKANA LETTER MO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E3 KATAKANA LETTER SMALL YA: try adding one of: chinese-simplified, japanese</li>
<li>U+30E4 KATAKANA LETTER YA: try adding one of: chinese-simplified, japanese</li>
<li>U+30E5 KATAKANA LETTER SMALL YU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E6 KATAKANA LETTER YU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E7 KATAKANA LETTER SMALL YO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E8 KATAKANA LETTER YO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E9 KATAKANA LETTER RA: try adding one of: chinese-simplified, japanese</li>
<li>U+30EA KATAKANA LETTER RI: try adding one of: chinese-simplified, japanese</li>
<li>U+30EB KATAKANA LETTER RU: try adding one of: chinese-simplified, japanese</li>
<li>U+30EC KATAKANA LETTER RE: try adding one of: chinese-simplified, japanese</li>
<li>U+30ED KATAKANA LETTER RO: try adding one of: chinese-simplified, japanese</li>
<li>U+30EE KATAKANA LETTER SMALL WA: try adding one of: chinese-simplified, japanese</li>
<li>U+30EF KATAKANA LETTER WA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F0 KATAKANA LETTER WI: try adding one of: chinese-simplified, japanese</li>
<li>U+30F1 KATAKANA LETTER WE: try adding one of: chinese-simplified, japanese</li>
<li>U+30F2 KATAKANA LETTER WO: try adding one of: chinese-simplified, japanese</li>
<li>U+30F3 KATAKANA LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+30F4 KATAKANA LETTER VU: try adding one of: chinese-simplified, japanese</li>
<li>U+30F5 KATAKANA LETTER SMALL KA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F6 KATAKANA LETTER SMALL KE: try adding one of: chinese-simplified, japanese</li>
<li>U+30F7 KATAKANA LETTER VA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F8 KATAKANA LETTER VI: try adding one of: chinese-simplified, japanese</li>
<li>U+30F9 KATAKANA LETTER VE: try adding one of: chinese-simplified, japanese</li>
<li>U+30FA KATAKANA LETTER VO: try adding one of: chinese-simplified, japanese</li>
<li>U+30FB KATAKANA MIDDLE DOT: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+30FC KATAKANA-HIRAGANA PROLONGED SOUND MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FD KATAKANA ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FE KATAKANA VOICED ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FF KATAKANA DIGRAPH KOTO: try adding one of: chinese-simplified, japanese</li>
<li>U+31F0 KATAKANA LETTER SMALL KU: not included in any glyphset definition</li>
<li>U+31F1 KATAKANA LETTER SMALL SI: not included in any glyphset definition</li>
<li>U+31F2 KATAKANA LETTER SMALL SU: not included in any glyphset definition</li>
<li>U+31F3 KATAKANA LETTER SMALL TO: not included in any glyphset definition</li>
<li>U+31F4 KATAKANA LETTER SMALL NU: not included in any glyphset definition</li>
<li>U+31F5 KATAKANA LETTER SMALL HA: not included in any glyphset definition</li>
<li>U+31F6 KATAKANA LETTER SMALL HI: not included in any glyphset definition</li>
<li>U+31F7 KATAKANA LETTER SMALL HU: not included in any glyphset definition</li>
<li>U+31F8 KATAKANA LETTER SMALL HE: not included in any glyphset definition</li>
<li>U+31F9 KATAKANA LETTER SMALL HO: not included in any glyphset definition</li>
<li>U+31FA KATAKANA LETTER SMALL MU: not included in any glyphset definition</li>
<li>U+31FB KATAKANA LETTER SMALL RA: not included in any glyphset definition</li>
<li>U+31FC KATAKANA LETTER SMALL RI: not included in any glyphset definition</li>
<li>U+31FD KATAKANA LETTER SMALL RU: not included in any glyphset definition</li>
<li>U+31FE KATAKANA LETTER SMALL RE: not included in any glyphset definition</li>
<li>U+31FF KATAKANA LETTER SMALL RO: not included in any glyphset definition</li>
<li>U+33CB SQUARE HP: not included in any glyphset definition</li>
<li>U+4EDD CJK UNIFIED IDEOGRAPH-4EDD: try adding one of: chinese-traditional, japanese, chinese-simplified, chinese-hongkong</li>
<li>U+E133 : not included in any glyphset definition</li>
<li>U+E134 : not included in any glyphset definition</li>
<li>U+E139 : not included in any glyphset definition</li>
<li>U+E140 : not included in any glyphset definition</li>
<li>U+F001 : not included in any glyphset definition</li>
<li>U+F002 : not included in any glyphset definition</li>
<li>U+F003 : not included in any glyphset definition</li>
<li>U+F700 : not included in any glyphset definition</li>
<li>U+F701 : not included in any glyphset definition</li>
<li>U+F702 : not included in any glyphset definition</li>
<li>U+F703 : not included in any glyphset definition</li>
<li>U+F704 : not included in any glyphset definition</li>
<li>U+F705 : not included in any glyphset definition</li>
<li>U+F706 : not included in any glyphset definition</li>
<li>U+F707 : not included in any glyphset definition</li>
<li>U+F708 : not included in any glyphset definition</li>
<li>U+F709 : not included in any glyphset definition</li>
<li>U+F70A : not included in any glyphset definition</li>
<li>U+F70B : not included in any glyphset definition</li>
<li>U+F70C : not included in any glyphset definition</li>
<li>U+F70D : not included in any glyphset definition</li>
<li>U+F70E : not included in any glyphset definition</li>
<li>U+F70F : not included in any glyphset definition</li>
<li>U+F710 : not included in any glyphset definition</li>
<li>U+F711 : not included in any glyphset definition</li>
<li>U+F712 : not included in any glyphset definition</li>
<li>U+F713 : not included in any glyphset definition</li>
<li>U+F714 : not included in any glyphset definition</li>
<li>U+F715 : not included in any glyphset definition</li>
<li>U+F716 : not included in any glyphset definition</li>
<li>U+F717 : not included in any glyphset definition</li>
<li>U+F718 : not included in any glyphset definition</li>
<li>U+F719 : not included in any glyphset definition</li>
<li>U+F71A : not included in any glyphset definition</li>
<li>U+F71E : not included in any glyphset definition</li>
<li>U+F71F : not included in any glyphset definition</li>
<li>U+F720 : not included in any glyphset definition</li>
<li>U+F880 : not included in any glyphset definition</li>
<li>U+F881 : not included in any glyphset definition</li>
<li>U+F882 : not included in any glyphset definition</li>
<li>U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
<li>U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition</li>
<li>U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition</li>
<li>U+FE45 SESAME DOT: not included in any glyphset definition</li>
<li>U+FE46 WHITE SESAME DOT: not included in any glyphset definition</li>
<li>U+FF01 FULLWIDTH EXCLAMATION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF02 FULLWIDTH QUOTATION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF03 FULLWIDTH NUMBER SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF04 FULLWIDTH DOLLAR SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF05 FULLWIDTH PERCENT SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF06 FULLWIDTH AMPERSAND: try adding one of: chinese-simplified, japanese</li>
<li>U+FF07 FULLWIDTH APOSTROPHE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF08 FULLWIDTH LEFT PARENTHESIS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF09 FULLWIDTH RIGHT PARENTHESIS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0A FULLWIDTH ASTERISK: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0B FULLWIDTH PLUS SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0C FULLWIDTH COMMA: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0D FULLWIDTH HYPHEN-MINUS: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0E FULLWIDTH FULL STOP: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0F FULLWIDTH SOLIDUS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF10 FULLWIDTH DIGIT ZERO: try adding one of: chinese-simplified, japanese</li>
<li>U+FF11 FULLWIDTH DIGIT ONE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF12 FULLWIDTH DIGIT TWO: try adding one of: chinese-simplified, japanese</li>
<li>U+FF13 FULLWIDTH DIGIT THREE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF14 FULLWIDTH DIGIT FOUR: try adding one of: chinese-simplified, japanese</li>
<li>U+FF15 FULLWIDTH DIGIT FIVE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF16 FULLWIDTH DIGIT SIX: try adding one of: chinese-simplified, japanese</li>
<li>U+FF17 FULLWIDTH DIGIT SEVEN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF18 FULLWIDTH DIGIT EIGHT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF19 FULLWIDTH DIGIT NINE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1A FULLWIDTH COLON: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF1B FULLWIDTH SEMICOLON: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF1C FULLWIDTH LESS-THAN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1D FULLWIDTH EQUALS SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1E FULLWIDTH GREATER-THAN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1F FULLWIDTH QUESTION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF20 FULLWIDTH COMMERCIAL AT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF21 FULLWIDTH LATIN CAPITAL LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+FF22 FULLWIDTH LATIN CAPITAL LETTER B: try adding one of: chinese-simplified, japanese</li>
<li>U+FF23 FULLWIDTH LATIN CAPITAL LETTER C: try adding one of: chinese-simplified, japanese</li>
<li>U+FF24 FULLWIDTH LATIN CAPITAL LETTER D: try adding one of: chinese-simplified, japanese</li>
<li>U+FF25 FULLWIDTH LATIN CAPITAL LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+FF26 FULLWIDTH LATIN CAPITAL LETTER F: try adding one of: chinese-simplified, japanese</li>
<li>U+FF27 FULLWIDTH LATIN CAPITAL LETTER G: try adding one of: chinese-simplified, japanese</li>
<li>U+FF28 FULLWIDTH LATIN CAPITAL LETTER H: try adding one of: chinese-simplified, japanese</li>
<li>U+FF29 FULLWIDTH LATIN CAPITAL LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2A FULLWIDTH LATIN CAPITAL LETTER J: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2B FULLWIDTH LATIN CAPITAL LETTER K: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2C FULLWIDTH LATIN CAPITAL LETTER L: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2D FULLWIDTH LATIN CAPITAL LETTER M: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2E FULLWIDTH LATIN CAPITAL LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2F FULLWIDTH LATIN CAPITAL LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+FF30 FULLWIDTH LATIN CAPITAL LETTER P: try adding one of: chinese-simplified, japanese</li>
<li>U+FF31 FULLWIDTH LATIN CAPITAL LETTER Q: try adding one of: chinese-simplified, japanese</li>
<li>U+FF32 FULLWIDTH LATIN CAPITAL LETTER R: try adding one of: chinese-simplified, japanese</li>
<li>U+FF33 FULLWIDTH LATIN CAPITAL LETTER S: try adding one of: chinese-simplified, japanese</li>
<li>U+FF34 FULLWIDTH LATIN CAPITAL LETTER T: try adding one of: chinese-simplified, japanese</li>
<li>U+FF35 FULLWIDTH LATIN CAPITAL LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+FF36 FULLWIDTH LATIN CAPITAL LETTER V: try adding one of: chinese-simplified, japanese</li>
<li>U+FF37 FULLWIDTH LATIN CAPITAL LETTER W: try adding one of: chinese-simplified, japanese</li>
<li>U+FF38 FULLWIDTH LATIN CAPITAL LETTER X: try adding one of: chinese-simplified, japanese</li>
<li>U+FF39 FULLWIDTH LATIN CAPITAL LETTER Y: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3A FULLWIDTH LATIN CAPITAL LETTER Z: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3B FULLWIDTH LEFT SQUARE BRACKET: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF3C FULLWIDTH REVERSE SOLIDUS: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3D FULLWIDTH RIGHT SQUARE BRACKET: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF3E FULLWIDTH CIRCUMFLEX ACCENT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3F FULLWIDTH LOW LINE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF40 FULLWIDTH GRAVE ACCENT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF41 FULLWIDTH LATIN SMALL LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+FF42 FULLWIDTH LATIN SMALL LETTER B: try adding one of: chinese-simplified, japanese</li>
<li>U+FF43 FULLWIDTH LATIN SMALL LETTER C: try adding one of: chinese-simplified, japanese</li>
<li>U+FF44 FULLWIDTH LATIN SMALL LETTER D: try adding one of: chinese-simplified, japanese</li>
<li>U+FF45 FULLWIDTH LATIN SMALL LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+FF46 FULLWIDTH LATIN SMALL LETTER F: try adding one of: chinese-simplified, japanese</li>
<li>U+FF47 FULLWIDTH LATIN SMALL LETTER G: try adding one of: chinese-simplified, japanese</li>
<li>U+FF48 FULLWIDTH LATIN SMALL LETTER H: try adding one of: chinese-simplified, japanese</li>
<li>U+FF49 FULLWIDTH LATIN SMALL LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4A FULLWIDTH LATIN SMALL LETTER J: try adding japanese</li>
<li>U+FF4B FULLWIDTH LATIN SMALL LETTER K: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4C FULLWIDTH LATIN SMALL LETTER L: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4D FULLWIDTH LATIN SMALL LETTER M: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4E FULLWIDTH LATIN SMALL LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4F FULLWIDTH LATIN SMALL LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+FF50 FULLWIDTH LATIN SMALL LETTER P: try adding one of: chinese-simplified, japanese</li>
<li>U+FF51 FULLWIDTH LATIN SMALL LETTER Q: try adding one of: chinese-simplified, japanese</li>
<li>U+FF52 FULLWIDTH LATIN SMALL LETTER R: try adding one of: chinese-simplified, japanese</li>
<li>U+FF53 FULLWIDTH LATIN SMALL LETTER S: try adding one of: chinese-simplified, japanese</li>
<li>U+FF54 FULLWIDTH LATIN SMALL LETTER T: try adding one of: chinese-simplified, japanese</li>
<li>U+FF55 FULLWIDTH LATIN SMALL LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+FF56 FULLWIDTH LATIN SMALL LETTER V: try adding one of: chinese-simplified, japanese</li>
<li>U+FF57 FULLWIDTH LATIN SMALL LETTER W: try adding one of: chinese-simplified, japanese</li>
<li>U+FF58 FULLWIDTH LATIN SMALL LETTER X: try adding one of: chinese-simplified, japanese</li>
<li>U+FF59 FULLWIDTH LATIN SMALL LETTER Y: try adding one of: chinese-simplified, japanese</li>
<li>U+FF5A FULLWIDTH LATIN SMALL LETTER Z: try adding japanese</li>
<li>U+FF5B FULLWIDTH LEFT CURLY BRACKET: try adding one of: math, chinese-simplified, yi, japanese</li>
<li>U+FF5C FULLWIDTH VERTICAL LINE: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF5D FULLWIDTH RIGHT CURLY BRACKET: try adding one of: math, chinese-simplified, yi, japanese</li>
<li>U+FF5E FULLWIDTH TILDE: try adding one of: chinese-simplified, yi</li>
<li>U+FF5F FULLWIDTH LEFT WHITE PARENTHESIS: not included in any glyphset definition</li>
<li>U+FF60 FULLWIDTH RIGHT WHITE PARENTHESIS: not included in any glyphset definition</li>
<li>U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP: try adding yi</li>
<li>U+FF62 HALFWIDTH LEFT CORNER BRACKET: try adding yi</li>
<li>U+FF63 HALFWIDTH RIGHT CORNER BRACKET: try adding yi</li>
<li>U+FF64 HALFWIDTH IDEOGRAPHIC COMMA: try adding yi</li>
<li>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT: try adding yi</li>
<li>U+FF66 HALFWIDTH KATAKANA LETTER WO: not included in any glyphset definition</li>
<li>U+FF67 HALFWIDTH KATAKANA LETTER SMALL A: not included in any glyphset definition</li>
<li>U+FF68 HALFWIDTH KATAKANA LETTER SMALL I: not included in any glyphset definition</li>
<li>U+FF69 HALFWIDTH KATAKANA LETTER SMALL U: not included in any glyphset definition</li>
<li>U+FF6A HALFWIDTH KATAKANA LETTER SMALL E: not included in any glyphset definition</li>
<li>U+FF6B HALFWIDTH KATAKANA LETTER SMALL O: not included in any glyphset definition</li>
<li>U+FF6C HALFWIDTH KATAKANA LETTER SMALL YA: not included in any glyphset definition</li>
<li>U+FF6D HALFWIDTH KATAKANA LETTER SMALL YU: not included in any glyphset definition</li>
<li>U+FF6E HALFWIDTH KATAKANA LETTER SMALL YO: not included in any glyphset definition</li>
<li>U+FF6F HALFWIDTH KATAKANA LETTER SMALL TU: not included in any glyphset definition</li>
<li>U+FF70 HALFWIDTH KATAKANA-HIRAGANA PROLONGED SOUND MARK: not included in any glyphset definition</li>
<li>U+FF71 HALFWIDTH KATAKANA LETTER A: not included in any glyphset definition</li>
<li>U+FF72 HALFWIDTH KATAKANA LETTER I: not included in any glyphset definition</li>
<li>U+FF73 HALFWIDTH KATAKANA LETTER U: not included in any glyphset definition</li>
<li>U+FF74 HALFWIDTH KATAKANA LETTER E: not included in any glyphset definition</li>
<li>U+FF75 HALFWIDTH KATAKANA LETTER O: not included in any glyphset definition</li>
<li>U+FF76 HALFWIDTH KATAKANA LETTER KA: not included in any glyphset definition</li>
<li>U+FF77 HALFWIDTH KATAKANA LETTER KI: not included in any glyphset definition</li>
<li>U+FF78 HALFWIDTH KATAKANA LETTER KU: not included in any glyphset definition</li>
<li>U+FF79 HALFWIDTH KATAKANA LETTER KE: not included in any glyphset definition</li>
<li>U+FF7A HALFWIDTH KATAKANA LETTER KO: not included in any glyphset definition</li>
<li>U+FF7B HALFWIDTH KATAKANA LETTER SA: not included in any glyphset definition</li>
<li>U+FF7C HALFWIDTH KATAKANA LETTER SI: not included in any glyphset definition</li>
<li>U+FF7D HALFWIDTH KATAKANA LETTER SU: not included in any glyphset definition</li>
<li>U+FF7E HALFWIDTH KATAKANA LETTER SE: not included in any glyphset definition</li>
<li>U+FF7F HALFWIDTH KATAKANA LETTER SO: not included in any glyphset definition</li>
<li>U+FF80 HALFWIDTH KATAKANA LETTER TA: not included in any glyphset definition</li>
<li>U+FF81 HALFWIDTH KATAKANA LETTER TI: not included in any glyphset definition</li>
<li>U+FF82 HALFWIDTH KATAKANA LETTER TU: not included in any glyphset definition</li>
<li>U+FF83 HALFWIDTH KATAKANA LETTER TE: not included in any glyphset definition</li>
<li>U+FF84 HALFWIDTH KATAKANA LETTER TO: not included in any glyphset definition</li>
<li>U+FF85 HALFWIDTH KATAKANA LETTER NA: not included in any glyphset definition</li>
<li>U+FF86 HALFWIDTH KATAKANA LETTER NI: not included in any glyphset definition</li>
<li>U+FF87 HALFWIDTH KATAKANA LETTER NU: not included in any glyphset definition</li>
<li>U+FF88 HALFWIDTH KATAKANA LETTER NE: not included in any glyphset definition</li>
<li>U+FF89 HALFWIDTH KATAKANA LETTER NO: not included in any glyphset definition</li>
<li>U+FF8A HALFWIDTH KATAKANA LETTER HA: not included in any glyphset definition</li>
<li>U+FF8B HALFWIDTH KATAKANA LETTER HI: not included in any glyphset definition</li>
<li>U+FF8C HALFWIDTH KATAKANA LETTER HU: not included in any glyphset definition</li>
<li>U+FF8D HALFWIDTH KATAKANA LETTER HE: not included in any glyphset definition</li>
<li>U+FF8E HALFWIDTH KATAKANA LETTER HO: not included in any glyphset definition</li>
<li>U+FF8F HALFWIDTH KATAKANA LETTER MA: not included in any glyphset definition</li>
<li>U+FF90 HALFWIDTH KATAKANA LETTER MI: not included in any glyphset definition</li>
<li>U+FF91 HALFWIDTH KATAKANA LETTER MU: not included in any glyphset definition</li>
<li>U+FF92 HALFWIDTH KATAKANA LETTER ME: not included in any glyphset definition</li>
<li>U+FF93 HALFWIDTH KATAKANA LETTER MO: not included in any glyphset definition</li>
<li>U+FF94 HALFWIDTH KATAKANA LETTER YA: not included in any glyphset definition</li>
<li>U+FF95 HALFWIDTH KATAKANA LETTER YU: not included in any glyphset definition</li>
<li>U+FF96 HALFWIDTH KATAKANA LETTER YO: not included in any glyphset definition</li>
<li>U+FF97 HALFWIDTH KATAKANA LETTER RA: not included in any glyphset definition</li>
<li>U+FF98 HALFWIDTH KATAKANA LETTER RI: not included in any glyphset definition</li>
<li>U+FF99 HALFWIDTH KATAKANA LETTER RU: not included in any glyphset definition</li>
<li>U+FF9A HALFWIDTH KATAKANA LETTER RE: not included in any glyphset definition</li>
<li>U+FF9B HALFWIDTH KATAKANA LETTER RO: not included in any glyphset definition</li>
<li>U+FF9C HALFWIDTH KATAKANA LETTER WA: not included in any glyphset definition</li>
<li>U+FF9D HALFWIDTH KATAKANA LETTER N: not included in any glyphset definition</li>
<li>U+FF9E HALFWIDTH KATAKANA VOICED SOUND MARK: not included in any glyphset definition</li>
<li>U+FF9F HALFWIDTH KATAKANA SEMI-VOICED SOUND MARK: not included in any glyphset definition</li>
<li>U+FFE0 FULLWIDTH CENT SIGN: try adding chinese-simplified</li>
<li>U+FFE1 FULLWIDTH POUND SIGN: try adding chinese-simplified</li>
<li>U+FFE2 FULLWIDTH NOT SIGN: not included in any glyphset definition</li>
<li>U+FFE3 FULLWIDTH MACRON: try adding one of: chinese-simplified, japanese</li>
<li>U+FFE4 FULLWIDTH BROKEN BAR: not included in any glyphset definition</li>
<li>U+FFE5 FULLWIDTH YEN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FFE6 FULLWIDTH WON SIGN: not included in any glyphset definition</li>
<li>U+FFE8 HALFWIDTH FORMS LIGHT VERTICAL: not included in any glyphset definition</li>
<li>U+FFE9 HALFWIDTH LEFTWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEA HALFWIDTH UPWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEB HALFWIDTH RIGHTWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEC HALFWIDTH DOWNWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFED HALFWIDTH BLACK SQUARE: not included in any glyphset definition</li>
<li>U+FFEE HALFWIDTH WHITE CIRCLE: not included in any glyphset definition</li>
<li>U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition</li>
<li>U+1F494 BROKEN HEART: not included in any glyphset definition</li>
<li>U+1FBB0 ARROWHEAD-SHAPED POINTER: try adding symbols</li>
<li>U+1FBB2 LEFT HALF RUNNING MAN: try adding symbols</li>
<li>U+1FBB3 RIGHT HALF RUNNING MAN: try adding symbols</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>lao</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>thai</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>









* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ i̍ i̓ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ і́ ḭ̀ ḭ́ ḭ̄ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ i̎ i̒ i̔ i̛̅ i̛̇ i̛̊ i̛̋ i̛̍ i̛̎ i̛̒ i̛̓ i̛̔ i̤̅ i̤̇ i̤̊ i̤̋ i̤̍ i̤̎</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Do any segments have colinear vectors? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-colinear-vectors">outline_colinear_vectors</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have colinear vectors:</p>
<pre><code>* uni2075 (U+2075): L&lt;&lt;320.0,128.0&gt;--&lt;192.0,128.0&gt;&gt; -&gt; L&lt;&lt;192.0,128.0&gt;--&lt;64.0,128.0&gt;&gt;

* uni2076 (U+2076): L&lt;&lt;384.0,128.0&gt;--&lt;256.0,128.0&gt;&gt; -&gt; L&lt;&lt;256.0,128.0&gt;--&lt;128.0,128.0&gt;&gt;

* uni2078 (U+2078): L&lt;&lt;384.0,128.0&gt;--&lt;256.0,128.0&gt;&gt; -&gt; L&lt;&lt;256.0,128.0&gt;--&lt;128.0,128.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;128.0,384.0&gt;--&lt;192.0,384.0&gt;&gt; -&gt; L&lt;&lt;192.0,384.0&gt;--&lt;256.0,384.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;192.0,320.0&gt;--&lt;128.0,320.0&gt;&gt; -&gt; L&lt;&lt;128.0,320.0&gt;--&lt;64.0,320.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;192.0,384.0&gt;--&lt;256.0,384.0&gt;&gt; -&gt; L&lt;&lt;256.0,384.0&gt;--&lt;320.0,384.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;256.0,320.0&gt;--&lt;192.0,320.0&gt;&gt; -&gt; L&lt;&lt;192.0,320.0&gt;--&lt;128.0,320.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;256.0,384.0&gt;--&lt;320.0,384.0&gt;&gt; -&gt; L&lt;&lt;320.0,384.0&gt;--&lt;448.0,384.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;320.0,320.0&gt;--&lt;256.0,320.0&gt;&gt; -&gt; L&lt;&lt;256.0,320.0&gt;--&lt;192.0,320.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;320.0,384.0&gt;--&lt;448.0,384.0&gt;&gt; -&gt; L&lt;&lt;448.0,384.0&gt;--&lt;512.0,384.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;384.0,320.0&gt;--&lt;320.0,320.0&gt;&gt; -&gt; L&lt;&lt;320.0,320.0&gt;--&lt;256.0,320.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;448.0,320.0&gt;--&lt;384.0,320.0&gt;&gt; -&gt; L&lt;&lt;384.0,320.0&gt;--&lt;320.0,320.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;512.0,320.0&gt;--&lt;448.0,320.0&gt;&gt; -&gt; L&lt;&lt;448.0,320.0&gt;--&lt;384.0,320.0&gt;&gt;

* uni207B (U+207B): L&lt;&lt;64.0,384.0&gt;--&lt;128.0,384.0&gt;&gt; -&gt; L&lt;&lt;128.0,384.0&gt;--&lt;192.0,384.0&gt;&gt;

* uni2085 (U+2085): L&lt;&lt;320.0,-64.0&gt;--&lt;192.0,-64.0&gt;&gt; -&gt; L&lt;&lt;192.0,-64.0&gt;--&lt;64.0,-64.0&gt;&gt;

* uni2086 (U+2086): L&lt;&lt;384.0,-64.0&gt;--&lt;256.0,-64.0&gt;&gt; -&gt; L&lt;&lt;256.0,-64.0&gt;--&lt;128.0,-64.0&gt;&gt;

* uni2088 (U+2088): L&lt;&lt;384.0,-64.0&gt;--&lt;256.0,-64.0&gt;&gt; -&gt; L&lt;&lt;256.0,-64.0&gt;--&lt;128.0,-64.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;128.0,192.0&gt;--&lt;192.0,192.0&gt;&gt; -&gt; L&lt;&lt;192.0,192.0&gt;--&lt;256.0,192.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;192.0,128.0&gt;--&lt;128.0,128.0&gt;&gt; -&gt; L&lt;&lt;128.0,128.0&gt;--&lt;64.0,128.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;192.0,192.0&gt;--&lt;256.0,192.0&gt;&gt; -&gt; L&lt;&lt;256.0,192.0&gt;--&lt;320.0,192.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;256.0,128.0&gt;--&lt;192.0,128.0&gt;&gt; -&gt; L&lt;&lt;192.0,128.0&gt;--&lt;128.0,128.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;256.0,192.0&gt;--&lt;320.0,192.0&gt;&gt; -&gt; L&lt;&lt;320.0,192.0&gt;--&lt;448.0,192.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;320.0,128.0&gt;--&lt;256.0,128.0&gt;&gt; -&gt; L&lt;&lt;256.0,128.0&gt;--&lt;192.0,128.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;320.0,192.0&gt;--&lt;448.0,192.0&gt;&gt; -&gt; L&lt;&lt;448.0,192.0&gt;--&lt;512.0,192.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;384.0,128.0&gt;--&lt;320.0,128.0&gt;&gt; -&gt; L&lt;&lt;320.0,128.0&gt;--&lt;256.0,128.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;448.0,128.0&gt;--&lt;384.0,128.0&gt;&gt; -&gt; L&lt;&lt;384.0,128.0&gt;--&lt;320.0,128.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;512.0,128.0&gt;--&lt;448.0,128.0&gt;&gt; -&gt; L&lt;&lt;448.0,128.0&gt;--&lt;384.0,128.0&gt;&gt;

* uni208B (U+208B): L&lt;&lt;64.0,192.0&gt;--&lt;128.0,192.0&gt;&gt; -&gt; L&lt;&lt;128.0,192.0&gt;--&lt;192.0,192.0&gt;&gt;
</code></pre>
 [code: found-colinear-vectors]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[20] SyyUDS-Regular.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font. Please set PANOSE Proportion to 9 (monospaced)</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1912 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 626 glyphs (32.71%) have a different width. You should check the widths of: ['exclam', 'quotedbl', 'quotesingle', 'parenleft', 'parenright', 'comma', 'period', 'colon', 'semicolon', 'M', 'W', 'underscore', 'grave', 'm', 'w', 'braceleft', 'bar', 'braceright', 'exclamdown', 'acute', 'periodcentered', 'cedilla', 'AE', 'ae', 'OE', 'oe', 'Wcircumflex', 'wcircumflex', 'uni01C0', 'uni01C1', 'uni01E2', 'uni01E3', 'AEacute', 'aeacute', 'uni02B9', 'quoteleft', 'quoteright', 'quotereversed', 'uni0402', 'uni0409', 'uni040A', 'uni040B', 'uni0416', 'uni0424', 'uni0428', 'uni0429', 'uni042B', 'uni042E', 'uni0436', 'uni043C', 'uni0444', 'uni0448', 'uni0449', 'uni044B', 'uni044E', 'uni0452', 'uni0459', 'uni045A', 'uni045B', 'uni0496', 'uni0497', 'uni04C1', 'uni04C2', 'uni04DC', 'uni04DD', 'uni04F8', 'uni04F9', 'uni0E0C', 'uni0E0D', 'uni0E12', 'uni0E13', 'uni0E40', 'uni0E46', 'uni0E86', 'uni0E8E', 'uni0E91', 'uni0E92', 'uni0E93', 'uni0E97', 'uni0E9E', 'uni0E9F', 'uni0EA4', 'uni0EAB', 'uni0EC0', 'uni0EC6', 'uni0EDC', 'uni0EDD', 'uni1E3E', 'uni1E3F', 'uni1E40', 'uni1E41', 'uni1E42', 'uni1E43', 'Wgrave', 'wgrave', 'Wacute', 'wacute', 'Wdieresis', 'wdieresis', 'uni1E86', 'uni1E87', 'uni1E88', 'uni1E89', 'uni1E98', 'uni2001', 'uni2003', 'uni2004', 'uni2005', 'uni2006', 'uni2008', 'uni2009', 'uni200A', 'emdash', 'uni2015', 'uni2016', 'quotesinglbase', 'quotedblleft', 'quotedblright', 'quotedblbase', 'uni201F', 'twodotenleader', 'minute', 'uni2034', 'uni203B', 'uni203E', 'uni2103', 'uni210F', 'uni2113', 'uni212B', 'aleph', 'arrowleft', 'arrowup', 'arrowright', 'arrowdown', 'arrowboth', 'arrowupdn', 'uni2196', 'uni2197', 'uni2198', 'uni2199', 'uni21A9', 'uni21AA', 'carriagereturn', 'uni21C4', 'arrowdblleft', 'arrowdblup', 'arrowdblright', 'arrowdbldown', 'arrowdblboth', 'uni21D5', 'uni21D6', 'uni21D7', 'uni21D8', 'uni21D9', 'uni21E5', 'uni21E6', 'uni21E7', 'uni21E8', 'uni21E9', 'uni21EA', 'uni21EB', 'uni21EC', 'uni21ED', 'uni21EE', 'uni21EF', 'uni21F0', 'uni21F1', 'uni21F2', 'uni21F3', 'universal', 'existential', 'emptyset', 'gradient', 'element', 'notelement', 'suchthat', 'uni2213', 'proportional', 'infinity', 'angle', 'uni2225', 'uni2226', 'logicaland', 'logicalor', 'intersection', 'union', 'uni222C', 'therefore', 'uni2235', 'uni223D', 'uni2243', 'congruent', 'approxequal', 'uni2252', 'equivalence', 'uni2262', 'uni2266', 'uni2267', 'uni226A', 'uni226B', 'uni2276', 'uni2277', 'propersubset', 'propersuperset', 'notsubset', 'uni2285', 'reflexsubset', 'reflexsuperset', 'uni228A', 'uni228B', 'circleplus', 'uni2296', 'circlemultiply', 'perpendicular', 'uni2305', 'uni2306', 'uni2312', 'uni2318', 'uni2325', 'uni232B', 'uni2387', 'uni23CE', 'filledbox', 'H22073', 'triagup', 'uni25B3', 'uni25B6', 'uni25B7', 'triagdn', 'uni25BD', 'uni25C0', 'uni25C1', 'uni25C6', 'uni25C7', 'uni25C9', 'circle', 'uni25CE', 'H18533', 'uni25EF', 'uni2605', 'uni2606', 'female', 'male', 'uni2661', 'heart', 'uni2669', 'musicalnote', 'musicalnotedbl', 'uni266C', 'uni266D', 'uni266E', 'uni266F', 'uni26A0', 'uni2726', 'uni2727', 'uni2764', 'uni2765', 'uni2934', 'uni2935', 'uni29BF', 'uni29FA', 'uni29FB', 'uni3000', 'uni3001', 'uni3002', 'uni3003', 'uni3005', 'uni3006', 'uni3007', 'uni3008', 'uni3009', 'uni300A', 'uni300B', 'uni300C', 'uni300D', 'uni300E', 'uni300F', 'uni3010', 'uni3011', 'uni3012', 'uni3013', 'uni3014', 'uni3015', 'uni3016', 'uni3017', 'uni3018', 'uni3019', 'uni301C', 'uni301D', 'uni301E', 'uni301F', 'uni3033', 'uni3034', 'uni3035', 'uni303B', 'uni303C', 'uni303D', 'uni3041', 'uni3042', 'uni3043', 'uni3044', 'uni3045', 'uni3046', 'uni3047', 'uni3048', 'uni3049', 'uni304A', 'uni304B', 'uni304C', 'uni304D', 'uni304E', 'uni304F', 'uni3050', 'uni3051', 'uni3052', 'uni3053', 'uni3054', 'uni3055', 'uni3056', 'uni3057', 'uni3058', 'uni3059', 'uni305A', 'uni305B', 'uni305C', 'uni305D', 'uni305E', 'uni305F', 'uni3060', 'uni3061', 'uni3062', 'uni3063', 'uni3064', 'uni3065', 'uni3066', 'uni3067', 'uni3068', 'uni3069', 'uni306A', 'uni306B', 'uni306C', 'uni306D', 'uni306E', 'uni306F', 'uni3070', 'uni3071', 'uni3072', 'uni3073', 'uni3074', 'uni3075', 'uni3076', 'uni3077', 'uni3078', 'uni3079', 'uni307A', 'uni307B', 'uni307C', 'uni307D', 'uni307E', 'uni307F', 'uni3080', 'uni3081', 'uni3082', 'uni3083', 'uni3084', 'uni3085', 'uni3086', 'uni3087', 'uni3088', 'uni3089', 'uni308A', 'uni308B', 'uni308C', 'uni308D', 'uni308E', 'uni308F', 'uni3090', 'uni3091', 'uni3092', 'uni3093', 'uni3094', 'uni3095', 'uni3096', 'uni309B', 'uni309C', 'uni309D', 'uni309E', 'uni309F', 'uni30A0', 'uni30A1', 'uni30A2', 'uni30A3', 'uni30A4', 'uni30A5', 'uni30A6', 'uni30A7', 'uni30A8', 'uni30A9', 'uni30AA', 'uni30AB', 'uni30AC', 'uni30AD', 'uni30AE', 'uni30AF', 'uni30B0', 'uni30B1', 'uni30B2', 'uni30B3', 'uni30B4', 'uni30B5', 'uni30B6', 'uni30B7', 'uni30B8', 'uni30B9', 'uni30BA', 'uni30BB', 'uni30BC', 'uni30BD', 'uni30BE', 'uni30BF', 'uni30C0', 'uni30C1', 'uni30C2', 'uni30C3', 'uni30C4', 'uni30C5', 'uni30C6', 'uni30C7', 'uni30C8', 'uni30C9', 'uni30CA', 'uni30CB', 'uni30CC', 'uni30CD', 'uni30CE', 'uni30CF', 'uni30D0', 'uni30D1', 'uni30D2', 'uni30D3', 'uni30D4', 'uni30D5', 'uni30D6', 'uni30D7', 'uni30D8', 'uni30D9', 'uni30DA', 'uni30DB', 'uni30DC', 'uni30DD', 'uni30DE', 'uni30DF', 'uni30E0', 'uni30E1', 'uni30E2', 'uni30E3', 'uni30E4', 'uni30E5', 'uni30E6', 'uni30E7', 'uni30E8', 'uni30E9', 'uni30EA', 'uni30EB', 'uni30EC', 'uni30ED', 'uni30EE', 'uni30EF', 'uni30F0', 'uni30F1', 'uni30F2', 'uni30F3', 'uni30F4', 'uni30F5', 'uni30F6', 'uni30F7', 'uni30F8', 'uni30F9', 'uni30FA', 'uni30FB', 'uni30FC', 'uni30FD', 'uni30FE', 'uni30FF', 'uni31F0', 'uni31F1', 'uni31F2', 'uni31F3', 'uni31F4', 'uni31F5', 'uni31F6', 'uni31F7', 'uni31F8', 'uni31F9', 'uni31FA', 'uni31FB', 'uni31FC', 'uni31FD', 'uni31FE', 'uni31FF', 'uni33CB', 'uni4EDD', 'uniE133', 'uniE134', 'uniE139', 'uni0E0D.descless', 'uni0E24_uni0E45', 'uni0E26_uni0E45', 'uniFB00', 'uniFB01', 'uniFB02', 'uniFB03', 'uniFB04', 'uniFE45', 'uniFE46', 'uniFF01', 'uniFF02', 'uniFF03', 'uniFF04', 'uniFF05', 'uniFF06', 'uniFF07', 'uniFF08', 'uniFF09', 'uniFF0A', 'uniFF0B', 'uniFF0C', 'uniFF0D', 'uniFF0E', 'uniFF0F', 'uniFF10', 'uniFF11', 'uniFF12', 'uniFF13', 'uniFF14', 'uniFF15', 'uniFF16', 'uniFF17', 'uniFF18', 'uniFF19', 'uniFF1A', 'uniFF1B', 'uniFF1C', 'uniFF1D', 'uniFF1E', 'uniFF1F', 'uniFF20', 'uniFF21', 'uniFF22', 'uniFF23', 'uniFF24', 'uniFF25', 'uniFF26', 'uniFF27', 'uniFF28', 'uniFF29', 'uniFF2A', 'uniFF2B', 'uniFF2C', 'uniFF2D', 'uniFF2E', 'uniFF2F', 'uniFF30', 'uniFF31', 'uniFF32', 'uniFF33', 'uniFF34', 'uniFF35', 'uniFF36', 'uniFF37', 'uniFF38', 'uniFF39', 'uniFF3A', 'uniFF3B', 'uniFF3C', 'uniFF3D', 'uniFF3E', 'uniFF3F', 'uniFF40', 'uniFF41', 'uniFF42', 'uniFF43', 'uniFF44', 'uniFF45', 'uniFF46', 'uniFF47', 'uniFF48', 'uniFF49', 'uniFF4A', 'uniFF4B', 'uniFF4C', 'uniFF4D', 'uniFF4E', 'uniFF4F', 'uniFF50', 'uniFF51', 'uniFF52', 'uniFF53', 'uniFF54', 'uniFF55', 'uniFF56', 'uniFF57', 'uniFF58', 'uniFF59', 'uniFF5A', 'uniFF5B', 'uniFF5C', 'uniFF5D', 'uniFF5E', 'uniFF5F', 'uniFF60', 'uniFFE0', 'uniFFE1', 'uniFFE2', 'uniFFE3', 'uniFFE4', 'uniFFE5', 'uniFFE6', 'uniFFE9', 'uniFFEA', 'uniFFEB', 'uniFFEC', 'u1F494', 'u1FBB0', 'u1FBB2', 'u1FBB3']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>







* 🔥 **FAIL** <p>dcaron uses component uni030C.</p>
 [code: wrong-mark]



* 🔥 **FAIL** <p>tcaron uses component uni030C.</p>
 [code: wrong-mark]



* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0182: LATIN CAPITAL LETTER B WITH TOPBAR</td>
<td align="left">U+0183: LATIN SMALL LETTER B WITH TOPBAR</td>
</tr>
<tr>
<td align="left">U+026A: LATIN LETTER SMALL CAPITAL I</td>
<td align="left">U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I</td>
</tr>
<tr>
<td align="left">U+028A: LATIN SMALL LETTER UPSILON</td>
<td align="left">U+01B1: LATIN CAPITAL LETTER UPSILON</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҳ, ҷ</td>
<td align="left">tg_Cyrl (Tajik) and tg_Cyrl (Tajik)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҳ</td>
<td align="left">uz_Cyrl (Uzbek (Cyrillic)) and uz_Cyrl (Uzbek (Cyrillic))</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ɲ, Ɲ</td>
<td align="left">bm_Latn (Bambara)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ɲ, ɲ</td>
<td align="left">dyu_Latn (Dyula)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ƴ, Ƴ</td>
<td align="left">ff_Latn (Fulah)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ƴ, ƙ, Ƙ, Ƴ</td>
<td align="left">ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EB9 when shaping the text 'ẹ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EB9 when shaping the text 'ẹ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECD when shaping the text 'ọ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECD when shaping the text 'ọ̀'</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҙ, Ҫ, ҙ, ҡ, Ҡ, ҫ</td>
<td align="left">ba_Cyrl (Bashkir)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҫ, ҫ</td>
<td align="left">cv_Cyrl (Chuvash)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҝ, ҹ</td>
<td align="left">az_Cyrl (Azerbaijani (Cyrillic))</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ӏ, Ӏ</td>
<td align="left">kbd_Cyrl (Kabardian), ady_Cyrl (Adyghe), dar_Cyrl (Dargwa) and lez_Cyrl (Lezghian)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: чӏ, кӏ, тӏ, рхӏ, гӏ, цӏ, пӏ, хӏ</td>
<td align="left">ce_Cyrl (Chechen)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ӏ, ӏ</td>
<td align="left">av_Cyrl (Avaric) and inh_Cyrl (Ingush)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҥ, Ҥ</td>
<td align="left">chm_Cyrl (Mari)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҳ, ҳ</td>
<td align="left">kaa_Cyrl (Kara-Kalpak)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҥ, ҕ</td>
<td align="left">sah_Cyrl (Sakha)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǥ</td>
<td align="left">fi_Latn (Finnish)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to aogonek when shaping the text 'ą́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to aogonek when shaping the text 'ą̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to eogonek when shaping the text 'ę́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to eogonek when shaping the text 'ę̃'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left">lt_Latn (Lithuanian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to a when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to e when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to o when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to y when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">ru_Cyrl (Russian) and ru_Cyrl (Russian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to a when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to e when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0454 when shaping the text 'є́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni0438 when shaping the text 'и́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to o when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to y when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">uk_Cyrl (Ukrainian) and uk_Cyrl (Ukrainian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to a when shaping the text 'а́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to e when shaping the text 'е́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to o when shaping the text 'о́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to y when shaping the text 'у́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044D when shaping the text 'э́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni044F when shaping the text 'я́'</td>
<td align="left">be_Cyrl (Belarusian) and be_Cyrl (Belarusian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to a when shaping the text 'а̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to o when shaping the text 'о̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to y when shaping the text 'у̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044A when shaping the text 'ъ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni044F when shaping the text 'я̀'</td>
<td align="left">bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to a when shaping the text 'а̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to e when shaping the text 'е̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to uni0438 when shaping the text 'и̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to o when shaping the text 'о̂'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0302 to y when shaping the text 'у̂'</td>
<td align="left">sr_Cyrl (Serbian) and sr_Cyrl (Serbian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἀ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὰ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὲ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἠ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὴ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἰ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἴ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἲ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὸ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὺ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὼ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach tildecomb to r when shaping the text 'r̃'</td>
<td align="left">ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1ECD when shaping the text 'ọ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1ECD when shaping the text 'ọ̀'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach acutecomb to uni1EE5 when shaping the text 'ụ́'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach gravecomb to uni1EE5 when shaping the text 'ụ̀'</td>
<td align="left">ig_Latn (Igbo)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030C to uni1EB9 when shaping the text 'ẹ̌'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni030C to uni1ECD when shaping the text 'ọ̌'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to e when shaping the text 'e̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to E when shaping the text 'E̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to eacute when shaping the text 'é̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Eacute when shaping the text 'É̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to egrave when shaping the text 'è̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Egrave when shaping the text 'È̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to ecircumflex when shaping the text 'ê̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Ecircumflex when shaping the text 'Ê̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to ecaron when shaping the text 'ě̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Ecaron when shaping the text 'Ě̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to o when shaping the text 'o̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to O when shaping the text 'O̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to oacute when shaping the text 'ó̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Oacute when shaping the text 'Ó̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to ograve when shaping the text 'ò̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Ograve when shaping the text 'Ò̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to ocircumflex when shaping the text 'ô̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to Ocircumflex when shaping the text 'Ô̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to uni01D2 when shaping the text 'ǒ̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to uni01D1 when shaping the text 'Ǒ̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to s when shaping the text 's̩'</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">Shaper didn't attach uni0329 to S when shaping the text 'S̩'</td>
<td align="left">yo_Latn (Yoruba)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Name table entries should not contain line-breaks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-line-breaks">googlefonts/name/line_breaks</a></summary>
    <div>







* 🔥 **FAIL** <p>Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break.</p>
 [code: line-break]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2026 the syy beneathpoem project authors (<a href="https://github.com/plaenithaan/syy-beneathpoem">https://github.com/plaenithaan/syy-beneathpoem</a>)&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font follows the Google Fonts CJK vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics">googlefonts/cjk_vertical_metrics</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2 fsSelection bit 7 must be disabled</p>
 [code: bad-fselection-bit7]



* 🔥 **FAIL** <p>OS/2.sTypoAscender is &quot;960&quot; it should be 901</p>
 [code: bad-OS/2.sTypoAscender]



* 🔥 **FAIL** <p>OS/2.sTypoDescender is &quot;-256&quot; it should be -123</p>
 [code: bad-OS/2.sTypoDescender]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0334 (U+0334), uni0335 (U+0335), uni0336 (U+0336), uni0337 (U+0337), uni0338 (U+0338), uni0358 (U+0358), uni3099 (U+3099) and uni309A (U+309A)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain chws and vchw features? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-chws-feature">cjk_chws_feature</a></summary>
    <div>







* ⚠️ **WARN** <p>chws feature not found in font. Use chws_tool (<a href="https://github.com/googlefonts/chws_tool">https://github.com/googlefonts/chws_tool</a>) to add it.</p>
 [code: missing-chws-feature]



* ⚠️ **WARN** <p>vchw feature not found in font. Use chws_tool (<a href="https://github.com/googlefonts/chws_tool">https://github.com/googlefonts/chws_tool</a>) to add it.</p>
 [code: missing-vchw-feature]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: dollar	Contours detected: 6	Expected: 1, 3 or 5

- Glyph name: percent	Contours detected: 14	Expected: 4 or 5

- Glyph name: ampersand	Contours detected: 6	Expected: 1, 2 or 3

- Glyph name: parenleft	Contours detected: 5	Expected: 1

- Glyph name: parenright	Contours detected: 5	Expected: 1

- Glyph name: asterisk	Contours detected: 5	Expected: 1 or 4

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: zero	Contours detected: 5	Expected: 2 or 3

- Glyph name: one	Contours detected: 2	Expected: 1

- Glyph name: two	Contours detected: 8	Expected: 1

- Glyph name: three	Contours detected: 6	Expected: 1

- Glyph name: four	Contours detected: 3	Expected: 1 or 2

- Glyph name: five	Contours detected: 6	Expected: 1

- Glyph name: six	Contours detected: 5	Expected: 1 or 2

- Glyph name: seven	Contours detected: 3	Expected: 1

- Glyph name: eight	Contours detected: 4	Expected: 3

- Glyph name: nine	Contours detected: 4	Expected: 1 or 2

- Glyph name: less	Contours detected: 9	Expected: 1

- Glyph name: greater	Contours detected: 9	Expected: 1

- Glyph name: question	Contours detected: 7	Expected: 2

- Glyph name: at	Contours detected: 7	Expected: 2

- Glyph name: D	Contours detected: 4	Expected: 2

- Glyph name: G	Contours detected: 4	Expected: 1

- Glyph name: Q	Contours detected: 11	Expected: 2

- Glyph name: R	Contours detected: 4	Expected: 1 or 2

- Glyph name: U	Contours detected: 3	Expected: 1

- Glyph name: V	Contours detected: 5	Expected: 1

- Glyph name: W	Contours detected: 6	Expected: 1 or 2

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: grave	Contours detected: 3	Expected: 1

- Glyph name: b	Contours detected: 6	Expected: 2

- Glyph name: d	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: g	Contours detected: 10	Expected: 2 or 3

- Glyph name: h	Contours detected: 3	Expected: 1

- Glyph name: k	Contours detected: 8	Expected: 1 or 2

- Glyph name: m	Contours detected: 3	Expected: 1

- Glyph name: n	Contours detected: 3	Expected: 1

- Glyph name: q	Contours detected: 6	Expected: 2

- Glyph name: r	Contours detected: 3	Expected: 1

- Glyph name: t	Contours detected: 2	Expected: 1

- Glyph name: u	Contours detected: 3	Expected: 1

- Glyph name: v	Contours detected: 5	Expected: 1

- Glyph name: w	Contours detected: 7	Expected: 1

- Glyph name: z	Contours detected: 5	Expected: 1

- Glyph name: braceleft	Contours detected: 5	Expected: 1

- Glyph name: braceright	Contours detected: 3	Expected: 1

- Glyph name: asciitilde	Contours detected: 3	Expected: 1

- Glyph name: cent	Contours detected: 7	Expected: 1 or 2

- Glyph name: sterling	Contours detected: 6	Expected: 1 or 2

- Glyph name: currency	Contours detected: 5	Expected: 2

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: section	Contours detected: 6	Expected: 2

- Glyph name: copyright	Contours detected: 12	Expected: 3

- Glyph name: ordfeminine	Contours detected: 4	Expected: 2 or 3

- Glyph name: guillemotleft	Contours detected: 10	Expected: 2

- Glyph name: registered	Contours detected: 9	Expected: 3 or 4

- Glyph name: uni00B2	Contours detected: 6	Expected: 1

- Glyph name: uni00B3	Contours detected: 7	Expected: 1

- Glyph name: acute	Contours detected: 3	Expected: 1

- Glyph name: mu	Contours detected: 3	Expected: 1

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: uni00B9	Contours detected: 2	Expected: 1

- Glyph name: ordmasculine	Contours detected: 6	Expected: 2 or 3

- Glyph name: guillemotright	Contours detected: 10	Expected: 2

- Glyph name: onequarter	Contours detected: 8	Expected: 3 or 4

- Glyph name: onehalf	Contours detected: 8	Expected: 3

- Glyph name: threequarters	Contours detected: 13	Expected: 3 or 4

- Glyph name: questiondown	Contours detected: 4	Expected: 2

- Glyph name: Agrave	Contours detected: 6	Expected: 3

- Glyph name: Aacute	Contours detected: 6	Expected: 3

- Glyph name: Acircumflex	Contours detected: 7	Expected: 3

- Glyph name: Atilde	Contours detected: 7	Expected: 3

- Glyph name: Adieresis	Contours detected: 6	Expected: 4

- Glyph name: Aring	Contours detected: 5	Expected: 3 or 4

- Glyph name: Ccedilla	Contours detected: 10	Expected: 1 or 2

- Glyph name: Eacute	Contours detected: 3	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 4	Expected: 2

- Glyph name: Igrave	Contours detected: 3	Expected: 2

- Glyph name: Iacute	Contours detected: 3	Expected: 2

- Glyph name: Icircumflex	Contours detected: 4	Expected: 2

- Glyph name: Ntilde	Contours detected: 7	Expected: 2

- Glyph name: Ograve	Contours detected: 8	Expected: 3

- Glyph name: Oacute	Contours detected: 8	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 9	Expected: 3

- Glyph name: Otilde	Contours detected: 9	Expected: 3

- Glyph name: Odieresis	Contours detected: 8	Expected: 4

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: Oslash	Contours detected: 8	Expected: 2 or 3

- Glyph name: Ugrave	Contours detected: 5	Expected: 2

- Glyph name: Uacute	Contours detected: 5	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 6	Expected: 2

- Glyph name: Udieresis	Contours detected: 5	Expected: 3

- Glyph name: Yacute	Contours detected: 7	Expected: 2

- Glyph name: germandbls	Contours detected: 10	Expected: 1

- Glyph name: agrave	Contours detected: 6	Expected: 3

- Glyph name: aacute	Contours detected: 6	Expected: 3

- Glyph name: acircumflex	Contours detected: 7	Expected: 3

- Glyph name: atilde	Contours detected: 7	Expected: 3

- Glyph name: adieresis	Contours detected: 6	Expected: 4

- Glyph name: aring	Contours detected: 6	Expected: 4

- Glyph name: ccedilla	Contours detected: 7	Expected: 1 or 2

- Glyph name: eacute	Contours detected: 8	Expected: 3

- Glyph name: ecircumflex	Contours detected: 9	Expected: 3

- Glyph name: igrave	Contours detected: 3	Expected: 2

- Glyph name: iacute	Contours detected: 3	Expected: 2

- Glyph name: icircumflex	Contours detected: 4	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: ntilde	Contours detected: 6	Expected: 2

- Glyph name: ograve	Contours detected: 8	Expected: 3

- Glyph name: ocircumflex	Contours detected: 9	Expected: 3

- Glyph name: otilde	Contours detected: 9	Expected: 3

- Glyph name: odieresis	Contours detected: 8	Expected: 4

- Glyph name: oslash	Contours detected: 6	Expected: 3

- Glyph name: ugrave	Contours detected: 5	Expected: 2

- Glyph name: uacute	Contours detected: 5	Expected: 2

- Glyph name: ucircumflex	Contours detected: 6	Expected: 2

- Glyph name: udieresis	Contours detected: 5	Expected: 3

- Glyph name: yacute	Contours detected: 9	Expected: 2

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: ydieresis	Contours detected: 9	Expected: 3

- Glyph name: Amacron	Contours detected: 5	Expected: 3

- Glyph name: amacron	Contours detected: 5	Expected: 3

- Glyph name: Abreve	Contours detected: 7	Expected: 3

- Glyph name: abreve	Contours detected: 7	Expected: 3

- Glyph name: Aogonek	Contours detected: 7	Expected: 2 or 3

- Glyph name: aogonek	Contours detected: 7	Expected: 2

- Glyph name: Cacute	Contours detected: 9	Expected: 2

- Glyph name: cacute	Contours detected: 6	Expected: 2

- Glyph name: Ccircumflex	Contours detected: 10	Expected: 2

- Glyph name: ccircumflex	Contours detected: 7	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 8	Expected: 2

- Glyph name: cdotaccent	Contours detected: 5	Expected: 2

- Glyph name: Ccaron	Contours detected: 10	Expected: 2

- Glyph name: ccaron	Contours detected: 7	Expected: 2

- Glyph name: Dcaron	Contours detected: 7	Expected: 3

- Glyph name: dcaron	Contours detected: 6	Expected: 3

- Glyph name: Dcroat	Contours detected: 4	Expected: 2

- Glyph name: dcroat	Contours detected: 6	Expected: 2

- Glyph name: emacron	Contours detected: 7	Expected: 3

- Glyph name: Ebreve	Contours detected: 4	Expected: 2

- Glyph name: ebreve	Contours detected: 9	Expected: 3

- Glyph name: edotaccent	Contours detected: 7	Expected: 3

- Glyph name: Eogonek	Contours detected: 4	Expected: 1 or 2

- Glyph name: eogonek	Contours detected: 9	Expected: 2

- Glyph name: Ecaron	Contours detected: 4	Expected: 2

- Glyph name: ecaron	Contours detected: 9	Expected: 3

- Glyph name: Gcircumflex	Contours detected: 7	Expected: 2

- Glyph name: gcircumflex	Contours detected: 13	Expected: 3 or 4

- Glyph name: Gbreve	Contours detected: 7	Expected: 2

- Glyph name: gbreve	Contours detected: 13	Expected: 3 or 4

- Glyph name: Gdotaccent	Contours detected: 5	Expected: 2

- Glyph name: gdotaccent	Contours detected: 11	Expected: 3 or 4

- Glyph name: uni0122	Contours detected: 7	Expected: 2

- Glyph name: uni0123	Contours detected: 12	Expected: 3 or 4

- Glyph name: Hcircumflex	Contours detected: 4	Expected: 2

- Glyph name: hcircumflex	Contours detected: 6	Expected: 2

- Glyph name: hbar	Contours detected: 3	Expected: 1

- Glyph name: Itilde	Contours detected: 4	Expected: 2

- Glyph name: itilde	Contours detected: 4	Expected: 2

- Glyph name: Ibreve	Contours detected: 4	Expected: 2

- Glyph name: ibreve	Contours detected: 4	Expected: 2

- Glyph name: Iogonek	Contours detected: 4	Expected: 1 or 2

- Glyph name: iogonek	Contours detected: 5	Expected: 2 or 3

- Glyph name: IJ	Contours detected: 4	Expected: 1 or 2

- Glyph name: ij	Contours detected: 5	Expected: 3 or 4

- Glyph name: Jcircumflex	Contours detected: 6	Expected: 2

- Glyph name: jcircumflex	Contours detected: 6	Expected: 2

- Glyph name: uni0136	Contours detected: 9	Expected: 2 or 3

- Glyph name: uni0137	Contours detected: 11	Expected: 2 or 3

- Glyph name: kgreenlandic	Contours detected: 8	Expected: 1 or 2

- Glyph name: Lacute	Contours detected: 3	Expected: 2

- Glyph name: lacute	Contours detected: 3	Expected: 2

- Glyph name: uni013B	Contours detected: 4	Expected: 2

- Glyph name: uni013C	Contours detected: 4	Expected: 2

- Glyph name: Lcaron	Contours detected: 3	Expected: 2

- Glyph name: lcaron	Contours detected: 3	Expected: 2

- Glyph name: Lslash	Contours detected: 3	Expected: 1

- Glyph name: lslash	Contours detected: 3	Expected: 1

- Glyph name: Nacute	Contours detected: 6	Expected: 2

- Glyph name: nacute	Contours detected: 5	Expected: 2

- Glyph name: uni0145	Contours detected: 7	Expected: 2

- Glyph name: uni0146	Contours detected: 6	Expected: 2

- Glyph name: Ncaron	Contours detected: 7	Expected: 2

- Glyph name: ncaron	Contours detected: 6	Expected: 2

- Glyph name: napostrophe	Contours detected: 5	Expected: 2

- Glyph name: Eng	Contours detected: 3	Expected: 1

- Glyph name: eng	Contours detected: 3	Expected: 1

- Glyph name: Omacron	Contours detected: 7	Expected: 3

- Glyph name: omacron	Contours detected: 7	Expected: 3

- Glyph name: Obreve	Contours detected: 9	Expected: 3

- Glyph name: obreve	Contours detected: 9	Expected: 3

- Glyph name: Ohungarumlaut	Contours detected: 10	Expected: 4

- Glyph name: ohungarumlaut	Contours detected: 10	Expected: 4

- Glyph name: OE	Contours detected: 6	Expected: 2

- Glyph name: oe	Contours detected: 7	Expected: 3

- Glyph name: Racute	Contours detected: 6	Expected: 3

- Glyph name: racute	Contours detected: 5	Expected: 2

- Glyph name: uni0156	Contours detected: 7	Expected: 3

- Glyph name: uni0157	Contours detected: 6	Expected: 2

- Glyph name: Rcaron	Contours detected: 7	Expected: 3

- Glyph name: rcaron	Contours detected: 6	Expected: 2

- Glyph name: Sacute	Contours detected: 6	Expected: 2

- Glyph name: sacute	Contours detected: 6	Expected: 2

- Glyph name: Scircumflex	Contours detected: 7	Expected: 2

- Glyph name: scircumflex	Contours detected: 7	Expected: 2

- Glyph name: Scedilla	Contours detected: 7	Expected: 1 or 2

- Glyph name: scedilla	Contours detected: 7	Expected: 1 or 2

- Glyph name: Scaron	Contours detected: 7	Expected: 2

- Glyph name: scaron	Contours detected: 7	Expected: 2

- Glyph name: uni0162	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 5	Expected: 1 or 2

- Glyph name: Tcaron	Contours detected: 4	Expected: 2

- Glyph name: tcaron	Contours detected: 5	Expected: 2

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: Utilde	Contours detected: 6	Expected: 2

- Glyph name: utilde	Contours detected: 6	Expected: 2

- Glyph name: Umacron	Contours detected: 4	Expected: 2

- Glyph name: umacron	Contours detected: 4	Expected: 2

- Glyph name: Ubreve	Contours detected: 6	Expected: 2

- Glyph name: ubreve	Contours detected: 6	Expected: 2

- Glyph name: Uring	Contours detected: 5	Expected: 3

- Glyph name: uring	Contours detected: 5	Expected: 3

- Glyph name: Uhungarumlaut	Contours detected: 7	Expected: 3

- Glyph name: uhungarumlaut	Contours detected: 7	Expected: 3

- Glyph name: Uogonek	Contours detected: 6	Expected: 1

- Glyph name: uogonek	Contours detected: 6	Expected: 1

- Glyph name: Wcircumflex	Contours detected: 9	Expected: 2

- Glyph name: wcircumflex	Contours detected: 10	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 8	Expected: 2

- Glyph name: ycircumflex	Contours detected: 10	Expected: 2

- Glyph name: Zacute	Contours detected: 8	Expected: 2

- Glyph name: zacute	Contours detected: 7	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 7	Expected: 2

- Glyph name: zdotaccent	Contours detected: 6	Expected: 2

- Glyph name: Zcaron	Contours detected: 9	Expected: 2

- Glyph name: zcaron	Contours detected: 8	Expected: 2

- Glyph name: longs	Contours detected: 3	Expected: 1

- Glyph name: uni0180	Contours detected: 6	Expected: 2

- Glyph name: uni0181	Contours detected: 6	Expected: 3

- Glyph name: uni0186	Contours detected: 4	Expected: 1

- Glyph name: Eth	Contours detected: 4	Expected: 2

- Glyph name: uni018A	Contours detected: 4	Expected: 2

- Glyph name: uni0190	Contours detected: 4	Expected: 1

- Glyph name: uni0191	Contours detected: 2	Expected: 1

- Glyph name: florin	Contours detected: 3	Expected: 1

- Glyph name: uni0194	Contours detected: 3	Expected: 2

- Glyph name: ohorn	Contours detected: 6	Expected: 2

- Glyph name: Uhorn	Contours detected: 3	Expected: 1

- Glyph name: uhorn	Contours detected: 4	Expected: 1

- Glyph name: uni01B2	Contours detected: 4	Expected: 1

- Glyph name: uni01B5	Contours detected: 8	Expected: 1

- Glyph name: uni01B6	Contours detected: 7	Expected: 1

- Glyph name: uni01CD	Contours detected: 7	Expected: 3

- Glyph name: uni01CE	Contours detected: 7	Expected: 3

- Glyph name: uni01CF	Contours detected: 4	Expected: 2

- Glyph name: uni01D0	Contours detected: 4	Expected: 2

- Glyph name: uni01D1	Contours detected: 9	Expected: 3

- Glyph name: uni01D2	Contours detected: 9	Expected: 3

- Glyph name: uni01D3	Contours detected: 6	Expected: 2

- Glyph name: uni01D4	Contours detected: 6	Expected: 2

- Glyph name: uni01D5	Contours detected: 6	Expected: 4

- Glyph name: uni01D6	Contours detected: 6	Expected: 4

- Glyph name: uni01D7	Contours detected: 7	Expected: 4

- Glyph name: uni01D8	Contours detected: 7	Expected: 4

- Glyph name: uni01D9	Contours detected: 8	Expected: 4

- Glyph name: uni01DA	Contours detected: 8	Expected: 4

- Glyph name: uni01DB	Contours detected: 7	Expected: 4

- Glyph name: uni01DC	Contours detected: 7	Expected: 4

- Glyph name: uni01E3	Contours detected: 9	Expected: 4

- Glyph name: Gcaron	Contours detected: 7	Expected: 2

- Glyph name: gcaron	Contours detected: 13	Expected: 3 or 4

- Glyph name: uni01E8	Contours detected: 9	Expected: 2

- Glyph name: uni01E9	Contours detected: 11	Expected: 2

- Glyph name: uni01EA	Contours detected: 9	Expected: 2

- Glyph name: uni01EB	Contours detected: 9	Expected: 2

- Glyph name: uni01EE	Contours detected: 7	Expected: 2

- Glyph name: uni01EF	Contours detected: 7	Expected: 2

- Glyph name: uni01F0	Contours detected: 6	Expected: 2

- Glyph name: uni01F4	Contours detected: 6	Expected: 2

- Glyph name: uni01F5	Contours detected: 12	Expected: 3

- Glyph name: uni01F8	Contours detected: 6	Expected: 2

- Glyph name: uni01F9	Contours detected: 5	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: aeacute	Contours detected: 10	Expected: 4

- Glyph name: Oslashacute	Contours detected: 10	Expected: 4

- Glyph name: oslashacute	Contours detected: 8	Expected: 4

- Glyph name: uni0200	Contours detected: 8	Expected: 4

- Glyph name: uni0201	Contours detected: 8	Expected: 4

- Glyph name: uni0202	Contours detected: 5	Expected: 3

- Glyph name: uni0203	Contours detected: 5	Expected: 3

- Glyph name: uni0204	Contours detected: 5	Expected: 3

- Glyph name: uni0205	Contours detected: 10	Expected: 4

- Glyph name: uni0207	Contours detected: 7	Expected: 3

- Glyph name: uni0208	Contours detected: 5	Expected: 3

- Glyph name: uni0209	Contours detected: 5	Expected: 3

- Glyph name: uni020C	Contours detected: 10	Expected: 4

- Glyph name: uni020D	Contours detected: 10	Expected: 4

- Glyph name: uni020E	Contours detected: 7	Expected: 3

- Glyph name: uni020F	Contours detected: 7	Expected: 3

- Glyph name: uni0210	Contours detected: 8	Expected: 4

- Glyph name: uni0211	Contours detected: 7	Expected: 3

- Glyph name: uni0212	Contours detected: 5	Expected: 3

- Glyph name: uni0213	Contours detected: 4	Expected: 2

- Glyph name: uni0214	Contours detected: 7	Expected: 3

- Glyph name: uni0215	Contours detected: 7	Expected: 3

- Glyph name: uni0216	Contours detected: 4	Expected: 2

- Glyph name: uni0217	Contours detected: 4	Expected: 2

- Glyph name: uni0218	Contours detected: 7	Expected: 2

- Glyph name: uni0219	Contours detected: 7	Expected: 2

- Glyph name: uni021A	Contours detected: 4	Expected: 2

- Glyph name: uni021B	Contours detected: 5	Expected: 2

- Glyph name: uni021E	Contours detected: 4	Expected: 2

- Glyph name: uni021F	Contours detected: 6	Expected: 2

- Glyph name: uni0226	Contours detected: 5	Expected: 3

- Glyph name: uni0227	Contours detected: 5	Expected: 3

- Glyph name: uni0228	Contours detected: 4	Expected: 1

- Glyph name: uni0229	Contours detected: 9	Expected: 2

- Glyph name: uni022E	Contours detected: 7	Expected: 3

- Glyph name: uni022F	Contours detected: 7	Expected: 3

- Glyph name: uni0232	Contours detected: 6	Expected: 2

- Glyph name: uni0233	Contours detected: 8	Expected: 2

- Glyph name: uni0237	Contours detected: 3	Expected: 1

- Glyph name: uni0243	Contours detected: 5	Expected: 3

- Glyph name: uni0248	Contours detected: 3	Expected: 1

- Glyph name: uni0249	Contours detected: 4	Expected: 2

- Glyph name: tilde	Contours detected: 3	Expected: 1

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: gravecomb	Contours detected: 2	Expected: 1

- Glyph name: acutecomb	Contours detected: 2	Expected: 1

- Glyph name: uni0302	Contours detected: 3	Expected: 1

- Glyph name: tildecomb	Contours detected: 3	Expected: 1

- Glyph name: uni0306	Contours detected: 3	Expected: 1

- Glyph name: hookabovecomb	Contours detected: 3	Expected: 1

- Glyph name: uni030B	Contours detected: 4	Expected: 2

- Glyph name: uni030C	Contours detected: 3	Expected: 1

- Glyph name: uni030F	Contours detected: 4	Expected: 2

- Glyph name: uni0312	Contours detected: 2	Expected: 1

- Glyph name: uni0313	Contours detected: 2	Expected: 1

- Glyph name: uni031B	Contours detected: 2	Expected: 1

- Glyph name: uni0327	Contours detected: 3	Expected: 1

- Glyph name: uni0328	Contours detected: 3	Expected: 1

- Glyph name: uni0337	Contours detected: 5	Expected: 1

- Glyph name: uni0338	Contours detected: 6	Expected: 1

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: dieresistonos	Contours detected: 4	Expected: 3

- Glyph name: Alphatonos	Contours detected: 6	Expected: 3

- Glyph name: Epsilontonos	Contours detected: 3	Expected: 2

- Glyph name: Etatonos	Contours detected: 3	Expected: 2

- Glyph name: Iotatonos	Contours detected: 3	Expected: 2

- Glyph name: Omicrontonos	Contours detected: 8	Expected: 3

- Glyph name: Upsilontonos	Contours detected: 7	Expected: 2

- Glyph name: Omegatonos	Contours detected: 7	Expected: 2

- Glyph name: iotadieresistonos	Contours detected: 6	Expected: 4

- Glyph name: uni0394	Contours detected: 4	Expected: 2

- Glyph name: Z	Contours detected: 6	Expected: 1

- Glyph name: Theta	Contours detected: 8	Expected: 3

- Glyph name: Lambda	Contours detected: 4	Expected: 1

- Glyph name: N	Contours detected: 4	Expected: 1

- Glyph name: Sigma	Contours detected: 8	Expected: 1

- Glyph name: Y	Contours detected: 5	Expected: 1

- Glyph name: Psi	Contours detected: 3	Expected: 1

- Glyph name: uni03A9	Contours detected: 5	Expected: 1

- Glyph name: Ydieresis	Contours detected: 7	Expected: 3

- Glyph name: alphatonos	Contours detected: 11	Expected: 3

- Glyph name: epsilontonos	Contours detected: 9	Expected: 2

- Glyph name: etatonos	Contours detected: 5	Expected: 2

- Glyph name: iotatonos	Contours detected: 4	Expected: 2

- Glyph name: upsilondieresistonos	Contours detected: 9	Expected: 4

- Glyph name: alpha	Contours detected: 9	Expected: 2

- Glyph name: beta	Contours detected: 6	Expected: 2

- Glyph name: gamma	Contours detected: 6	Expected: 1 or 2

- Glyph name: delta	Contours detected: 3	Expected: 2

- Glyph name: uni025B	Contours detected: 7	Expected: 1

- Glyph name: zeta	Contours detected: 11	Expected: 1

- Glyph name: eta	Contours detected: 3	Expected: 1

- Glyph name: theta	Contours detected: 7	Expected: 3

- Glyph name: iota	Contours detected: 2	Expected: 1

- Glyph name: kappa	Contours detected: 8	Expected: 1

- Glyph name: lambda	Contours detected: 7	Expected: 1

- Glyph name: uni03BC	Contours detected: 3	Expected: 1

- Glyph name: nu	Contours detected: 6	Expected: 1

- Glyph name: xi	Contours detected: 12	Expected: 1

- Glyph name: pi	Contours detected: 2	Expected: 1

- Glyph name: rho	Contours detected: 4	Expected: 2

- Glyph name: sigma1	Contours detected: 7	Expected: 1

- Glyph name: sigma	Contours detected: 3	Expected: 2

- Glyph name: upsilon	Contours detected: 5	Expected: 1

- Glyph name: phi	Contours detected: 9	Expected: 2 or 3

- Glyph name: chi	Contours detected: 10	Expected: 1

- Glyph name: psi	Contours detected: 6	Expected: 1

- Glyph name: omega	Contours detected: 6	Expected: 1

- Glyph name: iotadieresis	Contours detected: 4	Expected: 3

- Glyph name: upsilondieresis	Contours detected: 7	Expected: 3

- Glyph name: oacute	Contours detected: 8	Expected: 3

- Glyph name: upsilontonos	Contours detected: 7	Expected: 2

- Glyph name: omegatonos	Contours detected: 8	Expected: 2

- Glyph name: Egrave	Contours detected: 3	Expected: 2

- Glyph name: uni0402	Contours detected: 4	Expected: 1

- Glyph name: uni0403	Contours detected: 3	Expected: 2

- Glyph name: uni0404	Contours detected: 7	Expected: 1

- Glyph name: S	Contours detected: 4	Expected: 1

- Glyph name: J	Contours detected: 3	Expected: 1

- Glyph name: uni0409	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 8	Expected: 2

- Glyph name: uni040D	Contours detected: 6	Expected: 2

- Glyph name: uni040E	Contours detected: 10	Expected: 2

- Glyph name: A	Contours detected: 4	Expected: 2

- Glyph name: uni0411	Contours detected: 4	Expected: 2

- Glyph name: B	Contours detected: 5	Expected: 3

- Glyph name: uni0414	Contours detected: 1	Expected: 2

- Glyph name: uni0416	Contours detected: 13	Expected: 1

- Glyph name: uni0417	Contours detected: 5	Expected: 1

- Glyph name: uni0418	Contours detected: 4	Expected: 1

- Glyph name: uni0419	Contours detected: 7	Expected: 2

- Glyph name: K	Contours detected: 6	Expected: 1

- Glyph name: uni041B	Contours detected: 2	Expected: 1

- Glyph name: M	Contours detected: 5	Expected: 1

- Glyph name: O	Contours detected: 6	Expected: 2

- Glyph name: C	Contours detected: 7	Expected: 1

- Glyph name: uni0423	Contours detected: 7	Expected: 1

- Glyph name: X	Contours detected: 9	Expected: 1

- Glyph name: uni0427	Contours detected: 2	Expected: 1

- Glyph name: uni042D	Contours detected: 7	Expected: 1

- Glyph name: uni042E	Contours detected: 8	Expected: 2

- Glyph name: uni042F	Contours detected: 4	Expected: 2

- Glyph name: a	Contours detected: 4	Expected: 2

- Glyph name: uni0431	Contours detected: 5	Expected: 2

- Glyph name: uni0432	Contours detected: 2	Expected: 3

- Glyph name: uni0434	Contours detected: 1	Expected: 2

- Glyph name: e	Contours detected: 6	Expected: 2

- Glyph name: uni0436	Contours detected: 13	Expected: 1

- Glyph name: uni0437	Contours detected: 5	Expected: 1

- Glyph name: uni0438	Contours detected: 4	Expected: 1

- Glyph name: uni0439	Contours detected: 7	Expected: 2

- Glyph name: uni043A	Contours detected: 8	Expected: 1

- Glyph name: uni043B	Contours detected: 2	Expected: 1

- Glyph name: uni043C	Contours detected: 5	Expected: 1

- Glyph name: o	Contours detected: 6	Expected: 2

- Glyph name: p	Contours detected: 3	Expected: 2

- Glyph name: c	Contours detected: 4	Expected: 1

- Glyph name: y	Contours detected: 7	Expected: 1

- Glyph name: uni0444	Contours detected: 8	Expected: 3

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: uni0447	Contours detected: 2	Expected: 1

- Glyph name: uni044A	Contours detected: 4	Expected: 2

- Glyph name: uni044B	Contours detected: 5	Expected: 3

- Glyph name: uni044C	Contours detected: 4	Expected: 2

- Glyph name: uni044D	Contours detected: 7	Expected: 1

- Glyph name: uni044E	Contours detected: 4	Expected: 2

- Glyph name: uni044F	Contours detected: 4	Expected: 2

- Glyph name: egrave	Contours detected: 8	Expected: 3

- Glyph name: edieresis	Contours detected: 8	Expected: 4

- Glyph name: uni0452	Contours detected: 4	Expected: 1

- Glyph name: uni0453	Contours detected: 3	Expected: 2

- Glyph name: uni0454	Contours detected: 4	Expected: 1

- Glyph name: s	Contours detected: 4	Expected: 1

- Glyph name: j	Contours detected: 4	Expected: 2

- Glyph name: uni0459	Contours detected: 3	Expected: 2

- Glyph name: uni045C	Contours detected: 10	Expected: 2

- Glyph name: uni045D	Contours detected: 6	Expected: 2

- Glyph name: uni045E	Contours detected: 10	Expected: 2

- Glyph name: uni0496	Contours detected: 13	Expected: 1 or 2

- Glyph name: uni0497	Contours detected: 13	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 8	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni04AE	Contours detected: 5	Expected: 1

- Glyph name: uni04AF	Contours detected: 5	Expected: 1

- Glyph name: uni04B0	Contours detected: 5	Expected: 1

- Glyph name: uni04B1	Contours detected: 5	Expected: 1

- Glyph name: uni04BA	Contours detected: 2	Expected: 1

- Glyph name: uni04BB	Contours detected: 4	Expected: 1

- Glyph name: uni04C1	Contours detected: 16	Expected: 2

- Glyph name: uni04C2	Contours detected: 16	Expected: 2

- Glyph name: uni04D0	Contours detected: 7	Expected: 3

- Glyph name: uni04D1	Contours detected: 7	Expected: 3

- Glyph name: uni04D2	Contours detected: 6	Expected: 4

- Glyph name: uni04D3	Contours detected: 6	Expected: 4

- Glyph name: ae	Contours detected: 8	Expected: 3

- Glyph name: uni04D6	Contours detected: 4	Expected: 2

- Glyph name: uni04D7	Contours detected: 9	Expected: 3

- Glyph name: uni018F	Contours detected: 5	Expected: 2

- Glyph name: uni0259	Contours detected: 4	Expected: 2

- Glyph name: uni04DA	Contours detected: 7	Expected: 4

- Glyph name: uni04DB	Contours detected: 6	Expected: 4

- Glyph name: uni04DC	Contours detected: 15	Expected: 3

- Glyph name: uni04DD	Contours detected: 15	Expected: 3

- Glyph name: uni04DE	Contours detected: 7	Expected: 3

- Glyph name: uni04DF	Contours detected: 7	Expected: 3

- Glyph name: uni01B7	Contours detected: 4	Expected: 1

- Glyph name: uni0292	Contours detected: 4	Expected: 1

- Glyph name: uni04E2	Contours detected: 5	Expected: 2

- Glyph name: uni04E3	Contours detected: 5	Expected: 2

- Glyph name: uni04E4	Contours detected: 6	Expected: 3

- Glyph name: uni04E5	Contours detected: 6	Expected: 3

- Glyph name: uni04E6	Contours detected: 8	Expected: 4

- Glyph name: uni04E7	Contours detected: 8	Expected: 4

- Glyph name: uni04E8	Contours detected: 7	Expected: 3

- Glyph name: uni04E9	Contours detected: 7	Expected: 3

- Glyph name: uni04EA	Contours detected: 9	Expected: 5

- Glyph name: uni04EB	Contours detected: 9	Expected: 5

- Glyph name: uni04EC	Contours detected: 9	Expected: 3

- Glyph name: uni04ED	Contours detected: 9	Expected: 3

- Glyph name: uni04EE	Contours detected: 8	Expected: 2

- Glyph name: uni04EF	Contours detected: 8	Expected: 2

- Glyph name: uni04F0	Contours detected: 9	Expected: 3

- Glyph name: uni04F1	Contours detected: 9	Expected: 3

- Glyph name: uni04F2	Contours detected: 11	Expected: 3

- Glyph name: uni04F3	Contours detected: 11	Expected: 3

- Glyph name: uni04F4	Contours detected: 4	Expected: 3

- Glyph name: uni04F5	Contours detected: 4	Expected: 3

- Glyph name: uni04F9	Contours detected: 7	Expected: 5

- Glyph name: uni0E01	Contours detected: 3	Expected: 1

- Glyph name: uni0E02	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E03	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E04	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E05	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E06	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E07	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E08	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E09	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E0A	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E0B	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E0C	Contours detected: 5	Expected: 1 or 3

- Glyph name: uni0E10	Contours detected: 7	Expected: 1 or 5

- Glyph name: uni0E11	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E12	Contours detected: 6	Expected: 1 or 3

- Glyph name: uni0E14	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E15	Contours detected: 7	Expected: 1 or 2

- Glyph name: uni0E16	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E17	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E18	Contours detected: 3	Expected: 1

- Glyph name: uni0E1C	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E1D	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E1E	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E1F	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E20	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E24	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E25	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E26	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E27	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E28	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E2A	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E2B	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E2C	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E2D	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E2F	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E32	Contours detected: 3	Expected: 1

- Glyph name: uni0E33	Contours detected: 5	Expected: 3

- Glyph name: uni0E43	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E44	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E45	Contours detected: 3	Expected: 1

- Glyph name: uni0E46	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E47	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E49	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E4E	Contours detected: 5	Expected: 1

- Glyph name: uni0E4F	Contours detected: 10	Expected: 4

- Glyph name: uni0E50	Contours detected: 6	Expected: 2

- Glyph name: uni0E51	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E52	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E53	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E54	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E55	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E56	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E57	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E58	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E59	Contours detected: 8	Expected: 1 or 2

- Glyph name: uni0E5A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E5B	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni1E00	Contours detected: 6	Expected: 4

- Glyph name: uni1E01	Contours detected: 6	Expected: 4

- Glyph name: uni1E02	Contours detected: 6	Expected: 4

- Glyph name: uni1E03	Contours detected: 7	Expected: 3

- Glyph name: uni1E0A	Contours detected: 5	Expected: 3

- Glyph name: uni1E0B	Contours detected: 4	Expected: 3

- Glyph name: uni1E0C	Contours detected: 5	Expected: 3

- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

- Glyph name: uni1E0E	Contours detected: 5	Expected: 3

- Glyph name: uni1E0F	Contours detected: 4	Expected: 3

- Glyph name: uni1E1F	Contours detected: 3	Expected: 2

- Glyph name: uni1E20	Contours detected: 5	Expected: 2

- Glyph name: uni1E21	Contours detected: 11	Expected: 3 or 4

- Glyph name: uni1E25	Contours detected: 4	Expected: 2

- Glyph name: uni1E2B	Contours detected: 4	Expected: 2

- Glyph name: uni1E3E	Contours detected: 7	Expected: 2

- Glyph name: uni1E3F	Contours detected: 5	Expected: 2

- Glyph name: uni1E40	Contours detected: 6	Expected: 2

- Glyph name: uni1E41	Contours detected: 4	Expected: 2

- Glyph name: uni1E42	Contours detected: 6	Expected: 2

- Glyph name: uni1E43	Contours detected: 4	Expected: 2

- Glyph name: uni1E44	Contours detected: 5	Expected: 2

- Glyph name: uni1E45	Contours detected: 4	Expected: 2

- Glyph name: uni1E46	Contours detected: 5	Expected: 2

- Glyph name: uni1E47	Contours detected: 4	Expected: 2

- Glyph name: uni1E48	Contours detected: 5	Expected: 2

- Glyph name: uni1E49	Contours detected: 4	Expected: 2

- Glyph name: uni1E57	Contours detected: 4	Expected: 3

- Glyph name: uni1E5A	Contours detected: 5	Expected: 3

- Glyph name: uni1E5B	Contours detected: 4	Expected: 2

- Glyph name: uni1E5E	Contours detected: 5	Expected: 3

- Glyph name: uni1E5F	Contours detected: 4	Expected: 2

- Glyph name: uni1E60	Contours detected: 5	Expected: 2

- Glyph name: uni1E61	Contours detected: 5	Expected: 2

- Glyph name: uni1E62	Contours detected: 5	Expected: 2

- Glyph name: uni1E63	Contours detected: 5	Expected: 2

- Glyph name: uni1E6B	Contours detected: 3	Expected: 2

- Glyph name: uni1E6D	Contours detected: 3	Expected: 2

- Glyph name: uni1E6F	Contours detected: 3	Expected: 2

- Glyph name: Wgrave	Contours detected: 8	Expected: 2

- Glyph name: wgrave	Contours detected: 9	Expected: 2

- Glyph name: Wacute	Contours detected: 8	Expected: 2

- Glyph name: wacute	Contours detected: 9	Expected: 2

- Glyph name: Wdieresis	Contours detected: 8	Expected: 3

- Glyph name: wdieresis	Contours detected: 9	Expected: 3

- Glyph name: uni1E8E	Contours detected: 6	Expected: 2

- Glyph name: uni1E8F	Contours detected: 8	Expected: 2

- Glyph name: uni1E92	Contours detected: 7	Expected: 2

- Glyph name: uni1E93	Contours detected: 6	Expected: 2

- Glyph name: uni1E97	Contours detected: 4	Expected: 3

- Glyph name: uni1E9E	Contours detected: 3	Expected: 1

- Glyph name: uni1EA0	Contours detected: 5	Expected: 3

- Glyph name: uni1EA1	Contours detected: 5	Expected: 3

- Glyph name: uni1EA2	Contours detected: 7	Expected: 3

- Glyph name: uni1EA3	Contours detected: 7	Expected: 3

- Glyph name: uni1EA4	Contours detected: 9	Expected: 4

- Glyph name: uni1EA5	Contours detected: 9	Expected: 4

- Glyph name: uni1EA6	Contours detected: 9	Expected: 4

- Glyph name: uni1EA7	Contours detected: 9	Expected: 4

- Glyph name: uni1EA8	Contours detected: 10	Expected: 4

- Glyph name: uni1EA9	Contours detected: 10	Expected: 4

- Glyph name: uni1EAA	Contours detected: 10	Expected: 4

- Glyph name: uni1EAB	Contours detected: 10	Expected: 4

- Glyph name: uni1EAC	Contours detected: 8	Expected: 4

- Glyph name: uni1EAD	Contours detected: 8	Expected: 4

- Glyph name: uni1EAE	Contours detected: 9	Expected: 4

- Glyph name: uni1EAF	Contours detected: 9	Expected: 4

- Glyph name: uni1EB0	Contours detected: 9	Expected: 4

- Glyph name: uni1EB1	Contours detected: 9	Expected: 4

- Glyph name: uni1EB2	Contours detected: 10	Expected: 4

- Glyph name: uni1EB3	Contours detected: 10	Expected: 4

- Glyph name: uni1EB4	Contours detected: 10	Expected: 4

- Glyph name: uni1EB5	Contours detected: 10	Expected: 4

- Glyph name: uni1EB6	Contours detected: 8	Expected: 4

- Glyph name: uni1EB7	Contours detected: 8	Expected: 4

- Glyph name: uni1EB9	Contours detected: 7	Expected: 3

- Glyph name: uni1EBA	Contours detected: 4	Expected: 2

- Glyph name: uni1EBB	Contours detected: 9	Expected: 3

- Glyph name: uni1EBC	Contours detected: 4	Expected: 2

- Glyph name: uni1EBD	Contours detected: 9	Expected: 3

- Glyph name: uni1EBE	Contours detected: 6	Expected: 3

- Glyph name: uni1EBF	Contours detected: 11	Expected: 4

- Glyph name: uni1EC0	Contours detected: 6	Expected: 3

- Glyph name: uni1EC1	Contours detected: 11	Expected: 4

- Glyph name: uni1EC2	Contours detected: 7	Expected: 3

- Glyph name: uni1EC3	Contours detected: 12	Expected: 4

- Glyph name: uni1EC4	Contours detected: 7	Expected: 3

- Glyph name: uni1EC5	Contours detected: 12	Expected: 4

- Glyph name: uni1EC6	Contours detected: 5	Expected: 3

- Glyph name: uni1EC7	Contours detected: 10	Expected: 4

- Glyph name: uni1EC8	Contours detected: 4	Expected: 2

- Glyph name: uni1EC9	Contours detected: 4	Expected: 2

- Glyph name: uni1ECC	Contours detected: 7	Expected: 3

- Glyph name: uni1ECD	Contours detected: 7	Expected: 3

- Glyph name: uni1ECE	Contours detected: 9	Expected: 3

- Glyph name: uni1ECF	Contours detected: 9	Expected: 3

- Glyph name: uni1ED0	Contours detected: 11	Expected: 4

- Glyph name: uni1ED1	Contours detected: 11	Expected: 4

- Glyph name: uni1ED2	Contours detected: 11	Expected: 4

- Glyph name: uni1ED3	Contours detected: 11	Expected: 4

- Glyph name: uni1ED4	Contours detected: 12	Expected: 4

- Glyph name: uni1ED5	Contours detected: 12	Expected: 4

- Glyph name: uni1ED6	Contours detected: 12	Expected: 4

- Glyph name: uni1ED7	Contours detected: 12	Expected: 4

- Glyph name: uni1ED8	Contours detected: 10	Expected: 4

- Glyph name: uni1ED9	Contours detected: 10	Expected: 4

- Glyph name: uni1EDA	Contours detected: 5	Expected: 3 or 4

- Glyph name: uni1EDB	Contours detected: 8	Expected: 3

- Glyph name: uni1EDC	Contours detected: 5	Expected: 3 or 4

- Glyph name: uni1EDD	Contours detected: 8	Expected: 3

- Glyph name: uni1EDE	Contours detected: 6	Expected: 3 or 4

- Glyph name: uni1EDF	Contours detected: 9	Expected: 3

- Glyph name: uni1EE0	Contours detected: 6	Expected: 3 or 4

- Glyph name: uni1EE1	Contours detected: 9	Expected: 3

- Glyph name: uni1EE3	Contours detected: 7	Expected: 3

- Glyph name: uni1EE4	Contours detected: 4	Expected: 2

- Glyph name: uni1EE5	Contours detected: 4	Expected: 2

- Glyph name: uni1EE6	Contours detected: 6	Expected: 2

- Glyph name: uni1EE7	Contours detected: 6	Expected: 2

- Glyph name: uni1EE8	Contours detected: 5	Expected: 2

- Glyph name: uni1EE9	Contours detected: 6	Expected: 2

- Glyph name: uni1EEA	Contours detected: 5	Expected: 2

- Glyph name: uni1EEB	Contours detected: 6	Expected: 2

- Glyph name: uni1EEC	Contours detected: 6	Expected: 2

- Glyph name: uni1EED	Contours detected: 7	Expected: 2

- Glyph name: uni1EEE	Contours detected: 6	Expected: 2

- Glyph name: uni1EEF	Contours detected: 7	Expected: 2

- Glyph name: uni1EF0	Contours detected: 4	Expected: 2

- Glyph name: uni1EF1	Contours detected: 5	Expected: 2

- Glyph name: Ygrave	Contours detected: 7	Expected: 2

- Glyph name: ygrave	Contours detected: 9	Expected: 2

- Glyph name: uni1EF4	Contours detected: 6	Expected: 2

- Glyph name: uni1EF5	Contours detected: 8	Expected: 2

- Glyph name: uni1EF6	Contours detected: 8	Expected: 2

- Glyph name: uni1EF7	Contours detected: 10	Expected: 2

- Glyph name: uni1EF8	Contours detected: 8	Expected: 2

- Glyph name: uni1EF9	Contours detected: 10	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: perthousand	Contours detected: 18	Expected: 6 or 7

- Glyph name: fraction	Contours detected: 8	Expected: 1

- Glyph name: uni2075	Contours detected: 5	Expected: 1

- Glyph name: uni2076	Contours detected: 4	Expected: 2

- Glyph name: uni2077	Contours detected: 4	Expected: 1

- Glyph name: uni2078	Contours detected: 7	Expected: 3

- Glyph name: uni2079	Contours detected: 5	Expected: 2

- Glyph name: uni207D	Contours detected: 5	Expected: 1

- Glyph name: uni207E	Contours detected: 5	Expected: 1

- Glyph name: uni207F	Contours detected: 3	Expected: 1

- Glyph name: uni2081	Contours detected: 2	Expected: 1

- Glyph name: uni2082	Contours detected: 6	Expected: 1

- Glyph name: uni2083	Contours detected: 7	Expected: 1

- Glyph name: uni2085	Contours detected: 5	Expected: 1

- Glyph name: uni2086	Contours detected: 4	Expected: 2

- Glyph name: uni2087	Contours detected: 4	Expected: 1

- Glyph name: uni2088	Contours detected: 7	Expected: 3

- Glyph name: uni2089	Contours detected: 5	Expected: 2

- Glyph name: uni208D	Contours detected: 5	Expected: 1

- Glyph name: uni208E	Contours detected: 5	Expected: 1

- Glyph name: Euro	Contours detected: 7	Expected: 1 or 2

- Glyph name: uni20AD	Contours detected: 7	Expected: 1

- Glyph name: uni2113	Contours detected: 12	Expected: 2

- Glyph name: trademark	Contours detected: 3	Expected: 2

- Glyph name: Omega	Contours detected: 5	Expected: 1

- Glyph name: arrowleft	Contours detected: 3	Expected: 1

- Glyph name: arrowup	Contours detected: 5	Expected: 1

- Glyph name: arrowright	Contours detected: 5	Expected: 1

- Glyph name: arrowdown	Contours detected: 5	Expected: 1

- Glyph name: arrowboth	Contours detected: 9	Expected: 1

- Glyph name: arrowupdn	Contours detected: 9	Expected: 1

- Glyph name: uni2196	Contours detected: 13	Expected: 1

- Glyph name: uni2197	Contours detected: 13	Expected: 1

- Glyph name: uni2198	Contours detected: 13	Expected: 1

- Glyph name: uni2199	Contours detected: 13	Expected: 1

- Glyph name: carriagereturn	Contours detected: 3	Expected: 1

- Glyph name: uni21C4	Contours detected: 10	Expected: 2

- Glyph name: arrowdblright	Contours detected: 7	Expected: 1

- Glyph name: arrowdblboth	Contours detected: 12	Expected: 2

- Glyph name: uni21E5	Contours detected: 6	Expected: 2

- Glyph name: universal	Contours detected: 7	Expected: 2

- Glyph name: partialdiff	Contours detected: 6	Expected: 2

- Glyph name: emptyset	Contours detected: 8	Expected: 3

- Glyph name: Delta	Contours detected: 4	Expected: 2

- Glyph name: gradient	Contours detected: 3	Expected: 2

- Glyph name: element	Contours detected: 7	Expected: 1

- Glyph name: notelement	Contours detected: 5	Expected: 3

- Glyph name: suchthat	Contours detected: 7	Expected: 1

- Glyph name: summation	Contours detected: 8	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 6	Expected: 1

- Glyph name: proportional	Contours detected: 10	Expected: 2

- Glyph name: infinity	Contours detected: 7	Expected: 3

- Glyph name: angle	Contours detected: 9	Expected: 1

- Glyph name: uni2226	Contours detected: 4	Expected: 1

- Glyph name: logicaland	Contours detected: 7	Expected: 1

- Glyph name: logicalor	Contours detected: 9	Expected: 1

- Glyph name: intersection	Contours detected: 5	Expected: 1

- Glyph name: union	Contours detected: 7	Expected: 1

- Glyph name: integral	Contours detected: 8	Expected: 1

- Glyph name: uni222C	Contours detected: 16	Expected: 2

- Glyph name: uni223D	Contours detected: 10	Expected: 1

- Glyph name: uni2243	Contours detected: 9	Expected: 2

- Glyph name: congruent	Contours detected: 10	Expected: 3

- Glyph name: approxequal	Contours detected: 16	Expected: 2

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: uni2262	Contours detected: 3	Expected: 1

- Glyph name: lessequal	Contours detected: 9	Expected: 2

- Glyph name: greaterequal	Contours detected: 9	Expected: 2

- Glyph name: uni226A	Contours detected: 22	Expected: 2

- Glyph name: uni226B	Contours detected: 22	Expected: 2

- Glyph name: propersubset	Contours detected: 7	Expected: 1

- Glyph name: propersuperset	Contours detected: 7	Expected: 1

- Glyph name: notsubset	Contours detected: 9	Expected: 2

- Glyph name: uni2285	Contours detected: 7	Expected: 2

- Glyph name: reflexsubset	Contours detected: 6	Expected: 2

- Glyph name: reflexsuperset	Contours detected: 6	Expected: 2

- Glyph name: circleplus	Contours detected: 11	Expected: 3

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 8	Expected: 1

- Glyph name: uni2572	Contours detected: 8	Expected: 1

- Glyph name: uni2573	Contours detected: 13	Expected: 1

- Glyph name: uni25B3	Contours detected: 10	Expected: 2

- Glyph name: uni25B7	Contours detected: 12	Expected: 2

- Glyph name: uni25BD	Contours detected: 6	Expected: 2

- Glyph name: uni25C1	Contours detected: 12	Expected: 2

- Glyph name: uni25C7	Contours detected: 15	Expected: 2

- Glyph name: uni25C9	Contours detected: 9	Expected: 3

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: circle	Contours detected: 3	Expected: 2

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: musicalnote	Contours detected: 3	Expected: 1

- Glyph name: uniFB00	Contours detected: 4	Expected: 1 or 2

- Glyph name: uniFB01	Contours detected: 4	Expected: 1, 2 or 3

- Glyph name: uniFB02	Contours detected: 3	Expected: 1 or 2

- Glyph name: uniFB03	Contours detected: 6	Expected: 1, 2, 3 or 4

- Glyph name: uniFB04	Contours detected: 5	Expected: 1, 2 or 3

- Glyph name: uniFFFC	Contours detected: 25	Expected: 22

- Glyph name: A	Contours detected: 4	Expected: 2

- Glyph name: AEacute	Contours detected: 4	Expected: 3

- Glyph name: Aacute	Contours detected: 6	Expected: 3

- Glyph name: Abreve	Contours detected: 7	Expected: 3

- Glyph name: Acircumflex	Contours detected: 7	Expected: 3

- Glyph name: Adieresis	Contours detected: 6	Expected: 4

- Glyph name: Agrave	Contours detected: 6	Expected: 3

- Glyph name: Alphatonos	Contours detected: 6	Expected: 3

- Glyph name: Amacron	Contours detected: 5	Expected: 3

- Glyph name: Aogonek	Contours detected: 7	Expected: 2 or 3

- Glyph name: Aring	Contours detected: 5	Expected: 3 or 4

- Glyph name: Atilde	Contours detected: 7	Expected: 3

- Glyph name: B	Contours detected: 5	Expected: 2 or 3

- Glyph name: C	Contours detected: 7	Expected: 1

- Glyph name: Cacute	Contours detected: 9	Expected: 2

- Glyph name: Ccaron	Contours detected: 10	Expected: 2

- Glyph name: Ccedilla	Contours detected: 10	Expected: 1 or 2

- Glyph name: Ccircumflex	Contours detected: 10	Expected: 2

- Glyph name: Cdotaccent	Contours detected: 8	Expected: 2

- Glyph name: D	Contours detected: 4	Expected: 2

- Glyph name: Dcaron	Contours detected: 7	Expected: 3

- Glyph name: Dcroat	Contours detected: 4	Expected: 2

- Glyph name: Eacute	Contours detected: 3	Expected: 2

- Glyph name: Ebreve	Contours detected: 4	Expected: 2

- Glyph name: Ecaron	Contours detected: 4	Expected: 2

- Glyph name: Ecircumflex	Contours detected: 4	Expected: 2

- Glyph name: Egrave	Contours detected: 3	Expected: 2

- Glyph name: Eng	Contours detected: 3	Expected: 1

- Glyph name: Eogonek	Contours detected: 4	Expected: 1 or 2

- Glyph name: Epsilontonos	Contours detected: 3	Expected: 2

- Glyph name: Etatonos	Contours detected: 3	Expected: 2

- Glyph name: Eth	Contours detected: 4	Expected: 2

- Glyph name: Euro	Contours detected: 7	Expected: 1 or 2

- Glyph name: G	Contours detected: 4	Expected: 1

- Glyph name: Gbreve	Contours detected: 7	Expected: 2

- Glyph name: Gcaron	Contours detected: 7	Expected: 2

- Glyph name: Gcircumflex	Contours detected: 7	Expected: 2

- Glyph name: Gdotaccent	Contours detected: 5	Expected: 2

- Glyph name: Hcircumflex	Contours detected: 4	Expected: 2

- Glyph name: IJ	Contours detected: 4	Expected: 1 or 2

- Glyph name: Iacute	Contours detected: 3	Expected: 2

- Glyph name: Ibreve	Contours detected: 4	Expected: 2

- Glyph name: Icircumflex	Contours detected: 4	Expected: 2

- Glyph name: Igrave	Contours detected: 3	Expected: 2

- Glyph name: Iogonek	Contours detected: 4	Expected: 1 or 2

- Glyph name: Iotatonos	Contours detected: 3	Expected: 2

- Glyph name: Itilde	Contours detected: 4	Expected: 2

- Glyph name: J	Contours detected: 3	Expected: 1

- Glyph name: Jcircumflex	Contours detected: 6	Expected: 2

- Glyph name: K	Contours detected: 6	Expected: 1 or 2

- Glyph name: Lacute	Contours detected: 3	Expected: 2

- Glyph name: Lambda	Contours detected: 4	Expected: 1

- Glyph name: Lcaron	Contours detected: 3	Expected: 2

- Glyph name: Lslash	Contours detected: 3	Expected: 1

- Glyph name: M	Contours detected: 5	Expected: 1

- Glyph name: N	Contours detected: 4	Expected: 1

- Glyph name: Nacute	Contours detected: 6	Expected: 2

- Glyph name: Ncaron	Contours detected: 7	Expected: 2

- Glyph name: Ntilde	Contours detected: 7	Expected: 2

- Glyph name: O	Contours detected: 6	Expected: 2

- Glyph name: OE	Contours detected: 6	Expected: 2

- Glyph name: Oacute	Contours detected: 8	Expected: 3

- Glyph name: Ocircumflex	Contours detected: 9	Expected: 3

- Glyph name: Odieresis	Contours detected: 8	Expected: 4

- Glyph name: Ograve	Contours detected: 8	Expected: 3

- Glyph name: Ohungarumlaut	Contours detected: 10	Expected: 4

- Glyph name: Omacron	Contours detected: 7	Expected: 3

- Glyph name: Omegatonos	Contours detected: 7	Expected: 2

- Glyph name: Omicrontonos	Contours detected: 8	Expected: 3

- Glyph name: Oslash	Contours detected: 8	Expected: 2 or 3

- Glyph name: Oslashacute	Contours detected: 10	Expected: 4

- Glyph name: Otilde	Contours detected: 9	Expected: 3

- Glyph name: Psi	Contours detected: 3	Expected: 1

- Glyph name: Q	Contours detected: 11	Expected: 2

- Glyph name: R	Contours detected: 4	Expected: 1 or 2

- Glyph name: Racute	Contours detected: 6	Expected: 3

- Glyph name: Rcaron	Contours detected: 7	Expected: 3

- Glyph name: S	Contours detected: 4	Expected: 1

- Glyph name: Sacute	Contours detected: 6	Expected: 2

- Glyph name: Scaron	Contours detected: 7	Expected: 2

- Glyph name: Scircumflex	Contours detected: 7	Expected: 2

- Glyph name: Sigma	Contours detected: 8	Expected: 1

- Glyph name: Tcaron	Contours detected: 4	Expected: 2

- Glyph name: Theta	Contours detected: 8	Expected: 3

- Glyph name: U	Contours detected: 3	Expected: 1

- Glyph name: Uacute	Contours detected: 5	Expected: 2

- Glyph name: Ubreve	Contours detected: 6	Expected: 2

- Glyph name: Ucircumflex	Contours detected: 6	Expected: 2

- Glyph name: Udieresis	Contours detected: 5	Expected: 3

- Glyph name: Ugrave	Contours detected: 5	Expected: 2

- Glyph name: Uhorn	Contours detected: 3	Expected: 1

- Glyph name: Uhungarumlaut	Contours detected: 7	Expected: 3

- Glyph name: Umacron	Contours detected: 4	Expected: 2

- Glyph name: Uogonek	Contours detected: 6	Expected: 1

- Glyph name: Upsilontonos	Contours detected: 7	Expected: 2

- Glyph name: Uring	Contours detected: 5	Expected: 3

- Glyph name: Utilde	Contours detected: 6	Expected: 2

- Glyph name: V	Contours detected: 5	Expected: 1

- Glyph name: W	Contours detected: 6	Expected: 1 or 2

- Glyph name: Wacute	Contours detected: 8	Expected: 2

- Glyph name: Wcircumflex	Contours detected: 9	Expected: 2

- Glyph name: Wdieresis	Contours detected: 8	Expected: 3

- Glyph name: Wgrave	Contours detected: 8	Expected: 2

- Glyph name: X	Contours detected: 9	Expected: 1

- Glyph name: Y	Contours detected: 5	Expected: 1

- Glyph name: Yacute	Contours detected: 7	Expected: 2

- Glyph name: Ycircumflex	Contours detected: 8	Expected: 2

- Glyph name: Ydieresis	Contours detected: 7	Expected: 3

- Glyph name: Ygrave	Contours detected: 7	Expected: 2

- Glyph name: Z	Contours detected: 6	Expected: 1

- Glyph name: Zacute	Contours detected: 8	Expected: 2

- Glyph name: Zcaron	Contours detected: 9	Expected: 2

- Glyph name: Zdotaccent	Contours detected: 7	Expected: 2

- Glyph name: a	Contours detected: 4	Expected: 2

- Glyph name: aacute	Contours detected: 6	Expected: 3

- Glyph name: abreve	Contours detected: 7	Expected: 3

- Glyph name: acircumflex	Contours detected: 7	Expected: 3

- Glyph name: acute	Contours detected: 3	Expected: 1

- Glyph name: adieresis	Contours detected: 6	Expected: 4

- Glyph name: ae	Contours detected: 8	Expected: 3

- Glyph name: aeacute	Contours detected: 10	Expected: 4

- Glyph name: agrave	Contours detected: 6	Expected: 3

- Glyph name: alpha	Contours detected: 9	Expected: 2

- Glyph name: alphatonos	Contours detected: 11	Expected: 3

- Glyph name: amacron	Contours detected: 5	Expected: 3

- Glyph name: ampersand	Contours detected: 6	Expected: 1, 2 or 3

- Glyph name: angle	Contours detected: 9	Expected: 1

- Glyph name: aogonek	Contours detected: 7	Expected: 2

- Glyph name: approxequal	Contours detected: 16	Expected: 2

- Glyph name: aring	Contours detected: 6	Expected: 4

- Glyph name: arrowboth	Contours detected: 9	Expected: 1

- Glyph name: arrowdblboth	Contours detected: 12	Expected: 2

- Glyph name: arrowdblright	Contours detected: 7	Expected: 1

- Glyph name: arrowdown	Contours detected: 5	Expected: 1

- Glyph name: arrowup	Contours detected: 5	Expected: 1

- Glyph name: arrowupdn	Contours detected: 9	Expected: 1

- Glyph name: asciicircum	Contours detected: 5	Expected: 1

- Glyph name: asciitilde	Contours detected: 3	Expected: 1

- Glyph name: asterisk	Contours detected: 5	Expected: 1 or 4

- Glyph name: at	Contours detected: 7	Expected: 2

- Glyph name: atilde	Contours detected: 7	Expected: 3

- Glyph name: b	Contours detected: 6	Expected: 2

- Glyph name: backslash	Contours detected: 5	Expected: 1

- Glyph name: beta	Contours detected: 6	Expected: 2

- Glyph name: braceleft	Contours detected: 5	Expected: 1

- Glyph name: braceright	Contours detected: 3	Expected: 1

- Glyph name: c	Contours detected: 4	Expected: 1

- Glyph name: cacute	Contours detected: 6	Expected: 2

- Glyph name: ccaron	Contours detected: 7	Expected: 2

- Glyph name: ccedilla	Contours detected: 7	Expected: 1 or 2

- Glyph name: ccircumflex	Contours detected: 7	Expected: 2

- Glyph name: cdotaccent	Contours detected: 5	Expected: 2

- Glyph name: cedilla	Contours detected: 3	Expected: 1

- Glyph name: cent	Contours detected: 7	Expected: 1 or 2

- Glyph name: chi	Contours detected: 10	Expected: 1

- Glyph name: circle	Contours detected: 3	Expected: 2

- Glyph name: circleplus	Contours detected: 11	Expected: 3

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: congruent	Contours detected: 10	Expected: 3

- Glyph name: copyright	Contours detected: 12	Expected: 3

- Glyph name: currency	Contours detected: 5	Expected: 2

- Glyph name: d	Contours detected: 3	Expected: 2

- Glyph name: dcaron	Contours detected: 6	Expected: 3

- Glyph name: dcroat	Contours detected: 6	Expected: 2

- Glyph name: delta	Contours detected: 3	Expected: 2

- Glyph name: dieresistonos	Contours detected: 4	Expected: 3

- Glyph name: dollar	Contours detected: 6	Expected: 1, 3 or 5

- Glyph name: e	Contours detected: 6	Expected: 2

- Glyph name: eacute	Contours detected: 8	Expected: 3

- Glyph name: ebreve	Contours detected: 9	Expected: 3

- Glyph name: ecaron	Contours detected: 9	Expected: 3

- Glyph name: ecircumflex	Contours detected: 9	Expected: 3

- Glyph name: edieresis	Contours detected: 8	Expected: 4

- Glyph name: edotaccent	Contours detected: 7	Expected: 3

- Glyph name: egrave	Contours detected: 8	Expected: 3

- Glyph name: eight	Contours detected: 4	Expected: 3

- Glyph name: element	Contours detected: 7	Expected: 1

- Glyph name: emacron	Contours detected: 7	Expected: 3

- Glyph name: emptyset	Contours detected: 8	Expected: 3

- Glyph name: eng	Contours detected: 3	Expected: 1

- Glyph name: eogonek	Contours detected: 9	Expected: 2

- Glyph name: epsilontonos	Contours detected: 9	Expected: 2

- Glyph name: eta	Contours detected: 3	Expected: 1

- Glyph name: etatonos	Contours detected: 5	Expected: 2

- Glyph name: eth	Contours detected: 3	Expected: 2

- Glyph name: f	Contours detected: 2	Expected: 1

- Glyph name: five	Contours detected: 6	Expected: 1

- Glyph name: four	Contours detected: 3	Expected: 1 or 2

- Glyph name: fraction	Contours detected: 8	Expected: 1

- Glyph name: g	Contours detected: 10	Expected: 2 or 3

- Glyph name: gamma	Contours detected: 6	Expected: 1 or 2

- Glyph name: gbreve	Contours detected: 13	Expected: 3 or 4

- Glyph name: gcaron	Contours detected: 13	Expected: 3 or 4

- Glyph name: gcircumflex	Contours detected: 13	Expected: 3 or 4

- Glyph name: gdotaccent	Contours detected: 11	Expected: 3 or 4

- Glyph name: germandbls	Contours detected: 10	Expected: 1

- Glyph name: gradient	Contours detected: 3	Expected: 2

- Glyph name: grave	Contours detected: 3	Expected: 1

- Glyph name: greater	Contours detected: 9	Expected: 1

- Glyph name: greaterequal	Contours detected: 9	Expected: 2

- Glyph name: guillemotleft	Contours detected: 10	Expected: 2

- Glyph name: guillemotright	Contours detected: 10	Expected: 2

- Glyph name: h	Contours detected: 3	Expected: 1

- Glyph name: hbar	Contours detected: 3	Expected: 1

- Glyph name: hcircumflex	Contours detected: 6	Expected: 2

- Glyph name: hungarumlaut	Contours detected: 4	Expected: 2

- Glyph name: iacute	Contours detected: 3	Expected: 2

- Glyph name: ibreve	Contours detected: 4	Expected: 2

- Glyph name: icircumflex	Contours detected: 4	Expected: 2

- Glyph name: igrave	Contours detected: 3	Expected: 2

- Glyph name: ij	Contours detected: 5	Expected: 3 or 4

- Glyph name: infinity	Contours detected: 7	Expected: 3

- Glyph name: integral	Contours detected: 8	Expected: 1

- Glyph name: intersection	Contours detected: 5	Expected: 1

- Glyph name: iogonek	Contours detected: 5	Expected: 2 or 3

- Glyph name: iota	Contours detected: 2	Expected: 1

- Glyph name: iotadieresis	Contours detected: 4	Expected: 3

- Glyph name: iotadieresistonos	Contours detected: 6	Expected: 4

- Glyph name: iotatonos	Contours detected: 4	Expected: 2

- Glyph name: itilde	Contours detected: 4	Expected: 2

- Glyph name: j	Contours detected: 4	Expected: 2

- Glyph name: jcircumflex	Contours detected: 6	Expected: 2

- Glyph name: k	Contours detected: 8	Expected: 1 or 2

- Glyph name: kappa	Contours detected: 8	Expected: 1

- Glyph name: kgreenlandic	Contours detected: 8	Expected: 1 or 2

- Glyph name: lacute	Contours detected: 3	Expected: 2

- Glyph name: lambda	Contours detected: 7	Expected: 1

- Glyph name: lcaron	Contours detected: 3	Expected: 2

- Glyph name: less	Contours detected: 9	Expected: 1

- Glyph name: lessequal	Contours detected: 9	Expected: 2

- Glyph name: logicaland	Contours detected: 7	Expected: 1

- Glyph name: logicalor	Contours detected: 9	Expected: 1

- Glyph name: longs	Contours detected: 3	Expected: 1

- Glyph name: lozenge	Contours detected: 12	Expected: 2

- Glyph name: lslash	Contours detected: 3	Expected: 1

- Glyph name: m	Contours detected: 3	Expected: 1

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: musicalnote	Contours detected: 3	Expected: 1

- Glyph name: n	Contours detected: 3	Expected: 1

- Glyph name: nacute	Contours detected: 5	Expected: 2

- Glyph name: napostrophe	Contours detected: 5	Expected: 2

- Glyph name: ncaron	Contours detected: 6	Expected: 2

- Glyph name: nine	Contours detected: 4	Expected: 1 or 2

- Glyph name: notelement	Contours detected: 5	Expected: 3

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: notsubset	Contours detected: 9	Expected: 2

- Glyph name: ntilde	Contours detected: 6	Expected: 2

- Glyph name: nu	Contours detected: 6	Expected: 1

- Glyph name: o	Contours detected: 6	Expected: 2

- Glyph name: oacute	Contours detected: 8	Expected: 3

- Glyph name: ocircumflex	Contours detected: 9	Expected: 3

- Glyph name: odieresis	Contours detected: 8	Expected: 4

- Glyph name: oe	Contours detected: 7	Expected: 3

- Glyph name: ograve	Contours detected: 8	Expected: 3

- Glyph name: ohorn	Contours detected: 6	Expected: 2

- Glyph name: ohungarumlaut	Contours detected: 10	Expected: 4

- Glyph name: omacron	Contours detected: 7	Expected: 3

- Glyph name: omega	Contours detected: 6	Expected: 1

- Glyph name: omegatonos	Contours detected: 8	Expected: 2

- Glyph name: one	Contours detected: 2	Expected: 1

- Glyph name: onehalf	Contours detected: 8	Expected: 3

- Glyph name: onequarter	Contours detected: 8	Expected: 3 or 4

- Glyph name: ordfeminine	Contours detected: 4	Expected: 2 or 3

- Glyph name: ordmasculine	Contours detected: 6	Expected: 2 or 3

- Glyph name: oslash	Contours detected: 6	Expected: 3

- Glyph name: oslashacute	Contours detected: 8	Expected: 4

- Glyph name: otilde	Contours detected: 9	Expected: 3

- Glyph name: p	Contours detected: 3	Expected: 2

- Glyph name: parenleft	Contours detected: 5	Expected: 1

- Glyph name: parenright	Contours detected: 5	Expected: 1

- Glyph name: partialdiff	Contours detected: 6	Expected: 2

- Glyph name: percent	Contours detected: 14	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 18	Expected: 6 or 7

- Glyph name: phi	Contours detected: 9	Expected: 2 or 3

- Glyph name: pi	Contours detected: 2	Expected: 1

- Glyph name: propersubset	Contours detected: 7	Expected: 1

- Glyph name: propersuperset	Contours detected: 7	Expected: 1

- Glyph name: proportional	Contours detected: 10	Expected: 2

- Glyph name: psi	Contours detected: 6	Expected: 1

- Glyph name: q	Contours detected: 6	Expected: 2

- Glyph name: question	Contours detected: 7	Expected: 2

- Glyph name: questiondown	Contours detected: 4	Expected: 2

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: r	Contours detected: 3	Expected: 1

- Glyph name: racute	Contours detected: 5	Expected: 2

- Glyph name: radical	Contours detected: 6	Expected: 1

- Glyph name: rcaron	Contours detected: 6	Expected: 2

- Glyph name: reflexsubset	Contours detected: 6	Expected: 2

- Glyph name: reflexsuperset	Contours detected: 6	Expected: 2

- Glyph name: registered	Contours detected: 9	Expected: 3 or 4

- Glyph name: rho	Contours detected: 4	Expected: 2

- Glyph name: s	Contours detected: 4	Expected: 1

- Glyph name: sacute	Contours detected: 6	Expected: 2

- Glyph name: scaron	Contours detected: 7	Expected: 2

- Glyph name: scircumflex	Contours detected: 7	Expected: 2

- Glyph name: section	Contours detected: 6	Expected: 2

- Glyph name: semicolon	Contours detected: 3	Expected: 2

- Glyph name: seven	Contours detected: 3	Expected: 1

- Glyph name: sigma	Contours detected: 3	Expected: 2

- Glyph name: six	Contours detected: 5	Expected: 1 or 2

- Glyph name: slash	Contours detected: 5	Expected: 1

- Glyph name: sterling	Contours detected: 6	Expected: 1 or 2

- Glyph name: suchthat	Contours detected: 7	Expected: 1

- Glyph name: summation	Contours detected: 8	Expected: 1

- Glyph name: t	Contours detected: 2	Expected: 1

- Glyph name: tbar	Contours detected: 2	Expected: 1

- Glyph name: tcaron	Contours detected: 5	Expected: 2

- Glyph name: theta	Contours detected: 7	Expected: 3

- Glyph name: thorn	Contours detected: 3	Expected: 2

- Glyph name: three	Contours detected: 6	Expected: 1

- Glyph name: threequarters	Contours detected: 13	Expected: 3 or 4

- Glyph name: tilde	Contours detected: 3	Expected: 1

- Glyph name: trademark	Contours detected: 3	Expected: 2

- Glyph name: two	Contours detected: 8	Expected: 1

- Glyph name: u	Contours detected: 3	Expected: 1

- Glyph name: uacute	Contours detected: 5	Expected: 2

- Glyph name: ubreve	Contours detected: 6	Expected: 2

- Glyph name: ucircumflex	Contours detected: 6	Expected: 2

- Glyph name: udieresis	Contours detected: 5	Expected: 3

- Glyph name: ugrave	Contours detected: 5	Expected: 2

- Glyph name: uhorn	Contours detected: 4	Expected: 1

- Glyph name: uhungarumlaut	Contours detected: 7	Expected: 3

- Glyph name: umacron	Contours detected: 4	Expected: 2

- Glyph name: uni0122	Contours detected: 7	Expected: 2

- Glyph name: uni0123	Contours detected: 12	Expected: 3 or 4

- Glyph name: uni0136	Contours detected: 9	Expected: 2 or 3

- Glyph name: uni0137	Contours detected: 11	Expected: 2 or 3

- Glyph name: uni013B	Contours detected: 4	Expected: 2

- Glyph name: uni013C	Contours detected: 4	Expected: 2

- Glyph name: uni0145	Contours detected: 7	Expected: 2

- Glyph name: uni0146	Contours detected: 6	Expected: 2

- Glyph name: uni0156	Contours detected: 7	Expected: 3

- Glyph name: uni0157	Contours detected: 6	Expected: 2

- Glyph name: uni0162	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0163	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0180	Contours detected: 6	Expected: 2

- Glyph name: uni0181	Contours detected: 6	Expected: 3

- Glyph name: uni0186	Contours detected: 4	Expected: 1

- Glyph name: uni018A	Contours detected: 4	Expected: 2

- Glyph name: uni018F	Contours detected: 5	Expected: 2

- Glyph name: uni0190	Contours detected: 4	Expected: 1

- Glyph name: uni0191	Contours detected: 2	Expected: 1

- Glyph name: uni0194	Contours detected: 3	Expected: 2

- Glyph name: uni01B2	Contours detected: 4	Expected: 1

- Glyph name: uni01B5	Contours detected: 8	Expected: 1

- Glyph name: uni01B6	Contours detected: 7	Expected: 1

- Glyph name: uni01B7	Contours detected: 4	Expected: 1

- Glyph name: uni01CD	Contours detected: 7	Expected: 3

- Glyph name: uni01CE	Contours detected: 7	Expected: 3

- Glyph name: uni01CF	Contours detected: 4	Expected: 2

- Glyph name: uni01D0	Contours detected: 4	Expected: 2

- Glyph name: uni01D1	Contours detected: 9	Expected: 3

- Glyph name: uni01D2	Contours detected: 9	Expected: 3

- Glyph name: uni01D3	Contours detected: 6	Expected: 2

- Glyph name: uni01D4	Contours detected: 6	Expected: 2

- Glyph name: uni01D5	Contours detected: 6	Expected: 4

- Glyph name: uni01D6	Contours detected: 6	Expected: 4

- Glyph name: uni01D7	Contours detected: 7	Expected: 4

- Glyph name: uni01D8	Contours detected: 7	Expected: 4

- Glyph name: uni01D9	Contours detected: 8	Expected: 4

- Glyph name: uni01DA	Contours detected: 8	Expected: 4

- Glyph name: uni01DB	Contours detected: 7	Expected: 4

- Glyph name: uni01DC	Contours detected: 7	Expected: 4

- Glyph name: uni01E3	Contours detected: 9	Expected: 4

- Glyph name: uni01E8	Contours detected: 9	Expected: 2

- Glyph name: uni01E9	Contours detected: 11	Expected: 2

- Glyph name: uni01EE	Contours detected: 7	Expected: 2

- Glyph name: uni01EF	Contours detected: 7	Expected: 2

- Glyph name: uni01F0	Contours detected: 6	Expected: 2

- Glyph name: uni01F8	Contours detected: 6	Expected: 2

- Glyph name: uni01F9	Contours detected: 5	Expected: 2

- Glyph name: uni0218	Contours detected: 7	Expected: 2

- Glyph name: uni0219	Contours detected: 7	Expected: 2

- Glyph name: uni021A	Contours detected: 4	Expected: 2

- Glyph name: uni021B	Contours detected: 5	Expected: 2

- Glyph name: uni021E	Contours detected: 4	Expected: 2

- Glyph name: uni021F	Contours detected: 6	Expected: 2

- Glyph name: uni0226	Contours detected: 5	Expected: 3

- Glyph name: uni0227	Contours detected: 5	Expected: 3

- Glyph name: uni0228	Contours detected: 4	Expected: 1

- Glyph name: uni0229	Contours detected: 9	Expected: 2

- Glyph name: uni022E	Contours detected: 7	Expected: 3

- Glyph name: uni022F	Contours detected: 7	Expected: 3

- Glyph name: uni0232	Contours detected: 6	Expected: 2

- Glyph name: uni0233	Contours detected: 8	Expected: 2

- Glyph name: uni0237	Contours detected: 3	Expected: 1

- Glyph name: uni0243	Contours detected: 5	Expected: 3

- Glyph name: uni0248	Contours detected: 3	Expected: 1

- Glyph name: uni0249	Contours detected: 4	Expected: 2

- Glyph name: uni0259	Contours detected: 4	Expected: 2

- Glyph name: uni0292	Contours detected: 4	Expected: 1

- Glyph name: uni0302	Contours detected: 3	Expected: 1

- Glyph name: uni0306	Contours detected: 3	Expected: 1

- Glyph name: uni030B	Contours detected: 4	Expected: 2

- Glyph name: uni030C	Contours detected: 3	Expected: 1

- Glyph name: uni030F	Contours detected: 4	Expected: 2

- Glyph name: uni0312	Contours detected: 2	Expected: 1

- Glyph name: uni0313	Contours detected: 2	Expected: 1

- Glyph name: uni031B	Contours detected: 2	Expected: 1

- Glyph name: uni0327	Contours detected: 3	Expected: 1

- Glyph name: uni0328	Contours detected: 3	Expected: 1

- Glyph name: uni0337	Contours detected: 5	Expected: 1

- Glyph name: uni0338	Contours detected: 6	Expected: 1

- Glyph name: uni0394	Contours detected: 4	Expected: 2

- Glyph name: uni03A9	Contours detected: 5	Expected: 1

- Glyph name: uni03BC	Contours detected: 3	Expected: 1

- Glyph name: uni0402	Contours detected: 4	Expected: 1

- Glyph name: uni0403	Contours detected: 3	Expected: 2

- Glyph name: uni0404	Contours detected: 7	Expected: 1

- Glyph name: uni0409	Contours detected: 3	Expected: 2

- Glyph name: uni040B	Contours detected: 2	Expected: 1

- Glyph name: uni040C	Contours detected: 8	Expected: 2

- Glyph name: uni040D	Contours detected: 6	Expected: 2

- Glyph name: uni040E	Contours detected: 10	Expected: 2

- Glyph name: uni0411	Contours detected: 4	Expected: 2

- Glyph name: uni0414	Contours detected: 1	Expected: 2

- Glyph name: uni0416	Contours detected: 13	Expected: 1

- Glyph name: uni0417	Contours detected: 5	Expected: 1

- Glyph name: uni0418	Contours detected: 4	Expected: 1

- Glyph name: uni0419	Contours detected: 7	Expected: 2

- Glyph name: uni041B	Contours detected: 2	Expected: 1

- Glyph name: uni0423	Contours detected: 7	Expected: 1

- Glyph name: uni0427	Contours detected: 2	Expected: 1

- Glyph name: uni042D	Contours detected: 7	Expected: 1

- Glyph name: uni042E	Contours detected: 8	Expected: 2

- Glyph name: uni042F	Contours detected: 4	Expected: 2

- Glyph name: uni0431	Contours detected: 5	Expected: 2

- Glyph name: uni0432	Contours detected: 2	Expected: 3

- Glyph name: uni0434	Contours detected: 1	Expected: 2

- Glyph name: uni0436	Contours detected: 13	Expected: 1

- Glyph name: uni0437	Contours detected: 5	Expected: 1

- Glyph name: uni0438	Contours detected: 4	Expected: 1

- Glyph name: uni0439	Contours detected: 7	Expected: 2

- Glyph name: uni043A	Contours detected: 8	Expected: 1

- Glyph name: uni043B	Contours detected: 2	Expected: 1

- Glyph name: uni043C	Contours detected: 5	Expected: 1

- Glyph name: uni0444	Contours detected: 8	Expected: 3

- Glyph name: uni0447	Contours detected: 2	Expected: 1

- Glyph name: uni044A	Contours detected: 4	Expected: 2

- Glyph name: uni044B	Contours detected: 5	Expected: 3

- Glyph name: uni044C	Contours detected: 4	Expected: 2

- Glyph name: uni044D	Contours detected: 7	Expected: 1

- Glyph name: uni044E	Contours detected: 4	Expected: 2

- Glyph name: uni044F	Contours detected: 4	Expected: 2

- Glyph name: uni0452	Contours detected: 4	Expected: 1

- Glyph name: uni0453	Contours detected: 3	Expected: 2

- Glyph name: uni0454	Contours detected: 4	Expected: 1

- Glyph name: uni0459	Contours detected: 3	Expected: 2

- Glyph name: uni045C	Contours detected: 10	Expected: 2

- Glyph name: uni045D	Contours detected: 6	Expected: 2

- Glyph name: uni045E	Contours detected: 10	Expected: 2

- Glyph name: uni0496	Contours detected: 13	Expected: 1 or 2

- Glyph name: uni0497	Contours detected: 13	Expected: 1 or 2

- Glyph name: uni049A	Contours detected: 8	Expected: 1 or 2

- Glyph name: uni049B	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni04AE	Contours detected: 5	Expected: 1

- Glyph name: uni04AF	Contours detected: 5	Expected: 1

- Glyph name: uni04B0	Contours detected: 5	Expected: 1

- Glyph name: uni04B1	Contours detected: 5	Expected: 1

- Glyph name: uni04BA	Contours detected: 2	Expected: 1

- Glyph name: uni04BB	Contours detected: 4	Expected: 1

- Glyph name: uni04C1	Contours detected: 16	Expected: 2

- Glyph name: uni04C2	Contours detected: 16	Expected: 2

- Glyph name: uni04D0	Contours detected: 7	Expected: 3

- Glyph name: uni04D1	Contours detected: 7	Expected: 3

- Glyph name: uni04D2	Contours detected: 6	Expected: 4

- Glyph name: uni04D3	Contours detected: 6	Expected: 4

- Glyph name: uni04D6	Contours detected: 4	Expected: 2

- Glyph name: uni04D7	Contours detected: 9	Expected: 3

- Glyph name: uni04DA	Contours detected: 7	Expected: 4

- Glyph name: uni04DB	Contours detected: 6	Expected: 4

- Glyph name: uni04DC	Contours detected: 15	Expected: 3

- Glyph name: uni04DD	Contours detected: 15	Expected: 3

- Glyph name: uni04DE	Contours detected: 7	Expected: 3

- Glyph name: uni04DF	Contours detected: 7	Expected: 3

- Glyph name: uni04E2	Contours detected: 5	Expected: 2

- Glyph name: uni04E3	Contours detected: 5	Expected: 2

- Glyph name: uni04E4	Contours detected: 6	Expected: 3

- Glyph name: uni04E5	Contours detected: 6	Expected: 3

- Glyph name: uni04E6	Contours detected: 8	Expected: 4

- Glyph name: uni04E7	Contours detected: 8	Expected: 4

- Glyph name: uni04E8	Contours detected: 7	Expected: 3

- Glyph name: uni04E9	Contours detected: 7	Expected: 3

- Glyph name: uni04EA	Contours detected: 9	Expected: 5

- Glyph name: uni04EB	Contours detected: 9	Expected: 5

- Glyph name: uni04EC	Contours detected: 9	Expected: 3

- Glyph name: uni04ED	Contours detected: 9	Expected: 3

- Glyph name: uni04EE	Contours detected: 8	Expected: 2

- Glyph name: uni04EF	Contours detected: 8	Expected: 2

- Glyph name: uni04F0	Contours detected: 9	Expected: 3

- Glyph name: uni04F1	Contours detected: 9	Expected: 3

- Glyph name: uni04F2	Contours detected: 11	Expected: 3

- Glyph name: uni04F3	Contours detected: 11	Expected: 3

- Glyph name: uni04F4	Contours detected: 4	Expected: 3

- Glyph name: uni04F5	Contours detected: 4	Expected: 3

- Glyph name: uni04F9	Contours detected: 7	Expected: 5

- Glyph name: uni0E01	Contours detected: 3	Expected: 1

- Glyph name: uni0E02	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E03	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E04	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E05	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E06	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E07	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E08	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E09	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E0A	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E0B	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E0C	Contours detected: 5	Expected: 1 or 3

- Glyph name: uni0E10	Contours detected: 7	Expected: 1 or 5

- Glyph name: uni0E11	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E12	Contours detected: 6	Expected: 1 or 3

- Glyph name: uni0E14	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E15	Contours detected: 7	Expected: 1 or 2

- Glyph name: uni0E16	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E17	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E18	Contours detected: 3	Expected: 1

- Glyph name: uni0E1C	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E1D	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E1E	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E1F	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E20	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E24	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E25	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E26	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E27	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E28	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E2A	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E2B	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E2C	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E2D	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E2F	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E32	Contours detected: 3	Expected: 1

- Glyph name: uni0E33	Contours detected: 5	Expected: 3

- Glyph name: uni0E43	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E44	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E45	Contours detected: 3	Expected: 1

- Glyph name: uni0E46	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E47	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E49	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E4E	Contours detected: 5	Expected: 1

- Glyph name: uni0E4F	Contours detected: 10	Expected: 4

- Glyph name: uni0E50	Contours detected: 6	Expected: 2

- Glyph name: uni0E51	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E52	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E53	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni0E54	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E55	Contours detected: 4	Expected: 1 or 3

- Glyph name: uni0E56	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E57	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E58	Contours detected: 6	Expected: 1 or 2

- Glyph name: uni0E59	Contours detected: 8	Expected: 1 or 2

- Glyph name: uni0E5A	Contours detected: 4	Expected: 1 or 2

- Glyph name: uni0E5B	Contours detected: 5	Expected: 1 or 2

- Glyph name: uni1E00	Contours detected: 6	Expected: 4

- Glyph name: uni1E01	Contours detected: 6	Expected: 4

- Glyph name: uni1E02	Contours detected: 6	Expected: 4

- Glyph name: uni1E03	Contours detected: 7	Expected: 3

- Glyph name: uni1E0A	Contours detected: 5	Expected: 3

- Glyph name: uni1E0B	Contours detected: 4	Expected: 3

- Glyph name: uni1E0C	Contours detected: 5	Expected: 3

- Glyph name: uni1E0D	Contours detected: 4	Expected: 3

- Glyph name: uni1E0E	Contours detected: 5	Expected: 3

- Glyph name: uni1E0F	Contours detected: 4	Expected: 3

- Glyph name: uni1E20	Contours detected: 5	Expected: 2

- Glyph name: uni1E21	Contours detected: 11	Expected: 3 or 4

- Glyph name: uni1E25	Contours detected: 4	Expected: 2

- Glyph name: uni1E2B	Contours detected: 4	Expected: 2

- Glyph name: uni1E3E	Contours detected: 7	Expected: 2

- Glyph name: uni1E3F	Contours detected: 5	Expected: 2

- Glyph name: uni1E40	Contours detected: 6	Expected: 2

- Glyph name: uni1E41	Contours detected: 4	Expected: 2

- Glyph name: uni1E42	Contours detected: 6	Expected: 2

- Glyph name: uni1E43	Contours detected: 4	Expected: 2

- Glyph name: uni1E44	Contours detected: 5	Expected: 2

- Glyph name: uni1E45	Contours detected: 4	Expected: 2

- Glyph name: uni1E46	Contours detected: 5	Expected: 2

- Glyph name: uni1E47	Contours detected: 4	Expected: 2

- Glyph name: uni1E48	Contours detected: 5	Expected: 2

- Glyph name: uni1E49	Contours detected: 4	Expected: 2

- Glyph name: uni1E57	Contours detected: 4	Expected: 3

- Glyph name: uni1E5A	Contours detected: 5	Expected: 3

- Glyph name: uni1E5B	Contours detected: 4	Expected: 2

- Glyph name: uni1E5E	Contours detected: 5	Expected: 3

- Glyph name: uni1E5F	Contours detected: 4	Expected: 2

- Glyph name: uni1E60	Contours detected: 5	Expected: 2

- Glyph name: uni1E61	Contours detected: 5	Expected: 2

- Glyph name: uni1E62	Contours detected: 5	Expected: 2

- Glyph name: uni1E63	Contours detected: 5	Expected: 2

- Glyph name: uni1E6B	Contours detected: 3	Expected: 2

- Glyph name: uni1E6D	Contours detected: 3	Expected: 2

- Glyph name: uni1E6F	Contours detected: 3	Expected: 2

- Glyph name: uni1E8E	Contours detected: 6	Expected: 2

- Glyph name: uni1E8F	Contours detected: 8	Expected: 2

- Glyph name: uni1E92	Contours detected: 7	Expected: 2

- Glyph name: uni1E93	Contours detected: 6	Expected: 2

- Glyph name: uni1E97	Contours detected: 4	Expected: 3

- Glyph name: uni1E9E	Contours detected: 3	Expected: 1

- Glyph name: uni1EA0	Contours detected: 5	Expected: 3

- Glyph name: uni1EA1	Contours detected: 5	Expected: 3

- Glyph name: uni1EA2	Contours detected: 7	Expected: 3

- Glyph name: uni1EA3	Contours detected: 7	Expected: 3

- Glyph name: uni1EA4	Contours detected: 9	Expected: 4

- Glyph name: uni1EA5	Contours detected: 9	Expected: 4

- Glyph name: uni1EA6	Contours detected: 9	Expected: 4

- Glyph name: uni1EA7	Contours detected: 9	Expected: 4

- Glyph name: uni1EA8	Contours detected: 10	Expected: 4

- Glyph name: uni1EA9	Contours detected: 10	Expected: 4

- Glyph name: uni1EAA	Contours detected: 10	Expected: 4

- Glyph name: uni1EAB	Contours detected: 10	Expected: 4

- Glyph name: uni1EAC	Contours detected: 8	Expected: 4

- Glyph name: uni1EAD	Contours detected: 8	Expected: 4

- Glyph name: uni1EAE	Contours detected: 9	Expected: 4

- Glyph name: uni1EAF	Contours detected: 9	Expected: 4

- Glyph name: uni1EB0	Contours detected: 9	Expected: 4

- Glyph name: uni1EB1	Contours detected: 9	Expected: 4

- Glyph name: uni1EB2	Contours detected: 10	Expected: 4

- Glyph name: uni1EB3	Contours detected: 10	Expected: 4

- Glyph name: uni1EB4	Contours detected: 10	Expected: 4

- Glyph name: uni1EB5	Contours detected: 10	Expected: 4

- Glyph name: uni1EB6	Contours detected: 8	Expected: 4

- Glyph name: uni1EB7	Contours detected: 8	Expected: 4

- Glyph name: uni1EB9	Contours detected: 7	Expected: 3

- Glyph name: uni1EBA	Contours detected: 4	Expected: 2

- Glyph name: uni1EBB	Contours detected: 9	Expected: 3

- Glyph name: uni1EBC	Contours detected: 4	Expected: 2

- Glyph name: uni1EBD	Contours detected: 9	Expected: 3

- Glyph name: uni1EBE	Contours detected: 6	Expected: 3

- Glyph name: uni1EBF	Contours detected: 11	Expected: 4

- Glyph name: uni1EC0	Contours detected: 6	Expected: 3

- Glyph name: uni1EC1	Contours detected: 11	Expected: 4

- Glyph name: uni1EC2	Contours detected: 7	Expected: 3

- Glyph name: uni1EC3	Contours detected: 12	Expected: 4

- Glyph name: uni1EC4	Contours detected: 7	Expected: 3

- Glyph name: uni1EC5	Contours detected: 12	Expected: 4

- Glyph name: uni1EC6	Contours detected: 5	Expected: 3

- Glyph name: uni1EC7	Contours detected: 10	Expected: 4

- Glyph name: uni1EC8	Contours detected: 4	Expected: 2

- Glyph name: uni1EC9	Contours detected: 4	Expected: 2

- Glyph name: uni1ECC	Contours detected: 7	Expected: 3

- Glyph name: uni1ECD	Contours detected: 7	Expected: 3

- Glyph name: uni1ECE	Contours detected: 9	Expected: 3

- Glyph name: uni1ECF	Contours detected: 9	Expected: 3

- Glyph name: uni1ED0	Contours detected: 11	Expected: 4

- Glyph name: uni1ED1	Contours detected: 11	Expected: 4

- Glyph name: uni1ED2	Contours detected: 11	Expected: 4

- Glyph name: uni1ED3	Contours detected: 11	Expected: 4

- Glyph name: uni1ED4	Contours detected: 12	Expected: 4

- Glyph name: uni1ED5	Contours detected: 12	Expected: 4

- Glyph name: uni1ED6	Contours detected: 12	Expected: 4

- Glyph name: uni1ED7	Contours detected: 12	Expected: 4

- Glyph name: uni1ED8	Contours detected: 10	Expected: 4

- Glyph name: uni1ED9	Contours detected: 10	Expected: 4

- Glyph name: uni1EDA	Contours detected: 5	Expected: 3 or 4

- Glyph name: uni1EDB	Contours detected: 8	Expected: 3

- Glyph name: uni1EDC	Contours detected: 5	Expected: 3 or 4

- Glyph name: uni1EDD	Contours detected: 8	Expected: 3

- Glyph name: uni1EDE	Contours detected: 6	Expected: 3 or 4

- Glyph name: uni1EDF	Contours detected: 9	Expected: 3

- Glyph name: uni1EE0	Contours detected: 6	Expected: 3 or 4

- Glyph name: uni1EE1	Contours detected: 9	Expected: 3

- Glyph name: uni1EE3	Contours detected: 7	Expected: 3

- Glyph name: uni1EE4	Contours detected: 4	Expected: 2

- Glyph name: uni1EE5	Contours detected: 4	Expected: 2

- Glyph name: uni1EE6	Contours detected: 6	Expected: 2

- Glyph name: uni1EE7	Contours detected: 6	Expected: 2

- Glyph name: uni1EE8	Contours detected: 5	Expected: 2

- Glyph name: uni1EE9	Contours detected: 6	Expected: 2

- Glyph name: uni1EEA	Contours detected: 5	Expected: 2

- Glyph name: uni1EEB	Contours detected: 6	Expected: 2

- Glyph name: uni1EEC	Contours detected: 6	Expected: 2

- Glyph name: uni1EED	Contours detected: 7	Expected: 2

- Glyph name: uni1EEE	Contours detected: 6	Expected: 2

- Glyph name: uni1EEF	Contours detected: 7	Expected: 2

- Glyph name: uni1EF0	Contours detected: 4	Expected: 2

- Glyph name: uni1EF1	Contours detected: 5	Expected: 2

- Glyph name: uni1EF4	Contours detected: 6	Expected: 2

- Glyph name: uni1EF5	Contours detected: 8	Expected: 2

- Glyph name: uni1EF6	Contours detected: 8	Expected: 2

- Glyph name: uni1EF7	Contours detected: 10	Expected: 2

- Glyph name: uni1EF8	Contours detected: 8	Expected: 2

- Glyph name: uni1EF9	Contours detected: 10	Expected: 2

- Glyph name: uni20AD	Contours detected: 7	Expected: 1

- Glyph name: uni2113	Contours detected: 12	Expected: 2

- Glyph name: uni2196	Contours detected: 13	Expected: 1

- Glyph name: uni2197	Contours detected: 13	Expected: 1

- Glyph name: uni2198	Contours detected: 13	Expected: 1

- Glyph name: uni2199	Contours detected: 13	Expected: 1

- Glyph name: uni21C4	Contours detected: 10	Expected: 2

- Glyph name: uni21E5	Contours detected: 6	Expected: 2

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni2226	Contours detected: 4	Expected: 1

- Glyph name: uni222C	Contours detected: 16	Expected: 2

- Glyph name: uni223D	Contours detected: 10	Expected: 1

- Glyph name: uni2243	Contours detected: 9	Expected: 2

- Glyph name: uni2262	Contours detected: 3	Expected: 1

- Glyph name: uni226A	Contours detected: 22	Expected: 2

- Glyph name: uni226B	Contours detected: 22	Expected: 2

- Glyph name: uni2285	Contours detected: 7	Expected: 2

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 8	Expected: 1

- Glyph name: uni2572	Contours detected: 8	Expected: 1

- Glyph name: uni2573	Contours detected: 13	Expected: 1

- Glyph name: uni25B3	Contours detected: 10	Expected: 2

- Glyph name: uni25B7	Contours detected: 12	Expected: 2

- Glyph name: uni25BD	Contours detected: 6	Expected: 2

- Glyph name: uni25C1	Contours detected: 12	Expected: 2

- Glyph name: uni25C7	Contours detected: 15	Expected: 2

- Glyph name: uni25C9	Contours detected: 9	Expected: 3

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uniFFFC	Contours detected: 25	Expected: 22

- Glyph name: union	Contours detected: 7	Expected: 1

- Glyph name: universal	Contours detected: 7	Expected: 2

- Glyph name: uogonek	Contours detected: 6	Expected: 1

- Glyph name: upsilon	Contours detected: 5	Expected: 1

- Glyph name: upsilondieresis	Contours detected: 7	Expected: 3

- Glyph name: upsilondieresistonos	Contours detected: 9	Expected: 4

- Glyph name: upsilontonos	Contours detected: 7	Expected: 2

- Glyph name: uring	Contours detected: 5	Expected: 3

- Glyph name: utilde	Contours detected: 6	Expected: 2

- Glyph name: v	Contours detected: 5	Expected: 1

- Glyph name: w	Contours detected: 7	Expected: 1

- Glyph name: wacute	Contours detected: 9	Expected: 2

- Glyph name: wcircumflex	Contours detected: 10	Expected: 2

- Glyph name: wdieresis	Contours detected: 9	Expected: 3

- Glyph name: wgrave	Contours detected: 9	Expected: 2

- Glyph name: x	Contours detected: 9	Expected: 1

- Glyph name: xi	Contours detected: 12	Expected: 1

- Glyph name: y	Contours detected: 7	Expected: 1

- Glyph name: yacute	Contours detected: 9	Expected: 2

- Glyph name: ycircumflex	Contours detected: 10	Expected: 2

- Glyph name: ydieresis	Contours detected: 9	Expected: 3

- Glyph name: yen	Contours detected: 3	Expected: 1 or 2

- Glyph name: ygrave	Contours detected: 9	Expected: 2

- Glyph name: z	Contours detected: 5	Expected: 1

- Glyph name: zacute	Contours detected: 7	Expected: 2

- Glyph name: zcaron	Contours detected: 8	Expected: 2

- Glyph name: zdotaccent	Contours detected: 6	Expected: 2

- Glyph name: zero	Contours detected: 5	Expected: 2 or 3

- Glyph name: zeta	Contours detected: 11	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos-kerning-info">gpos_kerning_info</a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 1024 among a set of 29 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 512:
logicalnot, notequal, less, greaterequal, divide, plus, greater, multiply, lessequal, equal, minus, plusminus</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* napostrophe (U+0149): L&lt;&lt;64.0,448.0&gt;--&lt;128.0,448.0&gt;&gt; has the same coordinates as a previous segment.

* uogonek (U+0173): L&lt;&lt;384.0,0.0&gt;--&lt;320.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EA2 (U+1EA2): L&lt;&lt;192.0,640.0&gt;--&lt;320.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EA4 (U+1EA4): L&lt;&lt;256.0,832.0&gt;--&lt;192.0,832.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBE (U+1EBE): L&lt;&lt;256.0,832.0&gt;--&lt;192.0,832.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ECE (U+1ECE): L&lt;&lt;192.0,640.0&gt;--&lt;320.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED0 (U+1ED0): L&lt;&lt;256.0,832.0&gt;--&lt;192.0,832.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EDE (U+1EDE): L&lt;&lt;192.0,640.0&gt;--&lt;320.0,640.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- NULL

- nonmarkingreturn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, cherokee, math</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: elbasan, glagolitic, coptic, gothic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, old-permic, canadian-aboriginal, tifinagh, coptic, malayalam, tai-le, todhri, math, duployan, syriac</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030E COMBINING DOUBLE VERTICAL LINE ABOVE: try adding ethiopic</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: todhri, coptic</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0314 COMBINING REVERSED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031A COMBINING LEFT ANGLE ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032A COMBINING BRIDGE BELOW: not included in any glyphset definition</li>
<li>U+032B COMBINING INVERTED DOUBLE ARCH BELOW: not included in any glyphset definition</li>
<li>U+032C COMBINING CARON BELOW: try adding math</li>
<li>U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding one of: syriac, sunuwar</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, cherokee, math</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0E83 : not included in any glyphset definition</li>
<li>U+0E85 : not included in any glyphset definition</li>
<li>U+0EA4 : not included in any glyphset definition</li>
<li>U+0EA6 : not included in any glyphset definition</li>
<li>U+2003 EM SPACE: try adding nushu</li>
<li>U+2010 HYPHEN: try adding one of: hebrew, kayah-li, syloti-nagri, sundanese, coptic, kaithi, sora-sompeng, kharoshthi, lisu, arabic, armenian, cham, yi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2034 TRIPLE PRIME: try adding math</li>
<li>U+203B REFERENCE MARK: not included in any glyphset definition</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2103 DEGREE CELSIUS: try adding math</li>
<li>U+210F PLANCK CONSTANT OVER TWO PI: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2127 INVERTED OHM SIGN: try adding math</li>
<li>U+212B ANGSTROM SIGN: try adding math</li>
<li>U+2135 ALEF SYMBOL: try adding math</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math</li>
<li>U+21C4 RIGHTWARDS ARROW OVER LEFTWARDS ARROW: try adding math</li>
<li>U+21D0 LEFTWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D1 UPWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D2 RIGHTWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D3 DOWNWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D4 LEFT RIGHT DOUBLE ARROW: try adding math</li>
<li>U+21D5 UP DOWN DOUBLE ARROW: try adding math</li>
<li>U+21D6 NORTH WEST DOUBLE ARROW: try adding math</li>
<li>U+21D7 NORTH EAST DOUBLE ARROW: try adding math</li>
<li>U+21D8 SOUTH EAST DOUBLE ARROW: try adding math</li>
<li>U+21D9 SOUTH WEST DOUBLE ARROW: try adding math</li>
<li>U+21E5 RIGHTWARDS ARROW TO BAR: try adding math</li>
<li>U+21E6 LEFTWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E8 RIGHTWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E9 DOWNWARDS WHITE ARROW: try adding symbols</li>
<li>U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols</li>
<li>U+21EB UPWARDS WHITE ARROW ON PEDESTAL: try adding symbols</li>
<li>U+21EC UPWARDS WHITE ARROW ON PEDESTAL WITH HORIZONTAL BAR: try adding symbols</li>
<li>U+21ED UPWARDS WHITE ARROW ON PEDESTAL WITH VERTICAL BAR: try adding symbols</li>
<li>U+21EE UPWARDS WHITE DOUBLE ARROW: try adding symbols</li>
<li>U+21EF UPWARDS WHITE DOUBLE ARROW ON PEDESTAL: try adding symbols</li>
<li>U+21F0 RIGHTWARDS WHITE ARROW FROM WALL: try adding symbols</li>
<li>U+21F1 NORTH WEST ARROW TO CORNER: try adding math</li>
<li>U+21F2 SOUTH EAST ARROW TO CORNER: try adding math</li>
<li>U+21F3 UP DOWN WHITE ARROW: try adding symbols</li>
<li>U+2200 FOR ALL: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2203 THERE EXISTS: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+2207 NABLA: try adding math</li>
<li>U+2208 ELEMENT OF: try adding math</li>
<li>U+2209 NOT AN ELEMENT OF: try adding math</li>
<li>U+220B CONTAINS AS MEMBER: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2213 MINUS-OR-PLUS SIGN: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, tai-tham, yi, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221D PROPORTIONAL TO: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2220 ANGLE: try adding math</li>
<li>U+2225 PARALLEL TO: try adding math</li>
<li>U+2226 NOT PARALLEL TO: try adding math</li>
<li>U+2227 LOGICAL AND: try adding math</li>
<li>U+2228 LOGICAL OR: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+222C DOUBLE INTEGRAL: try adding math</li>
<li>U+2234 THEREFORE: try adding math</li>
<li>U+2235 BECAUSE: try adding math</li>
<li>U+223D REVERSED TILDE: try adding math</li>
<li>U+2243 ASYMPTOTICALLY EQUAL TO: try adding math</li>
<li>U+2245 APPROXIMATELY EQUAL TO: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2252 APPROXIMATELY EQUAL TO OR THE IMAGE OF: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2262 NOT IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2266 LESS-THAN OVER EQUAL TO: try adding math</li>
<li>U+2267 GREATER-THAN OVER EQUAL TO: try adding math</li>
<li>U+226A MUCH LESS-THAN: try adding math</li>
<li>U+226B MUCH GREATER-THAN: try adding math</li>
<li>U+2276 LESS-THAN OR GREATER-THAN: try adding math</li>
<li>U+2277 GREATER-THAN OR LESS-THAN: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+2284 NOT A SUBSET OF: try adding math</li>
<li>U+2285 NOT A SUPERSET OF: try adding math</li>
<li>U+2286 SUBSET OF OR EQUAL TO: try adding math</li>
<li>U+2287 SUPERSET OF OR EQUAL TO: try adding math</li>
<li>U+228A SUBSET OF WITH NOT EQUAL TO: try adding math</li>
<li>U+228B SUPERSET OF WITH NOT EQUAL TO: try adding math</li>
<li>U+2295 CIRCLED PLUS: try adding math</li>
<li>U+2296 CIRCLED MINUS: try adding math</li>
<li>U+2297 CIRCLED TIMES: try adding math</li>
<li>U+22A5 UP TACK: try adding math</li>
<li>U+2305 PROJECTIVE: try adding symbols</li>
<li>U+2306 PERSPECTIVE: try adding symbols</li>
<li>U+2312 ARC: try adding symbols</li>
<li>U+2318 PLACE OF INTEREST SIGN: try adding symbols</li>
<li>U+2325 OPTION KEY: try adding symbols</li>
<li>U+232B ERASE TO THE LEFT: try adding symbols</li>
<li>U+2387 ALTERNATIVE KEY SYMBOL: try adding symbols</li>
<li>U+23CE RETURN SYMBOL: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25C9 FISHEYE: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E1 LOWER HALF CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+25EF LARGE CIRCLE: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2669 QUARTER NOTE: try adding one of: music, symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
<li>U+266B BEAMED EIGHTH NOTES: try adding one of: music, symbols</li>
<li>U+266C BEAMED SIXTEENTH NOTES: try adding one of: music, symbols</li>
<li>U+266D MUSIC FLAT SIGN: try adding one of: music, symbols, math</li>
<li>U+266E MUSIC NATURAL SIGN: try adding one of: music, symbols, math</li>
<li>U+266F MUSIC SHARP SIGN: try adding one of: music, symbols, math</li>
<li>U+26A0 WARNING SIGN: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2765 ROTATED HEAVY BLACK HEART BULLET: try adding symbols</li>
<li>U+2919 LEFTWARDS ARROW-TAIL: try adding math</li>
<li>U+2934 ARROW POINTING RIGHTWARDS THEN CURVING UPWARDS: try adding math</li>
<li>U+2935 ARROW POINTING RIGHTWARDS THEN CURVING DOWNWARDS: try adding math</li>
<li>U+29BF CIRCLED BULLET: try adding one of: symbols, math</li>
<li>U+29FA DOUBLE PLUS: try adding math</li>
<li>U+29FB TRIPLE PLUS: try adding math</li>
<li>U+3000 IDEOGRAPHIC SPACE: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, nushu, yi</li>
<li>U+3001 IDEOGRAPHIC COMMA: try adding one of: japanese, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3002 IDEOGRAPHIC FULL STOP: try adding one of: japanese, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, nushu, yi</li>
<li>U+3003 DITTO MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3005 IDEOGRAPHIC ITERATION MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3006 IDEOGRAPHIC CLOSING MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+3007 IDEOGRAPHIC NUMBER ZERO: try adding one of: phags-pa, chinese-simplified, japanese</li>
<li>U+3008 LEFT ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3009 RIGHT ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300A LEFT DOUBLE ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, lisu, phags-pa, yi</li>
<li>U+300B RIGHT DOUBLE ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, lisu, phags-pa, yi</li>
<li>U+300C LEFT CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300D RIGHT CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300E LEFT WHITE CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300F RIGHT WHITE CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3010 LEFT BLACK LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3011 RIGHT BLACK LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3012 POSTAL MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3013 GETA MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3014 LEFT TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3015 RIGHT TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3016 LEFT WHITE LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3017 RIGHT WHITE LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3018 LEFT WHITE TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3019 RIGHT WHITE TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+301C WAVE DASH: try adding japanese</li>
<li>U+301D REVERSED DOUBLE PRIME QUOTATION MARK: try adding one of: chinese-traditional, chinese-simplified, chinese-hongkong</li>
<li>U+301E DOUBLE PRIME QUOTATION MARK: try adding one of: chinese-traditional, chinese-simplified, chinese-hongkong</li>
<li>U+301F LOW DOUBLE PRIME QUOTATION MARK: not included in any glyphset definition</li>
<li>U+3033 VERTICAL KANA REPEAT MARK UPPER HALF: not included in any glyphset definition</li>
<li>U+3034 VERTICAL KANA REPEAT WITH VOICED SOUND MARK UPPER HALF: not included in any glyphset definition</li>
<li>U+3035 VERTICAL KANA REPEAT MARK LOWER HALF: not included in any glyphset definition</li>
<li>U+303B VERTICAL IDEOGRAPHIC ITERATION MARK: not included in any glyphset definition</li>
<li>U+303C MASU MARK: not included in any glyphset definition</li>
<li>U+303D PART ALTERNATION MARK: not included in any glyphset definition</li>
<li>U+3041 HIRAGANA LETTER SMALL A: try adding one of: chinese-simplified, japanese</li>
<li>U+3042 HIRAGANA LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+3043 HIRAGANA LETTER SMALL I: try adding one of: chinese-simplified, japanese</li>
<li>U+3044 HIRAGANA LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+3045 HIRAGANA LETTER SMALL U: try adding one of: chinese-simplified, japanese</li>
<li>U+3046 HIRAGANA LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+3047 HIRAGANA LETTER SMALL E: try adding one of: chinese-simplified, japanese</li>
<li>U+3048 HIRAGANA LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+3049 HIRAGANA LETTER SMALL O: try adding one of: chinese-simplified, japanese</li>
<li>U+304A HIRAGANA LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+304B HIRAGANA LETTER KA: try adding one of: chinese-simplified, japanese</li>
<li>U+304C HIRAGANA LETTER GA: try adding one of: chinese-simplified, japanese</li>
<li>U+304D HIRAGANA LETTER KI: try adding one of: chinese-simplified, japanese</li>
<li>U+304E HIRAGANA LETTER GI: try adding one of: chinese-simplified, japanese</li>
<li>U+304F HIRAGANA LETTER KU: try adding one of: chinese-simplified, japanese</li>
<li>U+3050 HIRAGANA LETTER GU: try adding one of: chinese-simplified, japanese</li>
<li>U+3051 HIRAGANA LETTER KE: try adding one of: chinese-simplified, japanese</li>
<li>U+3052 HIRAGANA LETTER GE: try adding one of: chinese-simplified, japanese</li>
<li>U+3053 HIRAGANA LETTER KO: try adding one of: chinese-simplified, japanese</li>
<li>U+3054 HIRAGANA LETTER GO: try adding one of: chinese-simplified, japanese</li>
<li>U+3055 HIRAGANA LETTER SA: try adding one of: chinese-simplified, japanese</li>
<li>U+3056 HIRAGANA LETTER ZA: try adding one of: chinese-simplified, japanese</li>
<li>U+3057 HIRAGANA LETTER SI: try adding one of: chinese-simplified, japanese</li>
<li>U+3058 HIRAGANA LETTER ZI: try adding one of: chinese-simplified, japanese</li>
<li>U+3059 HIRAGANA LETTER SU: try adding one of: chinese-simplified, japanese</li>
<li>U+305A HIRAGANA LETTER ZU: try adding one of: chinese-simplified, japanese</li>
<li>U+305B HIRAGANA LETTER SE: try adding one of: chinese-simplified, japanese</li>
<li>U+305C HIRAGANA LETTER ZE: try adding one of: chinese-simplified, japanese</li>
<li>U+305D HIRAGANA LETTER SO: try adding one of: chinese-simplified, japanese</li>
<li>U+305E HIRAGANA LETTER ZO: try adding one of: chinese-simplified, japanese</li>
<li>U+305F HIRAGANA LETTER TA: try adding one of: chinese-simplified, japanese</li>
<li>U+3060 HIRAGANA LETTER DA: try adding one of: chinese-simplified, japanese</li>
<li>U+3061 HIRAGANA LETTER TI: try adding one of: chinese-simplified, japanese</li>
<li>U+3062 HIRAGANA LETTER DI: try adding one of: chinese-simplified, japanese</li>
<li>U+3063 HIRAGANA LETTER SMALL TU: try adding one of: chinese-simplified, japanese</li>
<li>U+3064 HIRAGANA LETTER TU: try adding one of: chinese-simplified, japanese</li>
<li>U+3065 HIRAGANA LETTER DU: try adding one of: chinese-simplified, japanese</li>
<li>U+3066 HIRAGANA LETTER TE: try adding one of: chinese-simplified, japanese</li>
<li>U+3067 HIRAGANA LETTER DE: try adding one of: chinese-simplified, japanese</li>
<li>U+3068 HIRAGANA LETTER TO: try adding one of: chinese-simplified, japanese</li>
<li>U+3069 HIRAGANA LETTER DO: try adding one of: chinese-simplified, japanese</li>
<li>U+306A HIRAGANA LETTER NA: try adding one of: chinese-simplified, japanese</li>
<li>U+306B HIRAGANA LETTER NI: try adding one of: chinese-simplified, japanese</li>
<li>U+306C HIRAGANA LETTER NU: try adding one of: chinese-simplified, japanese</li>
<li>U+306D HIRAGANA LETTER NE: try adding one of: chinese-simplified, japanese</li>
<li>U+306E HIRAGANA LETTER NO: try adding one of: chinese-simplified, japanese</li>
<li>U+306F HIRAGANA LETTER HA: try adding one of: chinese-simplified, japanese</li>
<li>U+3070 HIRAGANA LETTER BA: try adding one of: chinese-simplified, japanese</li>
<li>U+3071 HIRAGANA LETTER PA: try adding one of: chinese-simplified, japanese</li>
<li>U+3072 HIRAGANA LETTER HI: try adding one of: chinese-simplified, japanese</li>
<li>U+3073 HIRAGANA LETTER BI: try adding one of: chinese-simplified, japanese</li>
<li>U+3074 HIRAGANA LETTER PI: try adding one of: chinese-simplified, japanese</li>
<li>U+3075 HIRAGANA LETTER HU: try adding one of: chinese-simplified, japanese</li>
<li>U+3076 HIRAGANA LETTER BU: try adding one of: chinese-simplified, japanese</li>
<li>U+3077 HIRAGANA LETTER PU: try adding one of: chinese-simplified, japanese</li>
<li>U+3078 HIRAGANA LETTER HE: try adding one of: chinese-simplified, japanese</li>
<li>U+3079 HIRAGANA LETTER BE: try adding one of: chinese-simplified, japanese</li>
<li>U+307A HIRAGANA LETTER PE: try adding one of: chinese-simplified, japanese</li>
<li>U+307B HIRAGANA LETTER HO: try adding one of: chinese-simplified, japanese</li>
<li>U+307C HIRAGANA LETTER BO: try adding one of: chinese-simplified, japanese</li>
<li>U+307D HIRAGANA LETTER PO: try adding one of: chinese-simplified, japanese</li>
<li>U+307E HIRAGANA LETTER MA: try adding one of: chinese-simplified, japanese</li>
<li>U+307F HIRAGANA LETTER MI: try adding one of: chinese-simplified, japanese</li>
<li>U+3080 HIRAGANA LETTER MU: try adding one of: chinese-simplified, japanese</li>
<li>U+3081 HIRAGANA LETTER ME: try adding one of: chinese-simplified, japanese</li>
<li>U+3082 HIRAGANA LETTER MO: try adding one of: chinese-simplified, japanese</li>
<li>U+3083 HIRAGANA LETTER SMALL YA: try adding one of: chinese-simplified, japanese</li>
<li>U+3084 HIRAGANA LETTER YA: try adding one of: chinese-simplified, japanese</li>
<li>U+3085 HIRAGANA LETTER SMALL YU: try adding one of: chinese-simplified, japanese</li>
<li>U+3086 HIRAGANA LETTER YU: try adding one of: chinese-simplified, japanese</li>
<li>U+3087 HIRAGANA LETTER SMALL YO: try adding one of: chinese-simplified, japanese</li>
<li>U+3088 HIRAGANA LETTER YO: try adding one of: chinese-simplified, japanese</li>
<li>U+3089 HIRAGANA LETTER RA: try adding one of: chinese-simplified, japanese</li>
<li>U+308A HIRAGANA LETTER RI: try adding one of: chinese-simplified, japanese</li>
<li>U+308B HIRAGANA LETTER RU: try adding one of: chinese-simplified, japanese</li>
<li>U+308C HIRAGANA LETTER RE: try adding one of: chinese-simplified, japanese</li>
<li>U+308D HIRAGANA LETTER RO: try adding one of: chinese-simplified, japanese</li>
<li>U+308E HIRAGANA LETTER SMALL WA: try adding one of: chinese-simplified, japanese</li>
<li>U+308F HIRAGANA LETTER WA: try adding one of: chinese-simplified, japanese</li>
<li>U+3090 HIRAGANA LETTER WI: try adding one of: chinese-simplified, japanese</li>
<li>U+3091 HIRAGANA LETTER WE: try adding one of: chinese-simplified, japanese</li>
<li>U+3092 HIRAGANA LETTER WO: try adding one of: chinese-simplified, japanese</li>
<li>U+3093 HIRAGANA LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+3094 HIRAGANA LETTER VU: try adding one of: chinese-simplified, japanese</li>
<li>U+3095 HIRAGANA LETTER SMALL KA: try adding one of: chinese-simplified, japanese</li>
<li>U+3096 HIRAGANA LETTER SMALL KE: try adding one of: chinese-simplified, japanese</li>
<li>U+3099 COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309A COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309B KATAKANA-HIRAGANA VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309C KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309D HIRAGANA ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+309E HIRAGANA VOICED ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+309F HIRAGANA DIGRAPH YORI: try adding one of: chinese-simplified, japanese</li>
<li>U+30A0 KATAKANA-HIRAGANA DOUBLE HYPHEN: try adding one of: chinese-simplified, japanese</li>
<li>U+30A1 KATAKANA LETTER SMALL A: try adding one of: chinese-simplified, japanese</li>
<li>U+30A2 KATAKANA LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+30A3 KATAKANA LETTER SMALL I: try adding one of: chinese-simplified, japanese</li>
<li>U+30A4 KATAKANA LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+30A5 KATAKANA LETTER SMALL U: try adding one of: chinese-simplified, japanese</li>
<li>U+30A6 KATAKANA LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+30A7 KATAKANA LETTER SMALL E: try adding one of: chinese-simplified, japanese</li>
<li>U+30A8 KATAKANA LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+30A9 KATAKANA LETTER SMALL O: try adding one of: chinese-simplified, japanese</li>
<li>U+30AA KATAKANA LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+30AB KATAKANA LETTER KA: try adding one of: chinese-simplified, japanese</li>
<li>U+30AC KATAKANA LETTER GA: try adding one of: chinese-simplified, japanese</li>
<li>U+30AD KATAKANA LETTER KI: try adding one of: chinese-simplified, japanese</li>
<li>U+30AE KATAKANA LETTER GI: try adding one of: chinese-simplified, japanese</li>
<li>U+30AF KATAKANA LETTER KU: try adding one of: chinese-simplified, japanese</li>
<li>U+30B0 KATAKANA LETTER GU: try adding one of: chinese-simplified, japanese</li>
<li>U+30B1 KATAKANA LETTER KE: try adding one of: chinese-simplified, japanese</li>
<li>U+30B2 KATAKANA LETTER GE: try adding one of: chinese-simplified, japanese</li>
<li>U+30B3 KATAKANA LETTER KO: try adding one of: chinese-simplified, japanese</li>
<li>U+30B4 KATAKANA LETTER GO: try adding one of: chinese-simplified, japanese</li>
<li>U+30B5 KATAKANA LETTER SA: try adding one of: chinese-simplified, japanese</li>
<li>U+30B6 KATAKANA LETTER ZA: try adding one of: chinese-simplified, japanese</li>
<li>U+30B7 KATAKANA LETTER SI: try adding one of: chinese-simplified, japanese</li>
<li>U+30B8 KATAKANA LETTER ZI: try adding one of: chinese-simplified, japanese</li>
<li>U+30B9 KATAKANA LETTER SU: try adding one of: chinese-simplified, japanese</li>
<li>U+30BA KATAKANA LETTER ZU: try adding one of: chinese-simplified, japanese</li>
<li>U+30BB KATAKANA LETTER SE: try adding one of: chinese-simplified, japanese</li>
<li>U+30BC KATAKANA LETTER ZE: try adding one of: chinese-simplified, japanese</li>
<li>U+30BD KATAKANA LETTER SO: try adding one of: chinese-simplified, japanese</li>
<li>U+30BE KATAKANA LETTER ZO: try adding one of: chinese-simplified, japanese</li>
<li>U+30BF KATAKANA LETTER TA: try adding one of: chinese-simplified, japanese</li>
<li>U+30C0 KATAKANA LETTER DA: try adding one of: chinese-simplified, japanese</li>
<li>U+30C1 KATAKANA LETTER TI: try adding one of: chinese-simplified, japanese</li>
<li>U+30C2 KATAKANA LETTER DI: try adding one of: chinese-simplified, japanese</li>
<li>U+30C3 KATAKANA LETTER SMALL TU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C4 KATAKANA LETTER TU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C5 KATAKANA LETTER DU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C6 KATAKANA LETTER TE: try adding one of: chinese-simplified, japanese</li>
<li>U+30C7 KATAKANA LETTER DE: try adding one of: chinese-simplified, japanese</li>
<li>U+30C8 KATAKANA LETTER TO: try adding one of: chinese-simplified, japanese</li>
<li>U+30C9 KATAKANA LETTER DO: try adding one of: chinese-simplified, japanese</li>
<li>U+30CA KATAKANA LETTER NA: try adding one of: chinese-simplified, japanese</li>
<li>U+30CB KATAKANA LETTER NI: try adding one of: chinese-simplified, japanese</li>
<li>U+30CC KATAKANA LETTER NU: try adding one of: chinese-simplified, japanese</li>
<li>U+30CD KATAKANA LETTER NE: try adding one of: chinese-simplified, japanese</li>
<li>U+30CE KATAKANA LETTER NO: try adding one of: chinese-simplified, japanese</li>
<li>U+30CF KATAKANA LETTER HA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D0 KATAKANA LETTER BA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D1 KATAKANA LETTER PA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D2 KATAKANA LETTER HI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D3 KATAKANA LETTER BI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D4 KATAKANA LETTER PI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D5 KATAKANA LETTER HU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D6 KATAKANA LETTER BU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D7 KATAKANA LETTER PU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D8 KATAKANA LETTER HE: try adding one of: chinese-simplified, japanese</li>
<li>U+30D9 KATAKANA LETTER BE: try adding one of: chinese-simplified, japanese</li>
<li>U+30DA KATAKANA LETTER PE: try adding one of: chinese-simplified, japanese</li>
<li>U+30DB KATAKANA LETTER HO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DC KATAKANA LETTER BO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DD KATAKANA LETTER PO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DE KATAKANA LETTER MA: try adding one of: chinese-simplified, japanese</li>
<li>U+30DF KATAKANA LETTER MI: try adding one of: chinese-simplified, japanese</li>
<li>U+30E0 KATAKANA LETTER MU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E1 KATAKANA LETTER ME: try adding one of: chinese-simplified, japanese</li>
<li>U+30E2 KATAKANA LETTER MO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E3 KATAKANA LETTER SMALL YA: try adding one of: chinese-simplified, japanese</li>
<li>U+30E4 KATAKANA LETTER YA: try adding one of: chinese-simplified, japanese</li>
<li>U+30E5 KATAKANA LETTER SMALL YU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E6 KATAKANA LETTER YU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E7 KATAKANA LETTER SMALL YO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E8 KATAKANA LETTER YO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E9 KATAKANA LETTER RA: try adding one of: chinese-simplified, japanese</li>
<li>U+30EA KATAKANA LETTER RI: try adding one of: chinese-simplified, japanese</li>
<li>U+30EB KATAKANA LETTER RU: try adding one of: chinese-simplified, japanese</li>
<li>U+30EC KATAKANA LETTER RE: try adding one of: chinese-simplified, japanese</li>
<li>U+30ED KATAKANA LETTER RO: try adding one of: chinese-simplified, japanese</li>
<li>U+30EE KATAKANA LETTER SMALL WA: try adding one of: chinese-simplified, japanese</li>
<li>U+30EF KATAKANA LETTER WA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F0 KATAKANA LETTER WI: try adding one of: chinese-simplified, japanese</li>
<li>U+30F1 KATAKANA LETTER WE: try adding one of: chinese-simplified, japanese</li>
<li>U+30F2 KATAKANA LETTER WO: try adding one of: chinese-simplified, japanese</li>
<li>U+30F3 KATAKANA LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+30F4 KATAKANA LETTER VU: try adding one of: chinese-simplified, japanese</li>
<li>U+30F5 KATAKANA LETTER SMALL KA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F6 KATAKANA LETTER SMALL KE: try adding one of: chinese-simplified, japanese</li>
<li>U+30F7 KATAKANA LETTER VA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F8 KATAKANA LETTER VI: try adding one of: chinese-simplified, japanese</li>
<li>U+30F9 KATAKANA LETTER VE: try adding one of: chinese-simplified, japanese</li>
<li>U+30FA KATAKANA LETTER VO: try adding one of: chinese-simplified, japanese</li>
<li>U+30FB KATAKANA MIDDLE DOT: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+30FC KATAKANA-HIRAGANA PROLONGED SOUND MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FD KATAKANA ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FE KATAKANA VOICED ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FF KATAKANA DIGRAPH KOTO: try adding one of: chinese-simplified, japanese</li>
<li>U+31F0 KATAKANA LETTER SMALL KU: not included in any glyphset definition</li>
<li>U+31F1 KATAKANA LETTER SMALL SI: not included in any glyphset definition</li>
<li>U+31F2 KATAKANA LETTER SMALL SU: not included in any glyphset definition</li>
<li>U+31F3 KATAKANA LETTER SMALL TO: not included in any glyphset definition</li>
<li>U+31F4 KATAKANA LETTER SMALL NU: not included in any glyphset definition</li>
<li>U+31F5 KATAKANA LETTER SMALL HA: not included in any glyphset definition</li>
<li>U+31F6 KATAKANA LETTER SMALL HI: not included in any glyphset definition</li>
<li>U+31F7 KATAKANA LETTER SMALL HU: not included in any glyphset definition</li>
<li>U+31F8 KATAKANA LETTER SMALL HE: not included in any glyphset definition</li>
<li>U+31F9 KATAKANA LETTER SMALL HO: not included in any glyphset definition</li>
<li>U+31FA KATAKANA LETTER SMALL MU: not included in any glyphset definition</li>
<li>U+31FB KATAKANA LETTER SMALL RA: not included in any glyphset definition</li>
<li>U+31FC KATAKANA LETTER SMALL RI: not included in any glyphset definition</li>
<li>U+31FD KATAKANA LETTER SMALL RU: not included in any glyphset definition</li>
<li>U+31FE KATAKANA LETTER SMALL RE: not included in any glyphset definition</li>
<li>U+31FF KATAKANA LETTER SMALL RO: not included in any glyphset definition</li>
<li>U+33CB SQUARE HP: not included in any glyphset definition</li>
<li>U+4EDD CJK UNIFIED IDEOGRAPH-4EDD: try adding one of: chinese-traditional, japanese, chinese-simplified, chinese-hongkong</li>
<li>U+E133 : not included in any glyphset definition</li>
<li>U+E134 : not included in any glyphset definition</li>
<li>U+E139 : not included in any glyphset definition</li>
<li>U+E140 : not included in any glyphset definition</li>
<li>U+F001 : not included in any glyphset definition</li>
<li>U+F002 : not included in any glyphset definition</li>
<li>U+F003 : not included in any glyphset definition</li>
<li>U+F700 : not included in any glyphset definition</li>
<li>U+F701 : not included in any glyphset definition</li>
<li>U+F702 : not included in any glyphset definition</li>
<li>U+F703 : not included in any glyphset definition</li>
<li>U+F704 : not included in any glyphset definition</li>
<li>U+F705 : not included in any glyphset definition</li>
<li>U+F706 : not included in any glyphset definition</li>
<li>U+F707 : not included in any glyphset definition</li>
<li>U+F708 : not included in any glyphset definition</li>
<li>U+F709 : not included in any glyphset definition</li>
<li>U+F70A : not included in any glyphset definition</li>
<li>U+F70B : not included in any glyphset definition</li>
<li>U+F70C : not included in any glyphset definition</li>
<li>U+F70D : not included in any glyphset definition</li>
<li>U+F70E : not included in any glyphset definition</li>
<li>U+F70F : not included in any glyphset definition</li>
<li>U+F710 : not included in any glyphset definition</li>
<li>U+F711 : not included in any glyphset definition</li>
<li>U+F712 : not included in any glyphset definition</li>
<li>U+F713 : not included in any glyphset definition</li>
<li>U+F714 : not included in any glyphset definition</li>
<li>U+F715 : not included in any glyphset definition</li>
<li>U+F716 : not included in any glyphset definition</li>
<li>U+F717 : not included in any glyphset definition</li>
<li>U+F718 : not included in any glyphset definition</li>
<li>U+F719 : not included in any glyphset definition</li>
<li>U+F71A : not included in any glyphset definition</li>
<li>U+F71E : not included in any glyphset definition</li>
<li>U+F71F : not included in any glyphset definition</li>
<li>U+F720 : not included in any glyphset definition</li>
<li>U+F880 : not included in any glyphset definition</li>
<li>U+F881 : not included in any glyphset definition</li>
<li>U+F882 : not included in any glyphset definition</li>
<li>U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
<li>U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition</li>
<li>U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition</li>
<li>U+FE45 SESAME DOT: not included in any glyphset definition</li>
<li>U+FE46 WHITE SESAME DOT: not included in any glyphset definition</li>
<li>U+FF01 FULLWIDTH EXCLAMATION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF02 FULLWIDTH QUOTATION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF03 FULLWIDTH NUMBER SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF04 FULLWIDTH DOLLAR SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF05 FULLWIDTH PERCENT SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF06 FULLWIDTH AMPERSAND: try adding one of: chinese-simplified, japanese</li>
<li>U+FF07 FULLWIDTH APOSTROPHE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF08 FULLWIDTH LEFT PARENTHESIS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF09 FULLWIDTH RIGHT PARENTHESIS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0A FULLWIDTH ASTERISK: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0B FULLWIDTH PLUS SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0C FULLWIDTH COMMA: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0D FULLWIDTH HYPHEN-MINUS: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0E FULLWIDTH FULL STOP: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0F FULLWIDTH SOLIDUS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF10 FULLWIDTH DIGIT ZERO: try adding one of: chinese-simplified, japanese</li>
<li>U+FF11 FULLWIDTH DIGIT ONE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF12 FULLWIDTH DIGIT TWO: try adding one of: chinese-simplified, japanese</li>
<li>U+FF13 FULLWIDTH DIGIT THREE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF14 FULLWIDTH DIGIT FOUR: try adding one of: chinese-simplified, japanese</li>
<li>U+FF15 FULLWIDTH DIGIT FIVE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF16 FULLWIDTH DIGIT SIX: try adding one of: chinese-simplified, japanese</li>
<li>U+FF17 FULLWIDTH DIGIT SEVEN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF18 FULLWIDTH DIGIT EIGHT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF19 FULLWIDTH DIGIT NINE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1A FULLWIDTH COLON: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF1B FULLWIDTH SEMICOLON: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF1C FULLWIDTH LESS-THAN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1D FULLWIDTH EQUALS SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1E FULLWIDTH GREATER-THAN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1F FULLWIDTH QUESTION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF20 FULLWIDTH COMMERCIAL AT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF21 FULLWIDTH LATIN CAPITAL LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+FF22 FULLWIDTH LATIN CAPITAL LETTER B: try adding one of: chinese-simplified, japanese</li>
<li>U+FF23 FULLWIDTH LATIN CAPITAL LETTER C: try adding one of: chinese-simplified, japanese</li>
<li>U+FF24 FULLWIDTH LATIN CAPITAL LETTER D: try adding one of: chinese-simplified, japanese</li>
<li>U+FF25 FULLWIDTH LATIN CAPITAL LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+FF26 FULLWIDTH LATIN CAPITAL LETTER F: try adding one of: chinese-simplified, japanese</li>
<li>U+FF27 FULLWIDTH LATIN CAPITAL LETTER G: try adding one of: chinese-simplified, japanese</li>
<li>U+FF28 FULLWIDTH LATIN CAPITAL LETTER H: try adding one of: chinese-simplified, japanese</li>
<li>U+FF29 FULLWIDTH LATIN CAPITAL LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2A FULLWIDTH LATIN CAPITAL LETTER J: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2B FULLWIDTH LATIN CAPITAL LETTER K: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2C FULLWIDTH LATIN CAPITAL LETTER L: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2D FULLWIDTH LATIN CAPITAL LETTER M: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2E FULLWIDTH LATIN CAPITAL LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2F FULLWIDTH LATIN CAPITAL LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+FF30 FULLWIDTH LATIN CAPITAL LETTER P: try adding one of: chinese-simplified, japanese</li>
<li>U+FF31 FULLWIDTH LATIN CAPITAL LETTER Q: try adding one of: chinese-simplified, japanese</li>
<li>U+FF32 FULLWIDTH LATIN CAPITAL LETTER R: try adding one of: chinese-simplified, japanese</li>
<li>U+FF33 FULLWIDTH LATIN CAPITAL LETTER S: try adding one of: chinese-simplified, japanese</li>
<li>U+FF34 FULLWIDTH LATIN CAPITAL LETTER T: try adding one of: chinese-simplified, japanese</li>
<li>U+FF35 FULLWIDTH LATIN CAPITAL LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+FF36 FULLWIDTH LATIN CAPITAL LETTER V: try adding one of: chinese-simplified, japanese</li>
<li>U+FF37 FULLWIDTH LATIN CAPITAL LETTER W: try adding one of: chinese-simplified, japanese</li>
<li>U+FF38 FULLWIDTH LATIN CAPITAL LETTER X: try adding one of: chinese-simplified, japanese</li>
<li>U+FF39 FULLWIDTH LATIN CAPITAL LETTER Y: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3A FULLWIDTH LATIN CAPITAL LETTER Z: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3B FULLWIDTH LEFT SQUARE BRACKET: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF3C FULLWIDTH REVERSE SOLIDUS: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3D FULLWIDTH RIGHT SQUARE BRACKET: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF3E FULLWIDTH CIRCUMFLEX ACCENT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3F FULLWIDTH LOW LINE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF40 FULLWIDTH GRAVE ACCENT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF41 FULLWIDTH LATIN SMALL LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+FF42 FULLWIDTH LATIN SMALL LETTER B: try adding one of: chinese-simplified, japanese</li>
<li>U+FF43 FULLWIDTH LATIN SMALL LETTER C: try adding one of: chinese-simplified, japanese</li>
<li>U+FF44 FULLWIDTH LATIN SMALL LETTER D: try adding one of: chinese-simplified, japanese</li>
<li>U+FF45 FULLWIDTH LATIN SMALL LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+FF46 FULLWIDTH LATIN SMALL LETTER F: try adding one of: chinese-simplified, japanese</li>
<li>U+FF47 FULLWIDTH LATIN SMALL LETTER G: try adding one of: chinese-simplified, japanese</li>
<li>U+FF48 FULLWIDTH LATIN SMALL LETTER H: try adding one of: chinese-simplified, japanese</li>
<li>U+FF49 FULLWIDTH LATIN SMALL LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4A FULLWIDTH LATIN SMALL LETTER J: try adding japanese</li>
<li>U+FF4B FULLWIDTH LATIN SMALL LETTER K: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4C FULLWIDTH LATIN SMALL LETTER L: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4D FULLWIDTH LATIN SMALL LETTER M: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4E FULLWIDTH LATIN SMALL LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4F FULLWIDTH LATIN SMALL LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+FF50 FULLWIDTH LATIN SMALL LETTER P: try adding one of: chinese-simplified, japanese</li>
<li>U+FF51 FULLWIDTH LATIN SMALL LETTER Q: try adding one of: chinese-simplified, japanese</li>
<li>U+FF52 FULLWIDTH LATIN SMALL LETTER R: try adding one of: chinese-simplified, japanese</li>
<li>U+FF53 FULLWIDTH LATIN SMALL LETTER S: try adding one of: chinese-simplified, japanese</li>
<li>U+FF54 FULLWIDTH LATIN SMALL LETTER T: try adding one of: chinese-simplified, japanese</li>
<li>U+FF55 FULLWIDTH LATIN SMALL LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+FF56 FULLWIDTH LATIN SMALL LETTER V: try adding one of: chinese-simplified, japanese</li>
<li>U+FF57 FULLWIDTH LATIN SMALL LETTER W: try adding one of: chinese-simplified, japanese</li>
<li>U+FF58 FULLWIDTH LATIN SMALL LETTER X: try adding one of: chinese-simplified, japanese</li>
<li>U+FF59 FULLWIDTH LATIN SMALL LETTER Y: try adding one of: chinese-simplified, japanese</li>
<li>U+FF5A FULLWIDTH LATIN SMALL LETTER Z: try adding japanese</li>
<li>U+FF5B FULLWIDTH LEFT CURLY BRACKET: try adding one of: math, chinese-simplified, yi, japanese</li>
<li>U+FF5C FULLWIDTH VERTICAL LINE: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF5D FULLWIDTH RIGHT CURLY BRACKET: try adding one of: math, chinese-simplified, yi, japanese</li>
<li>U+FF5E FULLWIDTH TILDE: try adding one of: chinese-simplified, yi</li>
<li>U+FF5F FULLWIDTH LEFT WHITE PARENTHESIS: not included in any glyphset definition</li>
<li>U+FF60 FULLWIDTH RIGHT WHITE PARENTHESIS: not included in any glyphset definition</li>
<li>U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP: try adding yi</li>
<li>U+FF62 HALFWIDTH LEFT CORNER BRACKET: try adding yi</li>
<li>U+FF63 HALFWIDTH RIGHT CORNER BRACKET: try adding yi</li>
<li>U+FF64 HALFWIDTH IDEOGRAPHIC COMMA: try adding yi</li>
<li>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT: try adding yi</li>
<li>U+FF66 HALFWIDTH KATAKANA LETTER WO: not included in any glyphset definition</li>
<li>U+FF67 HALFWIDTH KATAKANA LETTER SMALL A: not included in any glyphset definition</li>
<li>U+FF68 HALFWIDTH KATAKANA LETTER SMALL I: not included in any glyphset definition</li>
<li>U+FF69 HALFWIDTH KATAKANA LETTER SMALL U: not included in any glyphset definition</li>
<li>U+FF6A HALFWIDTH KATAKANA LETTER SMALL E: not included in any glyphset definition</li>
<li>U+FF6B HALFWIDTH KATAKANA LETTER SMALL O: not included in any glyphset definition</li>
<li>U+FF6C HALFWIDTH KATAKANA LETTER SMALL YA: not included in any glyphset definition</li>
<li>U+FF6D HALFWIDTH KATAKANA LETTER SMALL YU: not included in any glyphset definition</li>
<li>U+FF6E HALFWIDTH KATAKANA LETTER SMALL YO: not included in any glyphset definition</li>
<li>U+FF6F HALFWIDTH KATAKANA LETTER SMALL TU: not included in any glyphset definition</li>
<li>U+FF70 HALFWIDTH KATAKANA-HIRAGANA PROLONGED SOUND MARK: not included in any glyphset definition</li>
<li>U+FF71 HALFWIDTH KATAKANA LETTER A: not included in any glyphset definition</li>
<li>U+FF72 HALFWIDTH KATAKANA LETTER I: not included in any glyphset definition</li>
<li>U+FF73 HALFWIDTH KATAKANA LETTER U: not included in any glyphset definition</li>
<li>U+FF74 HALFWIDTH KATAKANA LETTER E: not included in any glyphset definition</li>
<li>U+FF75 HALFWIDTH KATAKANA LETTER O: not included in any glyphset definition</li>
<li>U+FF76 HALFWIDTH KATAKANA LETTER KA: not included in any glyphset definition</li>
<li>U+FF77 HALFWIDTH KATAKANA LETTER KI: not included in any glyphset definition</li>
<li>U+FF78 HALFWIDTH KATAKANA LETTER KU: not included in any glyphset definition</li>
<li>U+FF79 HALFWIDTH KATAKANA LETTER KE: not included in any glyphset definition</li>
<li>U+FF7A HALFWIDTH KATAKANA LETTER KO: not included in any glyphset definition</li>
<li>U+FF7B HALFWIDTH KATAKANA LETTER SA: not included in any glyphset definition</li>
<li>U+FF7C HALFWIDTH KATAKANA LETTER SI: not included in any glyphset definition</li>
<li>U+FF7D HALFWIDTH KATAKANA LETTER SU: not included in any glyphset definition</li>
<li>U+FF7E HALFWIDTH KATAKANA LETTER SE: not included in any glyphset definition</li>
<li>U+FF7F HALFWIDTH KATAKANA LETTER SO: not included in any glyphset definition</li>
<li>U+FF80 HALFWIDTH KATAKANA LETTER TA: not included in any glyphset definition</li>
<li>U+FF81 HALFWIDTH KATAKANA LETTER TI: not included in any glyphset definition</li>
<li>U+FF82 HALFWIDTH KATAKANA LETTER TU: not included in any glyphset definition</li>
<li>U+FF83 HALFWIDTH KATAKANA LETTER TE: not included in any glyphset definition</li>
<li>U+FF84 HALFWIDTH KATAKANA LETTER TO: not included in any glyphset definition</li>
<li>U+FF85 HALFWIDTH KATAKANA LETTER NA: not included in any glyphset definition</li>
<li>U+FF86 HALFWIDTH KATAKANA LETTER NI: not included in any glyphset definition</li>
<li>U+FF87 HALFWIDTH KATAKANA LETTER NU: not included in any glyphset definition</li>
<li>U+FF88 HALFWIDTH KATAKANA LETTER NE: not included in any glyphset definition</li>
<li>U+FF89 HALFWIDTH KATAKANA LETTER NO: not included in any glyphset definition</li>
<li>U+FF8A HALFWIDTH KATAKANA LETTER HA: not included in any glyphset definition</li>
<li>U+FF8B HALFWIDTH KATAKANA LETTER HI: not included in any glyphset definition</li>
<li>U+FF8C HALFWIDTH KATAKANA LETTER HU: not included in any glyphset definition</li>
<li>U+FF8D HALFWIDTH KATAKANA LETTER HE: not included in any glyphset definition</li>
<li>U+FF8E HALFWIDTH KATAKANA LETTER HO: not included in any glyphset definition</li>
<li>U+FF8F HALFWIDTH KATAKANA LETTER MA: not included in any glyphset definition</li>
<li>U+FF90 HALFWIDTH KATAKANA LETTER MI: not included in any glyphset definition</li>
<li>U+FF91 HALFWIDTH KATAKANA LETTER MU: not included in any glyphset definition</li>
<li>U+FF92 HALFWIDTH KATAKANA LETTER ME: not included in any glyphset definition</li>
<li>U+FF93 HALFWIDTH KATAKANA LETTER MO: not included in any glyphset definition</li>
<li>U+FF94 HALFWIDTH KATAKANA LETTER YA: not included in any glyphset definition</li>
<li>U+FF95 HALFWIDTH KATAKANA LETTER YU: not included in any glyphset definition</li>
<li>U+FF96 HALFWIDTH KATAKANA LETTER YO: not included in any glyphset definition</li>
<li>U+FF97 HALFWIDTH KATAKANA LETTER RA: not included in any glyphset definition</li>
<li>U+FF98 HALFWIDTH KATAKANA LETTER RI: not included in any glyphset definition</li>
<li>U+FF99 HALFWIDTH KATAKANA LETTER RU: not included in any glyphset definition</li>
<li>U+FF9A HALFWIDTH KATAKANA LETTER RE: not included in any glyphset definition</li>
<li>U+FF9B HALFWIDTH KATAKANA LETTER RO: not included in any glyphset definition</li>
<li>U+FF9C HALFWIDTH KATAKANA LETTER WA: not included in any glyphset definition</li>
<li>U+FF9D HALFWIDTH KATAKANA LETTER N: not included in any glyphset definition</li>
<li>U+FF9E HALFWIDTH KATAKANA VOICED SOUND MARK: not included in any glyphset definition</li>
<li>U+FF9F HALFWIDTH KATAKANA SEMI-VOICED SOUND MARK: not included in any glyphset definition</li>
<li>U+FFE0 FULLWIDTH CENT SIGN: try adding chinese-simplified</li>
<li>U+FFE1 FULLWIDTH POUND SIGN: try adding chinese-simplified</li>
<li>U+FFE2 FULLWIDTH NOT SIGN: not included in any glyphset definition</li>
<li>U+FFE3 FULLWIDTH MACRON: try adding one of: chinese-simplified, japanese</li>
<li>U+FFE4 FULLWIDTH BROKEN BAR: not included in any glyphset definition</li>
<li>U+FFE5 FULLWIDTH YEN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FFE6 FULLWIDTH WON SIGN: not included in any glyphset definition</li>
<li>U+FFE8 HALFWIDTH FORMS LIGHT VERTICAL: not included in any glyphset definition</li>
<li>U+FFE9 HALFWIDTH LEFTWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEA HALFWIDTH UPWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEB HALFWIDTH RIGHTWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEC HALFWIDTH DOWNWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFED HALFWIDTH BLACK SQUARE: not included in any glyphset definition</li>
<li>U+FFEE HALFWIDTH WHITE CIRCLE: not included in any glyphset definition</li>
<li>U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition</li>
<li>U+1F494 BROKEN HEART: not included in any glyphset definition</li>
<li>U+1FBB0 ARROWHEAD-SHAPED POINTER: try adding symbols</li>
<li>U+1FBB2 LEFT HALF RUNNING MAN: try adding symbols</li>
<li>U+1FBB3 RIGHT HALF RUNNING MAN: try adding symbols</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>lao</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>thai</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>









* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ i̍ i̓ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ і́ ḭ̀ ḭ́ ḭ̄ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ i̎ i̒ i̔ i̛̅ i̛̇ i̛̊ i̛̋ i̛̍ i̛̎ i̛̒ i̛̓ i̛̔ i̤̅ i̤̇ i̤̊ i̤̋ i̤̍ i̤̎</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>

<details><summary>[20] SyyFlowey-Bold.ttf</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>







* 🔥 **FAIL** <p>The PANOSE numbers are incorrect for a monospaced font. Please set PANOSE Proportion to 9 (monospaced)</p>
 [code: mono-bad-panose]



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1912 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 695 glyphs (36.31%) have a different width. You should check the widths of: ['nonmarkingreturn', 'sterling', 'currency', 'dieresis', 'copyright', 'registered', 'plusminus', 'onequarter', 'onehalf', 'threequarters', 'multiply', 'divide', 'uni01C0', 'uni01C1', 'uni02B9', 'uni02BA', 'quoteleft', 'quoteright', 'quotereversed', 'circumflex', 'caron', 'uni02C8', 'uni02C9', 'uni02CA', 'uni02CB', 'breve', 'dotaccent', 'ring', 'ogonek', 'tilde', 'hungarumlaut', 'uni02F6', 'dieresistonos', 'uni0409', 'uni040A', 'uni0416', 'uni0424', 'uni0428', 'uni0429', 'uni042E', 'uni0436', 'uni0444', 'uni0448', 'uni0449', 'uni044E', 'uni0459', 'uni045A', 'uni0496', 'uni0497', 'uni04A2', 'uni04A3', 'uni04C1', 'uni04C2', 'uni04DC', 'uni04DD', 'uni0E01', 'uni0E03', 'uni0E04', 'uni0E05', 'uni0E06', 'uni0E09', 'uni0E0A', 'uni0E0B', 'uni0E0C', 'uni0E0D', 'uni0E11', 'uni0E12', 'uni0E13', 'uni0E14', 'uni0E15', 'uni0E16', 'uni0E17', 'uni0E1A', 'uni0E1B', 'uni0E1E', 'uni0E1F', 'uni0E23', 'uni0E24', 'uni0E27', 'uni0E28', 'uni0E29', 'uni0E2B', 'uni0E2C', 'uni0E30', 'uni0E32', 'uni0E33', 'uni0E40', 'uni0E41', 'uni0E45', 'uni0E4F', 'uni0E50', 'uni0E51', 'uni0E52', 'uni0E53', 'uni0E54', 'uni0E55', 'uni0E56', 'uni0E57', 'uni0E58', 'uni0E59', 'uni0E5A', 'uni0E5B', 'uni0E84', 'uni0E85', 'uni0E86', 'uni0E87', 'uni0E8E', 'uni0E91', 'uni0E92', 'uni0E93', 'uni0E94', 'uni0E95', 'uni0E97', 'uni0E9A', 'uni0E9B', 'uni0E9E', 'uni0E9F', 'uni0EA4', 'uni0EA5', 'uni0EA6', 'uni0EA8', 'uni0EA9', 'uni0EAA', 'uni0EAB', 'uni0EAC', 'uni0EB0', 'uni0EB2', 'uni0EB3', 'uni0EC0', 'uni0EC1', 'uni0ED0', 'uni0ED1', 'uni0ED2', 'uni0ED3', 'uni0ED4', 'uni0ED5', 'uni0ED6', 'uni0ED7', 'uni0ED8', 'uni0ED9', 'uni0EDC', 'uni0EDD', 'uni2000', 'uni2001', 'uni2002', 'uni2003', 'uni2004', 'uni2005', 'uni2006', 'uni2007', 'uni2008', 'uni2009', 'uni200A', 'uni2010', 'uni2011', 'figuredash', 'endash', 'emdash', 'uni2015', 'uni2016', 'quotesinglbase', 'twodotenleader', 'perthousand', 'minute', 'second', 'uni2034', 'uni203B', 'uni203E', 'uni2081', 'uni2082', 'uni2083', 'uni2084', 'uni2085', 'uni2086', 'uni2087', 'uni2088', 'uni2089', 'uni208A', 'uni208B', 'uni208C', 'uni208D', 'uni208E', 'Euro', 'uni2103', 'uni210F', 'uni2113', 'trademark', 'Omega', 'uni2127', 'uni212B', 'aleph', 'arrowleft', 'arrowup', 'arrowright', 'arrowdown', 'arrowboth', 'arrowupdn', 'uni2196', 'uni2197', 'uni2198', 'uni2199', 'uni21A9', 'uni21AA', 'carriagereturn', 'uni21C4', 'arrowdblleft', 'arrowdblup', 'arrowdblright', 'arrowdbldown', 'arrowdblboth', 'uni21D5', 'uni21D6', 'uni21D7', 'uni21D8', 'uni21D9', 'uni21E5', 'uni21E6', 'uni21E7', 'uni21E8', 'uni21E9', 'uni21EA', 'uni21EB', 'uni21EC', 'uni21ED', 'uni21EE', 'uni21EF', 'uni21F0', 'uni21F1', 'uni21F2', 'uni21F3', 'universal', 'partialdiff', 'existential', 'emptyset', 'Delta', 'gradient', 'element', 'notelement', 'suchthat', 'summation', 'minus', 'uni2213', 'radical', 'proportional', 'infinity', 'angle', 'uni2225', 'uni2226', 'logicaland', 'logicalor', 'intersection', 'union', 'uni222C', 'therefore', 'uni2235', 'uni223D', 'uni2243', 'congruent', 'approxequal', 'uni2252', 'equivalence', 'uni2262', 'uni2266', 'uni2267', 'uni226A', 'uni226B', 'uni2276', 'uni2277', 'propersubset', 'propersuperset', 'notsubset', 'uni2285', 'reflexsubset', 'reflexsuperset', 'uni228A', 'uni228B', 'circleplus', 'uni2296', 'circlemultiply', 'perpendicular', 'uni2305', 'uni2306', 'uni2312', 'uni2318', 'uni2325', 'uni232B', 'uni2387', 'uni23CE', 'filledbox', 'H22073', 'triagup', 'uni25B3', 'uni25B6', 'uni25B7', 'triagdn', 'uni25BD', 'uni25C0', 'uni25C1', 'uni25C6', 'uni25C7', 'uni25C9', 'circle', 'uni25CE', 'H18533', 'uni25EF', 'uni2605', 'uni2606', 'female', 'male', 'uni2661', 'heart', 'uni2669', 'musicalnote', 'musicalnotedbl', 'uni266C', 'uni266D', 'uni266E', 'uni266F', 'uni26A0', 'uni2726', 'uni2727', 'uni2764', 'uni2765', 'uni2934', 'uni2935', 'uni29BF', 'uni29FA', 'uni29FB', 'uni3000', 'uni3001', 'uni3002', 'uni3003', 'uni3005', 'uni3006', 'uni3007', 'uni3008', 'uni3009', 'uni300A', 'uni300B', 'uni300C', 'uni300D', 'uni300E', 'uni300F', 'uni3010', 'uni3011', 'uni3012', 'uni3013', 'uni3014', 'uni3015', 'uni3016', 'uni3017', 'uni3018', 'uni3019', 'uni301C', 'uni301D', 'uni301E', 'uni301F', 'uni3033', 'uni3034', 'uni3035', 'uni303B', 'uni303C', 'uni303D', 'uni3041', 'uni3042', 'uni3043', 'uni3044', 'uni3045', 'uni3046', 'uni3047', 'uni3048', 'uni3049', 'uni304A', 'uni304B', 'uni304C', 'uni304D', 'uni304E', 'uni304F', 'uni3050', 'uni3051', 'uni3052', 'uni3053', 'uni3054', 'uni3055', 'uni3056', 'uni3057', 'uni3058', 'uni3059', 'uni305A', 'uni305B', 'uni305C', 'uni305D', 'uni305E', 'uni305F', 'uni3060', 'uni3061', 'uni3062', 'uni3063', 'uni3064', 'uni3065', 'uni3066', 'uni3067', 'uni3068', 'uni3069', 'uni306A', 'uni306B', 'uni306C', 'uni306D', 'uni306E', 'uni306F', 'uni3070', 'uni3071', 'uni3072', 'uni3073', 'uni3074', 'uni3075', 'uni3076', 'uni3077', 'uni3078', 'uni3079', 'uni307A', 'uni307B', 'uni307C', 'uni307D', 'uni307E', 'uni307F', 'uni3080', 'uni3081', 'uni3082', 'uni3083', 'uni3084', 'uni3085', 'uni3086', 'uni3087', 'uni3088', 'uni3089', 'uni308A', 'uni308B', 'uni308C', 'uni308D', 'uni308E', 'uni308F', 'uni3090', 'uni3091', 'uni3092', 'uni3093', 'uni3094', 'uni3095', 'uni3096', 'uni309B', 'uni309C', 'uni309D', 'uni309E', 'uni309F', 'uni30A0', 'uni30A1', 'uni30A2', 'uni30A3', 'uni30A4', 'uni30A5', 'uni30A6', 'uni30A7', 'uni30A8', 'uni30A9', 'uni30AA', 'uni30AB', 'uni30AC', 'uni30AD', 'uni30AE', 'uni30AF', 'uni30B0', 'uni30B1', 'uni30B2', 'uni30B3', 'uni30B4', 'uni30B5', 'uni30B6', 'uni30B7', 'uni30B8', 'uni30B9', 'uni30BA', 'uni30BB', 'uni30BC', 'uni30BD', 'uni30BE', 'uni30BF', 'uni30C0', 'uni30C1', 'uni30C2', 'uni30C3', 'uni30C4', 'uni30C5', 'uni30C6', 'uni30C7', 'uni30C8', 'uni30C9', 'uni30CA', 'uni30CB', 'uni30CC', 'uni30CD', 'uni30CE', 'uni30CF', 'uni30D0', 'uni30D1', 'uni30D2', 'uni30D3', 'uni30D4', 'uni30D5', 'uni30D6', 'uni30D7', 'uni30D8', 'uni30D9', 'uni30DA', 'uni30DB', 'uni30DC', 'uni30DD', 'uni30DE', 'uni30DF', 'uni30E0', 'uni30E1', 'uni30E2', 'uni30E3', 'uni30E4', 'uni30E5', 'uni30E6', 'uni30E7', 'uni30E8', 'uni30E9', 'uni30EA', 'uni30EB', 'uni30EC', 'uni30ED', 'uni30EE', 'uni30EF', 'uni30F0', 'uni30F1', 'uni30F2', 'uni30F3', 'uni30F4', 'uni30F5', 'uni30F6', 'uni30F7', 'uni30F8', 'uni30F9', 'uni30FA', 'uni30FB', 'uni30FC', 'uni30FD', 'uni30FE', 'uni30FF', 'uni31F0', 'uni31F1', 'uni31F2', 'uni31F3', 'uni31F4', 'uni31F5', 'uni31F6', 'uni31F7', 'uni31F8', 'uni31F9', 'uni31FA', 'uni31FB', 'uni31FC', 'uni31FD', 'uni31FE', 'uni31FF', 'uni33CB', 'uni4EDD', 'uniE133', 'uniE134', 'uniE139', 'uni0E0D.descless', 'uniF880', 'uni0E24_uni0E45', 'uni0E26_uni0E45', 'uniFB00', 'uniFB01', 'uniFB02', 'uniFB03', 'uniFB04', 'uniFE45', 'uniFE46', 'uniFF01', 'uniFF02', 'uniFF03', 'uniFF04', 'uniFF05', 'uniFF06', 'uniFF07', 'uniFF08', 'uniFF09', 'uniFF0A', 'uniFF0B', 'uniFF0C', 'uniFF0D', 'uniFF0E', 'uniFF0F', 'uniFF10', 'uniFF11', 'uniFF12', 'uniFF13', 'uniFF14', 'uniFF15', 'uniFF16', 'uniFF17', 'uniFF18', 'uniFF19', 'uniFF1A', 'uniFF1B', 'uniFF1C', 'uniFF1D', 'uniFF1E', 'uniFF1F', 'uniFF20', 'uniFF21', 'uniFF22', 'uniFF23', 'uniFF24', 'uniFF25', 'uniFF26', 'uniFF27', 'uniFF28', 'uniFF29', 'uniFF2A', 'uniFF2B', 'uniFF2C', 'uniFF2D', 'uniFF2E', 'uniFF2F', 'uniFF30', 'uniFF31', 'uniFF32', 'uniFF33', 'uniFF34', 'uniFF35', 'uniFF36', 'uniFF37', 'uniFF38', 'uniFF39', 'uniFF3A', 'uniFF3B', 'uniFF3C', 'uniFF3D', 'uniFF3E', 'uniFF3F', 'uniFF40', 'uniFF41', 'uniFF42', 'uniFF43', 'uniFF44', 'uniFF45', 'uniFF46', 'uniFF47', 'uniFF48', 'uniFF49', 'uniFF4A', 'uniFF4B', 'uniFF4C', 'uniFF4D', 'uniFF4E', 'uniFF4F', 'uniFF50', 'uniFF51', 'uniFF52', 'uniFF53', 'uniFF54', 'uniFF55', 'uniFF56', 'uniFF57', 'uniFF58', 'uniFF59', 'uniFF5A', 'uniFF5B', 'uniFF5C', 'uniFF5D', 'uniFF5E', 'uniFF5F', 'uniFF60', 'uniFFE0', 'uniFFE1', 'uniFFE2', 'uniFFE3', 'uniFFE4', 'uniFFE5', 'uniFFE6', 'uniFFE8', 'uniFFE9', 'uniFFEA', 'uniFFEB', 'uniFFEC', 'uniFFFC', 'u1F494', 'u1FBB0', 'u1FBB2', 'u1FBB3']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>







* 🔥 **FAIL** <p>dcaron uses component uni030C.</p>
 [code: wrong-mark]



* 🔥 **FAIL** <p>tcaron uses component uni030C.</p>
 [code: wrong-mark]



* ⚠️ **WARN** <p>Lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



* ⚠️ **WARN** <p>lcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Ensure the font supports case swapping for all its glyphs. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#case-mapping">case_mapping</a></summary>
    <div>







* 🔥 **FAIL** <p>The following glyphs lack their case-swapping counterparts:</p>
<table>
<thead>
<tr>
<th align="left">Glyph present in the font</th>
<th align="left">Missing case-swapping counterpart</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">U+0182: LATIN CAPITAL LETTER B WITH TOPBAR</td>
<td align="left">U+0183: LATIN SMALL LETTER B WITH TOPBAR</td>
</tr>
<tr>
<td align="left">U+026A: LATIN LETTER SMALL CAPITAL I</td>
<td align="left">U+A7AE: LATIN CAPITAL LETTER SMALL CAPITAL I</td>
</tr>
<tr>
<td align="left">U+028A: LATIN SMALL LETTER UPSILON</td>
<td align="left">U+01B1: LATIN CAPITAL LETTER UPSILON</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Shapes languages in all GF glyphsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyphsets-shape-languages">googlefonts/glyphsets/shape_languages</a></summary>
    <div>







* 🔥 **FAIL** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">FAIL messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҷ, ҳ</td>
<td align="left">tg_Cyrl (Tajik) and tg_Cyrl (Tajik)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҳ</td>
<td align="left">uz_Cyrl (Uzbek (Cyrillic)) and uz_Cyrl (Uzbek (Cyrillic))</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ɲ, ɲ</td>
<td align="left">bm_Latn (Bambara) and dyu_Latn (Dyula)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ƴ, ƴ</td>
<td align="left">ff_Latn (Fulah)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ƙ, ƴ, Ƴ, Ƙ</td>
<td align="left">ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҫ, ҙ, Ҡ, ҡ, ҫ, Ҙ</td>
<td align="left">ba_Cyrl (Bashkir)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҫ, ҫ</td>
<td align="left">cv_Cyrl (Chuvash)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҝ, ҹ</td>
<td align="left">az_Cyrl (Azerbaijani (Cyrillic))</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ӏ, ӏ</td>
<td align="left">kbd_Cyrl (Kabardian), av_Cyrl (Avaric) and lez_Cyrl (Lezghian)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: кӏ, хӏ, цӏ, гӏ, чӏ, рхӏ, пӏ, тӏ</td>
<td align="left">ce_Cyrl (Chechen)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ҥ, ҥ</td>
<td align="left">chm_Cyrl (Mari)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҳ, Ҳ</td>
<td align="left">kaa_Cyrl (Kara-Kalpak)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ҕ, ҥ</td>
<td align="left">sah_Cyrl (Sakha)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ӏ, Ӏ</td>
<td align="left">ady_Cyrl (Adyghe), dar_Cyrl (Dargwa) and inh_Cyrl (Ingush)</td>
</tr>
</tbody>
</table>
 [code: failed-language-shaping]



* ⚠️ **WARN** <p>GF_Phonetics_SinoExt glyphset:</p>
<table>
<thead>
<tr>
<th align="left">WARN messages</th>
<th align="left">Languages</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ǥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ǥ</td>
<td align="left">fi_Latn (Finnish)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ѫ</td>
<td align="left">bg_Cyrl (Bulgarian) and bg_Cyrl (Bulgarian)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἀ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἁ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἅ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἇ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὰ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ᾶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὲ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἠ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἡ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὴ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῆ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἰ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἴ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἲ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἱ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἵ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἳ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ἷ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὶ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὄ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὂ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὃ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὸ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὐ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὔ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὒ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὖ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὑ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὕ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὓ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὗ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὺ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὤ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὢ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὦ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὥ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὣ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὧ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ὼ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ῶ</td>
<td align="left">el_Grek (Greek)</td>
</tr>
<tr>
<td align="left">Auxiliary orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: ӊ</td>
<td align="left">mn_Cyrl (Mongolian)</td>
</tr>
</tbody>
</table>
 [code: warning-language-shaping]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Name table entries should not contain line-breaks. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-line-breaks">googlefonts/name/line_breaks</a></summary>
    <div>







* 🔥 **FAIL** <p>Name entry LICENSE_DESCRIPTION on platform WINDOWS contains a line-break.</p>
 [code: line-break]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check license file has good copyright string. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-license-OFL-copyright">googlefonts/license/OFL_copyright</a></summary>
    <div>







* 🔥 **FAIL** <p>First line in license file is:</p>
<p>&quot;copyright (c) 2026 the syy beneathpoem project authors (<a href="https://github.com/plaenithaan/syy-beneathpoem">https://github.com/plaenithaan/syy-beneathpoem</a>)&quot;</p>
<p>which does not match the expected format, similar to:</p>
<p>&quot;Copyright 2022 The Familyname Project Authors (git url)&quot;</p>
 [code: bad-format]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font follows the Google Fonts CJK vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-cjk-vertical-metrics">googlefonts/cjk_vertical_metrics</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2 fsSelection bit 7 must be disabled</p>
 [code: bad-fselection-bit7]



* 🔥 **FAIL** <p>OS/2.sTypoAscender is &quot;896&quot; it should be 901</p>
 [code: bad-OS/2.sTypoAscender]



* 🔥 **FAIL** <p>OS/2.sTypoDescender is &quot;-384&quot; it should be -123</p>
 [code: bad-OS/2.sTypoDescender]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0334 (U+0334), uni0335 (U+0335), uni0336 (U+0336), uni0337 (U+0337), uni0338 (U+0338), uni0358 (U+0358), uni3099 (U+3099) and uni309A (U+309A)</p>
 [code: mark-chars]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does the font contain chws and vchw features? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#cjk-chws-feature">cjk_chws_feature</a></summary>
    <div>







* ⚠️ **WARN** <p>chws feature not found in font. Use chws_tool (<a href="https://github.com/googlefonts/chws_tool">https://github.com/googlefonts/chws_tool</a>) to add it.</p>
 [code: missing-chws-feature]



* ⚠️ **WARN** <p>vchw feature not found in font. Use chws_tool (<a href="https://github.com/googlefonts/chws_tool">https://github.com/googlefonts/chws_tool</a>) to add it.</p>
 [code: missing-vchw-feature]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check if each glyph has the recommended amount of contours. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#contour-count">contour_count</a></summary>
    <div>







* ⚠️ **WARN** <p>This check inspects the glyph outlines and detects the total number of contours in each of them. The expected values are infered from the typical ammounts of contours observed in a large collection of reference font families. The divergences listed below may simply indicate a significantly different design on some of your glyphs. On the other hand, some of these may flag actual bugs in the font such as glyphs mapped to an incorrect codepoint. Please consider reviewing the design and codepoint assignment of these to make sure they are correct.</p>
<p>The following glyphs do not have the recommended number of contours:</p>
<pre><code>- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: germandbls	Contours detected: 3	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: ldot	Contours detected: 1	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: uni0194	Contours detected: 1	Expected: 2

- Glyph name: uni01EA	Contours detected: 3	Expected: 2

- Glyph name: uni01EB	Contours detected: 3	Expected: 2

- Glyph name: uni0228	Contours detected: 2	Expected: 1

- Glyph name: uni0229	Contours detected: 3	Expected: 2

- Glyph name: Omegatonos	Contours detected: 3	Expected: 2

- Glyph name: uni03A9	Contours detected: 2	Expected: 1

- Glyph name: beta	Contours detected: 3	Expected: 2

- Glyph name: uni042B	Contours detected: 2	Expected: 3

- Glyph name: uni044B	Contours detected: 2	Expected: 3

- Glyph name: uni04F8	Contours detected: 4	Expected: 5

- Glyph name: uni04F9	Contours detected: 4	Expected: 5

- Glyph name: uni0E0D	Contours detected: 2	Expected: 1 or 4

- Glyph name: uni0E10	Contours detected: 2	Expected: 1 or 5

- Glyph name: uni0E12	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E2C	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E4F	Contours detected: 3	Expected: 4

- Glyph name: uni0E53	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E55	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: trademark	Contours detected: 1	Expected: 2

- Glyph name: uni21E5	Contours detected: 1	Expected: 2

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 9	Expected: 1

- Glyph name: uni2572	Contours detected: 9	Expected: 1

- Glyph name: uni2573	Contours detected: 17	Expected: 1

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uniFFFC	Contours detected: 18	Expected: 22

- Glyph name: Omegatonos	Contours detected: 3	Expected: 2

- Glyph name: Uogonek	Contours detected: 2	Expected: 1

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: beta	Contours detected: 3	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: germandbls	Contours detected: 3	Expected: 1

- Glyph name: ldot	Contours detected: 1	Expected: 2

- Glyph name: percent	Contours detected: 3	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 4	Expected: 6 or 7

- Glyph name: trademark	Contours detected: 1	Expected: 2

- Glyph name: uni0194	Contours detected: 1	Expected: 2

- Glyph name: uni0228	Contours detected: 2	Expected: 1

- Glyph name: uni0229	Contours detected: 3	Expected: 2

- Glyph name: uni03A9	Contours detected: 2	Expected: 1

- Glyph name: uni042B	Contours detected: 2	Expected: 3

- Glyph name: uni044B	Contours detected: 2	Expected: 3

- Glyph name: uni04F8	Contours detected: 4	Expected: 5

- Glyph name: uni04F9	Contours detected: 4	Expected: 5

- Glyph name: uni0E0D	Contours detected: 2	Expected: 1 or 4

- Glyph name: uni0E10	Contours detected: 2	Expected: 1 or 5

- Glyph name: uni0E12	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E2C	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E4F	Contours detected: 3	Expected: 4

- Glyph name: uni0E53	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni0E55	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni1E9E	Contours detected: 2	Expected: 1

- Glyph name: uni21E5	Contours detected: 1	Expected: 2

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 9	Expected: 1

- Glyph name: uni2572	Contours detected: 9	Expected: 1

- Glyph name: uni2573	Contours detected: 17	Expected: 1

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uniFFFC	Contours detected: 18	Expected: 22

- Glyph name: uogonek	Contours detected: 2	Expected: 1
</code></pre>
 [code: contour-count]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Does GPOS table have kerning information? This check skips monospaced fonts as defined by post.isFixedPitch value <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#gpos-kerning-info">gpos_kerning_info</a></summary>
    <div>







* ⚠️ **WARN** <p>GPOS table lacks kerning information.</p>
 [code: lacks-kern-info]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check math signs have the same width. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#math-signs-width">math_signs_width</a></summary>
    <div>







* ⚠️ **WARN** <p>The most common width is 1088 among a set of 33 math glyphs.
The following math glyphs have a different width, though:</p>
<p>Width = 576:
logicalnot, notequal, less, greaterequal, plus, greater, lessequal, equal</p>
 [code: width-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni013C (U+013C): L&lt;&lt;320.0,-128.0&gt;--&lt;192.0,-128.0&gt;&gt; has the same coordinates as a previous segment.

* uni0162 (U+0162): L&lt;&lt;320.0,-128.0&gt;--&lt;192.0,-128.0&gt;&gt; has the same coordinates as a previous segment.

* uni01CD (U+01CD): L&lt;&lt;192.0,640.0&gt;--&lt;320.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni01CF (U+01CF): L&lt;&lt;192.0,640.0&gt;--&lt;320.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni021A (U+021A): L&lt;&lt;320.0,-128.0&gt;--&lt;192.0,-128.0&gt;&gt; has the same coordinates as a previous segment.

* Etatonos (U+0389): L&lt;&lt;0.0,640.0&gt;--&lt;128.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* Omicrontonos (U+038C): L&lt;&lt;128.0,576.0&gt;--&lt;128.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* Upsilontonos (U+038E): L&lt;&lt;0.0,640.0&gt;--&lt;128.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* Omegatonos (U+038F): L&lt;&lt;128.0,576.0&gt;--&lt;128.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EC1 (U+1EC1): L&lt;&lt;384.0,640.0&gt;--&lt;256.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED0 (U+1ED0): L&lt;&lt;320.0,832.0&gt;--&lt;192.0,832.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EEA (U+1EEA): L&lt;&lt;256.0,640.0&gt;--&lt;384.0,640.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- NULL

- nonmarkingreturn
</code></pre>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>







* ⚠️ **WARN** <p>Family metadata at fonts/ttf does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>







* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: tifinagh, coptic, cherokee, math</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: elbasan, glagolitic, coptic, gothic, math</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: hebrew, old-permic, canadian-aboriginal, tifinagh, coptic, malayalam, tai-le, todhri, math, duployan, syriac</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: osage, cherokee</li>
<li>U+030C COMBINING CARON: try adding one of: tai-le, cherokee</li>
<li>U+030D COMBINING VERTICAL LINE ABOVE: try adding sunuwar</li>
<li>U+030E COMBINING DOUBLE VERTICAL LINE ABOVE: try adding ethiopic</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition</li>
<li>U+0311 COMBINING INVERTED BREVE: try adding one of: todhri, coptic</li>
<li>U+0312 COMBINING TURNED COMMA ABOVE: try adding math</li>
<li>U+0313 COMBINING COMMA ABOVE: try adding one of: old-permic, todhri</li>
<li>U+0314 COMBINING REVERSED COMMA ABOVE: not included in any glyphset definition</li>
<li>U+0315 COMBINING COMMA ABOVE RIGHT: try adding math</li>
<li>U+031A COMBINING LEFT ANGLE ABOVE: try adding math</li>
<li>U+031B COMBINING HORN: not included in any glyphset definition</li>
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, cherokee, duployan</li>
<li>U+0325 COMBINING RING BELOW: try adding syriac</li>
<li>U+0326 COMBINING COMMA BELOW: try adding math</li>
<li>U+0327 COMBINING CEDILLA: try adding math</li>
<li>U+0328 COMBINING OGONEK: not included in any glyphset definition</li>
<li>U+032A COMBINING BRIDGE BELOW: not included in any glyphset definition</li>
<li>U+032B COMBINING INVERTED DOUBLE ARCH BELOW: not included in any glyphset definition</li>
<li>U+032C COMBINING CARON BELOW: try adding math</li>
<li>U+032D COMBINING CIRCUMFLEX ACCENT BELOW: try adding one of: syriac, sunuwar</li>
<li>U+032E COMBINING BREVE BELOW: try adding syriac</li>
<li>U+032F COMBINING INVERTED BREVE BELOW: try adding math</li>
<li>U+0330 COMBINING TILDE BELOW: try adding one of: syriac, cherokee, math</li>
<li>U+0332 COMBINING LOW LINE: try adding math</li>
<li>U+0334 COMBINING TILDE OVERLAY: not included in any glyphset definition</li>
<li>U+0335 COMBINING SHORT STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0336 COMBINING LONG STROKE OVERLAY: not included in any glyphset definition</li>
<li>U+0337 COMBINING SHORT SOLIDUS OVERLAY: not included in any glyphset definition</li>
<li>U+0338 COMBINING LONG SOLIDUS OVERLAY: try adding math</li>
<li>U+0358 COMBINING DOT ABOVE RIGHT: try adding osage</li>
<li>U+0E83 : not included in any glyphset definition</li>
<li>U+0E85 : not included in any glyphset definition</li>
<li>U+0EA4 : not included in any glyphset definition</li>
<li>U+0EA6 : not included in any glyphset definition</li>
<li>U+2003 EM SPACE: try adding nushu</li>
<li>U+2010 HYPHEN: try adding one of: hebrew, kayah-li, syloti-nagri, sundanese, coptic, kaithi, sora-sompeng, kharoshthi, lisu, arabic, armenian, cham, yi</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+2016 DOUBLE VERTICAL LINE: try adding math</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2025 TWO DOT LEADER: try adding phags-pa</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
<li>U+2034 TRIPLE PRIME: try adding math</li>
<li>U+203B REFERENCE MARK: not included in any glyphset definition</li>
<li>U+203E OVERLINE: not included in any glyphset definition</li>
<li>U+2070 SUPERSCRIPT ZERO: try adding math</li>
<li>U+2071 SUPERSCRIPT LATIN SMALL LETTER I: try adding math</li>
<li>U+2074 SUPERSCRIPT FOUR: try adding math</li>
<li>U+2075 SUPERSCRIPT FIVE: try adding math</li>
<li>U+2076 SUPERSCRIPT SIX: try adding math</li>
<li>U+2077 SUPERSCRIPT SEVEN: try adding math</li>
<li>U+2078 SUPERSCRIPT EIGHT: try adding math</li>
<li>U+2079 SUPERSCRIPT NINE: try adding math</li>
<li>U+207A SUPERSCRIPT PLUS SIGN: try adding math</li>
<li>U+207B SUPERSCRIPT MINUS: try adding math</li>
<li>U+207C SUPERSCRIPT EQUALS SIGN: try adding math</li>
<li>U+207D SUPERSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+207E SUPERSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+207F SUPERSCRIPT LATIN SMALL LETTER N: try adding math</li>
<li>U+2080 SUBSCRIPT ZERO: try adding math</li>
<li>U+2081 SUBSCRIPT ONE: try adding math</li>
<li>U+2082 SUBSCRIPT TWO: try adding math</li>
<li>U+2083 SUBSCRIPT THREE: try adding math</li>
<li>U+2084 SUBSCRIPT FOUR: try adding math</li>
<li>U+2085 SUBSCRIPT FIVE: try adding math</li>
<li>U+2086 SUBSCRIPT SIX: try adding math</li>
<li>U+2087 SUBSCRIPT SEVEN: try adding math</li>
<li>U+2088 SUBSCRIPT EIGHT: try adding math</li>
<li>U+2089 SUBSCRIPT NINE: try adding math</li>
<li>U+208A SUBSCRIPT PLUS SIGN: try adding math</li>
<li>U+208B SUBSCRIPT MINUS: try adding math</li>
<li>U+208C SUBSCRIPT EQUALS SIGN: try adding math</li>
<li>U+208D SUBSCRIPT LEFT PARENTHESIS: try adding math</li>
<li>U+208E SUBSCRIPT RIGHT PARENTHESIS: try adding math</li>
<li>U+2103 DEGREE CELSIUS: try adding math</li>
<li>U+210F PLANCK CONSTANT OVER TWO PI: try adding math</li>
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2127 INVERTED OHM SIGN: try adding math</li>
<li>U+212B ANGSTROM SIGN: try adding math</li>
<li>U+2135 ALEF SYMBOL: try adding math</li>
<li>U+2190 LEFTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2192 RIGHTWARDS ARROW: try adding one of: symbols, math</li>
<li>U+2194 LEFT RIGHT ARROW: try adding one of: symbols, math</li>
<li>U+2195 UP DOWN ARROW: try adding one of: symbols, math</li>
<li>U+2196 NORTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+2197 NORTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2198 SOUTH EAST ARROW: try adding one of: symbols, math</li>
<li>U+2199 SOUTH WEST ARROW: try adding one of: symbols, math</li>
<li>U+21A9 LEFTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21AA RIGHTWARDS ARROW WITH HOOK: try adding math</li>
<li>U+21B5 DOWNWARDS ARROW WITH CORNER LEFTWARDS: try adding math</li>
<li>U+21C4 RIGHTWARDS ARROW OVER LEFTWARDS ARROW: try adding math</li>
<li>U+21D0 LEFTWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D1 UPWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D2 RIGHTWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D3 DOWNWARDS DOUBLE ARROW: try adding math</li>
<li>U+21D4 LEFT RIGHT DOUBLE ARROW: try adding math</li>
<li>U+21D5 UP DOWN DOUBLE ARROW: try adding math</li>
<li>U+21D6 NORTH WEST DOUBLE ARROW: try adding math</li>
<li>U+21D7 NORTH EAST DOUBLE ARROW: try adding math</li>
<li>U+21D8 SOUTH EAST DOUBLE ARROW: try adding math</li>
<li>U+21D9 SOUTH WEST DOUBLE ARROW: try adding math</li>
<li>U+21E5 RIGHTWARDS ARROW TO BAR: try adding math</li>
<li>U+21E6 LEFTWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E7 UPWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E8 RIGHTWARDS WHITE ARROW: try adding symbols</li>
<li>U+21E9 DOWNWARDS WHITE ARROW: try adding symbols</li>
<li>U+21EA UPWARDS WHITE ARROW FROM BAR: try adding symbols</li>
<li>U+21EB UPWARDS WHITE ARROW ON PEDESTAL: try adding symbols</li>
<li>U+21EC UPWARDS WHITE ARROW ON PEDESTAL WITH HORIZONTAL BAR: try adding symbols</li>
<li>U+21ED UPWARDS WHITE ARROW ON PEDESTAL WITH VERTICAL BAR: try adding symbols</li>
<li>U+21EE UPWARDS WHITE DOUBLE ARROW: try adding symbols</li>
<li>U+21EF UPWARDS WHITE DOUBLE ARROW ON PEDESTAL: try adding symbols</li>
<li>U+21F0 RIGHTWARDS WHITE ARROW FROM WALL: try adding symbols</li>
<li>U+21F1 NORTH WEST ARROW TO CORNER: try adding math</li>
<li>U+21F2 SOUTH EAST ARROW TO CORNER: try adding math</li>
<li>U+21F3 UP DOWN WHITE ARROW: try adding symbols</li>
<li>U+2200 FOR ALL: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2203 THERE EXISTS: try adding math</li>
<li>U+2205 EMPTY SET: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+2207 NABLA: try adding math</li>
<li>U+2208 ELEMENT OF: try adding math</li>
<li>U+2209 NOT AN ELEMENT OF: try adding math</li>
<li>U+220B CONTAINS AS MEMBER: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2213 MINUS-OR-PLUS SIGN: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: symbols, tai-tham, yi, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221D PROPORTIONAL TO: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+2220 ANGLE: try adding math</li>
<li>U+2225 PARALLEL TO: try adding math</li>
<li>U+2226 NOT PARALLEL TO: try adding math</li>
<li>U+2227 LOGICAL AND: try adding math</li>
<li>U+2228 LOGICAL OR: try adding math</li>
<li>U+2229 INTERSECTION: try adding math</li>
<li>U+222A UNION: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+222C DOUBLE INTEGRAL: try adding math</li>
<li>U+2234 THEREFORE: try adding math</li>
<li>U+2235 BECAUSE: try adding math</li>
<li>U+223D REVERSED TILDE: try adding math</li>
<li>U+2243 ASYMPTOTICALLY EQUAL TO: try adding math</li>
<li>U+2245 APPROXIMATELY EQUAL TO: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2252 APPROXIMATELY EQUAL TO OR THE IMAGE OF: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2261 IDENTICAL TO: try adding math</li>
<li>U+2262 NOT IDENTICAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+2266 LESS-THAN OVER EQUAL TO: try adding math</li>
<li>U+2267 GREATER-THAN OVER EQUAL TO: try adding math</li>
<li>U+226A MUCH LESS-THAN: try adding math</li>
<li>U+226B MUCH GREATER-THAN: try adding math</li>
<li>U+2276 LESS-THAN OR GREATER-THAN: try adding math</li>
<li>U+2277 GREATER-THAN OR LESS-THAN: try adding math</li>
<li>U+2282 SUBSET OF: try adding math</li>
<li>U+2283 SUPERSET OF: try adding math</li>
<li>U+2284 NOT A SUBSET OF: try adding math</li>
<li>U+2285 NOT A SUPERSET OF: try adding math</li>
<li>U+2286 SUBSET OF OR EQUAL TO: try adding math</li>
<li>U+2287 SUPERSET OF OR EQUAL TO: try adding math</li>
<li>U+228A SUBSET OF WITH NOT EQUAL TO: try adding math</li>
<li>U+228B SUPERSET OF WITH NOT EQUAL TO: try adding math</li>
<li>U+2295 CIRCLED PLUS: try adding math</li>
<li>U+2296 CIRCLED MINUS: try adding math</li>
<li>U+2297 CIRCLED TIMES: try adding math</li>
<li>U+22A5 UP TACK: try adding math</li>
<li>U+2305 PROJECTIVE: try adding symbols</li>
<li>U+2306 PERSPECTIVE: try adding symbols</li>
<li>U+2312 ARC: try adding symbols</li>
<li>U+2318 PLACE OF INTEREST SIGN: try adding symbols</li>
<li>U+2325 OPTION KEY: try adding symbols</li>
<li>U+232B ERASE TO THE LEFT: try adding symbols</li>
<li>U+2387 ALTERNATIVE KEY SYMBOL: try adding symbols</li>
<li>U+23CE RETURN SYMBOL: try adding symbols</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25B2 BLACK UP-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B3 WHITE UP-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25B6 BLACK RIGHT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25B7 WHITE RIGHT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25BC BLACK DOWN-POINTING TRIANGLE: try adding symbols</li>
<li>U+25BD WHITE DOWN-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C0 BLACK LEFT-POINTING TRIANGLE: try adding symbols</li>
<li>U+25C1 WHITE LEFT-POINTING TRIANGLE: try adding one of: symbols, math</li>
<li>U+25C6 BLACK DIAMOND: try adding symbols</li>
<li>U+25C7 WHITE DIAMOND: try adding symbols</li>
<li>U+25C9 FISHEYE: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25CE BULLSEYE: try adding symbols</li>
<li>U+25CF BLACK CIRCLE: try adding symbols</li>
<li>U+25E1 LOWER HALF CIRCLE: try adding symbols</li>
<li>U+25E6 WHITE BULLET: try adding symbols</li>
<li>U+25EF LARGE CIRCLE: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2640 FEMALE SIGN: try adding symbols</li>
<li>U+2642 MALE SIGN: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2669 QUARTER NOTE: try adding one of: music, symbols</li>
<li>U+266A EIGHTH NOTE: try adding one of: music, symbols</li>
<li>U+266B BEAMED EIGHTH NOTES: try adding one of: music, symbols</li>
<li>U+266C BEAMED SIXTEENTH NOTES: try adding one of: music, symbols</li>
<li>U+266D MUSIC FLAT SIGN: try adding one of: music, symbols, math</li>
<li>U+266E MUSIC NATURAL SIGN: try adding one of: music, symbols, math</li>
<li>U+266F MUSIC SHARP SIGN: try adding one of: music, symbols, math</li>
<li>U+26A0 WARNING SIGN: try adding symbols</li>
<li>U+2726 BLACK FOUR POINTED STAR: try adding symbols</li>
<li>U+2727 WHITE FOUR POINTED STAR: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2765 ROTATED HEAVY BLACK HEART BULLET: try adding symbols</li>
<li>U+2919 LEFTWARDS ARROW-TAIL: try adding math</li>
<li>U+2934 ARROW POINTING RIGHTWARDS THEN CURVING UPWARDS: try adding math</li>
<li>U+2935 ARROW POINTING RIGHTWARDS THEN CURVING DOWNWARDS: try adding math</li>
<li>U+29BF CIRCLED BULLET: try adding one of: symbols, math</li>
<li>U+29FA DOUBLE PLUS: try adding math</li>
<li>U+29FB TRIPLE PLUS: try adding math</li>
<li>U+3000 IDEOGRAPHIC SPACE: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, nushu, yi</li>
<li>U+3001 IDEOGRAPHIC COMMA: try adding one of: japanese, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3002 IDEOGRAPHIC FULL STOP: try adding one of: japanese, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, nushu, yi</li>
<li>U+3003 DITTO MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3005 IDEOGRAPHIC ITERATION MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3006 IDEOGRAPHIC CLOSING MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+3007 IDEOGRAPHIC NUMBER ZERO: try adding one of: phags-pa, chinese-simplified, japanese</li>
<li>U+3008 LEFT ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3009 RIGHT ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300A LEFT DOUBLE ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, lisu, phags-pa, yi</li>
<li>U+300B RIGHT DOUBLE ANGLE BRACKET: try adding one of: japanese, tibetan, mongolian, chinese-traditional, tai-le, chinese-simplified, chinese-hongkong, lisu, phags-pa, yi</li>
<li>U+300C LEFT CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300D RIGHT CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300E LEFT WHITE CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+300F RIGHT WHITE CORNER BRACKET: try adding one of: japanese, mongolian, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3010 LEFT BLACK LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3011 RIGHT BLACK LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3012 POSTAL MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3013 GETA MARK: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3014 LEFT TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3015 RIGHT TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3016 LEFT WHITE LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3017 RIGHT WHITE LENTICULAR BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3018 LEFT WHITE TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+3019 RIGHT WHITE TORTOISE SHELL BRACKET: try adding one of: japanese, chinese-traditional, chinese-simplified, chinese-hongkong, phags-pa, yi</li>
<li>U+301C WAVE DASH: try adding japanese</li>
<li>U+301D REVERSED DOUBLE PRIME QUOTATION MARK: try adding one of: chinese-traditional, chinese-simplified, chinese-hongkong</li>
<li>U+301E DOUBLE PRIME QUOTATION MARK: try adding one of: chinese-traditional, chinese-simplified, chinese-hongkong</li>
<li>U+301F LOW DOUBLE PRIME QUOTATION MARK: not included in any glyphset definition</li>
<li>U+3033 VERTICAL KANA REPEAT MARK UPPER HALF: not included in any glyphset definition</li>
<li>U+3034 VERTICAL KANA REPEAT WITH VOICED SOUND MARK UPPER HALF: not included in any glyphset definition</li>
<li>U+3035 VERTICAL KANA REPEAT MARK LOWER HALF: not included in any glyphset definition</li>
<li>U+303B VERTICAL IDEOGRAPHIC ITERATION MARK: not included in any glyphset definition</li>
<li>U+303C MASU MARK: not included in any glyphset definition</li>
<li>U+303D PART ALTERNATION MARK: not included in any glyphset definition</li>
<li>U+3041 HIRAGANA LETTER SMALL A: try adding one of: chinese-simplified, japanese</li>
<li>U+3042 HIRAGANA LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+3043 HIRAGANA LETTER SMALL I: try adding one of: chinese-simplified, japanese</li>
<li>U+3044 HIRAGANA LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+3045 HIRAGANA LETTER SMALL U: try adding one of: chinese-simplified, japanese</li>
<li>U+3046 HIRAGANA LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+3047 HIRAGANA LETTER SMALL E: try adding one of: chinese-simplified, japanese</li>
<li>U+3048 HIRAGANA LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+3049 HIRAGANA LETTER SMALL O: try adding one of: chinese-simplified, japanese</li>
<li>U+304A HIRAGANA LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+304B HIRAGANA LETTER KA: try adding one of: chinese-simplified, japanese</li>
<li>U+304C HIRAGANA LETTER GA: try adding one of: chinese-simplified, japanese</li>
<li>U+304D HIRAGANA LETTER KI: try adding one of: chinese-simplified, japanese</li>
<li>U+304E HIRAGANA LETTER GI: try adding one of: chinese-simplified, japanese</li>
<li>U+304F HIRAGANA LETTER KU: try adding one of: chinese-simplified, japanese</li>
<li>U+3050 HIRAGANA LETTER GU: try adding one of: chinese-simplified, japanese</li>
<li>U+3051 HIRAGANA LETTER KE: try adding one of: chinese-simplified, japanese</li>
<li>U+3052 HIRAGANA LETTER GE: try adding one of: chinese-simplified, japanese</li>
<li>U+3053 HIRAGANA LETTER KO: try adding one of: chinese-simplified, japanese</li>
<li>U+3054 HIRAGANA LETTER GO: try adding one of: chinese-simplified, japanese</li>
<li>U+3055 HIRAGANA LETTER SA: try adding one of: chinese-simplified, japanese</li>
<li>U+3056 HIRAGANA LETTER ZA: try adding one of: chinese-simplified, japanese</li>
<li>U+3057 HIRAGANA LETTER SI: try adding one of: chinese-simplified, japanese</li>
<li>U+3058 HIRAGANA LETTER ZI: try adding one of: chinese-simplified, japanese</li>
<li>U+3059 HIRAGANA LETTER SU: try adding one of: chinese-simplified, japanese</li>
<li>U+305A HIRAGANA LETTER ZU: try adding one of: chinese-simplified, japanese</li>
<li>U+305B HIRAGANA LETTER SE: try adding one of: chinese-simplified, japanese</li>
<li>U+305C HIRAGANA LETTER ZE: try adding one of: chinese-simplified, japanese</li>
<li>U+305D HIRAGANA LETTER SO: try adding one of: chinese-simplified, japanese</li>
<li>U+305E HIRAGANA LETTER ZO: try adding one of: chinese-simplified, japanese</li>
<li>U+305F HIRAGANA LETTER TA: try adding one of: chinese-simplified, japanese</li>
<li>U+3060 HIRAGANA LETTER DA: try adding one of: chinese-simplified, japanese</li>
<li>U+3061 HIRAGANA LETTER TI: try adding one of: chinese-simplified, japanese</li>
<li>U+3062 HIRAGANA LETTER DI: try adding one of: chinese-simplified, japanese</li>
<li>U+3063 HIRAGANA LETTER SMALL TU: try adding one of: chinese-simplified, japanese</li>
<li>U+3064 HIRAGANA LETTER TU: try adding one of: chinese-simplified, japanese</li>
<li>U+3065 HIRAGANA LETTER DU: try adding one of: chinese-simplified, japanese</li>
<li>U+3066 HIRAGANA LETTER TE: try adding one of: chinese-simplified, japanese</li>
<li>U+3067 HIRAGANA LETTER DE: try adding one of: chinese-simplified, japanese</li>
<li>U+3068 HIRAGANA LETTER TO: try adding one of: chinese-simplified, japanese</li>
<li>U+3069 HIRAGANA LETTER DO: try adding one of: chinese-simplified, japanese</li>
<li>U+306A HIRAGANA LETTER NA: try adding one of: chinese-simplified, japanese</li>
<li>U+306B HIRAGANA LETTER NI: try adding one of: chinese-simplified, japanese</li>
<li>U+306C HIRAGANA LETTER NU: try adding one of: chinese-simplified, japanese</li>
<li>U+306D HIRAGANA LETTER NE: try adding one of: chinese-simplified, japanese</li>
<li>U+306E HIRAGANA LETTER NO: try adding one of: chinese-simplified, japanese</li>
<li>U+306F HIRAGANA LETTER HA: try adding one of: chinese-simplified, japanese</li>
<li>U+3070 HIRAGANA LETTER BA: try adding one of: chinese-simplified, japanese</li>
<li>U+3071 HIRAGANA LETTER PA: try adding one of: chinese-simplified, japanese</li>
<li>U+3072 HIRAGANA LETTER HI: try adding one of: chinese-simplified, japanese</li>
<li>U+3073 HIRAGANA LETTER BI: try adding one of: chinese-simplified, japanese</li>
<li>U+3074 HIRAGANA LETTER PI: try adding one of: chinese-simplified, japanese</li>
<li>U+3075 HIRAGANA LETTER HU: try adding one of: chinese-simplified, japanese</li>
<li>U+3076 HIRAGANA LETTER BU: try adding one of: chinese-simplified, japanese</li>
<li>U+3077 HIRAGANA LETTER PU: try adding one of: chinese-simplified, japanese</li>
<li>U+3078 HIRAGANA LETTER HE: try adding one of: chinese-simplified, japanese</li>
<li>U+3079 HIRAGANA LETTER BE: try adding one of: chinese-simplified, japanese</li>
<li>U+307A HIRAGANA LETTER PE: try adding one of: chinese-simplified, japanese</li>
<li>U+307B HIRAGANA LETTER HO: try adding one of: chinese-simplified, japanese</li>
<li>U+307C HIRAGANA LETTER BO: try adding one of: chinese-simplified, japanese</li>
<li>U+307D HIRAGANA LETTER PO: try adding one of: chinese-simplified, japanese</li>
<li>U+307E HIRAGANA LETTER MA: try adding one of: chinese-simplified, japanese</li>
<li>U+307F HIRAGANA LETTER MI: try adding one of: chinese-simplified, japanese</li>
<li>U+3080 HIRAGANA LETTER MU: try adding one of: chinese-simplified, japanese</li>
<li>U+3081 HIRAGANA LETTER ME: try adding one of: chinese-simplified, japanese</li>
<li>U+3082 HIRAGANA LETTER MO: try adding one of: chinese-simplified, japanese</li>
<li>U+3083 HIRAGANA LETTER SMALL YA: try adding one of: chinese-simplified, japanese</li>
<li>U+3084 HIRAGANA LETTER YA: try adding one of: chinese-simplified, japanese</li>
<li>U+3085 HIRAGANA LETTER SMALL YU: try adding one of: chinese-simplified, japanese</li>
<li>U+3086 HIRAGANA LETTER YU: try adding one of: chinese-simplified, japanese</li>
<li>U+3087 HIRAGANA LETTER SMALL YO: try adding one of: chinese-simplified, japanese</li>
<li>U+3088 HIRAGANA LETTER YO: try adding one of: chinese-simplified, japanese</li>
<li>U+3089 HIRAGANA LETTER RA: try adding one of: chinese-simplified, japanese</li>
<li>U+308A HIRAGANA LETTER RI: try adding one of: chinese-simplified, japanese</li>
<li>U+308B HIRAGANA LETTER RU: try adding one of: chinese-simplified, japanese</li>
<li>U+308C HIRAGANA LETTER RE: try adding one of: chinese-simplified, japanese</li>
<li>U+308D HIRAGANA LETTER RO: try adding one of: chinese-simplified, japanese</li>
<li>U+308E HIRAGANA LETTER SMALL WA: try adding one of: chinese-simplified, japanese</li>
<li>U+308F HIRAGANA LETTER WA: try adding one of: chinese-simplified, japanese</li>
<li>U+3090 HIRAGANA LETTER WI: try adding one of: chinese-simplified, japanese</li>
<li>U+3091 HIRAGANA LETTER WE: try adding one of: chinese-simplified, japanese</li>
<li>U+3092 HIRAGANA LETTER WO: try adding one of: chinese-simplified, japanese</li>
<li>U+3093 HIRAGANA LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+3094 HIRAGANA LETTER VU: try adding one of: chinese-simplified, japanese</li>
<li>U+3095 HIRAGANA LETTER SMALL KA: try adding one of: chinese-simplified, japanese</li>
<li>U+3096 HIRAGANA LETTER SMALL KE: try adding one of: chinese-simplified, japanese</li>
<li>U+3099 COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309A COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309B KATAKANA-HIRAGANA VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309C KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK: try adding one of: kana-extended, chinese-simplified, japanese</li>
<li>U+309D HIRAGANA ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+309E HIRAGANA VOICED ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+309F HIRAGANA DIGRAPH YORI: try adding one of: chinese-simplified, japanese</li>
<li>U+30A0 KATAKANA-HIRAGANA DOUBLE HYPHEN: try adding one of: chinese-simplified, japanese</li>
<li>U+30A1 KATAKANA LETTER SMALL A: try adding one of: chinese-simplified, japanese</li>
<li>U+30A2 KATAKANA LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+30A3 KATAKANA LETTER SMALL I: try adding one of: chinese-simplified, japanese</li>
<li>U+30A4 KATAKANA LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+30A5 KATAKANA LETTER SMALL U: try adding one of: chinese-simplified, japanese</li>
<li>U+30A6 KATAKANA LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+30A7 KATAKANA LETTER SMALL E: try adding one of: chinese-simplified, japanese</li>
<li>U+30A8 KATAKANA LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+30A9 KATAKANA LETTER SMALL O: try adding one of: chinese-simplified, japanese</li>
<li>U+30AA KATAKANA LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+30AB KATAKANA LETTER KA: try adding one of: chinese-simplified, japanese</li>
<li>U+30AC KATAKANA LETTER GA: try adding one of: chinese-simplified, japanese</li>
<li>U+30AD KATAKANA LETTER KI: try adding one of: chinese-simplified, japanese</li>
<li>U+30AE KATAKANA LETTER GI: try adding one of: chinese-simplified, japanese</li>
<li>U+30AF KATAKANA LETTER KU: try adding one of: chinese-simplified, japanese</li>
<li>U+30B0 KATAKANA LETTER GU: try adding one of: chinese-simplified, japanese</li>
<li>U+30B1 KATAKANA LETTER KE: try adding one of: chinese-simplified, japanese</li>
<li>U+30B2 KATAKANA LETTER GE: try adding one of: chinese-simplified, japanese</li>
<li>U+30B3 KATAKANA LETTER KO: try adding one of: chinese-simplified, japanese</li>
<li>U+30B4 KATAKANA LETTER GO: try adding one of: chinese-simplified, japanese</li>
<li>U+30B5 KATAKANA LETTER SA: try adding one of: chinese-simplified, japanese</li>
<li>U+30B6 KATAKANA LETTER ZA: try adding one of: chinese-simplified, japanese</li>
<li>U+30B7 KATAKANA LETTER SI: try adding one of: chinese-simplified, japanese</li>
<li>U+30B8 KATAKANA LETTER ZI: try adding one of: chinese-simplified, japanese</li>
<li>U+30B9 KATAKANA LETTER SU: try adding one of: chinese-simplified, japanese</li>
<li>U+30BA KATAKANA LETTER ZU: try adding one of: chinese-simplified, japanese</li>
<li>U+30BB KATAKANA LETTER SE: try adding one of: chinese-simplified, japanese</li>
<li>U+30BC KATAKANA LETTER ZE: try adding one of: chinese-simplified, japanese</li>
<li>U+30BD KATAKANA LETTER SO: try adding one of: chinese-simplified, japanese</li>
<li>U+30BE KATAKANA LETTER ZO: try adding one of: chinese-simplified, japanese</li>
<li>U+30BF KATAKANA LETTER TA: try adding one of: chinese-simplified, japanese</li>
<li>U+30C0 KATAKANA LETTER DA: try adding one of: chinese-simplified, japanese</li>
<li>U+30C1 KATAKANA LETTER TI: try adding one of: chinese-simplified, japanese</li>
<li>U+30C2 KATAKANA LETTER DI: try adding one of: chinese-simplified, japanese</li>
<li>U+30C3 KATAKANA LETTER SMALL TU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C4 KATAKANA LETTER TU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C5 KATAKANA LETTER DU: try adding one of: chinese-simplified, japanese</li>
<li>U+30C6 KATAKANA LETTER TE: try adding one of: chinese-simplified, japanese</li>
<li>U+30C7 KATAKANA LETTER DE: try adding one of: chinese-simplified, japanese</li>
<li>U+30C8 KATAKANA LETTER TO: try adding one of: chinese-simplified, japanese</li>
<li>U+30C9 KATAKANA LETTER DO: try adding one of: chinese-simplified, japanese</li>
<li>U+30CA KATAKANA LETTER NA: try adding one of: chinese-simplified, japanese</li>
<li>U+30CB KATAKANA LETTER NI: try adding one of: chinese-simplified, japanese</li>
<li>U+30CC KATAKANA LETTER NU: try adding one of: chinese-simplified, japanese</li>
<li>U+30CD KATAKANA LETTER NE: try adding one of: chinese-simplified, japanese</li>
<li>U+30CE KATAKANA LETTER NO: try adding one of: chinese-simplified, japanese</li>
<li>U+30CF KATAKANA LETTER HA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D0 KATAKANA LETTER BA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D1 KATAKANA LETTER PA: try adding one of: chinese-simplified, japanese</li>
<li>U+30D2 KATAKANA LETTER HI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D3 KATAKANA LETTER BI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D4 KATAKANA LETTER PI: try adding one of: chinese-simplified, japanese</li>
<li>U+30D5 KATAKANA LETTER HU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D6 KATAKANA LETTER BU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D7 KATAKANA LETTER PU: try adding one of: chinese-simplified, japanese</li>
<li>U+30D8 KATAKANA LETTER HE: try adding one of: chinese-simplified, japanese</li>
<li>U+30D9 KATAKANA LETTER BE: try adding one of: chinese-simplified, japanese</li>
<li>U+30DA KATAKANA LETTER PE: try adding one of: chinese-simplified, japanese</li>
<li>U+30DB KATAKANA LETTER HO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DC KATAKANA LETTER BO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DD KATAKANA LETTER PO: try adding one of: chinese-simplified, japanese</li>
<li>U+30DE KATAKANA LETTER MA: try adding one of: chinese-simplified, japanese</li>
<li>U+30DF KATAKANA LETTER MI: try adding one of: chinese-simplified, japanese</li>
<li>U+30E0 KATAKANA LETTER MU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E1 KATAKANA LETTER ME: try adding one of: chinese-simplified, japanese</li>
<li>U+30E2 KATAKANA LETTER MO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E3 KATAKANA LETTER SMALL YA: try adding one of: chinese-simplified, japanese</li>
<li>U+30E4 KATAKANA LETTER YA: try adding one of: chinese-simplified, japanese</li>
<li>U+30E5 KATAKANA LETTER SMALL YU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E6 KATAKANA LETTER YU: try adding one of: chinese-simplified, japanese</li>
<li>U+30E7 KATAKANA LETTER SMALL YO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E8 KATAKANA LETTER YO: try adding one of: chinese-simplified, japanese</li>
<li>U+30E9 KATAKANA LETTER RA: try adding one of: chinese-simplified, japanese</li>
<li>U+30EA KATAKANA LETTER RI: try adding one of: chinese-simplified, japanese</li>
<li>U+30EB KATAKANA LETTER RU: try adding one of: chinese-simplified, japanese</li>
<li>U+30EC KATAKANA LETTER RE: try adding one of: chinese-simplified, japanese</li>
<li>U+30ED KATAKANA LETTER RO: try adding one of: chinese-simplified, japanese</li>
<li>U+30EE KATAKANA LETTER SMALL WA: try adding one of: chinese-simplified, japanese</li>
<li>U+30EF KATAKANA LETTER WA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F0 KATAKANA LETTER WI: try adding one of: chinese-simplified, japanese</li>
<li>U+30F1 KATAKANA LETTER WE: try adding one of: chinese-simplified, japanese</li>
<li>U+30F2 KATAKANA LETTER WO: try adding one of: chinese-simplified, japanese</li>
<li>U+30F3 KATAKANA LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+30F4 KATAKANA LETTER VU: try adding one of: chinese-simplified, japanese</li>
<li>U+30F5 KATAKANA LETTER SMALL KA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F6 KATAKANA LETTER SMALL KE: try adding one of: chinese-simplified, japanese</li>
<li>U+30F7 KATAKANA LETTER VA: try adding one of: chinese-simplified, japanese</li>
<li>U+30F8 KATAKANA LETTER VI: try adding one of: chinese-simplified, japanese</li>
<li>U+30F9 KATAKANA LETTER VE: try adding one of: chinese-simplified, japanese</li>
<li>U+30FA KATAKANA LETTER VO: try adding one of: chinese-simplified, japanese</li>
<li>U+30FB KATAKANA MIDDLE DOT: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+30FC KATAKANA-HIRAGANA PROLONGED SOUND MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FD KATAKANA ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FE KATAKANA VOICED ITERATION MARK: try adding one of: chinese-simplified, japanese</li>
<li>U+30FF KATAKANA DIGRAPH KOTO: try adding one of: chinese-simplified, japanese</li>
<li>U+31F0 KATAKANA LETTER SMALL KU: not included in any glyphset definition</li>
<li>U+31F1 KATAKANA LETTER SMALL SI: not included in any glyphset definition</li>
<li>U+31F2 KATAKANA LETTER SMALL SU: not included in any glyphset definition</li>
<li>U+31F3 KATAKANA LETTER SMALL TO: not included in any glyphset definition</li>
<li>U+31F4 KATAKANA LETTER SMALL NU: not included in any glyphset definition</li>
<li>U+31F5 KATAKANA LETTER SMALL HA: not included in any glyphset definition</li>
<li>U+31F6 KATAKANA LETTER SMALL HI: not included in any glyphset definition</li>
<li>U+31F7 KATAKANA LETTER SMALL HU: not included in any glyphset definition</li>
<li>U+31F8 KATAKANA LETTER SMALL HE: not included in any glyphset definition</li>
<li>U+31F9 KATAKANA LETTER SMALL HO: not included in any glyphset definition</li>
<li>U+31FA KATAKANA LETTER SMALL MU: not included in any glyphset definition</li>
<li>U+31FB KATAKANA LETTER SMALL RA: not included in any glyphset definition</li>
<li>U+31FC KATAKANA LETTER SMALL RI: not included in any glyphset definition</li>
<li>U+31FD KATAKANA LETTER SMALL RU: not included in any glyphset definition</li>
<li>U+31FE KATAKANA LETTER SMALL RE: not included in any glyphset definition</li>
<li>U+31FF KATAKANA LETTER SMALL RO: not included in any glyphset definition</li>
<li>U+33CB SQUARE HP: not included in any glyphset definition</li>
<li>U+4EDD CJK UNIFIED IDEOGRAPH-4EDD: try adding one of: chinese-traditional, japanese, chinese-simplified, chinese-hongkong</li>
<li>U+E133 : not included in any glyphset definition</li>
<li>U+E134 : not included in any glyphset definition</li>
<li>U+E139 : not included in any glyphset definition</li>
<li>U+E140 : not included in any glyphset definition</li>
<li>U+F001 : not included in any glyphset definition</li>
<li>U+F002 : not included in any glyphset definition</li>
<li>U+F003 : not included in any glyphset definition</li>
<li>U+F700 : not included in any glyphset definition</li>
<li>U+F701 : not included in any glyphset definition</li>
<li>U+F702 : not included in any glyphset definition</li>
<li>U+F703 : not included in any glyphset definition</li>
<li>U+F704 : not included in any glyphset definition</li>
<li>U+F705 : not included in any glyphset definition</li>
<li>U+F706 : not included in any glyphset definition</li>
<li>U+F707 : not included in any glyphset definition</li>
<li>U+F708 : not included in any glyphset definition</li>
<li>U+F709 : not included in any glyphset definition</li>
<li>U+F70A : not included in any glyphset definition</li>
<li>U+F70B : not included in any glyphset definition</li>
<li>U+F70C : not included in any glyphset definition</li>
<li>U+F70D : not included in any glyphset definition</li>
<li>U+F70E : not included in any glyphset definition</li>
<li>U+F70F : not included in any glyphset definition</li>
<li>U+F710 : not included in any glyphset definition</li>
<li>U+F711 : not included in any glyphset definition</li>
<li>U+F712 : not included in any glyphset definition</li>
<li>U+F713 : not included in any glyphset definition</li>
<li>U+F714 : not included in any glyphset definition</li>
<li>U+F715 : not included in any glyphset definition</li>
<li>U+F716 : not included in any glyphset definition</li>
<li>U+F717 : not included in any glyphset definition</li>
<li>U+F718 : not included in any glyphset definition</li>
<li>U+F719 : not included in any glyphset definition</li>
<li>U+F71A : not included in any glyphset definition</li>
<li>U+F71E : not included in any glyphset definition</li>
<li>U+F71F : not included in any glyphset definition</li>
<li>U+F720 : not included in any glyphset definition</li>
<li>U+F880 : not included in any glyphset definition</li>
<li>U+F881 : not included in any glyphset definition</li>
<li>U+F882 : not included in any glyphset definition</li>
<li>U+FB00 LATIN SMALL LIGATURE FF: not included in any glyphset definition</li>
<li>U+FB01 LATIN SMALL LIGATURE FI: not included in any glyphset definition</li>
<li>U+FB02 LATIN SMALL LIGATURE FL: not included in any glyphset definition</li>
<li>U+FB03 LATIN SMALL LIGATURE FFI: not included in any glyphset definition</li>
<li>U+FB04 LATIN SMALL LIGATURE FFL: not included in any glyphset definition</li>
<li>U+FE45 SESAME DOT: not included in any glyphset definition</li>
<li>U+FE46 WHITE SESAME DOT: not included in any glyphset definition</li>
<li>U+FF01 FULLWIDTH EXCLAMATION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF02 FULLWIDTH QUOTATION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF03 FULLWIDTH NUMBER SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF04 FULLWIDTH DOLLAR SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF05 FULLWIDTH PERCENT SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF06 FULLWIDTH AMPERSAND: try adding one of: chinese-simplified, japanese</li>
<li>U+FF07 FULLWIDTH APOSTROPHE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF08 FULLWIDTH LEFT PARENTHESIS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF09 FULLWIDTH RIGHT PARENTHESIS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0A FULLWIDTH ASTERISK: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0B FULLWIDTH PLUS SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0C FULLWIDTH COMMA: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0D FULLWIDTH HYPHEN-MINUS: try adding one of: chinese-simplified, japanese</li>
<li>U+FF0E FULLWIDTH FULL STOP: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF0F FULLWIDTH SOLIDUS: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF10 FULLWIDTH DIGIT ZERO: try adding one of: chinese-simplified, japanese</li>
<li>U+FF11 FULLWIDTH DIGIT ONE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF12 FULLWIDTH DIGIT TWO: try adding one of: chinese-simplified, japanese</li>
<li>U+FF13 FULLWIDTH DIGIT THREE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF14 FULLWIDTH DIGIT FOUR: try adding one of: chinese-simplified, japanese</li>
<li>U+FF15 FULLWIDTH DIGIT FIVE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF16 FULLWIDTH DIGIT SIX: try adding one of: chinese-simplified, japanese</li>
<li>U+FF17 FULLWIDTH DIGIT SEVEN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF18 FULLWIDTH DIGIT EIGHT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF19 FULLWIDTH DIGIT NINE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1A FULLWIDTH COLON: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF1B FULLWIDTH SEMICOLON: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF1C FULLWIDTH LESS-THAN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1D FULLWIDTH EQUALS SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1E FULLWIDTH GREATER-THAN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FF1F FULLWIDTH QUESTION MARK: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF20 FULLWIDTH COMMERCIAL AT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF21 FULLWIDTH LATIN CAPITAL LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+FF22 FULLWIDTH LATIN CAPITAL LETTER B: try adding one of: chinese-simplified, japanese</li>
<li>U+FF23 FULLWIDTH LATIN CAPITAL LETTER C: try adding one of: chinese-simplified, japanese</li>
<li>U+FF24 FULLWIDTH LATIN CAPITAL LETTER D: try adding one of: chinese-simplified, japanese</li>
<li>U+FF25 FULLWIDTH LATIN CAPITAL LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+FF26 FULLWIDTH LATIN CAPITAL LETTER F: try adding one of: chinese-simplified, japanese</li>
<li>U+FF27 FULLWIDTH LATIN CAPITAL LETTER G: try adding one of: chinese-simplified, japanese</li>
<li>U+FF28 FULLWIDTH LATIN CAPITAL LETTER H: try adding one of: chinese-simplified, japanese</li>
<li>U+FF29 FULLWIDTH LATIN CAPITAL LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2A FULLWIDTH LATIN CAPITAL LETTER J: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2B FULLWIDTH LATIN CAPITAL LETTER K: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2C FULLWIDTH LATIN CAPITAL LETTER L: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2D FULLWIDTH LATIN CAPITAL LETTER M: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2E FULLWIDTH LATIN CAPITAL LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+FF2F FULLWIDTH LATIN CAPITAL LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+FF30 FULLWIDTH LATIN CAPITAL LETTER P: try adding one of: chinese-simplified, japanese</li>
<li>U+FF31 FULLWIDTH LATIN CAPITAL LETTER Q: try adding one of: chinese-simplified, japanese</li>
<li>U+FF32 FULLWIDTH LATIN CAPITAL LETTER R: try adding one of: chinese-simplified, japanese</li>
<li>U+FF33 FULLWIDTH LATIN CAPITAL LETTER S: try adding one of: chinese-simplified, japanese</li>
<li>U+FF34 FULLWIDTH LATIN CAPITAL LETTER T: try adding one of: chinese-simplified, japanese</li>
<li>U+FF35 FULLWIDTH LATIN CAPITAL LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+FF36 FULLWIDTH LATIN CAPITAL LETTER V: try adding one of: chinese-simplified, japanese</li>
<li>U+FF37 FULLWIDTH LATIN CAPITAL LETTER W: try adding one of: chinese-simplified, japanese</li>
<li>U+FF38 FULLWIDTH LATIN CAPITAL LETTER X: try adding one of: chinese-simplified, japanese</li>
<li>U+FF39 FULLWIDTH LATIN CAPITAL LETTER Y: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3A FULLWIDTH LATIN CAPITAL LETTER Z: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3B FULLWIDTH LEFT SQUARE BRACKET: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF3C FULLWIDTH REVERSE SOLIDUS: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3D FULLWIDTH RIGHT SQUARE BRACKET: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF3E FULLWIDTH CIRCUMFLEX ACCENT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF3F FULLWIDTH LOW LINE: try adding one of: chinese-simplified, japanese</li>
<li>U+FF40 FULLWIDTH GRAVE ACCENT: try adding one of: chinese-simplified, japanese</li>
<li>U+FF41 FULLWIDTH LATIN SMALL LETTER A: try adding one of: chinese-simplified, japanese</li>
<li>U+FF42 FULLWIDTH LATIN SMALL LETTER B: try adding one of: chinese-simplified, japanese</li>
<li>U+FF43 FULLWIDTH LATIN SMALL LETTER C: try adding one of: chinese-simplified, japanese</li>
<li>U+FF44 FULLWIDTH LATIN SMALL LETTER D: try adding one of: chinese-simplified, japanese</li>
<li>U+FF45 FULLWIDTH LATIN SMALL LETTER E: try adding one of: chinese-simplified, japanese</li>
<li>U+FF46 FULLWIDTH LATIN SMALL LETTER F: try adding one of: chinese-simplified, japanese</li>
<li>U+FF47 FULLWIDTH LATIN SMALL LETTER G: try adding one of: chinese-simplified, japanese</li>
<li>U+FF48 FULLWIDTH LATIN SMALL LETTER H: try adding one of: chinese-simplified, japanese</li>
<li>U+FF49 FULLWIDTH LATIN SMALL LETTER I: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4A FULLWIDTH LATIN SMALL LETTER J: try adding japanese</li>
<li>U+FF4B FULLWIDTH LATIN SMALL LETTER K: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4C FULLWIDTH LATIN SMALL LETTER L: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4D FULLWIDTH LATIN SMALL LETTER M: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4E FULLWIDTH LATIN SMALL LETTER N: try adding one of: chinese-simplified, japanese</li>
<li>U+FF4F FULLWIDTH LATIN SMALL LETTER O: try adding one of: chinese-simplified, japanese</li>
<li>U+FF50 FULLWIDTH LATIN SMALL LETTER P: try adding one of: chinese-simplified, japanese</li>
<li>U+FF51 FULLWIDTH LATIN SMALL LETTER Q: try adding one of: chinese-simplified, japanese</li>
<li>U+FF52 FULLWIDTH LATIN SMALL LETTER R: try adding one of: chinese-simplified, japanese</li>
<li>U+FF53 FULLWIDTH LATIN SMALL LETTER S: try adding one of: chinese-simplified, japanese</li>
<li>U+FF54 FULLWIDTH LATIN SMALL LETTER T: try adding one of: chinese-simplified, japanese</li>
<li>U+FF55 FULLWIDTH LATIN SMALL LETTER U: try adding one of: chinese-simplified, japanese</li>
<li>U+FF56 FULLWIDTH LATIN SMALL LETTER V: try adding one of: chinese-simplified, japanese</li>
<li>U+FF57 FULLWIDTH LATIN SMALL LETTER W: try adding one of: chinese-simplified, japanese</li>
<li>U+FF58 FULLWIDTH LATIN SMALL LETTER X: try adding one of: chinese-simplified, japanese</li>
<li>U+FF59 FULLWIDTH LATIN SMALL LETTER Y: try adding one of: chinese-simplified, japanese</li>
<li>U+FF5A FULLWIDTH LATIN SMALL LETTER Z: try adding japanese</li>
<li>U+FF5B FULLWIDTH LEFT CURLY BRACKET: try adding one of: math, chinese-simplified, yi, japanese</li>
<li>U+FF5C FULLWIDTH VERTICAL LINE: try adding one of: chinese-simplified, yi, japanese</li>
<li>U+FF5D FULLWIDTH RIGHT CURLY BRACKET: try adding one of: math, chinese-simplified, yi, japanese</li>
<li>U+FF5E FULLWIDTH TILDE: try adding one of: chinese-simplified, yi</li>
<li>U+FF5F FULLWIDTH LEFT WHITE PARENTHESIS: not included in any glyphset definition</li>
<li>U+FF60 FULLWIDTH RIGHT WHITE PARENTHESIS: not included in any glyphset definition</li>
<li>U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP: try adding yi</li>
<li>U+FF62 HALFWIDTH LEFT CORNER BRACKET: try adding yi</li>
<li>U+FF63 HALFWIDTH RIGHT CORNER BRACKET: try adding yi</li>
<li>U+FF64 HALFWIDTH IDEOGRAPHIC COMMA: try adding yi</li>
<li>U+FF65 HALFWIDTH KATAKANA MIDDLE DOT: try adding yi</li>
<li>U+FF66 HALFWIDTH KATAKANA LETTER WO: not included in any glyphset definition</li>
<li>U+FF67 HALFWIDTH KATAKANA LETTER SMALL A: not included in any glyphset definition</li>
<li>U+FF68 HALFWIDTH KATAKANA LETTER SMALL I: not included in any glyphset definition</li>
<li>U+FF69 HALFWIDTH KATAKANA LETTER SMALL U: not included in any glyphset definition</li>
<li>U+FF6A HALFWIDTH KATAKANA LETTER SMALL E: not included in any glyphset definition</li>
<li>U+FF6B HALFWIDTH KATAKANA LETTER SMALL O: not included in any glyphset definition</li>
<li>U+FF6C HALFWIDTH KATAKANA LETTER SMALL YA: not included in any glyphset definition</li>
<li>U+FF6D HALFWIDTH KATAKANA LETTER SMALL YU: not included in any glyphset definition</li>
<li>U+FF6E HALFWIDTH KATAKANA LETTER SMALL YO: not included in any glyphset definition</li>
<li>U+FF6F HALFWIDTH KATAKANA LETTER SMALL TU: not included in any glyphset definition</li>
<li>U+FF70 HALFWIDTH KATAKANA-HIRAGANA PROLONGED SOUND MARK: not included in any glyphset definition</li>
<li>U+FF71 HALFWIDTH KATAKANA LETTER A: not included in any glyphset definition</li>
<li>U+FF72 HALFWIDTH KATAKANA LETTER I: not included in any glyphset definition</li>
<li>U+FF73 HALFWIDTH KATAKANA LETTER U: not included in any glyphset definition</li>
<li>U+FF74 HALFWIDTH KATAKANA LETTER E: not included in any glyphset definition</li>
<li>U+FF75 HALFWIDTH KATAKANA LETTER O: not included in any glyphset definition</li>
<li>U+FF76 HALFWIDTH KATAKANA LETTER KA: not included in any glyphset definition</li>
<li>U+FF77 HALFWIDTH KATAKANA LETTER KI: not included in any glyphset definition</li>
<li>U+FF78 HALFWIDTH KATAKANA LETTER KU: not included in any glyphset definition</li>
<li>U+FF79 HALFWIDTH KATAKANA LETTER KE: not included in any glyphset definition</li>
<li>U+FF7A HALFWIDTH KATAKANA LETTER KO: not included in any glyphset definition</li>
<li>U+FF7B HALFWIDTH KATAKANA LETTER SA: not included in any glyphset definition</li>
<li>U+FF7C HALFWIDTH KATAKANA LETTER SI: not included in any glyphset definition</li>
<li>U+FF7D HALFWIDTH KATAKANA LETTER SU: not included in any glyphset definition</li>
<li>U+FF7E HALFWIDTH KATAKANA LETTER SE: not included in any glyphset definition</li>
<li>U+FF7F HALFWIDTH KATAKANA LETTER SO: not included in any glyphset definition</li>
<li>U+FF80 HALFWIDTH KATAKANA LETTER TA: not included in any glyphset definition</li>
<li>U+FF81 HALFWIDTH KATAKANA LETTER TI: not included in any glyphset definition</li>
<li>U+FF82 HALFWIDTH KATAKANA LETTER TU: not included in any glyphset definition</li>
<li>U+FF83 HALFWIDTH KATAKANA LETTER TE: not included in any glyphset definition</li>
<li>U+FF84 HALFWIDTH KATAKANA LETTER TO: not included in any glyphset definition</li>
<li>U+FF85 HALFWIDTH KATAKANA LETTER NA: not included in any glyphset definition</li>
<li>U+FF86 HALFWIDTH KATAKANA LETTER NI: not included in any glyphset definition</li>
<li>U+FF87 HALFWIDTH KATAKANA LETTER NU: not included in any glyphset definition</li>
<li>U+FF88 HALFWIDTH KATAKANA LETTER NE: not included in any glyphset definition</li>
<li>U+FF89 HALFWIDTH KATAKANA LETTER NO: not included in any glyphset definition</li>
<li>U+FF8A HALFWIDTH KATAKANA LETTER HA: not included in any glyphset definition</li>
<li>U+FF8B HALFWIDTH KATAKANA LETTER HI: not included in any glyphset definition</li>
<li>U+FF8C HALFWIDTH KATAKANA LETTER HU: not included in any glyphset definition</li>
<li>U+FF8D HALFWIDTH KATAKANA LETTER HE: not included in any glyphset definition</li>
<li>U+FF8E HALFWIDTH KATAKANA LETTER HO: not included in any glyphset definition</li>
<li>U+FF8F HALFWIDTH KATAKANA LETTER MA: not included in any glyphset definition</li>
<li>U+FF90 HALFWIDTH KATAKANA LETTER MI: not included in any glyphset definition</li>
<li>U+FF91 HALFWIDTH KATAKANA LETTER MU: not included in any glyphset definition</li>
<li>U+FF92 HALFWIDTH KATAKANA LETTER ME: not included in any glyphset definition</li>
<li>U+FF93 HALFWIDTH KATAKANA LETTER MO: not included in any glyphset definition</li>
<li>U+FF94 HALFWIDTH KATAKANA LETTER YA: not included in any glyphset definition</li>
<li>U+FF95 HALFWIDTH KATAKANA LETTER YU: not included in any glyphset definition</li>
<li>U+FF96 HALFWIDTH KATAKANA LETTER YO: not included in any glyphset definition</li>
<li>U+FF97 HALFWIDTH KATAKANA LETTER RA: not included in any glyphset definition</li>
<li>U+FF98 HALFWIDTH KATAKANA LETTER RI: not included in any glyphset definition</li>
<li>U+FF99 HALFWIDTH KATAKANA LETTER RU: not included in any glyphset definition</li>
<li>U+FF9A HALFWIDTH KATAKANA LETTER RE: not included in any glyphset definition</li>
<li>U+FF9B HALFWIDTH KATAKANA LETTER RO: not included in any glyphset definition</li>
<li>U+FF9C HALFWIDTH KATAKANA LETTER WA: not included in any glyphset definition</li>
<li>U+FF9D HALFWIDTH KATAKANA LETTER N: not included in any glyphset definition</li>
<li>U+FF9E HALFWIDTH KATAKANA VOICED SOUND MARK: not included in any glyphset definition</li>
<li>U+FF9F HALFWIDTH KATAKANA SEMI-VOICED SOUND MARK: not included in any glyphset definition</li>
<li>U+FFE0 FULLWIDTH CENT SIGN: try adding chinese-simplified</li>
<li>U+FFE1 FULLWIDTH POUND SIGN: try adding chinese-simplified</li>
<li>U+FFE2 FULLWIDTH NOT SIGN: not included in any glyphset definition</li>
<li>U+FFE3 FULLWIDTH MACRON: try adding one of: chinese-simplified, japanese</li>
<li>U+FFE4 FULLWIDTH BROKEN BAR: not included in any glyphset definition</li>
<li>U+FFE5 FULLWIDTH YEN SIGN: try adding one of: chinese-simplified, japanese</li>
<li>U+FFE6 FULLWIDTH WON SIGN: not included in any glyphset definition</li>
<li>U+FFE8 HALFWIDTH FORMS LIGHT VERTICAL: not included in any glyphset definition</li>
<li>U+FFE9 HALFWIDTH LEFTWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEA HALFWIDTH UPWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEB HALFWIDTH RIGHTWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFEC HALFWIDTH DOWNWARDS ARROW: not included in any glyphset definition</li>
<li>U+FFED HALFWIDTH BLACK SQUARE: not included in any glyphset definition</li>
<li>U+FFEE HALFWIDTH WHITE CIRCLE: not included in any glyphset definition</li>
<li>U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition</li>
<li>U+1F494 BROKEN HEART: not included in any glyphset definition</li>
<li>U+1FBB0 ARROWHEAD-SHAPED POINTER: try adding symbols</li>
<li>U+1FBB2 LEFT HALF RUNNING MAN: try adding symbols</li>
<li>U+1FBB3 RIGHT HALF RUNNING MAN: try adding symbols</li>
</ul>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>lao</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>thai</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check copyright namerecords match license file. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license">googlefonts/name/license</a></summary>
    <div>







* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider updating the url from '<a href="https://scripts.sil.org/OFL">https://scripts.sil.org/OFL</a>' to '<a href="https://openfontlicense.org">https://openfontlicense.org</a>'.</p>
 [code: old-url]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> License URL matches License text on name table? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-name-license-url">googlefonts/name/license_url</a></summary>
    <div>









* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



* ⚠️ **WARN** <p>Please consider using HTTPS URLs at name table entry [plat=3, enc=1, name=13]</p>
 [code: http-in-description]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure soft_dotted characters lose their dot when combined with marks that replace the dot. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#soft-dotted">soft_dotted</a></summary>
    <div>







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ i̍ i̓ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ і́ ḭ̀ ḭ́ ḭ̄ ị̀ ị́ ị̂ ị̃ ị̄</p>
<p>The dot of soft dotted characters <em>should</em> disappear in other cases, for example: i̅ i̇ i̎ i̒ i̔ i̛̅ i̛̇ i̛̊ i̛̋ i̛̍ i̛̎ i̛̒ i̛̓ i̛̔ i̤̅ i̤̇ i̤̊ i̤̋ i̤̍ i̤̎</p>
 [code: soft-dotted]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Ensure fonts have ScriptLangTags declared on the 'meta' table. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-meta-script-lang-tags">googlefonts/meta/script_lang_tags</a></summary>
    <div>







* ⚠️ **WARN** <p>This font file does not have a 'meta' table.</p>
 [code: lacks-meta-table]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 23 | 40 | 310 | 16 | 285 | 0 | 
| 0% | 0% | 3% | 6% | 46% | 2% | 42% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
