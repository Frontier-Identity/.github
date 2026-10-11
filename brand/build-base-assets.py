"""Build the selected Horizon Modular v2 base artwork in this repository only."""
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont
OUT=Path(__file__).resolve().parent/'assets'
BLACK,WHITE,ORANGE='#0B0D0F','#F4F5F6','#FF6B21'
FONT='/System/Library/Fonts/Supplemental/Arial Bold.ttf'
def symbol(a=ORANGE,b=WHITE):
 return f'<path fill="{a}" d="M112 180Q112 116 176 116H400Q400 180 336 180ZM112 216h56v56h-56z"/><path fill="{b}" d="M192 216H324V228Q324 272 280 272H192ZM112 312H168V352Q168 408 112 408Z"/>'
def svg(name,w,h,body):
 p=OUT/f'{name}.svg';p.write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="Frontier Identity — Horizon Modular">{body}</svg>\n');return p
for name,a,b in [('symbol-color',ORANGE,WHITE),('symbol-black','#000000','#000000'),('symbol-white','#FFFFFF','#FFFFFF')]:svg(name,512,512,symbol(a,b))
svg('avatar',512,512,f'<path fill="{BLACK}" d="M0 0h512v512H0z"/>'+symbol())
identity_font=ImageFont.truetype(FONT,64)
x=440;letters=[]
for ch in 'IDENTITY':
 letters.append(f'<text x="{x:.2f}" y="293" font-size="64" fill="{ORANGE}">{ch}</text>');x+=identity_font.getlength(ch)+11
wordmark=f'<g font-family="Arial, Helvetica, sans-serif" font-weight="700"><text x="440" y="195" font-size="88" fill="{WHITE}">FRONTIER</text>'+''.join(letters)+'</g>' 
bannerbody=f'<path fill="{BLACK}" d="M0 0h1600v420H0z"/><g transform="translate(32 30) scale(.7)">{symbol()}</g>'+wordmark
svg('banner',1600,420,bannerbody)
svg('social-preview',1280,640,f'<path fill="{BLACK}" d="M0 0h1280v640H0z"/><g transform="translate(0 152) scale(.8)">{bannerbody}</g>')
for p in [OUT/(name+'.svg') for name in ['symbol-color','symbol-black','symbol-white','avatar','banner','social-preview']]:subprocess.run(['magick','-background','none','-font',FONT,str(p),str(p.with_suffix('.png'))],check=True)
sheet=Image.new('RGB',(1600,1020),BLACK);sheet.paste(Image.open(OUT/'banner.png').convert('RGB'),(0,0));d=ImageDraw.Draw(sheet);font=ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial.ttf',24);bold=ImageFont.truetype(FONT,30)
d.text((64,455),'Horizon Modular · valt förslag 01',fill=WHITE,font=bold)
icon=Image.open(OUT/'avatar.png').convert('RGB');sheet.paste(icon.resize((220,220),Image.Resampling.LANCZOS),(64,525));mask=Image.new('L',(220,220),0);ImageDraw.Draw(mask).ellipse((0,0,219,219),fill=255);sheet.paste(icon.resize((220,220),Image.Resampling.LANCZOS),(330,525),mask)
d.text((625,480),'Ikonstorlekar',fill=WHITE,font=font)
for size,x in [(64,625),(32,745),(24,845),(16,935)]:
 sheet.paste(icon.resize((size,size),Image.Resampling.LANCZOS),(x,550));d.text((x,650),str(size)+' px',fill='#A8B0B7',font=font)
white=Image.open(OUT/'symbol-white.png').convert('RGBA').resize((170,170),Image.Resampling.LANCZOS);sheet.paste(white,(1100,515),white)
patch=Image.new('RGB',(170,170),WHITE);im=Image.open(OUT/'symbol-black.png').convert('RGBA').resize((170,170),Image.Resampling.LANCZOS);patch.paste(im,(0,0),im);sheet.paste(patch,(1320,515))
d.text((64,830),'Rundad horisont · orange accentkvadrat · separata ljusa segment',font=font,fill='#A8B0B7')
d.text((64,890),'Samma geometri i färg, svart och vitt. Fullständigt ordmärke.',font=font,fill='#A8B0B7');sheet.save(OUT/'preview.png')
print(OUT)
