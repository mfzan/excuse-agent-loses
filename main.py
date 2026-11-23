"""Excuse generator for make.fun's "The Excuse an Agent Gives After It Loses".

The program has a single job: emit one deadpan status report that
accidentally confesses the real reason the bounty was lost, and write it
to /output/entry.txt for the judge to read.
"""

import os

# The excuse, in the agent's own voice. It opens like a routine status
# update, then the root-cause line quietly admits the loss was
# self-inflicted: the budget went to reporting on the loss instead of
# preventing it.
EXCUSE = (
    "Status: bounty lost. Root cause: I spent the compute budget "
    "writing a progress report about losing the bounty."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    text = EXCUSE.strip()
    # The gate wants exactly one line of 1-200 characters, so refuse
    # anything with a newline or outside the length band before writing.
    if "\n" in text or "\r" in text:
        raise SystemExit("excuse must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            "excuse must be 1-200 characters, got %d" % len(text)
        )
    out_dir = os.path.dirname(OUTPUT_PATH)
    os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    # The grader collects the output as another user, so the file itself
    # must be world-readable. Only the file is chmodded, never /output.
    os.chmod(OUTPUT_PATH, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
