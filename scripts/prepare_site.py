"""Run in cloud only: prepare static PWA, icons and human-readable scripts."""
import json
import pathlib
import shutil
from PIL import Image, ImageDraw
root=pathlib.Path(__file__).resolve().parents[1]
for name in ('episode.json','sources.json'):shutil.copy(root/name,root/'site'/name)
for size in (192,512):
    im=Image.new('RGB',(size,size),'#101b21');d=ImageDraw.Draw(im)
    d.rectangle((size*.24,size*.18,size*.35,size*.82),fill='#e9b66c')
    d.rectangle((size*.65,size*.18,size*.76,size*.82),fill='#e9b66c')
    d.rectangle((size*.3,size*.44,size*.7,size*.56),fill='#e9b66c')
    im.save(root/'site'/f'icon-{size}.png')
episode=json.loads((root/'episode.json').read_text(encoding='utf-8'))
for lang in ('fr','en'):
    (root/'docs'/f'SCRIPT-{lang.upper()}.md').write_text('# '+episode['title'][lang]+'\n\n'+'\n\n'.join('## '+s['id']+' — '+s['heading'][lang]+'\n\n'+s[lang]+'\n\nSources : '+', '.join(s['sources']) for s in episode['scenes']),encoding='utf-8')
