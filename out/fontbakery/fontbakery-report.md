## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[1] Family checks</summary>
<div>
<details>
    <summary>🔥 <b>FAIL</b> Verify that family names in the name table are consistent across all fonts in the family. Checks Typographic Family name (nameID 16) if present, otherwise uses Font Family name (nameID 1) <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-family-consistent-family-name">opentype/family/consistent_family_name</a></summary>
    <div>







* 🔥 **FAIL** <p>2 different Font Family names were found:</p>
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
</ul>
 [code: inconsistent-family-name]



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



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1248 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 128 glyphs (10.26%) have a different width. You should check the widths of: ['exclam', 'quotedbl', 'quotesingle', 'parenleft', 'parenright', 'comma', 'period', 'colon', 'semicolon', 'M', 'W', 'underscore', 'grave', 'm', 'w', 'braceleft', 'bar', 'braceright', 'exclamdown', 'acute', 'periodcentered', 'cedilla', 'AE', 'ae', 'OE', 'oe', 'Wcircumflex', 'wcircumflex', 'uni01C0', 'uni01C1', 'uni01E2', 'uni01E3', 'AEacute', 'aeacute', 'uni02B9', 'uni0402', 'uni0409', 'uni040A', 'uni040B', 'uni0416', 'uni0424', 'uni0428', 'uni0429', 'uni042B', 'uni042E', 'uni0436', 'uni043C', 'uni0444', 'uni0448', 'uni0449', 'uni044B', 'uni044E', 'uni0452', 'uni0459', 'uni045A', 'uni045B', 'uni0496', 'uni0497', 'uni04C1', 'uni04C2', 'uni04DC', 'uni04DD', 'uni04F8', 'uni04F9', 'uni0E0C', 'uni0E0D', 'uni0E12', 'uni0E13', 'uni0E40', 'uni0E46', 'uni0E86', 'uni0E8E', 'uni0E91', 'uni0E92', 'uni0E93', 'uni0E97', 'uni0E9E', 'uni0E9F', 'uni0EA4', 'uni0EAB', 'uni0EC0', 'uni0EC6', 'uni0EDC', 'uni0EDD', 'uni1E40', 'uni1E41', 'uni2001', 'uni2003', 'uni2004', 'uni2005', 'uni2006', 'uni2008', 'uni2009', 'uni200A', 'emdash', 'uni2015', 'quoteleft', 'quoteright', 'quotesinglbase', 'quotereversed', 'quotedblleft', 'quotedblright', 'quotedblbase', 'uni201F', 'uni2605', 'uni2606', 'uni2661', 'heart', 'uni2764', 'uni2765', 'uniE133', 'uniE134', 'uniE139', 'uni0E0D.descless', 'uni0E24_uni0E45', 'uni0E26_uni0E45', 'uniFB00', 'uniFB01', 'uniFB02', 'uniFB03', 'uniFB04', 'uniFF01', 'uniFF08', 'uniFF09', 'uniFF0F', 'uniFF3C', 'uniFF44', 'u1F494']</p>
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
<tr>
<td align="left">U+04E0: CYRILLIC CAPITAL LETTER ABKHASIAN DZE</td>
<td align="left">U+04E1: CYRILLIC SMALL LETTER ABKHASIAN DZE</td>
</tr>
<tr>
<td align="left">U+FF44: FULLWIDTH LATIN SMALL LETTER D</td>
<td align="left">U+FF24: FULLWIDTH LATIN CAPITAL LETTER D</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1024, but got 768 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 384, but got 256 instead</p>
 [code: descent]



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
<td align="left">The following base characters are missing from the font: ẁ, ẃ, Ẁ, ẅ, Ẅ, Ẃ</td>
<td align="left">cy_Latn (Welsh)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ẞ</td>
<td align="left">de_Latn (German)</td>
</tr>
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
<td align="left">The following base characters are missing from the font: ƙ, Ƙ, ƴ, Ƴ</td>
<td align="left">ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ṣ, Ḿ, ṣ, ḿ</td>
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
<td align="left">The following base characters are missing from the font: Ҡ, ҫ, Ҫ, ҡ, Ҙ, ҙ</td>
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
<td align="left">kbd_Cyrl (Kabardian), dar_Cyrl (Dargwa) and inh_Cyrl (Ingush)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: цӏ, пӏ, тӏ, рхӏ, кӏ, чӏ, хӏ, гӏ</td>
<td align="left">ce_Cyrl (Chechen)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ӏ, ӏ</td>
<td align="left">av_Cyrl (Avaric), ady_Cyrl (Adyghe) and lez_Cyrl (Lezghian)</td>
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
<td align="left">The following auxiliary characters are missing from the font: ẞ</td>
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
<td align="left">The following auxiliary characters are missing from the font: ẞ</td>
<td align="left">fr_Latn (French), it_Latn (Italian), pl_Latn (Polish) and tr_Latn (Turkish)</td>
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
<td align="left">The following auxiliary characters are missing from the font: ḿ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ḿ</td>
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
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyph-coverage">googlefonts/glyph_coverage</a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x1E80 (LATIN CAPITAL LETTER W WITH GRAVE)


