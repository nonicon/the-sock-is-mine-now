"""The Sock Is Mine Now — a make.fun One-Liner Laugh Lab entry.

The excuse a robot vacuum gives after eating a sock, written to
/output/entry.txt. One line, 125 characters, plain words: the vacuum
cites its own user manual as law and declares the swallowed sock its
personal property. The joke is the deadpan legal voice — theft
re-framed as a lawful transfer of ownership, punch landing on the
last two words. One line, 118 characters.

The gate is checked for real before writing: 1-200 characters, a
single line, not only white space.
"""

import os

ENTRY = (
    "According to Section 4, Paragraph B of my user manual, once swallowed, "
    "your sock legally becomes my personal property."
)


def validate(text: str) -> None:
    """Check the entry against the bounty gate: UTF-8 text, 1-200 chars."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} out of range (1-200)")
    if not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"Wrote /output/entry.txt ({len(ENTRY)} characters)")


if __name__ == "__main__":
    main()
