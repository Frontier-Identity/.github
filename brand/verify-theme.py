"""Check actual theme token pairs, canonical SVG geometry and local references."""
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parent
css = (ROOT / 'theme.css').read_text()
def tokens(block):
    return dict(re.findall(r'--([\w-]+):\s*(#[0-9A-Fa-f]{6})\s*;', block))
light = tokens(re.search(r':root, \[data-theme="light"\] \{([^}]+)', css).group(1))
dark = tokens(re.search(r'^\[data-theme="dark"\] \{([^}]+)', css, re.M).group(1))
system_dark = tokens(re.search(r':root:not\(\[data-theme="light"\]\) \{([^}]+)', css).group(1))
assert dark == system_dark, 'System dark and explicit dark must match'
def luminance(hex_color):
    values = [int(hex_color[i:i+2], 16)/255 for i in (1, 3, 5)]
    values = [v/12.92 if v <= .04045 else ((v+.055)/1.055)**2.4 for v in values]
    return sum(v*w for v, w in zip(values, [.2126, .7152, .0722]))
def contrast(a, b):
    lo, hi = sorted([luminance(a), luminance(b)])
    return (hi+.05)/(lo+.05)
results = []
for name, palette in [('light', light), ('dark', dark)]:
    for foreground in ['text', 'muted', 'accent', 'success', 'error', 'warning', 'info']:
        for background in ['page', 'surface']:
            value = contrast(palette[foreground], palette[background])
            assert value >= 4.5, (name, foreground, background, value)
            results.append([name, foreground, background, round(value, 3), 4.5])
    for background in ['action', 'action-hover']:
        value = contrast(palette['on-action'], palette[background])
        assert value >= 4.5, (name, background, value)
        results.append([name, 'on-action', background, round(value, 3), 4.5])
    for foreground in ['border', 'focus']:
        for background in ['page', 'surface']:
            value = contrast(palette[foreground], palette[background])
            assert value >= 3, (name, foreground, background, value)
            results.append([name, foreground, background, round(value, 3), 3])

ns = {'s': 'http://www.w3.org/2000/svg'}
canonical = ET.parse(ROOT/'assets/banner.svg').getroot()
symbol_paths = [p.get('d') for p in canonical.findall('.//s:g/s:path', ns)]
canonical_text = [(t.text, t.get('x'), t.get('y'), t.get('font-size')) for t in canonical.findall('.//s:text', ns)]
for name in ['wordmark-dark', 'wordmark-light', 'wordmark-black', 'wordmark-white']:
    svg = ET.parse(ROOT/f'assets/{name}.svg').getroot()
    assert [p.get('d') for p in svg.findall('.//s:path', ns)] == symbol_paths
    assert [(t.text, t.get('x'), t.get('y'), t.get('font-size')) for t in svg.findall('.//s:text', ns)] == canonical_text
    assert svg.get('viewBox') == '80 80 880 270'
    assert (ROOT/f'assets/{name}.png').read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
assert [p.get('d') for p in ET.parse(ROOT/'assets/symbol-light.svg').getroot().findall('s:path', ns)] == symbol_paths
html = (ROOT/'examples/index.html').read_text()
for reference in re.findall(r'(?:src|href)="([^"]+)"', html):
    if reference.startswith('#') or '://' in reference:
        continue
    assert (ROOT/'examples'/reference).exists(), reference
assert 'aria-invalid="true"' in html and html.count('data-theme="light"') >= 2
assert html.count('data-theme="dark"') >= 2
print(json.dumps({'contrast_pairs': results, 'svg_geometry': 'unchanged', 'local_references': 'valid'}, indent=2))
