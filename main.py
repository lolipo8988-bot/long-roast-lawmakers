"""The Long Roast: Lawmakers and the File They Cannot Convert entry.

Writes a single satirical sentence to /output/entry.txt.
The competition gate requires UTF-8 text of 1 to 320 characters,
not only white space, and the judge requires exactly one sentence.
The program is deterministic: every run writes exactly the same bytes.

An alternate output path may be given as the first command-line
argument (used only for isolated local verification); with no
argument the program writes to the competition path
/output/entry.txt.
"""

import os
import sys

DEFAULT_OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 320

ENTRY = (
    "The lawmakers who voted to regulate AI, crypto, and the entire "
    "internet couldn't convert their own tech bill to a PDF, so the "
    "law went live as a tilted phone photo of a Word doc titled "
    "FINAL_BILL.pdf.docx."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )
    assert text, "entry must not be only white space"
    output_path = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_OUTPUT_PATH
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