- 0x1E81 (LATIN SMALL LETTER W WITH GRAVE)


- 0x1E82 (LATIN CAPITAL LETTER W WITH ACUTE)


- 0x1E83 (LATIN SMALL LETTER W WITH ACUTE)


- 0x1E84 (LATIN CAPITAL LETTER W WITH DIAERESIS)


- 0x1E85 (LATIN SMALL LETTER W WITH DIAERESIS)


- 0x1E9E (LATIN CAPITAL LETTER SHARP S)


- 0x2212 (MINUS SIGN)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font follows the Google Fonts vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vertical-metrics">googlefonts/vertical_metrics</a></summary>
    <div>







* 🔥 **FAIL** <p>The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1024 when it should be at least 1228</p>
 [code: bad-hhea-range]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0334 (U+0334), uni0335 (U+0335), uni0336 (U+0336), uni0337 (U+0337), uni0338 (U+0338) and uni0358 (U+0358)</p>
 [code: mark-chars]



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

- Glyph name: hookabovecomb	Contours detected: 3	Expected: 1

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

- Glyph name: uni0E4E	Contours detected: 5	Expected: 1

- Glyph name: uni0E4F	Contours detected: 3	Expected: 4

- Glyph name: uni0E55	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E5B	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni1E44	Contours detected: 3	Expected: 2

- Glyph name: uni1EA2	Contours detected: 5	Expected: 3

- Glyph name: uni1EA3	Contours detected: 5	Expected: 3

- Glyph name: uni1EA8	Contours detected: 6	Expected: 4

- Glyph name: uni1EA9	Contours detected: 6	Expected: 4

- Glyph name: uni1EB2	Contours detected: 6	Expected: 4

- Glyph name: uni1EB3	Contours detected: 6	Expected: 4

- Glyph name: uni1EBA	Contours detected: 4	Expected: 2

- Glyph name: uni1EBB	Contours detected: 5	Expected: 3

- Glyph name: uni1EC2	Contours detected: 5	Expected: 3

- Glyph name: uni1EC3	Contours detected: 6	Expected: 4

- Glyph name: uni1EC8	Contours detected: 4	Expected: 2

- Glyph name: uni1EC9	Contours detected: 4	Expected: 2

- Glyph name: uni1ECE	Contours detected: 5	Expected: 3

- Glyph name: uni1ECF	Contours detected: 5	Expected: 3

- Glyph name: uni1ED4	Contours detected: 6	Expected: 4

- Glyph name: uni1ED5	Contours detected: 6	Expected: 4

- Glyph name: uni1EDE	Contours detected: 5	Expected: 3 or 4

- Glyph name: uni1EDF	Contours detected: 5	Expected: 3

- Glyph name: uni1EE6	Contours detected: 4	Expected: 2

- Glyph name: uni1EE7	Contours detected: 4	Expected: 2

- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

- Glyph name: uni1EED	Contours detected: 4	Expected: 2

- Glyph name: uni1EF6	Contours detected: 4	Expected: 2

- Glyph name: uni1EF7	Contours detected: 4	Expected: 2

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

- Glyph name: infinity	Contours detected: 1	Expected: 3

- Glyph name: lessequal	Contours detected: 1	Expected: 2

- Glyph name: greaterequal	Contours detected: 1	Expected: 2

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 8	Expected: 1

- Glyph name: uni2572	Contours detected: 8	Expected: 1

- Glyph name: uni2573	Contours detected: 13	Expected: 1

- Glyph name: circle	Contours detected: 8	Expected: 2

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

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

- Glyph name: Wcircumflex	Contours detected: 4	Expected: 2

- Glyph name: ae	Contours detected: 1	Expected: 3

- Glyph name: aeacute	Contours detected: 2	Expected: 4

