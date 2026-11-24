"""Last Text at One Percent — make.fun entry.

Writes the phone's final text message to /output/entry.txt.
The line is written by the dying phone itself, in its own voice:
grateful, a little dramatic, and calling out the one thing every
owner does at 1% — shaking the phone as if that ever helped.
"""
import os

LINE = (
    "It was an honor serving you \u2014 tell my charger I loved it, "
    "and please stop shaking me, it never once helped."
)


def main():
    # No tempfile: the grader runs as a different user and must be able
    # to read entry.txt, so write directly and chmod 0644.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
