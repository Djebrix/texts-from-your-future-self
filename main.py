"""Texts From Your Future Self — one funny text message from your future self.

Writes the line to stdout and to the path in ENTRY_OUTPUT_DIR if set,
else /output/entry.txt. Deterministic: the same line every run.
"""

import os

LINE = (
    "It's me, future you. Stop refreshing your ex's profile — in 10 years you "
    "marry the barista who spelled your name 'Greg.' Also floss. The dentist "
    "just charged me $4,200 for one tooth."
)


def main() -> None:
    print(LINE)
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
