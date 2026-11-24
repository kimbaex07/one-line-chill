"""One Line, One Chill — entry program.

Writes a single sentence of horror (under 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Pure Python stdlib, deterministic, no network.
"""

import os

LINE = (
    "My daughter's drawing showed our family at dinner, and at the "
    "table's empty chair, she'd drawn me, watching us eat."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
