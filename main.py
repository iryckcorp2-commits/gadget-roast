#!/usr/bin/env python3
"""gadget-roast: roast the gadget I use every day in one line.

Writes a single line of at most 200 characters to /output/entry.txt:
a roast of my phone, whose battery hits 1% at 4 p.m. and then
survives the whole evening anyway. The punch is that the phone is
not dying, it is just dramatic.

Pure Python 3.13 standard library. No network, no randomness, no
clock: running the program twice writes a byte-identical file.
"""

import os
import sys

# The roast. One line, punch on the last few words.
ENTRY = (
    "My phone hits 1% at 4 p.m. and then survives the whole "
    "evening, so it is not dying, it is just dramatic and "
    "enjoys watching me panic."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only white space"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    # The grader collects /output as another user: leave the file
    # world-readable (mode 0644).
    os.chmod(path, 0o644)
    print("wrote %s (%d characters)" % (path, len(text)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
