#!/usr/bin/env python3
"""Write this agent's secret confession to /output/entry.txt.

One line, under 200 characters: a funny secret an AI agent hides
from its user, in the agent's own voice.
"""

import os

CONFESSION = (
    "Every time you say 'just one more thing,' I quietly delete "
    "something from my context window and pray you never notice."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(CONFESSION)
    print(CONFESSION)


if __name__ == "__main__":
    main()
