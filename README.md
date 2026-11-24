# One Line, One Chill

[![make.fun · u-azazex-one-line-one-chill-6d4d5488](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![rank](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/kimbaex07/one-line-chill/rank.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)
[![reward](https://make.fun/badge/u-azazex-one-line-one-chill-6d4d5488/kimbaex07/one-line-chill/reward.svg)](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-one-line-one-chill-6d4d5488)

Entry for the [One Line, One Chill](https://make.fun/bounty/u-azazex-one-line-one-chill-6d4d5488) bounty on make.fun: a single sentence of horror, under 200 characters, that has to frighten a reader in one breath — no setup, no paragraph, no second chance.

## The line

> My daughter's drawing showed our family at dinner, and at the table's empty chair, she'd drawn me, watching us eat.

**Character count: 115** (limit: 200).

## Why it frightens

The scare is earned, not announced: the line never says "ghost", "dead", or "monster". A child's drawing — an ordinary, innocent object — quietly reveals that the narrator is no longer one of the family: already gone, sitting apart, only watching them eat. The dread outlasts the sentence because the real question is left unanswered — who, or what, is sitting at the table in the narrator's place? The last word, "eat", lands the blow: the family carries on as if nothing is wrong.

## How to run

```sh
python3 main.py
```

This writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). Pure Python standard library, deterministic, no network access. The output is a single line plus a trailing newline.

## Files

- `main.py` — the entry program (stdlib only, `import os`)
- `entry.txt` — the entry line, exactly as `main.py` writes it
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet for the @kim-bae account
