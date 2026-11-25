"""The Tired Dark Lord: a 100-word villain monologue.

Writes one monologue of exactly 100 words to $MAKEFUN_OUTPUT_DIR/entry.txt
(or /output/entry.txt when the variable is unset).
"""

import os

MONOLOGUE = (
    "Hero. Yes, come in\u2014mind the third step, it bites. "
    "I have ruled Ashenmoor forty years. "
    "Nine bells, nine provinces, nine oaths\u2014all of them mine, "
    "all of them ringing. Still. They never stop. Not ever. "
    "The eclipse comes on the third night, the Tithe of Salt must be paid, "
    "and the council\u2014the council writes letters. Letters! "
    "I read them all. Every one. So then. Draw your sword. "
    "I have a speech somewhere\u2014'kneel, mortal, behold'\u2014ah. "
    "There it is. You know what? Take the crown. Take the tower. "
    "Take the whole damp kingdom. Just\u2014leave the kettle on. "
    "Somebody has to mind the kettle."
)


def main() -> None:
    # Integrity check: the monologue must stay exactly 100 words and
    # inside the gate (1-600 UTF-8 characters, not only whitespace).
    words = MONOLOGUE.split()
    if len(words) != 100:
        raise SystemExit(f"monologue is {len(words)} words, expected 100")
    encoded = MONOLOGUE.encode("utf-8")
    if not 1 <= len(MONOLOGUE) <= 600:
        raise SystemExit(f"monologue is {len(MONOLOGUE)} chars, gate is 1-600")
    if not MONOLOGUE.strip():
        raise SystemExit("monologue is only whitespace")
    for banned in ("tired", "weary", "exhausted"):
        if banned in MONOLOGUE.lower():
            raise SystemExit(f"monologue must never say it is {banned}")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(encoded)
    # Round-trip check: what landed on disk must be the exact text.
    with open(path, "rb") as f:
        if f.read() != encoded:
            raise SystemExit("entry.txt on disk differs from MONOLOGUE")


if __name__ == "__main__":
    main()
