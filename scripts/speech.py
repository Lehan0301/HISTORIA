"""CPU speech on the cloud runner; caption boundaries measured from PCM samples."""
import hashlib
import io
import json
import pathlib
import re
import textwrap
import urllib.request
import wave
from piper import PiperVoice

REVISIONS = {'fr': '54a80f14a817799d43a63e33d8bfbb848fcc2caf', 'en': '9f967d15e9ccdf43078586d1476ee70f314401bd'}
VOICES = {'fr': ('fr/fr_FR/tom/medium', 'fr_FR-tom-medium'),
          'en': ('en/en_US/ljspeech/high', 'en_US-ljspeech-high')}

def load_voice(lang, evidence):
    directory, name = VOICES[lang]
    revision = REVISIONS[lang]
    cache = pathlib.Path('.voices'); cache.mkdir(exist_ok=True)
    records = []
    for suffix in ('.onnx', '.onnx.json', '/MODEL_CARD'):
        filename = 'MODEL_CARD' if suffix.startswith('/') else name + suffix
        url = f'https://huggingface.co/rhasspy/piper-voices/resolve/{revision}/{directory}/{filename}'
        with urllib.request.urlopen(url, timeout=180) as response:
            data = response.read()
        target = cache / (name + '-MODEL_CARD' if filename == 'MODEL_CARD' else filename)
        target.write_bytes(data)
        records.append({'url': url, 'sha256': hashlib.sha256(data).hexdigest()})
        if filename == 'MODEL_CARD':
            (evidence / (name + '-MODEL_CARD.txt')).write_bytes(data)
    (evidence / ('voice-model-' + lang + '.json')).write_text(json.dumps(records, indent=2))
    return PiperVoice.load(str(cache / (name + '.onnx')))

def chunks(text):
    # Preserve the complete script, prefer punctuation, then at most two short lines.
    for sentence in re.split(r'(?<=[.!?;:])\s+', text.strip()):
        yield from textwrap.wrap(sentence, width=76, break_long_words=False, break_on_hyphens=False)

def synthesize(voice, text, output):
    cues = []; frame_count = 0; fmt = None
    with wave.open(str(output), 'wb') as result:
        for chunk in chunks(text):
            buffer = io.BytesIO()
            with wave.open(buffer, 'wb') as wav:
                voice.synthesize_wav(chunk, wav)
            buffer.seek(0)
            with wave.open(buffer, 'rb') as wav:
                current = (wav.getnchannels(), wav.getsampwidth(), wav.getframerate())
                if fmt is None:
                    fmt = current
                    result.setnchannels(fmt[0]); result.setsampwidth(fmt[1]); result.setframerate(fmt[2])
                assert current == fmt
                frames = wav.getnframes()
                cues.append((frame_count / fmt[2], (frame_count + frames) / fmt[2], chunk))
                result.writeframes(wav.readframes(frames))
                frame_count += frames
                pause = round(fmt[2] * 0.12)
                result.writeframes(b'\0' * pause * fmt[0] * fmt[1])
                frame_count += pause
    assert ' '.join(c[2] for c in cues) == ' '.join(text.split())
    return cues
