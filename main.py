"""One Letter for Your Day -- make.fun bounty entry.

The letter: Q
The word behind it: queasy

Why Q: a queasy stomach is a sharp, physical, specific picture of a
real day -- the churn before a big presentation, after dodgy street
food, or on a rattling commute. It is honest, it is funny to retell,
and Q is a letter almost nobody reaches for, so the word lands
instead of blending in with the obvious A/F/Z crowd.
"""

import os

LETTER = "Q"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate check: the server demands exactly one ASCII uppercase letter.
    assert len(LETTER) == 1 and LETTER.isalpha() and LETTER.isupper(), LETTER
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
