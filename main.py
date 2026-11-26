"""Real-life patch notes: one line, written to the output directory.

Writes a single-line changelog entry for a bug fix to the human body.
Uses MAKEFUN_OUTPUT_DIR when set, otherwise /output.
Standard library only, no network access.
"""

import os

LINE = "v2.4.1 — Fixed: sneezing no longer shuts both eyes while driving. Yawns now give a 2s warning before meetings. Known issue: hiccups still bypass mute."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
