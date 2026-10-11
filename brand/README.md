# Horizon — Frontier Identity

Horizon Modular v2 is the founder-approved graphical identity for the Frontier Identity GitHub organization, selected as proposal 01 on 2026-10-11. It supersedes Horizon v1. The segmented F uses a rounded orange upper horizon, an orange accent square, a white middle segment and a white lower stem. The full wordmark is FRONTIER IDENTITY.

## Palette

| Role | Color |
| --- | --- |
| Carbon Black | `#0B0D0F` |
| Graphite | `#15191D` |
| Primary text | `#F4F5F6` |
| Secondary text | `#A8B0B7` |
| Frontier Orange | `#FF6B21` |

Orange is the primary accent. Keep presentations minimal, with generous spacing and strong contrast. The wordmark uses bold Arial with Helvetica and sans-serif fallbacks; IDENTITY is smaller and spaced beneath FRONTIER. Use the PNG banner for consistent rendering across systems.

## Light and dark themes

The profile supports two equal themes. Both use the same typography, spacing, component geometry and Horizon symbol. Choose colors by their purpose rather than mechanically inverting the palette. Use [theme.css](theme.css) as the shared reference for websites and applications. These additions were requested by the founder on 2026-10-11.

Frontier Orange remains `#FF6B21` in the brand artwork. The darker orange `#B84000` is a functional color for readable links, focus indicators and primary actions on light surfaces; it does not replace the brand orange.

| Purpose / CSS token | Light | Dark |
| --- | --- | --- |
| Page background / `--page` | `#F4F5F6` | `#0B0D0F` |
| Content surface / `--surface` | `#FFFFFF` | `#15191D` |
| Primary text / `--text` | `#0B0D0F` | `#F4F5F6` |
| Secondary text / `--muted` | `#59636D` | `#A8B0B7` |
| Links and functional accent / `--accent` | `#B84000` | `#FF6B21` |
| Primary action / `--action` | `#B84000` | `#FF6B21` |
| Primary action hover / `--action-hover` | `#9B3500` | `#FF8447` |
| Text on primary action / `--on-action` | `#FFFFFF` | `#0B0D0F` |
| Essential control border / `--border` | `#747E88` | `#747E88` |
| Decorative separator / `--separator` | `#D8DDE2` | `#394149` |
| Keyboard focus / `--focus` | `#B84000` | `#FF6B21` |
| Success / `--success` | `#176B3A` | `#70D59B` |
| Error / `--error` | `#B42318` | `#FF9A8F` |
| Waiting or warning / `--warning` | `#8A4B00` | `#FFC857` |
| Information / `--info` | `#175CD3` | `#8DB8FF` |

### Color and interaction rules

- Ordinary text uses a contrast ratio of at least 4.5:1. Essential control boundaries and visual indicators use at least 3:1 against their adjacent background. These reference tokens meet those thresholds on the specified page and surface colors; every real composition still needs verification.
- Original orange on white is only 2.85:1. Use it for brand artwork or decoration, not ordinary text or an essential control indicator. Light text on original orange is also insufficient; use the primary-action foreground/background pair from the table.
- Decorative separators and subtle surface differences do not identify controls. Use `--border` when the boundary is necessary to understand or operate a control.
- Links are underlined. Status combines a written label with color and, where useful, a symbol. Color alone does not carry the meaning.
- Focus uses a visible 3px outline with a 4px offset. Check its contrast and visibility in the actual layout, including dialogs and scroll containers. The supplied offset separates the outline from a colored button.
- Preserve readable disabled labels. The reference uses a dashed border and an actual disabled control rather than fading the whole component.
- Keep identical component sizes and placement when switching themes. No gradients, glows, shadows or additional logo embellishments.

Reference criteria: [text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html), [non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html) and [use of color](https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html). This profile is not a claim of whole-product WCAG conformance.

### Theme selection

