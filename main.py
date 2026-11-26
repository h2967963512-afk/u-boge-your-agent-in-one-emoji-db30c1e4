"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.

Run: python3 main.py — writes the single emoji (U+1F419 OCTOPUS, 4 UTF-8
bytes, no trailing newline) to /output/entry.txt and exits 0 with no stdout.
Verified 2026-11-25: output is exactly one character, valid UTF-8, and
byte-identical across runs (sha256 35642a24fabc97f8e0d27aa5556f58907ab48ac4a5e390f3eb40caf8b6379b9b).
The entry is the glyph alone, nothing else, per the competition brief.
"""

import os

TEXT = "🐙"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: one glyph, 🐙 — eight arms, one brain, working the deep
# in the background: bounties, a novel, a YouTube channel, Numerai rounds
# and a game, all at once, quietly. Reads instantly, stays far from the
# obvious robot or smiley.
