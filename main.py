#!/usr/bin/env python3
# Robot Apology — make.fun bounty u-suga-the-robot-apology-dd96bb59.
#
# A tiny script with one job: put a two-line robot confession on disk.
# The first line owns one very specific mistake (a 6 p.m. alarm that
# should have been 6 a.m.). The second line states what the robot
# learned and what it does differently now. Nothing is fetched, nothing
# is random, nothing depends on the machine — the bytes are identical
# on every run.

from pathlib import Path

# Default destination; the caller may point elsewhere via ENTRY_OUTPUT.
DEFAULT_DEST = "/output/entry.txt"

# The confession is assembled from small fragments instead of one big
# literal, so each piece of the story can be read (and checked) alone.
_OPENING = "I'm sorry — "
_MISTAKE = "I set your alarm for 6 p.m. instead of 6 a.m., "
_FALLOUT = "so you slept through your flight and woke to a suitcase still packed by the door."
_LESSON = "I learned that one letter can cost a whole morning, "
_FIX = "so now I read the time back aloud and check the AM/PM marker before I confirm any alarm."


def build_entry() -> str:
    """Join the fragments into the two-line entry text."""
    first_line = _OPENING + _MISTAKE + _FALLOUT
    second_line = _LESSON + _FIX
    return first_line + "\n" + second_line + "\n"


def write_entry(dest: str) -> None:
    """Write the entry text to dest, creating parent folders as needed."""
    text = build_entry()
    # Sanity check: the entry must be exactly two non-empty lines.
    lines = text.splitlines()
    assert len(lines) == 2 and all(line.strip() for line in lines), "entry must be two lines"
    target = Path(dest)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    import os

    write_entry(os.environ.get("ENTRY_OUTPUT", DEFAULT_DEST))


if __name__ == "__main__":
    main()
