"""Cloud-only renderer. No paid service, no credentials, no shell interpolation."""
import argparse
import hashlib
import json
import math
import pathlib
import shutil
import subprocess
import textwrap
import time
import urllib.parse
import urllib.request
import wave
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'build'
FONT = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
BOLD = '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf'
BG, INK, GOLD, MUTED = '#101b21', '#f1e9d8', '#e9b66c', '#b9bcae'

def run(*args):
    subprocess.run([str(a) for a in args], check=True, timeout=1800)

def request(url):
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={'User-Agent':'HISTORIA-documentary/1.0 (license-audited educational pilot)'})
            with urllib.request.urlopen(req, timeout=60) as response:
                return response.read()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(3 * (attempt + 1))

def photo():
    """Resolve current original via Commons API, then require audited hash/license."""
    asset = json.loads((ROOT/'media.json').read_text(encoding='utf-8'))[0]
    query = urllib.parse.urlencode({'action':'query','format':'json','prop':'imageinfo','iiprop':'url|sha1|extmetadata','titles':asset['title']})
    raw = request('https://commons.wikimedia.org/w/api.php?'+query)
    (OUT/'commons-metadata.json').write_bytes(raw)
    pages = json.loads(raw)['query']['pages']
    info = next(iter(pages.values()))['imageinfo'][0]
    metadata = info['extmetadata']
    license_name = metadata.get('LicenseShortName',{}).get('value','')
    if license_name != 'CC0' and not license_name.startswith('CC0 '):
        raise RuntimeError('Media license changed; human review required. No silent substitute.')
    url = info['url']
    if urllib.parse.urlparse(url).hostname != 'upload.wikimedia.org':
        raise RuntimeError('Unexpected media host')
    data = request(url)
    if hashlib.sha1(data).hexdigest() != asset['sha1']:
        raise RuntimeError('Media hash changed; human review required.')
    path = OUT/'photo.jpg'
    path.write_bytes(data)
    return path

def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else FONT, size)

def write(draw, xy, text, size=30, color=INK, width=60, bold=False):
    draw.multiline_text(xy, textwrap.fill(text,width), font=font(size,bold), fill=color, spacing=12)

