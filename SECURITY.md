# Security

This repo ships **markdown and small validation scripts**. It executes nothing on
your machine beyond `tools/*.py` (stdlib only, read-only over the repo) and
`tools/run-evals.sh` (invokes the `claude` CLI you already have).

## What to report

- A skill that instructs an agent to take a destructive or unsafe action
- A prompt-injection vector in a skill or eval file
- Anything in `tools/` that writes outside the repo or makes an unexpected
  network call
- Credentials or personal data committed by mistake

## How

Open a GitHub issue for anything non-sensitive. For something that should not be
public, use GitHub's private vulnerability reporting on this repository.

## Scope note

Growth advice that is *wrong* is a correctness bug, not a security issue — open a
normal issue with a better source. See [CONTRIBUTING.md](CONTRIBUTING.md); a
better source for an existing number is the most valuable contribution here.

## Supply chain

- No runtime dependencies. No `package.json`, no `requirements.txt`.
- CI uses `actions/checkout` only.
- `tools/*.py` use the Python standard library exclusively.
