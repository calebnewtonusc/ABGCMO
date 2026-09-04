#!/usr/bin/env python3
"""Enforce the repo's central rule: numeric claims carry evidence tags, and an
[M] Measured tag must sit near a citation of an actual primary artifact."""
import glob, re, sys

TAG = re.compile(r'\[(M|P|R|A)\]')
NUM = re.compile(r'\d+(?:\.\d+)?\s*(?:%|x)\b')
PRIMARY = re.compile(r'github\.com|arxiv|\.pdf|primary source|source repo|source repository', re.I)

fail = []

# 1. every numeric table in data/ carries tags
for f in sorted(glob.glob('data/*.md')):
    lines = open(f).read().split('\n')
    i = 0
    while i < len(lines):
        if lines[i].startswith('|') and i + 1 < len(lines) and \
           set(lines[i + 1].replace('|', '').strip()) <= set('-: '):
            start, j = i, i + 2
            while j < len(lines) and lines[j].startswith('|'):
                j += 1
            block = '\n'.join(lines[start:j])
            ctx = '\n'.join(lines[max(0, start - 6):start])
            exempt = re.search(r'Ratio to a like|Raw weight|Tag\b', lines[start])
            if NUM.search(block) and not (TAG.search(block + ctx) or exempt or
                                          re.search(r'Measured', block + ctx)):
                fail.append(f'{f}:{start+1}: untagged numeric table -> {lines[start][:60]}')
            i = j
        else:
            i += 1

# 2. [M] tags must cite a primary artifact within 12 lines
DEFINITION_FILE = 'data/evidence-tiers.md'  # defines the tags rather than using them
for f in sorted(glob.glob('data/*.md') + glob.glob('skills/*/SKILL.md')):
    if f == DEFINITION_FILE:
        continue
    lines = open(f).read().split('\n')
    for i, line in enumerate(lines):
        if '[M]' in line or 'Measured' in line:
            ctx = '\n'.join(lines[max(0, i - 12):i + 12])
            if not PRIMARY.search(ctx):
                fail.append(f'{f}:{i+1}: [M] without a primary-source citation nearby')

for f in fail:
    print(f'::error::{f}')
print(f'{len(fail)} evidence problems')
sys.exit(1 if fail else 0)