def card(scene, lang, photo_path):
    im = Image.new('RGB',(1280,720),BG)
    d = ImageDraw.Draw(im)
    write(d,(55,28),'HISTORIA  /  '+scene['id'],22,GOLD)
    write(d,(55,76),scene['heading'][lang],42,INK,47,True)
    visual = scene['visual']
    fr = lang == 'fr'
    label = 'SCHÉMA PÉDAGOGIQUE · NON À L’ÉCHELLE' if fr else 'EDUCATIONAL DIAGRAM · NOT TO SCALE'
    if visual == 'photo':
        p = Image.open(photo_path).convert('RGB')
        p.thumbnail((670,440))
        im.paste(p,((750-p.width)//2,177+(440-p.height)//2))
        write(d,(770,205),'Portique d’Eumachia' if fr else 'Eumachia portico',28,GOLD,25)
        write(d,(770,300),'Vue de 2015 ; campanile moderne visible.' if fr else '2015 view; modern bell tower visible.',24,INK,27)
        write(d,(770,440),'Jebulon · CC0 1.0',22,MUTED,26)
        label = 'PHOTOGRAPHIE MODERNE · 24/07/2015' if fr else 'MODERN PHOTOGRAPH · 24 JUL 2015'
    elif visual in ('volcano','fall','current'):
        d.ellipse((750,160,940,350),fill=GOLD)
        d.polygon([(70,570),(420,310),(470,325),(510,300),(860,570)],fill='#56706c')
        d.rectangle((55,570,1225,576),fill=GOLD)
        if visual in ('fall','volcano'):
            for i in range(6):
                d.ellipse((350-i*34,180-i*12,590+i*34,265-i*4),fill='#64716c')
            d.line((480,300,480,240),fill=MUTED,width=15)
            for i in range(15):
                x=680+i*32;y=300+(i%5)*44
                d.line((x,y,x-10,y+26),fill=GOLD,width=4)
        if visual == 'current':
            d.polygon([(500,350),(700,480),(1140,525),(1180,565),(780,565),(620,480)],fill='#a26c4e')
        write(d,(70,600),('Retombées volcaniques' if fr else 'Volcanic fallout') if visual!='current' else ('Gaz + particules près du sol' if fr else 'Gases + particles near the ground'),27,GOLD,65)
    elif visual == 'cast':
        labels = ['Corps enfoui','Cavité','Moulage'] if fr else ['Buried body','Cavity','Cast']
        for i,t in enumerate(labels):
            x=70+i*400
            d.rounded_rectangle((x,230,x+340,490),radius=20,fill='#6d6252')
            d.ellipse((x+45,325,x+290,405),fill=[BG,BG,INK][i])
            write(d,(x,530),t,29,GOLD,22)
        write(d,(55,615),'Fiorelli · 1863',24,MUTED)
    elif visual == 'date':
        for x,t,sub in [(70,'24 / 08','Tradition'),(660,'17 / 10','Indice au charbon' if fr else 'Charcoal clue')]:
            d.rounded_rectangle((x,230,x+540,490),radius=15,outline=GOLD,width=2)
            write(d,(x+55,270),t,65,GOLD)
            write(d,(x+55,400),sub,27,INK,28)
        write(d,(70,550),'Année 79 établie. Jour exact discuté.' if fr else 'Year 79 established. Exact day debated.',30,INK,65)
    elif visual == 'timeline':
        d.line((100,360,1180,360),fill=GOLD,width=4)
        items=[('79','Éruption' if fr else 'Eruption'),('Après / After','Retours' if fr else 'Returns'),('1748','Fouilles' if fr else 'Excavations')]
        for x,(t,sub) in zip((110,500,960),items):
            d.ellipse((x,350,x+20,370),fill=GOLD)
            write(d,(x-10,270),t,29,GOLD,22)
            write(d,(x-10,410),sub,25,INK,20)
    else:
        write(d,(70,240),'OBSERVER\nCOMPARER\nRÉVISER' if fr else 'OBSERVE\nCOMPARE\nREVISE',58,GOLD,25,True)
        write(d,(730,300),'Références et crédits dans la description.' if fr else 'References and credits in the description.',29,INK,25)
        label = 'HISTORIA · FIN / END'
    write(d,(55,670),label,17,MUTED,90)
    write(d,(850,670),' / '.join(scene['sources']),17,MUTED,40)
    return im

def timestamp(t, sep=','):
    ms = round(t*1000)
    h,ms=divmod(ms,3600000);m,ms=divmod(ms,60000);s,ms=divmod(ms,1000)
    return f'{h:02}:{m:02}:{s:02}{sep}{ms:03}'

def render(lang, episode, photo_path, smoke):
    folder=OUT/lang;folder.mkdir(parents=True,exist_ok=True)
    scenes=episode['scenes'][:1] if smoke else episode['scenes']
    timeline=[];srt=[];offset=0;cue=1
    for scene in scenes:
        stem=folder/scene['id']
        text=stem.with_suffix('.txt');text.write_text(scene[lang],encoding='utf-8')
        wav=stem.with_suffix('.wav')
        run('espeak-ng','-v','fr-fr' if lang=='fr' else 'en-us','-s','145','-w',wav,'-f',text)
        with wave.open(str(wav)) as audio:
            length=audio.getnframes()/audio.getframerate()
        length=math.ceil((length+0.8)*25)/25
        png=stem.with_suffix('.png');card(scene,lang,photo_path).save(png)
        # Letterboxed photo and diagrams; restrained push-in preserves all edges.
        frames=round(length*25)
        vf=f"scale=1280:720,zoompan=z='min(zoom+0.000015,1.015)':x='iw/2-iw/zoom/2':y='ih/2-ih/zoom/2':d={frames}:s=1280x720:fps=25,format=yuv420p"
        if smoke:length=min(length,8);vf='scale=1280:720,format=yuv420p'
        clip=stem.with_suffix('.mp4')
        run('ffmpeg','-hide_banner','-loglevel','error','-y','-loop','1','-framerate','25','-i',png,'-i',wav,'-vf',vf,'-af','apad,loudnorm=I=-16:TP=-1.5:LRA=11','-t',f'{length:.2f}','-c:v','libx264','-preset','veryfast','-crf','24','-threads','2','-c:a','aac','-b:a','128k','-ar','48000','-ac','2','-pix_fmt','yuv420p',clip)
        # Proportional captions: not forced alignment; human timing check required.
        chunks=textwrap.wrap(scene[lang],width=76,break_long_words=False)
        total=sum(len(c) for c in chunks);t=offset
        for chunk in chunks:
            end=t+length*len(chunk)/total
            srt.append(f'{cue}\n{timestamp(t)} --> {timestamp(end)}\n'+textwrap.fill(chunk,38)+'\n')
            cue+=1;t=end
        timeline.append({'scene':scene['id'],'start':round(offset,2),'duration':length,'sources':scene['sources'],'heading':scene['heading'][lang]})
        offset+=length
    concat=folder/'concat.txt';concat.write_text('\n'.join(f"file '{s['id']}.mp4'" for s in scenes),encoding='utf-8')
    final=folder/('SMOKE-NOT-FULL-EPISODE.mp4' if smoke else 'historia-pompeii.mp4')
    run('ffmpeg','-hide_banner','-loglevel','error','-y','-f','concat','-safe','1','-i',concat,'-c','copy','-movflags','+faststart',final)
    run('ffmpeg','-hide_banner','-loglevel','error','-y','-i',final,'-vn','-c:a','pcm_s16le',folder/'voice.wav')
    (folder/'captions.srt').write_text('\n'.join(srt),encoding='utf-8')
    (folder/'timeline.json').write_text(json.dumps(timeline,ensure_ascii=False,indent=2),encoding='utf-8')
    probe=json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(final)]))
    video=next(s for s in probe['streams'] if s['codec_type']=='video')
    assert video['width']==1280 and video['height']==720
    assert any(s['codec_type']=='audio' for s in probe['streams'])
    assert abs(float(probe['format']['duration'])-offset)<2
    # Actual decode test catches truncated files, beyond container inspection.
    run('ffmpeg','-hide_banner','-loglevel','error','-xerror','-i',final,'-f','null','-')
    (folder/'probe.json').write_text(json.dumps(probe,indent=2),encoding='utf-8')
    thumb=Image.new('RGB',(1280,720),BG);d=ImageDraw.Draw(thumb)
    d.ellipse((880,100,1130,350),fill=GOLD)
    d.polygon([(650,600),(930,270),(980,300),(1020,285),(1270,600)],fill='#56706c')
    write(d,(65,50),'HISTORIA / 001',25,GOLD)
    write(d,(65,205),'POMPÉI' if lang=='fr' else 'POMPEII',95,INK,12,True)
    write(d,(65,350),'LES CENDRES\nONT DES INDICES' if lang=='fr' else 'CLUES IN\nTHE ASHES',43,GOLD,22,True)
    write(d,(65,650),'ILLUSTRATION SYMBOLIQUE' if lang=='fr' else 'SYMBOLIC ILLUSTRATION',18,MUTED)
    thumb.save(folder/'thumbnail.jpg',quality=93)
    refs=json.loads((ROOT/'sources.json').read_text(encoding='utf-8'))
    desc=(episode['title'][lang]+'\n\n'+('Une enquête documentaire originale sur les retombées, les moulages et la date discutée de la catastrophe. Voix de synthèse eSpeak NG. Schémas pédagogiques, aucune reconstitution présentée comme une archive antique.\n\nCHAPITRES\n' if lang=='fr' else 'An original documentary investigation of volcanic deposits, casts and the disputed date. Synthetic eSpeak NG narration. Educational diagrams, no reconstruction presented as an ancient record.\n\nCHAPTERS\n'))
    for entry in timeline:
        t=int(entry['start']);desc+=f"{t//60:02}:{t%60:02} {entry['heading']}\n"
    desc+='\nSOURCES\n'+'\n'.join(f"{r['id']} — {r['title']}\n{r['url']}" for r in refs)
    desc+='\n\nMEDIA\nJebulon — Church forum Pompeii.jpg (2015), CC0 1.0\nhttps://commons.wikimedia.org/wiki/File:Church_forum_Pompeii.jpg\nhttps://creativecommons.org/publicdomain/zero/1.0/\nScaled; caption added. Original educational graphics: HISTORIA, CC0 1.0. No third-party music.\n#Pompeii #History #HISTORIA\n'
    (folder/'description.txt').write_text(desc,encoding='utf-8')
    # Keep deliverables and evidence, discard per-scene intermediate encodes.
    for pattern in ('[0-9][0-9].mp4','[0-9][0-9].wav'):
        for p in folder.glob(pattern):p.unlink()
    return {'language':lang,'duration_seconds':offset,'file':str(final.relative_to(OUT)),'decode_test':'passed','caption_timing':'proportional, not forced-aligned'}

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--lang',choices=['fr','en','both'],default='both');parser.add_argument('--smoke',action='store_true');args=parser.parse_args()
    OUT.mkdir(exist_ok=True)
    episode=json.loads((ROOT/'episode.json').read_text(encoding='utf-8'))
    path=photo()
    report={'mode':'smoke' if args.smoke else 'full','outputs':[]}
    for lang in (['fr','en'] if args.lang=='both' else [args.lang]):report['outputs'].append(render(lang,episode,path,args.smoke))
    for name in ['sources.json','media.json','episode.json']:shutil.copy(ROOT/name,OUT/name)
    for name in ['DROITS.md','RECHERCHE.md']:shutil.copy(ROOT/'docs'/name,OUT/name)
    (OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    # Hard artifact bound, below shared 500 MB free storage; no upload if exceeded.
    total=sum(p.stat().st_size for p in OUT.rglob('*') if p.is_file())
    if total>240*1024*1024:raise RuntimeError('Artifact >240 MiB; lower duration/bitrate before upload')
    print(json.dumps(report,ensure_ascii=False))

if __name__=='__main__':main()
