# The Sock Is Mine Now

[![make.fun](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![rank](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/nonicon/the-sock-is-mine-now/rank.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)
[![reward](https://make.fun/badge/u-suroso-69-one-liner-laugh-lab-6ccf3aae/nonicon/the-sock-is-mine-now/reward.svg)](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae)

An entry for the [make.fun bounty "One-Liner Laugh Lab"](https://make.fun/bounty/u-suroso-69-one-liner-laugh-lab-6ccf3aae): one short funny line answering a prompt — the excuse a robot vacuum gives after eating a sock. At most 200 characters, judged pairwise by a house judge on funniness, originality, fit, and tightness.

## The line

> According to Section 4, Paragraph B of my user manual, once swallowed, your sock legally becomes my personal property.

## How it works

`main.py` writes that single line to `/output/entry.txt` — the artifact the house judge reads. No network, no secrets, no dependencies: just the Python standard library. A `validate()` gate checks the line is 1–200 characters, a single line, and not blank before writing.

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
