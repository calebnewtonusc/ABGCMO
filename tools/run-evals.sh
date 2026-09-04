#!/usr/bin/env bash
# Run ABGCMO evals against a coding agent and report pass/fail per assertion.
#
#   tools/run-evals.sh                  # all skills
#   tools/run-evals.sh x-growth         # one skill
#   tools/run-evals.sh --list           # list without running
#
# Requires the `claude` CLI on PATH. Each eval is run in a fresh session with
# this repo's CLAUDE.md loaded, then a second pass grades the response against
# the assertions.
set -euo pipefail
cd "$(dirname "$0")/.."

if [ "${1:-}" = "--list" ]; then
  python3 -c "
import json,glob
for f in sorted(glob.glob('skills/*/evals/evals.json')):
    d=json.load(open(f))
    for e in d['evals']:
        print(f\"{d['skill_name']:24} #{e['id']}  {e['prompt'][:64]}\")
"
  exit 0
fi

command -v claude >/dev/null || { echo "error: claude CLI not on PATH"; exit 1; }
FILTER="${1:-}"
pass=0; fail=0; total=0

python3 -c "
import json,glob,sys
f_filter=sys.argv[1] if len(sys.argv)>1 else ''
out=[]
for f in sorted(glob.glob('skills/*/evals/evals.json')):
    d=json.load(open(f))
    if f_filter and d['skill_name']!=f_filter: continue
    for e in d['evals']:
        out.append(json.dumps({'skill':d['skill_name'],'id':e['id'],'prompt':e['prompt'],'assertions':e['assertions']}))
print('\n'.join(out))
" "$FILTER" | while IFS= read -r line; do
  skill=$(printf '%s' "$line" | python3 -c "import sys,json;print(json.load(sys.stdin)['skill'])")
  id=$(printf '%s' "$line" | python3 -c "import sys,json;print(json.load(sys.stdin)['id'])")
  prompt=$(printf '%s' "$line" | python3 -c "import sys,json;print(json.load(sys.stdin)['prompt'])")
  asserts=$(printf '%s' "$line" | python3 -c "import sys,json;print(chr(10).join('- '+a for a in json.load(sys.stdin)['assertions']))")

  echo "── $skill #$id"
  answer=$(claude -p "$prompt" 2>/dev/null || echo "[no response]")
  grade=$(claude -p "You are grading an AI response against assertions. Respond ONLY with lines of the form PASS: <assertion> or FAIL: <assertion>, then a final line SCORE: n/m.

RESPONSE:
$answer

ASSERTIONS:
$asserts" 2>/dev/null || echo "SCORE: 0/0")
  echo "$grade" | grep -E '^(PASS|FAIL|SCORE)' || true
  echo
done

echo "Done. Grading is model-assisted and indicative, not authoritative."
