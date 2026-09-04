# Verification log

Platform mechanics go stale fast. This log records when each claim class was last
checked against a primary source, and what "stale" means for it.

| Claim class | Last verified | Method | Half-life | Status |
|---|---|---|---|---|
| X Heavy Ranker weights | **2026-09-03** | Read `twitter/the-algorithm-ml/projects/home/recap/README.md` directly | Weights dated 2023-04-05 and the source says they "can be adjusted at any time" | **Known stale at source.** Best available; treat as directional. |
| GitHub fake-star study | 2026-09-03 | ICSE 2026 paper (peer-reviewed), StarScout repo | Multi-year | Current |
| HN launch effects | 2026-09-03 | arXiv 2511.04453 abstract confirmed; single-author preprint, n=138 | Unknown | Current, weak tier |
| Claude Code marketplace process | 2026-09-03 | `anthropics/claude-plugins-community` | ~6 months | Current |
| LinkedIn format engagement | 2026-09-03 | AuthoredUp 3M-post analysis (secondary) | ~6 months | Current |
| LinkedIn link penalties | 2026-09-03 | Multiple secondary sources only | ~3 months | **Unverified against primary** |
| X reach decay / link penalties | 2026-09-03 | Secondary sources only; not in published config | ~3 months | **Unverified against primary** |
| TikTok / Instagram / YouTube signals | 2026-09-03 | Secondary sources; some Mosseri statements | ~3 months | **Unverified against primary** |
| Product Hunt traffic by rank | 2026-09-03 | Secondary only | ~6 months | **Unverified against primary** |
| PLG / retention / cold email benchmarks | 2026-09-03 | Vendor benchmark reports | ~12 months | Current, `[R]`/`[A]` |
| Competing repo star counts | 2026-09-03 | GitHub API | ~1 month | Will drift |

## How to re-verify

```bash
# X weights — the only one with a readable primary source
gh api repos/twitter/the-algorithm-ml/contents/projects/home/recap/README.md \
  --jq '.content' | base64 -d | grep -A14 'weight_fav'

# Competing repo stars for docs/LANDSCAPE.md
gh api repos/coreyhaines31/marketingskills --jq '.stargazers_count'

# All external links in the repo
grep -ohE 'https?://[^ )>"]+' $(git ls-files '*.md') | sed 's/[.,)]*$//' | sort -u | \
  while read u; do c=$(curl -s -o /dev/null -w "%{http_code}" -L --max-time 8 "$u"); \
  case "$c" in 2*|3*|401|403|429) ;; *) echo "$c $u";; esac; done
```

## Standing warning

Rows marked **Unverified against primary** are `[A] Asserted` throughout the repo.
They are included because the direction is consistent across many sources and the
cost of acting on them is low. They are not facts. If you are making an expensive
decision on one of them, verify it yourself first.
