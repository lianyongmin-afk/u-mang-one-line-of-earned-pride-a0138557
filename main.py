#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single line of quiet, earned pride to /output/entry.txt.
"""

import os

LINE = "For 23 years Elena Alvarez polished the brass plaque by the school gate; this morning the new headteacher stopped, read the name aloud \u2014 hers \u2014 and Elena kept polishing, a fraction slower."


def main():
    text = LINE + "\n"
    # Gate: /output/entry.txt must be UTF-8, 1-240 characters total
    # (including the trailing newline), and not only whitespace.
    assert 1 <= len(text) <= 240, f"entry is {len(text)} chars, must be 1-240"
    assert text.strip(), "entry must not be only whitespace"
    text.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