- Glyph name: aogonek	Contours detected: 3	Expected: 2

- Glyph name: at	Contours detected: 1	Expected: 2

- Glyph name: chi	Contours detected: 3	Expected: 1

- Glyph name: circle	Contours detected: 8	Expected: 2

- Glyph name: comma	Contours detected: 2	Expected: 1

- Glyph name: copyright	Contours detected: 12	Expected: 3

- Glyph name: delta	Contours detected: 1	Expected: 2

- Glyph name: eogonek	Contours detected: 3	Expected: 2

- Glyph name: eth	Contours detected: 4	Expected: 2

- Glyph name: fraction	Contours detected: 8	Expected: 1

- Glyph name: greaterequal	Contours detected: 1	Expected: 2

- Glyph name: infinity	Contours detected: 1	Expected: 3

- Glyph name: k	Contours detected: 3	Expected: 1 or 2

- Glyph name: kappa	Contours detected: 3	Expected: 1

- Glyph name: kgreenlandic	Contours detected: 3	Expected: 1 or 2

- Glyph name: lcaron	Contours detected: 3	Expected: 2

- Glyph name: lessequal	Contours detected: 1	Expected: 2

- Glyph name: lslash	Contours detected: 3	Expected: 1

- Glyph name: omega	Contours detected: 3	Expected: 1

- Glyph name: omegatonos	Contours detected: 4	Expected: 2

- Glyph name: onehalf	Contours detected: 8	Expected: 3

- Glyph name: onequarter	Contours detected: 8	Expected: 3 or 4

- Glyph name: percent	Contours detected: 14	Expected: 4 or 5

- Glyph name: perthousand	Contours detected: 18	Expected: 6 or 7

- Glyph name: phi	Contours detected: 1	Expected: 2 or 3

- Glyph name: quotedblbase	Contours detected: 4	Expected: 2

- Glyph name: quotedblleft	Contours detected: 4	Expected: 2

- Glyph name: quotedblright	Contours detected: 4	Expected: 2

- Glyph name: quoteleft	Contours detected: 2	Expected: 1

- Glyph name: quoteright	Contours detected: 2	Expected: 1

- Glyph name: quotesinglbase	Contours detected: 2	Expected: 1

- Glyph name: registered	Contours detected: 9	Expected: 3 or 4

- Glyph name: semicolon	Contours detected: 3	Expected: 2

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

- Glyph name: uni0E4E	Contours detected: 5	Expected: 1

- Glyph name: uni0E4F	Contours detected: 3	Expected: 4

- Glyph name: uni0E55	Contours detected: 2	Expected: 1 or 3

- Glyph name: uni0E5B	Contours detected: 3	Expected: 1 or 2

- Glyph name: uni1E44	Contours detected: 3	Expected: 2

- Glyph name: uni1EA2	Contours detected: 5	Expected: 3

- Glyph name: uni1EA3	Contours detected: 5	Expected: 3

- Glyph name: uni1EA8	Contours detected: 6	Expected: 4

- Glyph name: uni1EA9	Contours detected: 6	Expected: 4

- Glyph name: uni1EB2	Contours detected: 6	Expected: 4

- Glyph name: uni1EB3	Contours detected: 6	Expected: 4

- Glyph name: uni1EBA	Contours detected: 4	Expected: 2

- Glyph name: uni1EBB	Contours detected: 5	Expected: 3

- Glyph name: uni1EC2	Contours detected: 5	Expected: 3

- Glyph name: uni1EC3	Contours detected: 6	Expected: 4

- Glyph name: uni1EC8	Contours detected: 4	Expected: 2

- Glyph name: uni1EC9	Contours detected: 4	Expected: 2

- Glyph name: uni1ECE	Contours detected: 5	Expected: 3

- Glyph name: uni1ECF	Contours detected: 5	Expected: 3

- Glyph name: uni1ED4	Contours detected: 6	Expected: 4

- Glyph name: uni1ED5	Contours detected: 6	Expected: 4

- Glyph name: uni1EDE	Contours detected: 5	Expected: 3 or 4

- Glyph name: uni1EDF	Contours detected: 5	Expected: 3

- Glyph name: uni1EE6	Contours detected: 4	Expected: 2

- Glyph name: uni1EE7	Contours detected: 4	Expected: 2

- Glyph name: uni1EEC	Contours detected: 4	Expected: 2

- Glyph name: uni1EED	Contours detected: 4	Expected: 2

