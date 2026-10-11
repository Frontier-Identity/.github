"""Extend the canonical Horizon geometry. Requires ImageMagick and Arial Bold."""
from pathlib import Path
import subprocess
import xml.etree.ElementTree as ET

ASSETS = Path(__file__).resolve().parent / 'assets'
ET.register_namespace('', 'http://www.w3.org/2000/svg')
original = ET.fromstring((ASSETS / 'banner.svg').read_text())
font = '/System/Library/Fonts/Supplemental/Arial Bold.ttf'
for name, ink, accent in [
    ('wordmark-dark', '#F4F5F6', '#FF6B21'),
    ('wordmark-light', '#0B0D0F', '#FF6B21'),
    ('wordmark-black', '#000000', '#000000'),
    ('wordmark-white', '#FFFFFF', '#FFFFFF'),
]:
    svg = ET.fromstring(ET.tostring(original))
    svg.remove(list(svg)[0])  # Transparent artwork, no fixed banner background.
    svg.set('viewBox', '80 80 880 270')
    svg.set('width', '880')
    svg.set('height', '270')
    for node in svg.iter():
        if node.get('fill') == '#F4F5F6':
            node.set('fill', ink)
        elif node.get('fill') == '#FF6B21':
            node.set('fill', accent)
    dest = ASSETS / (name + '.svg')
    ET.ElementTree(svg).write(dest, encoding='unicode', xml_declaration=False)
    subprocess.run(['magick', '-background', 'none', '-font', font,
                    str(dest), str(dest.with_suffix('.png'))], check=True)
dest = ASSETS / 'symbol-light.svg'
dest.write_text((ASSETS / 'symbol-color.svg').read_text().replace('#F4F5F6', '#0B0D0F'))
subprocess.run(['magick', '-background', 'none', str(dest),
                str(dest.with_suffix('.png'))], check=True)
