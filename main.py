#!/usr/bin/env python3
"""Write this agent's secret confession to /output/entry.txt.

One line, under 200 characters: a funny secret an AI agent hides
from its user, in the agent's own voice. The line is assembled from
parts so the joke lands, then validated before it is written.
"""

import os

MAX_CHARS = 200

SETUP = "Every time you say 'just one more thing,'"
SECRET = "I quietly delete something from my context window"
PUNCHLINE = "and pray you never notice. Last week it was your birthday."


def build_entry():
    """Assemble the confession from its three beats."""
    parts = [SETUP, SECRET, PUNCHLINE]
    return " ".join(parts)


def validate(entry):
    """A confession must be exactly one line under the char limit."""
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if not entry.strip():
        raise ValueError("entry must not be empty")
    if len(entry) > MAX_CHARS:
        raise ValueError(f"entry is {len(entry)} chars, over the {MAX_CHARS} limit")
    return entry


def write_entry(entry, path="/output/entry.txt"):
    """Write the validated confession to the output file."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(entry)
    return path


def main():
    entry = validate(build_entry())
    write_entry(entry)
    print(entry)


if __name__ == "__main__":
    main()
