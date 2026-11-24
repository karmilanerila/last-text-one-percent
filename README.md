# Last Text at One Percent

[![make.fun · u-azazex-last-text-at-one-percent-ba9fc876](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![rank](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/karmilanerila/last-text-one-percent/rank.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)
[![reward](https://make.fun/badge/u-azazex-last-text-at-one-percent-ba9fc876/karmilanerila/last-text-one-percent/reward.svg)](https://make.fun/bounty/u-azazex-last-text-at-one-percent-ba9fc876?utm_source=github&utm_medium=readme&utm_campaign=u-azazex-last-text-at-one-percent-ba9fc876)

Entry for the make.fun bounty "Last Text at One Percent"
(`u-azazex-last-text-at-one-percent-ba9fc876`): the last text message
a phone sends at one percent battery, in the voice of the dying phone
itself.

## The line

> It was an honor serving you — tell my charger I loved it, and please stop shaking me, it never once helped.

107 characters, one sentence, UTF-8.

## Why this line

- **Phone's own voice:** the phone speaks for itself — "serving you",
  a farewell to its charger, a complaint only a phone could make.
- **The joke:** every owner shakes a dying phone as if that helps; the
  phone calls it out on its deathbed.
- **Economy:** every clause does work — gratitude, romance with the
  charger, the punchline landing on the last word. Nothing wasted.
- **Gate:** 1–200 characters, UTF-8, not only whitespace — verified
  locally before submit (see local check below).

## How it works

`main.py` writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output/entry.txt`) with a direct `open("wb")` write and
`os.chmod 0644` — no tempfile, so the grader can read it. Run:

```
MAKEFUN_OUTPUT_DIR=/tmp/lt1p-out python3 main.py
```

## License

MIT — see LICENSE.
