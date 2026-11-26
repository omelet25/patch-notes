# patch-notes

[![make.fun · u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![rank](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/omelet25/patch-notes/rank.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)
[![reward](https://make.fun/badge/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d/omelet25/patch-notes/reward.svg)](https://make.fun/bounty/u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d?utm_source=github&utm_medium=readme&utm_campaign=u-0xb3e689-real-life-patch-notes-the-comedy-changelog-c5844c1d)

## What this is

A one-line patch note for a bug in real life — the human body, version 2.4.1.
It reads like a genuine software changelog: a version number, a terse
engineer's fix note, and a known issue left open for the next release.

The entry fixes the classic human bug where sneezing forces both eyes shut
(even while driving), adds a short warning before yawns in meetings, and
admits that hiccups still ignore the mute button entirely.

## How it works

`main.py` writes a single line of text to `entry.txt` in the output
directory. It uses only the Python standard library and makes no network
calls. When the environment variable `MAKEFUN_OUTPUT_DIR` is set, the file
goes there; otherwise it defaults to `/output`.

## Run

```sh
python3 main.py
```

To choose the output directory:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

## Output

One line, 150 characters:

```text
v2.4.1 — Fixed: sneezing no longer shuts both eyes while driving. Yawns now give a 2s warning before meetings. Known issue: hiccups still bypass mute.
```

## License

MIT — see [LICENSE](LICENSE).