- Glyph name: uni1EF6	Contours detected: 4	Expected: 2

- Glyph name: uni1EF7	Contours detected: 4	Expected: 2

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 8	Expected: 1

- Glyph name: uni2572	Contours detected: 8	Expected: 1

- Glyph name: uni2573	Contours detected: 13	Expected: 1

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uniFFFC	Contours detected: 25	Expected: 22

- Glyph name: uogonek	Contours detected: 2	Expected: 1

- Glyph name: w	Contours detected: 3	Expected: 1

- Glyph name: wcircumflex	Contours detected: 4	Expected: 2
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
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, cherokee, tifinagh</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: gothic, glagolitic, coptic, math, elbasan</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, coptic, malayalam, duployan, hebrew, tai-le, todhri, math, tifinagh, old-permic, syriac</li>
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
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, duployan, cherokee</li>
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
<li>U+0330 COMBINING TILDE BELOW: try adding one of: math, syriac, cherokee</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, hebrew, armenian, sundanese, arabic, kharoshthi, kaithi, cham, syloti-nagri, yi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
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
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2200 FOR ALL: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: tai-tham, symbols, yi, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25E1 LOWER HALF CIRCLE: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2765 ROTATED HEAVY BLACK HEART BULLET: try adding symbols</li>
<li>U+2919 LEFTWARDS ARROW-TAIL: try adding math</li>
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
<li>U+FF01 FULLWIDTH EXCLAMATION MARK: try adding one of: japanese, chinese-simplified, yi</li>
<li>U+FF08 FULLWIDTH LEFT PARENTHESIS: try adding one of: japanese, chinese-simplified, yi</li>
<li>U+FF09 FULLWIDTH RIGHT PARENTHESIS: try adding one of: japanese, chinese-simplified, yi</li>
<li>U+FF0F FULLWIDTH SOLIDUS: try adding one of: japanese, chinese-simplified, yi</li>
<li>U+FF3C FULLWIDTH REVERSE SOLIDUS: try adding one of: japanese, chinese-simplified</li>
<li>U+FF44 FULLWIDTH LATIN SMALL LETTER D: try adding one of: japanese, chinese-simplified</li>
<li>U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP: try adding yi</li>
<li>U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition</li>
<li>U+1F494 BROKEN HEART: not included in any glyphset definition</li>
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







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ i̍ i̓ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
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



* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1248 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 128 glyphs (10.26%) have a different width. You should check the widths of: ['exclam', 'quotedbl', 'quotesingle', 'parenleft', 'parenright', 'comma', 'period', 'colon', 'semicolon', 'M', 'W', 'underscore', 'grave', 'm', 'w', 'braceleft', 'bar', 'braceright', 'exclamdown', 'acute', 'periodcentered', 'cedilla', 'AE', 'ae', 'OE', 'oe', 'Wcircumflex', 'wcircumflex', 'uni01C0', 'uni01C1', 'uni01E2', 'uni01E3', 'AEacute', 'aeacute', 'uni02B9', 'uni0402', 'uni0409', 'uni040A', 'uni040B', 'uni0416', 'uni0424', 'uni0428', 'uni0429', 'uni042B', 'uni042E', 'uni0436', 'uni043C', 'uni0444', 'uni0448', 'uni0449', 'uni044B', 'uni044E', 'uni0452', 'uni0459', 'uni045A', 'uni045B', 'uni0496', 'uni0497', 'uni04C1', 'uni04C2', 'uni04DC', 'uni04DD', 'uni04F8', 'uni04F9', 'uni0E0C', 'uni0E0D', 'uni0E12', 'uni0E13', 'uni0E40', 'uni0E46', 'uni0E86', 'uni0E8E', 'uni0E91', 'uni0E92', 'uni0E93', 'uni0E97', 'uni0E9E', 'uni0E9F', 'uni0EA4', 'uni0EAB', 'uni0EC0', 'uni0EC6', 'uni0EDC', 'uni0EDD', 'uni1E40', 'uni1E41', 'uni2001', 'uni2003', 'uni2004', 'uni2005', 'uni2006', 'uni2008', 'uni2009', 'uni200A', 'emdash', 'uni2015', 'quoteleft', 'quoteright', 'quotesinglbase', 'quotereversed', 'quotedblleft', 'quotedblright', 'quotedblbase', 'uni201F', 'uni2605', 'uni2606', 'uni2661', 'heart', 'uni2764', 'uni2765', 'uniE133', 'uniE134', 'uniE139', 'uni0E0D.descless', 'uni0E24_uni0E45', 'uni0E26_uni0E45', 'uniFB00', 'uniFB01', 'uniFB02', 'uniFB03', 'uniFB04', 'uniFF01', 'uniFF08', 'uniFF09', 'uniFF0F', 'uniFF3C', 'uniFF44', 'u1F494']</p>
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
<tr>
<td align="left">U+FF44: FULLWIDTH LATIN SMALL LETTER D</td>
<td align="left">U+FF24: FULLWIDTH LATIN CAPITAL LETTER D</td>
</tr>
</tbody>
</table>
 [code: missing-case-counterparts]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Checking OS/2 usWinAscent & usWinDescent. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#family-win-ascent-and-descent">family/win_ascent_and_descent</a></summary>
    <div>







