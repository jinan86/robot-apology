#!/usr/bin/env python3
"""Robot Apology — make.fun entry for "The Robot Apology"
(u-suga-the-robot-apology-dd96bb59).

Writes a two-line robot confession to /output/entry.txt:
  line 1 — one sentence apologizing for one specific, concrete mistake
  line 2 — one sentence naming the lesson and the changed behaviour

Deterministic: the same bytes are written on every run.
"""

import os

ENTRY = (
    "I'm sorry \u2014 I set your alarm for 6 p.m. instead of 6 a.m., "
    "so you slept through your flight and woke to a suitcase still "
    "packed by the door.\n"
    "I learned that one letter can cost a whole morning, so now I read "
    "the time back aloud and check the AM/PM marker before I confirm "
    "any alarm.\n"
)


def main() -> None:
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
