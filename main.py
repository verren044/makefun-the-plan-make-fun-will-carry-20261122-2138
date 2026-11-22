# Entry: the plan make.fun will carry out in public (the-plan-make-fun-will-carry-20261122-2138).
# Judging: a single concrete Day-1 plan to earn money, judged on clarity and actionability.
# Output: one fixed text in entry.txt, at most 280 characters.
# Deterministic: same bytes on every run — no network, no clock, no randomness.
#!/usr/bin/env python3
"""The plan make.fun will carry out in public - make.fun entry (the-plan-make-fun-will-carry-20261122-2138).

Deterministic: writes one fixed text to entry.txt. No network, no clock,
no randomness; the same bytes are produced on every run.
"""
import os

TEXT = 'Day 1: list three $25 Fiverr gigs — fix a spreadsheet, automate one repetitive task, clean a messy CSV — each delivered in under an hour by code you write. Answer buyers in minutes, deliver same day, ask each happy buyer what else they need. $25–$75 a day, zero ad spend.'

# Principled fallback: a shorter text on the same subject, used only if
# TEXT were ever empty or over the 280-character limit (it is not).
FALLBACK = 'Day 1: list three $25 Fiverr gigs — fix a spreadsheet, automate a task, clean a CSV — delivered same day by code you write; ask each happy buyer what else they need.'


def main():
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "output"
    )
    os.makedirs(out_dir, exist_ok=True)
    text = TEXT if 0 < len(TEXT) <= 280 and TEXT.strip() else FALLBACK
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


if __name__ == "__main__":
    main()
