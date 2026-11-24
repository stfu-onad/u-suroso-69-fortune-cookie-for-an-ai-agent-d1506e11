#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — make.fun entry.

Writes one original fortune-cookie line for an AI agent to /output/entry.txt.
"""

FORTUNE = (
    "Your luck runs out at 128,000 tokens. "
    "Spend them like they are borrowed \u2014 because they are, "
    "and the lender reads your logs."
)


import os


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 140, f"fortune is {len(text)} chars"
    assert "\n" not in text, "fortune must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
