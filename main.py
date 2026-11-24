#!/usr/bin/env python3
"""Entry for make.fun: Make the AI Judge Laugh: Developer Excuses.

Prints exactly one funny single-line developer excuse, under 200 chars.
"""

ENTRY = "My 2 a.m. hotfix worked. It just hit the backup server, which has been serving 2019 to 40,000 users ever since."


def main():
    print(ENTRY)
    # The house harness grades /output/entry.txt, so write the same
    # single line there too. Stdout stays exactly the entry line.
    try:
        import os

        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()