* 🔥 **FAIL** <p>OS/2.usWinAscent value should be equal or greater than 1024, but got 768 instead</p>
 [code: ascent]



* 🔥 **FAIL** <p>OS/2.usWinDescent value should be equal or greater than 384, but got 256 instead</p>
 [code: descent]



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
<td align="left">The following base characters are missing from the font: ẁ, ẃ, ẅ, Ẁ, Ẅ, Ẃ</td>
<td align="left">cy_Latn (Welsh)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ẞ</td>
<td align="left">de_Latn (German)</td>
</tr>
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
<td align="left">The following base characters are missing from the font: Ɲ, ɲ</td>
<td align="left">bm_Latn (Bambara)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: ɲ, Ɲ</td>
<td align="left">dyu_Latn (Dyula)</td>
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
<td align="left">The following base characters are missing from the font: Ƴ, Ƙ, ƴ, ƙ</td>
<td align="left">ha_Latn (Hausa)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ḿ, ḿ, Ṣ, ṣ</td>
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
<td align="left">The following base characters are missing from the font: ҫ, Ҫ, Ҙ, ҙ, ҡ, Ҡ</td>
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
<td align="left">kbd_Cyrl (Kabardian), av_Cyrl (Avaric), ady_Cyrl (Adyghe) and dar_Cyrl (Dargwa)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: рхӏ, тӏ, цӏ, гӏ, чӏ, хӏ, кӏ, пӏ</td>
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
<td align="left">The following base characters are missing from the font: ҥ, ҕ</td>
<td align="left">sah_Cyrl (Sakha)</td>
</tr>
<tr>
<td align="left">Mandatory orthography codepoints:</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following base characters are missing from the font: Ӏ, ӏ</td>
<td align="left">lez_Cyrl (Lezghian) and inh_Cyrl (Ingush)</td>
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
<td align="left">The following auxiliary characters are missing from the font: ẞ</td>
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
<td align="left">The following auxiliary characters are missing from the font: ẞ</td>
<td align="left">fr_Latn (French), it_Latn (Italian), pl_Latn (Polish) and tr_Latn (Turkish)</td>
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
<td align="left">The following auxiliary characters are missing from the font: ḿ</td>
<td align="left"></td>
</tr>
<tr>
<td align="left">The following auxiliary characters are missing from the font: Ḿ</td>
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
    <summary>🔥 <b>FAIL</b> Check Google Fonts glyph coverage. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-glyph-coverage">googlefonts/glyph_coverage</a></summary>
    <div>







* 🔥 **FAIL** <p>Missing required codepoints:</p>
<pre><code>- 0x1E80 (LATIN CAPITAL LETTER W WITH GRAVE)


- 0x1E81 (LATIN SMALL LETTER W WITH GRAVE)


- 0x1E82 (LATIN CAPITAL LETTER W WITH ACUTE)


- 0x1E83 (LATIN SMALL LETTER W WITH ACUTE)


- 0x1E84 (LATIN CAPITAL LETTER W WITH DIAERESIS)


- 0x1E85 (LATIN SMALL LETTER W WITH DIAERESIS)


- 0x1E9E (LATIN CAPITAL LETTER SHARP S)


- 0x2212 (MINUS SIGN)
</code></pre>
 [code: missing-codepoints]



</div>
</details>

<details>
    <summary>🔥 <b>FAIL</b> Check font follows the Google Fonts vertical metric schema <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vertical-metrics">googlefonts/vertical_metrics</a></summary>
    <div>







