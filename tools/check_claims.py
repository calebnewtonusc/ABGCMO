#!/usr/bin/env python3
"""Verify the repo's claims about itself match reality."""
import glob, json, re, sys

fail = []
skills = len(glob.glob('skills/*/'))
evals = sum(len(json.load(open(f))['evals']) for f in glob.glob('skills/*/evals/evals.json'))

roster_text = open('cases/README.md').read()
m = re.search(r'<!-- ROSTER:START -->(.*?)<!-- ROSTER:END -->', roster_text, re.S)
if not m:
    fail.append('cases/README.md: roster markers missing')
    cases = 0
else:
    cases = len([l for l in m.group(1).strip().split('\n') if l.startswith('- ')])

readme = open('README.md').read()
for label, value in (('skills', skills), ('evals', evals), ('case_studies', cases)):
    if f'badge/{label}-{value}-' not in readme:
        got = re.search(rf'badge/{label}-([0-9+]+)-', readme)
        fail.append(f'README badge {label} says {got.group(1) if got else "?"}, repo has {value}')

reg = [l for l in open('registry/skills.csv').read().strip().split('\n')[1:] if l.strip()]
if len(reg) != skills:
    fail.append(f'registry has {len(reg)} rows, disk has {skills} skills')

for f in fail:
    print(f'::error::{f}')
print(f'skills={skills} evals={evals} cases={cases}, {len(fail)} problems')
sys.exit(1 if fail else 0)