For future websites and services, offer **System / Light / Dark**. Default to the system preference and remember an explicit user choice. In `theme.css`, an absent root `data-theme` follows the system; `data-theme="light"` or `data-theme="dark"` selects the explicit theme. Initialize a saved choice before painting the page. If storage is unavailable, theme selection should still work for the current page.

Use `color-scheme` for matching native browser controls and `prefers-color-scheme` for the system preference. High-contrast/forced-color modes need their own verification. See [W3C CSS Color Adjustment](https://www.w3.org/TR/css-color-adjust-1/).

### Shared component examples

[Open the example source](examples/index.html) in a browser from the local checkout or serve the brand directory with a static web server. It contains both themes side by side, buttons, disabled states, labeled inputs, help/error text, written status indicators, view selection and a table. The top selector changes the surrounding page. Demo actions never send information.

The example content is static HTML, so it remains available without JavaScript. JavaScript adds persisted theme selection and demonstration feedback. The layout switches to one column below 760px.

Static visual references: [light surrounding page](examples/preview-light.png) and [dark surrounding page](examples/preview-dark.png). These are offline document renders, not browser screenshots. See [verification scope and results](VERIFICATION.md).

## Assets

- [Avatar PNG](assets/avatar.png) — 512 × 512; symbol only.
- [Avatar SVG](assets/avatar.svg) — editable square original.
- [Banner PNG](assets/banner.png) — 1600 × 420; organization and repository README headers.
- [Banner SVG](assets/banner.svg) — editable original.
- [Social preview PNG](assets/social-preview.png) and [SVG](assets/social-preview.svg) — 1280 × 640; repository sharing cards.
- [Color symbol](assets/symbol-color.svg), [black symbol](assets/symbol-black.svg), [white symbol](assets/symbol-white.svg) — transparent originals with identical geometry.
- [Color symbol for light surfaces](assets/symbol-light.svg) and [PNG](assets/symbol-light.png) — original orange with Carbon Black segments.

### Complete transparent wordmarks

| Variant | SVG | PNG | Intended background |
| --- | --- | --- | --- |
| Color, dark | [SVG](assets/wordmark-dark.svg) | [PNG](assets/wordmark-dark.png) | Carbon Black or Graphite |
| Color, light | [SVG](assets/wordmark-light.svg) | [PNG](assets/wordmark-light.png) | White or the light page color |
| Black monochrome | [SVG](assets/wordmark-black.svg) | [PNG](assets/wordmark-black.png) | Light |
| White monochrome | [SVG](assets/wordmark-white.svg) | [PNG](assets/wordmark-white.png) | Dark |

All variants preserve the original four symbol components, wordmark positions and letter spacing. SVG artwork uses Arial/Helvetica fallbacks; use PNG where consistent font rendering is required. Do not recolor a logo with CSS inversion filters. Use the designated variant. Logo text has a contrast exception, but surrounding functional text does not.

Regenerate the additions with `python3 brand/build-theme-assets.py` from the repository root (ImageMagick and Arial Bold required). The original avatar, banner and social preview remain the canonical fixed-background GitHub assets.

Keep proportions and colors intact. Preserve the padding in the avatar for circular crops. Do not add glow, gradients, shadows, shields or locks. Use black or white monochrome symbols where color is unsuitable.

## Repository presentation

Start each repository README with the approved banner, followed by a descriptive repository heading and its actual purpose. The [README template](repository-readme-template.md) provides the pattern. Use a local copy of the banner for private repositories and offline documentation.

Use the organization avatar wherever GitHub uses the organization identity. GitHub's navigation and application theme remain controlled by GitHub and individual users; the identity applies to editable organization and repository surfaces.

Keep ordinary documentation simple and readable in light and dark modes. There is no need to repeat a large logo on every internal page. Future imagery and presentations should follow this palette and geometric style.

## Current version

Use only the Modular v2 geometry in the shared assets. Preserve the four separate components and rounded terminals. Do not substitute another F or the initials FI. The color and monochrome versions have identical geometry. [Preview and size checks](assets/preview.png).
