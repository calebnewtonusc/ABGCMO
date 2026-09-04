# README template

Target ~120 lines. The star decision happens in about 15 seconds, in the first
screenful. Everything below the fold is for people who already decided.

```markdown
<p align="center"><h1 align="center">NAME</h1></p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg" alt="License"></a>
  <img src="https://img.shields.io/badge/KEY_NUMBER-VALUE-color" alt="...">
</p>

<p align="center">
  <b>ONE SENTENCE THAT NAMES THE CATEGORY.</b><br>
  One more line on what makes it different from the obvious alternative.
</p>

![demo](docs/demo.gif)   <!-- 2-5 MB. This is the whole pitch. -->

## Install

```bash
one command
```

## Use it

```bash
the simplest real example, which must work on a clean machine
```

## What it does

- Five bullets. Not fifteen.
- Each one a capability, not an adjective.

## Docs

Links out. Everything long lives in docs/.

## License

MIT
```

## The four failures

1. **A table of contents where the demo should be.** The single most common
   mistake. Move it to `docs/`.
2. **No image at all.** If the tool does something visible, show it.
3. **Fifteen badges.** Four functional ones: license, build, version, community.
   Badge rows longer than the tagline read as insecurity.
4. **A quick start that does not work on a clean machine.** Test it in a fresh
   container. This is the most expensive bug in a README because it converts
   interest into distrust.

## Optional, worth it

- **Star history chart** — reported ~15% star-conversion lift
- **A "why not X" section** — naming what you do not do buys credibility on what
  you do, especially on Hacker News

## Before you push

- [ ] Someone who has never seen it can name the category in 5 seconds
- [ ] Quick start tested on a clean machine
- [ ] GIF under 5 MB
- [ ] LICENSE exists
- [ ] Topics set
- [ ] Description and homepage fields filled
