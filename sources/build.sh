#!/bin/bash
# set -e

# Configuration
font_families=("SyyUDT" "SyyUDS")
weights=("Regular")
output_base="fonts"
sources_base="sources"

echo_art() {
  echo -e "\e[97m\e[46m                         \e[49m
\e[46m   ███  █▄▛█ █▄█ ██ ███  \e[49m
\e[46m  █ █ █   ▃█▃  █  █ █ █  \e[49m
\e[46m  █ █ █ ██ █  █   █ █ █  \e[49m
\e[46m   ███  █ ██  ██  ███ █  \e[49m
\e[46m                         \e[49m\e[39m
╓─ ░▒▓\e[107m\e[90m   SyyDai    \e[49m\e[39m▓▒░
║"
}

echo_end() {
  echo -e "║
║   ▄▄            ▄▄▄
║  █  █          █▄ ▗
║   ██           █ ██ 
║      █
║ ▄▄▄ █  ▄▄▄  ▄   ▄▄▄▄  ▄▄▄   ▄
║    █  █   █ █  █▄▄▄▄ █   █  █
║ ▄▄▄ █     █ █      █   ███  █
║ █  ██     █ █▄     █     █   
║ ██  █     █ ██    ██     █  █
╙─
"
}

check_requirements() {
  local missing=""

  for cmd in fontmake woff2_compress gftools fontbakery shaperglot python; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
      missing="$missing $cmd"
    fi
  done

  if [ -n "$missing" ]; then
    echo -e "❌ \e[31mRequired commands not found:\e[0m\e[97m$missing\e[31m. Please install them before proceeding.\e[0m"
    exit 1
  fi

  echo -e "\e[32m✓ All requirements satisfied\e[0m"
}

cleanup() {
  echo "╟─ Cleaning font directories"

  rm -rf \
    "$output_base" \
    ./out/diffenator2 \
    ./out/fontbakery \
    ./out/htmltest || exit 1
}

run_fix_ufo() {
  local ufo_path="$1"

  python ./scripts/fix_ufo.py "$ufo_path" || exit 1
}

copy_features_if_needed() {
  local weight="$1"
  local font_name="$2"

  if [ "$weight" != "Regular" ]; then
    echo -e "║\n╟─ Copying features.fea from Regular → $font_name-$weight"

    cp \
      "$sources_base/$font_name-Regular.ufo/features.fea" \
      "$sources_base/$font_name-$weight.ufo/features.fea" || exit 1
  fi
}

generate_unhinted_ttf() {
  local ufo_path="$1"
  local output_name="$2"

  mkdir -p "$output_base/unhinted/ttf" || exit 1

  echo -e "║\n╟─ Generating \e[32munhinted .ttf\e[39m ($output_name)"

  fontmake \
    -u "$ufo_path" \
    -o ttf \
    --output-dir "$output_base/unhinted/ttf" \
    --overlaps-backend pathops || exit 1

  local generated="$output_base/unhinted/ttf/${output_name}.ttf"

  if [ ! -f "$generated" ]; then
    echo -e "❌ \e[31mUnhinted TTF not generated: $generated\e[0m"
    exit 1
  fi
}

generate_unhinted_otf() {
  local ufo_path="$1"
  local output_name="$2"

  mkdir -p "$output_base/unhinted/otf" || exit 1

  echo -e "║\n╟─ Generating \e[32munhinted .otf\e[39m ($output_name)"

  fontmake \
    -u "$ufo_path" \
    -o otf \
    --output-dir "$output_base/unhinted/otf" \
    --overlaps-backend pathops || exit 1

  local generated="$output_base/unhinted/otf/${output_name}.otf"

  if [ ! -f "$generated" ]; then
    echo -e "❌ \e[31mUnhinted OTF not generated: $generated\e[0m"
    exit 1
  fi
}

generate_woff2() {
  local ttf_path="$1"
  local output_path="$2"

  if [ ! -f "$ttf_path" ]; then
    echo -e "❌ \e[31mTTF not found: $ttf_path\e[0m"
    exit 1
  fi

  local temp_woff2="${ttf_path%.ttf}.woff2"

  rm -f "$temp_woff2"

  woff2_compress "$ttf_path" || exit 1

  if [ ! -f "$temp_woff2" ]; then
    echo -e "❌ \e[31mWOFF2 was not generated: $temp_woff2\e[0m"
    exit 1
  fi

  mkdir -p "$(dirname "$output_path")" || exit 1

  mv "$temp_woff2" "$output_path" || exit 1
}

hint_font() {
  local input_ttf="$1"
  local output_ttf="$2"
  local font_name="$3"
  local weight="$4"

  if [ ! -f "$input_ttf" ]; then
    echo -e "❌ \e[31mUnhinted TTF not found: $input_ttf\e[0m"
    exit 1
  fi

  echo -e "║\n╟─ Generating \e[92mhinted .ttf\e[39m ($font_name-$weight)"

  mkdir -p "$output_base/ttf" || exit 1

  gftools autohint \
    "$input_ttf" \
    -o "$output_ttf" \
    --args "-X -" || exit 1

  gftools fix-hinting "$output_ttf" || exit 1

  if [ -f "${output_ttf}.fix" ]; then
    mv "${output_ttf}.fix" "$output_ttf" || exit 1
  fi

  if [ ! -f "$output_ttf" ]; then
    echo -e "❌ \e[31mHinted TTF was not generated: $output_ttf\e[0m"
    exit 1
  fi
}

generate_webfonts() {
  local unhinted_ttf="$1"
  local hinted_ttf="$2"
  local font_file="$3"

  echo -e "║\n╟─ Generating \e[32munhinted .woff2\e[39m ($font_file)"

  generate_woff2 \
    "$unhinted_ttf" \
    "$output_base/unhinted/webfonts/${font_file}.woff2"

  echo -e "║\n╟─ Generating \e[92mhinted .woff2\e[39m ($font_file)"

  generate_woff2 \
    "$hinted_ttf" \
    "$output_base/webfonts/${font_file}.woff2"
}

generate_images() {
  local ttf_path="$1"
  local dia_index="$2"


  if [ ! -f "$ttf_path" ]; then
    echo -e "❌ \e[31mTTF not found for images: $ttf_path\e[0m"
    return 1
  fi

  echo -e "║\n╟─ Generating Images for $(basename "$ttf_path")"

  python ./scripts/gen_glyph_grid.py "$ttf_path" || true
  python ./scripts/gen_img_text.py "$ttf_path" || true
  python ./scripts/gen_img_dia.py "$ttf_path"  "-$dia_index" || true
}

process_font() {
  local font_name="$1"
  local weight="$2"
  local dia_index="$3"

  local ufo_file="${sources_base}/${font_name}-${weight}.ufo"
  local font_file="${font_name}-${weight}"

  local unhinted_ttf="$output_base/unhinted/ttf/${font_file}.ttf"
  local unhinted_otf="$output_base/unhinted/otf/${font_file}.otf"
  local hinted_ttf="$output_base/ttf/${font_file}.ttf"

  echo -e "║\n╟─ Processing: \e[36m${font_file}\e[39m"

  run_fix_ufo "$ufo_file"

  copy_features_if_needed "$weight" "$font_name"

  # ============================================================
  # UNHINTED
  # ============================================================

  generate_unhinted_ttf \
    "$ufo_file" \
    "$font_file"

  generate_unhinted_otf \
    "$ufo_file" \
    "$font_file"

  generate_webfonts \
    "$unhinted_ttf" \
    "$unhinted_ttf" \
    "$font_file"

  # ============================================================
  # HINTED
  # ============================================================

  hint_font \
    "$unhinted_ttf" \
    "$hinted_ttf" \
    "$font_name" \
    "$weight"

  # ============================================================
  # HINTED WOFF2
  # ============================================================

  generate_woff2 \
    "$hinted_ttf" \
    "$output_base/webfonts/${font_file}.woff2"

  # ============================================================
  # IMAGES
  # ============================================================

  generate_images "$hinted_ttf" "$dia_index"
}

process_all() {
  echo_art

  check_requirements
  cleanup

  # ============================================================
  # PROCESS FONTS
  # ============================================================

  for i in "${!font_families[@]}"; do
    font_name="${font_families[$i]}"

    for weight in "${weights[@]}"; do
      ufo_path="$sources_base/$font_name-$weight.ufo"

      if [ -d "$ufo_path" ]; then
        process_font "$font_name" "$weight" "$i"
      else
        echo -e "❌ \e[31mSource not found: $ufo_path\e[0m"
        exit 1
      fi
    done
  done

  # ============================================================
  # FONTBAKERY
  # ============================================================

  echo "║"
  echo "╟─ Testing output with FontBakery"

  mkdir -p ./out/fontbakery || exit 1

  SKIP_NETWORK=""
  DO_DIFFENATOR=false

  for arg in "$@"; do
    case "$arg" in
      --skip-network)
        echo "║  --skip-network"
        SKIP_NETWORK="--skip-network"
        ;;

      --diffenator)
        echo "║  --diffenator"
        DO_DIFFENATOR=true
        ;;
    esac
  done

  local all_ttf_files=()

  for font_name in "${font_families[@]}"; do
    for weight in "${weights[@]}"; do
      local ttf_file="$output_base/ttf/${font_name}-${weight}.ttf"

      if [ -f "$ttf_file" ]; then
        all_ttf_files+=("$ttf_file")
      fi
    done
  done

  if [ "${#all_ttf_files[@]}" -gt 0 ]; then
    fontbakery check-googlefonts \
      -F \
      --succinct \
      --json out/fontbakery/fontbakery-report.json \
      "${all_ttf_files[@]}" \
      --html out/fontbakery/fontbakery-report.html \
      --ghmarkdown out/fontbakery/fontbakery-report.md \
      --configuration fontbakery.yaml \
      $SKIP_NETWORK
  fi

  # ============================================================
  # DIFFENATOR
  # ============================================================

  if [ "$DO_DIFFENATOR" = true ]; then

    echo "║"
    echo "╟─ Run Diffenator 2 : compare hinted vs unhinted TTF fonts (HTML output, ~2-3 min)"

    mkdir -p ./out/diffenator2 || exit 1

    local unhinted_files=()
    local hinted_files=()

    for font_name in "${font_families[@]}"; do
      for weight in "${weights[@]}"; do

        local unhinted="$output_base/unhinted/ttf/${font_name}-${weight}.ttf"
        local hinted="$output_base/ttf/${font_name}-${weight}.ttf"

        if [ -f "$unhinted" ] && [ -f "$hinted" ]; then
          unhinted_files+=("$unhinted")
          hinted_files+=("$hinted")
        fi

      done
    done

    if [ "${#unhinted_files[@]}" -gt 0 ]; then
      diffenator2 diff \
        --out out/diffenator2/ \
        -fb "${unhinted_files[@]}" \
        -fa "${hinted_files[@]}" \
        2>/dev/null || true
    fi

  else
    echo "║  Skipped Diffenator 2"
  fi

  echo_end
}

# Main execution
case "$1" in
  --all)
    process_all "$@"
    ;;

  *)
    process_all "$@"
    ;;
esac