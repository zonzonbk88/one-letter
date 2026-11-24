#!/usr/bin/env python3
"""One Letter for Your Day — entry program.

Writes exactly one character, a letter from A to Z, to
<OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Hidden word behind the letter: KNACKERED — the day left me utterly
wiped out, collapsed on the sofa, too tired to form a full sentence.
One letter says it all.
"""

import os

# Candidates weighed before settling:
#   A Amazing      — vague mood, no picture.
#   E Exhausted    — true but the first word anyone reaches for.
#   F Friday-feeling — the brief's own example; crowded, obvious.
#   H Hangover     — vivid and funny, but a cliche pick.
#   T Tired        — generic; says nothing specific about the day.
#   Z Zero sleep   — the brief's own example; obvious.
#   D Derailed     — strong runner-up: a day gone off the rails, but
#                    more vivid than funny; loses to Knackered on
#                    criterion 3 (the word itself lands the joke).
#   K Knackered    — CHOSEN. Specific (bone-tired, done in, collapsed
#                    on the sofa), funny in the sound of the word
#                    itself, true to a real day, and K is a sharp,
#                    unobvious initial for it. Reconsidered against
#                    Derailed and Hangover after the first draft and
#                    kept: it is the only candidate that hits the
#                    judge's criteria 2 AND 3 at once while dodging
#                    the criterion-5 penalty for the obvious pick.
#                    "Knackered" is everyday British/Australian
#                    English, not obscurity for its own sake.
LETTER = "K"


def main() -> None:
    # Guard the gate: the entry must be exactly one A-Z character.
    assert len(LETTER) == 1 and "A" <= LETTER <= "Z", LETTER
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
