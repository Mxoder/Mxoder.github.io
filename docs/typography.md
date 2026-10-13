# Typography

The existing academic layout and colors are preserved.

- Home and section pages: Inter for Latin text, with the existing system sans-serif
  stack for Chinese. The base size is 16 px, increasing to 17 px at the 925 px
  desktop breakpoint; body line height is 1.65.
- Article body (`.blog-article`): Source Serif 4 for Latin text and Source Han Serif
  SC for Chinese. The size is 18 px (17 px below 768 px), line height is 1.75, and
  maximum reading width is 42 rem. Headings, dates and navigation remain sans-serif.
- Code: JetBrains Mono, with code ligatures disabled for literal code display.

All webfonts are hosted under `assets/fonts/`, use `font-display: swap`, and retain
their SIL Open Font License files. Inter's normal face is preloaded. Browsers only
download a face when it is used; article-only fonts are declared in a separate
stylesheet loaded by the post layout.

Source Han Serif uses the Simplified Chinese region subset from Adobe's official
release. It is split into Unicode blocks for on-demand loading and retains its
variable weight axis. The modified blocks use the internal family name
`Homepage CJK Serif` to respect the license's reserved font names; their CSS alias
is `Source Han Serif SC`. System serif fonts cover glyphs outside the source font.

## Sources

- Inter: https://cdn.jsdelivr.net/npm/@fontsource-variable/inter/
- Source Serif 4: https://cdn.jsdelivr.net/npm/@fontsource-variable/source-serif-4/
- JetBrains Mono: https://cdn.jsdelivr.net/npm/@fontsource-variable/jetbrains-mono/
- Source Han Serif:
  https://github.com/adobe-fonts/source-han-serif/tree/release/Variable/WOFF2/TTF/Subset

Normal and italic Latin faces are included. Chinese blocks are normal faces;
italic emphasis uses the browser's synthetic italic rendering where necessary.