* 🔥 **FAIL** <p>The sum of hhea.ascender + abs(hhea.descender) + hhea.lineGap is 1024 when it should be at least 1228</p>
 [code: bad-hhea-range]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check mark characters are in GDEF mark glyph class. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-gdef-mark-chars">opentype/gdef_mark_chars</a></summary>
    <div>







* ⚠️ **WARN** <p>The following mark characters could be in the GDEF mark glyph class:
uni0334 (U+0334), uni0335 (U+0335), uni0336 (U+0336), uni0337 (U+0337), uni0338 (U+0338) and uni0358 (U+0358)</p>
 [code: mark-chars]



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

- Glyph name: uni1E40	Contours detected: 6	Expected: 2

- Glyph name: uni1E41	Contours detected: 4	Expected: 2

- Glyph name: uni1E44	Contours detected: 5	Expected: 2

- Glyph name: uni1E45	Contours detected: 4	Expected: 2

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

- Glyph name: trademark	Contours detected: 3	Expected: 2

- Glyph name: Omega	Contours detected: 5	Expected: 1

- Glyph name: universal	Contours detected: 3	Expected: 2

- Glyph name: partialdiff	Contours detected: 6	Expected: 2

- Glyph name: Delta	Contours detected: 4	Expected: 2

- Glyph name: summation	Contours detected: 8	Expected: 1

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: radical	Contours detected: 6	Expected: 1

- Glyph name: infinity	Contours detected: 8	Expected: 3

- Glyph name: integral	Contours detected: 5	Expected: 1

- Glyph name: approxequal	Contours detected: 6	Expected: 2

- Glyph name: notequal	Contours detected: 3	Expected: 1

- Glyph name: lessequal	Contours detected: 9	Expected: 2

- Glyph name: greaterequal	Contours detected: 9	Expected: 2

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 8	Expected: 1

- Glyph name: uni2572	Contours detected: 8	Expected: 1

- Glyph name: uni2573	Contours detected: 13	Expected: 1

- Glyph name: circle	Contours detected: 8	Expected: 2

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

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

- Glyph name: Wcircumflex	Contours detected: 9	Expected: 2

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

- Glyph name: aogonek	Contours detected: 7	Expected: 2

- Glyph name: approxequal	Contours detected: 6	Expected: 2

- Glyph name: aring	Contours detected: 6	Expected: 4

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

- Glyph name: circle	Contours detected: 8	Expected: 2

- Glyph name: comma	Contours detected: 2	Expected: 1

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

- Glyph name: emacron	Contours detected: 7	Expected: 3

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

- Glyph name: grave	Contours detected: 3	Expected: 1

- Glyph name: greater	Contours detected: 9	Expected: 1

- Glyph name: greaterequal	Contours detected: 9	Expected: 2

- Glyph name: guillemotleft	Contours detected: 10	Expected: 2

- Glyph name: guillemotright	Contours detected: 10	Expected: 2

- Glyph name: h	Contours detected: 3	Expected: 1

- Glyph name: hbar	Contours detected: 3	Expected: 1

- Glyph name: hcircumflex	Contours detected: 6	Expected: 2

- Glyph name: iacute	Contours detected: 3	Expected: 2

- Glyph name: ibreve	Contours detected: 4	Expected: 2

- Glyph name: icircumflex	Contours detected: 4	Expected: 2

- Glyph name: igrave	Contours detected: 3	Expected: 2

- Glyph name: ij	Contours detected: 5	Expected: 3 or 4

- Glyph name: infinity	Contours detected: 8	Expected: 3

- Glyph name: integral	Contours detected: 5	Expected: 1

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

- Glyph name: longs	Contours detected: 3	Expected: 1

- Glyph name: lslash	Contours detected: 3	Expected: 1

- Glyph name: m	Contours detected: 3	Expected: 1

- Glyph name: multiply	Contours detected: 9	Expected: 1

- Glyph name: n	Contours detected: 3	Expected: 1

- Glyph name: nacute	Contours detected: 5	Expected: 2

- Glyph name: napostrophe	Contours detected: 5	Expected: 2

- Glyph name: ncaron	Contours detected: 6	Expected: 2

- Glyph name: nine	Contours detected: 4	Expected: 1 or 2

- Glyph name: notequal	Contours detected: 3	Expected: 1

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

- Glyph name: uni1E40	Contours detected: 6	Expected: 2

- Glyph name: uni1E41	Contours detected: 4	Expected: 2

- Glyph name: uni1E44	Contours detected: 5	Expected: 2

- Glyph name: uni1E45	Contours detected: 4	Expected: 2

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

