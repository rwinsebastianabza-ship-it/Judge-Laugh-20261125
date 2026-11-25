#!/usr/bin/env python3
"""Make the AI Judge Laugh: a single joke about office life, one line, under
200 characters, written to be read aloud in one breath. The line is 96
characters."""

ENTRY_LINE = "The office printer only jams when the document is urgent, confidential, and due in five minutes."


def main():
    entry_path = "/output/entry.txt"
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)
    print(f"Wrote {len(ENTRY_LINE)} characters to {entry_path}")
    with open(entry_path, "r", encoding="utf-8") as f:
        content = f.read()
    assert content == ENTRY_LINE, "entry.txt does not match the line"
    print("Test passed:", content)


if __name__ == "__main__":
    main()
