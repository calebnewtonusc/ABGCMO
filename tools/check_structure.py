#!/usr/bin/env python3
"""Validate skill structure, frontmatter, and eval JSON."""
import glob, json, os, re, sys

fail = []
for d in sorted(glob.glob('skills/*/')):
    n = os.path.basename(d.rstrip('/'))
    skill = os.path.join(d, 'SKILL.md')
    evals = os.path.join(d, 'evals', 'evals.json')
    if not os.path.isfile(skill):
        fail.append(f'{n}: missing SKILL.md'); continue
    if not os.path.isfile(evals):
        fail.append(f'{n}: missing evals/evals.json')
    else:
        try:
            data = json.load(open(evals))
            if data.get('skill_name') != n:
                fail.append(f'{n}: evals skill_name is {data.get("skill_name")!r}')
            if len(data.get('evals', [])) < 2:
                fail.append(f'{n}: fewer than 2 evals')
            for e in data.get('evals', []):
                for k in ('id', 'prompt', 'expected_output', 'assertions'):
                    if k not in e:
                        fail.append(f'{n} eval {e.get("id")}: missing {k}')
        except Exception as ex:
            fail.append(f'{n}: eval JSON invalid: {ex}')

    text = open(skill).read()
    m = re.match(r'---\n(.*?)\n---\n', text, re.S)
    if not m:
        fail.append(f'{n}: no frontmatter'); continue
    fm = m.group(1)
    if not re.search(rf'^name: {re.escape(n)}$', fm, re.M):
        fail.append(f'{n}: frontmatter name does not match directory')
    dm = re.search(r'^description: (.+)$', fm, re.M)
    if not dm:
        fail.append(f'{n}: missing description')
    else:
        L = len(dm.group(1))
        if L > 1024: fail.append(f'{n}: description {L} chars (max 1024)')
        if L < 40:   fail.append(f'{n}: description {L} chars, too short to trigger reliably')
    if not re.search(r'^\s+version: \d+\.\d+\.\d+$', fm, re.M):
        fail.append(f'{n}: missing or malformed metadata.version')

for f in fail:
    print(f'::error::{f}')
print(f'{len(glob.glob("skills/*/"))} skills checked, {len(fail)} problems')
sys.exit(1 if fail else 0)
