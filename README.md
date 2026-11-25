# The Tired Dark Lord: A 100-Word Villain Monologue

[![make.fun](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![Rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/ukyo9k/tired-dark-lord-monologue/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![Reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/ukyo9k/tired-dark-lord-monologue/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

Entry for the [make.fun bounty "The Tired Dark Lord: A 100-Word Villain Monologue"](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb).

## What it does

`main.py` (Python 3, standard library only) writes a single 100-word monologue
(576 characters) to `$MAKEFUN_OUTPUT_DIR/entry.txt` (or `/output/entry.txt`
when the variable is unset). The speaker is the ruler of Ashenmoor: forty
years on the throne, nine bells, nine provinces, nine oaths, an eclipse on
the third night, a Tithe of Salt to collect — and a council that writes
letters. The tiredness lives in the rhythm, the pauses and the small
deflections; the villain never says he is tired. The last line lands the
sting: he would hand over the whole damp kingdom, if somebody would only
mind the kettle.

## The monologue

> Hero. Yes, come in—mind the third step, it bites. I have ruled Ashenmoor forty years. Nine bells, nine provinces, nine oaths—all of them mine, all of them ringing. Still. They never stop. Not ever. The eclipse comes on the third night, the Tithe of Salt must be paid, and the council—the council writes letters. Letters! I read them all. Every one. So then. Draw your sword. I have a speech somewhere—'kneel, mortal, behold'—ah. There it is. You know what? Take the crown. Take the tower. Take the whole damp kingdom. Just—leave the kettle on. Somebody has to mind the kettle.

## How to run

```sh
python3 main.py
# writes entry.txt to $MAKEFUN_OUTPUT_DIR (default /output)
```

`main.py` validates the text before writing: exactly 100 words, 1–600
characters, valid UTF-8, not only whitespace, and never plainly saying the
villain is tired — then verifies the bytes on disk match the source text.

## License

MIT — see [LICENSE](LICENSE).
