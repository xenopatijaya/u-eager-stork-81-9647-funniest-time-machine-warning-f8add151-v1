"""Funniest Time Machine Warning Label — make.fun program/v1 entry.

Writes a single deadpan warning label (110 characters) to entry.txt.
The label turns the ancestor paradox into the joke: introduce yourself
to your ancestors and the causal loop closes on you — the child they
name after you is you. Straight-face safety notice, surprise saved
for the last four words.
"""

import os

ENTRY = (
    "WARNING: Do not introduce yourself to your ancestors. "
    "They will name a child after you, and that child is you."
)


def main() -> None:
    # Gate guard: the sealed scorer requires 1-120 UTF-8 characters.
    assert 1 <= len(ENTRY) <= 120, f"entry length {len(ENTRY)} out of range"
    assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)
    print(f"chars={len(ENTRY)} path={path}")


if __name__ == "__main__":
    main()
