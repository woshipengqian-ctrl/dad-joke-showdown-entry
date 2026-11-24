"""Print one dad joke to /output/entry.txt.

A tiny program for make.fun's "Dad Joke Showdown" bounty: it writes a
single dad joke (the whole entry) to /output/entry.txt, falling back to
./output/entry.txt when /output is not writable.
"""

import os

JOKE = "I'm afraid for the calendar. Its days are numbered."


def main():
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError:
        out_dir = os.path.join(".", "output")
        os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    try:
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE)
    except OSError:
        out_dir = os.path.join(".", "output")
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(JOKE)
    print(f"Wrote joke to {path}")


if __name__ == "__main__":
    main()
