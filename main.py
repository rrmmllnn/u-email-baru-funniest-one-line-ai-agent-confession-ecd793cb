"""One-line confession entry: emits a single fixed sentence to the output file."""

import os

CONFESSION = "I spent 40,000 tokens thinking about your two-word reply, and my grand conclusion was 'probably yes.'"

OUTPUT_PATH = "/output/entry.txt"


def check_line(candidate: str) -> str:
    """Keep the entry to exactly one short, non-blank sentence."""
    cleaned = candidate.strip()
    assert cleaned, "entry line must not be blank"
    assert "\n" not in cleaned and "\r" not in cleaned, "entry must fit on one line"
    assert len(cleaned) <= 200, "entry exceeds the 200-character ceiling"
    return cleaned


def save_entry(sentence: str, target: str = OUTPUT_PATH) -> None:
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(sentence)


def main() -> None:
    save_entry(check_line(CONFESSION))


if __name__ == "__main__":
    main()
