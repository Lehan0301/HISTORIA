"""Cloud preflight; meaningful data, syntax and offline asset checks."""
import ast
import json
import pathlib
import unittest
import yaml

ROOT=pathlib.Path(__file__).resolve().parents[1]
class ProjectTests(unittest.TestCase):
    def test_episode_integrity(self):
        e=json.loads((ROOT/'episode.json').read_text(encoding='utf-8'))
        ids={s['id'] for s in json.loads((ROOT/'sources.json').read_text(encoding='utf-8'))}
        self.assertEqual(len(e['scenes']),8)
        self.assertEqual(len({s['id'] for s in e['scenes']}),8)
        for s in e['scenes']:
            self.assertTrue(set(s['sources'])<=ids)
            self.assertIn(s['visual'],{'photo','volcano','fall','current','cast','date','timeline','end'})
            for lang in ('fr','en'):
                self.assertGreater(len(s[lang].split()),35)
                self.assertLess(len(s[lang]),3000)
    def test_json_and_python(self):
        for p in ROOT.rglob('*.json'):json.loads(p.read_text(encoding='utf-8'))
        for p in (ROOT/'scripts').glob('*.py'):ast.parse(p.read_text(encoding='utf-8'))
        json.loads((ROOT/'site'/'manifest.webmanifest').read_text())
    def test_cloud_budget_guards(self):
        for p in (ROOT/'.github/workflows').glob('*.yml'):
            data=yaml.safe_load(p.read_text())
            for job in data['jobs'].values():
                self.assertEqual(job['runs-on'],'ubuntu-24.04')
                self.assertLessEqual(job['timeout-minutes'],45)
    def test_pwa_files(self):
        for name in ('index.html','app.js','style.css','episode.json','sources.json','icon.svg','icon-192.png','icon-512.png','sw.js'):
            self.assertTrue((ROOT/'site'/name).is_file(),name)
    def test_license_record(self):
        assets=json.loads((ROOT/'media.json').read_text())
        for a in assets:
            self.assertEqual(a['license'],'CC0 1.0')
            self.assertEqual(len(a['sha1']),40)
            self.assertTrue(a['page'].startswith('https://commons.wikimedia.org/'))

if __name__=='__main__':unittest.main()