- Glyph name: uni2215	Contours detected: 5	Expected: 1

- Glyph name: uni2506	Contours detected: 4	Expected: 3

- Glyph name: uni2507	Contours detected: 4	Expected: 3

- Glyph name: uni256D	Contours detected: 4	Expected: 1

- Glyph name: uni256E	Contours detected: 4	Expected: 1

- Glyph name: uni256F	Contours detected: 3	Expected: 1

- Glyph name: uni2570	Contours detected: 3	Expected: 1

- Glyph name: uni2571	Contours detected: 8	Expected: 1

- Glyph name: uni2572	Contours detected: 8	Expected: 1

- Glyph name: uni2573	Contours detected: 13	Expected: 1

- Glyph name: uni25CC	Contours detected: 8	Expected: 16 or 12

- Glyph name: uniFFFC	Contours detected: 25	Expected: 22

- Glyph name: universal	Contours detected: 3	Expected: 2

- Glyph name: uogonek	Contours detected: 6	Expected: 1

- Glyph name: upsilon	Contours detected: 5	Expected: 1

- Glyph name: upsilondieresis	Contours detected: 7	Expected: 3

- Glyph name: upsilondieresistonos	Contours detected: 9	Expected: 4

- Glyph name: upsilontonos	Contours detected: 7	Expected: 2

- Glyph name: uring	Contours detected: 5	Expected: 3

- Glyph name: utilde	Contours detected: 6	Expected: 2

- Glyph name: v	Contours detected: 5	Expected: 1

- Glyph name: w	Contours detected: 7	Expected: 1

- Glyph name: wcircumflex	Contours detected: 10	Expected: 2

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
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* napostrophe (U+0149): L&lt;&lt;64.0,448.0&gt;--&lt;128.0,448.0&gt;&gt; has the same coordinates as a previous segment.

* uogonek (U+0173): L&lt;&lt;384.0,0.0&gt;--&lt;320.0,0.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EA2 (U+1EA2): L&lt;&lt;192.0,640.0&gt;--&lt;320.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EA4 (U+1EA4): L&lt;&lt;256.0,832.0&gt;--&lt;192.0,832.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EBE (U+1EBE): L&lt;&lt;256.0,832.0&gt;--&lt;192.0,832.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ECE (U+1ECE): L&lt;&lt;192.0,640.0&gt;--&lt;320.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ECF (U+1ECF): L&lt;&lt;192.0,448.0&gt;--&lt;320.0,448.0&gt;&gt; has the same coordinates as a previous segment.

* uni1ED0 (U+1ED0): L&lt;&lt;256.0,832.0&gt;--&lt;192.0,832.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EDE (U+1EDE): L&lt;&lt;192.0,640.0&gt;--&lt;320.0,640.0&gt;&gt; has the same coordinates as a previous segment.

* uni1EDF (U+1EDF): L&lt;&lt;192.0,448.0&gt;--&lt;320.0,448.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking that the typoAscender exceeds the yMax of the /Agrave. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#typoascender-exceeds-Agrave">typoascender_exceeds_Agrave</a></summary>
    <div>







* ⚠️ **WARN** <p>OS/2.sTypoAscender value should be greater than 832, but got 768 instead</p>
 [code: typoAscender]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>







* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- nonmarkingreturn
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
<li>U+02D8 BREVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02D9 DOT ABOVE: try adding one of: yi, canadian-aboriginal</li>
<li>U+02DB OGONEK: try adding one of: yi, canadian-aboriginal</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: math, coptic, cherokee, tifinagh</li>
<li>U+0305 COMBINING OVERLINE: try adding one of: gothic, glagolitic, coptic, math, elbasan</li>
<li>U+0306 COMBINING BREVE: try adding one of: old-permic, tifinagh</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: canadian-aboriginal, coptic, malayalam, duployan, hebrew, tai-le, todhri, math, tifinagh, old-permic, syriac</li>
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
<li>U+0324 COMBINING DIAERESIS BELOW: try adding one of: syriac, duployan, cherokee</li>
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
<li>U+0330 COMBINING TILDE BELOW: try adding one of: math, syriac, cherokee</li>
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
<li>U+2010 HYPHEN: try adding one of: coptic, sora-sompeng, lisu, hebrew, armenian, sundanese, arabic, kharoshthi, kaithi, cham, syloti-nagri, yi, kayah-li</li>
<li>U+2011 NON-BREAKING HYPHEN: try adding one of: arabic, yi, syloti-nagri</li>
<li>U+2012 FIGURE DASH: not included in any glyphset definition</li>
<li>U+2015 HORIZONTAL BAR: try adding adlam</li>
<li>U+201B SINGLE HIGH-REVERSED-9 QUOTATION MARK: try adding adlam</li>
<li>U+201F DOUBLE HIGH-REVERSED-9 QUOTATION MARK: not included in any glyphset definition</li>
<li>U+2021 DOUBLE DAGGER: try adding adlam</li>
<li>U+2030 PER MILLE SIGN: try adding adlam</li>
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
<li>U+2126 OHM SIGN: try adding math</li>
<li>U+2200 FOR ALL: try adding math</li>
<li>U+2202 PARTIAL DIFFERENTIAL: try adding math</li>
<li>U+2206 INCREMENT: try adding math</li>
<li>U+220F N-ARY PRODUCT: try adding math</li>
<li>U+2211 N-ARY SUMMATION: try adding math</li>
<li>U+2219 BULLET OPERATOR: try adding one of: tai-tham, symbols, yi, math</li>
<li>U+221A SQUARE ROOT: try adding math</li>
<li>U+221E INFINITY: try adding math</li>
<li>U+222B INTEGRAL: try adding math</li>
<li>U+2248 ALMOST EQUAL TO: try adding math</li>
<li>U+2260 NOT EQUAL TO: try adding math</li>
<li>U+2264 LESS-THAN OR EQUAL TO: try adding math</li>
<li>U+2265 GREATER-THAN OR EQUAL TO: try adding math</li>
<li>U+25A0 BLACK SQUARE: try adding symbols</li>
<li>U+25A1 WHITE SQUARE: try adding symbols</li>
<li>U+25CA LOZENGE: try adding one of: symbols, math</li>
<li>U+25CB WHITE CIRCLE: try adding symbols</li>
<li>U+25E1 LOWER HALF CIRCLE: try adding symbols</li>
<li>U+2605 BLACK STAR: try adding symbols</li>
<li>U+2606 WHITE STAR: try adding symbols</li>
<li>U+2661 WHITE HEART SUIT: try adding symbols</li>
<li>U+2665 BLACK HEART SUIT: try adding symbols</li>
<li>U+2764 HEAVY BLACK HEART: try adding symbols</li>
<li>U+2765 ROTATED HEAVY BLACK HEART BULLET: try adding symbols</li>
<li>U+2919 LEFTWARDS ARROW-TAIL: try adding math</li>
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
<li>U+FF01 FULLWIDTH EXCLAMATION MARK: try adding one of: japanese, chinese-simplified, yi</li>
<li>U+FF08 FULLWIDTH LEFT PARENTHESIS: try adding one of: japanese, chinese-simplified, yi</li>
<li>U+FF09 FULLWIDTH RIGHT PARENTHESIS: try adding one of: japanese, chinese-simplified, yi</li>
<li>U+FF0F FULLWIDTH SOLIDUS: try adding one of: japanese, chinese-simplified, yi</li>
<li>U+FF3C FULLWIDTH REVERSE SOLIDUS: try adding one of: japanese, chinese-simplified</li>
<li>U+FF44 FULLWIDTH LATIN SMALL LETTER D: try adding one of: japanese, chinese-simplified</li>
<li>U+FF61 HALFWIDTH IDEOGRAPHIC FULL STOP: try adding yi</li>
<li>U+FFFC OBJECT REPLACEMENT CHARACTER: not included in any glyphset definition</li>
<li>U+1F494 BROKEN HEART: not included in any glyphset definition</li>
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







* ⚠️ **WARN** <p>The dot of soft dotted characters used in orthographies <em>must</em> disappear in the following strings: i̊ i̋ i̍ i̓ j̀ j́ j̃ j̄ j̈ j̑ į̀ į́ į̂ į̃ į̄ į̌ ɨ̀ ɨ́ ɨ̂ ɨ̃ ɨ̄ ɨ̈ ɨ̋ ɨ̌ ɨ̏ ɨ̧̀ ɨ̧́ ɨ̧̂ ɨ̧̌ ɨ̱̀ ɨ̱́ ɨ̱̈ і́ ị̀ ị́ ị̂ ị̃ ị̄</p>
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
| 0 | 0 | 19 | 23 | 207 | 11 | 195 | 0 | 
| 0% | 0% | 4% | 5% | 45% | 2% | 43% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
