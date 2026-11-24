#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse.

Writes one line, in the dog's own voice, to /output/entry.txt.
Stdlib only.
"""

import os

ENTRY = (
    "The homework said 'show your work', so I ate it \u2014 now the work is "
    "inside me, the most honest place I know."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
