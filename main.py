#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes exactly one line of text to /output/entry.txt: an original
one-line excuse from a home Wi-Fi router for dropping the connection
at the exact moment a movie reaches its climax.

Pure Python standard library only. Deterministic: every run produces
byte-identical output.
"""

import os

LINE = "The villain was mid-monologue when I realized the only plot twist this house was getting tonight was me."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
