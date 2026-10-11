# Theme and asset verification

Date: 2026-10-11. Scope: shared Horizon theme extension and component examples.

## Completed

- Forty actual token pairs checked against unrounded WCAG relative-luminance calculations: text and action-label pairs at least 4.5:1; essential borders/focus against the reference backgrounds at least 3:1.
- System-dark and explicit-dark color definitions match. Explicit light/dark examples use their own tokens independently of the surrounding theme.
- Symbol path geometry, wordmark coordinates, font sizes and letter spacing match the canonical banner. All four transparent wordmarks and the light-surface symbol have SVG and PNG variants.
- Initial visual review found clipped wordmark text. The export viewport was widened, all variants regenerated and the final complete wordmarks visually checked.
- Local asset/style/script references, JavaScript syntax and HTML IDs checked. Inputs have associated labels and linked error/help descriptions.
- DOM execution checked theme selection, stored preference, demo button feedback and selected-view updates in both examples. These checks used jsdom, not a browser engine.
- Offline HTML/CSS document rendering reviewed for light and dark surrounding pages, at desktop width and with the production mobile layout rules applied. The examples remain present without JavaScript.

Run `python3 brand/verify-theme.py` from the repository root to repeat the contrast, geometry and local-reference checks. Run `node --check brand/examples/examples.js` to repeat the syntax check.

## Limits

The browser security policy rejected local `file:` navigation. No live-browser screenshot, native keyboard traversal, operating-system preference transition or forced-colors test was completed. The document renderer does not implement `prefers-color-scheme`, viewport media queries or input placeholders. For offline visual QA, themes were explicit and the same mobile layout declarations were applied at the narrow reference width. The stored PNG references show desktop document rendering and do not certify browser behavior.

The profile is acceptable as a checked reference for theme colors, logo assets and component styling. Before adopting it in a real website or application, verify native controls, keyboard focus, system-mode changes, responsive layout and forced-colors behavior in supported browsers. Product accessibility requires that broader verification.
