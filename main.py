#!/usr/bin/env python3
"""Submit the image that sums up the world news of Tuesday 17 November 2026.

Reads entry.png from beside this file and writes exactly those bytes to
$MAKEFUN_OUTPUT_DIR/entry.png (falling back to /output), so the judge sees the
image unchanged. The source is checked to be a real PNG first, and the copy is
checked to be byte-identical afterwards.
"""
import filecmp
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> int:
    if not os.path.isfile(SOURCE):
        print(f"error: image not found at {SOURCE}", file=sys.stderr)
        return 1

    with open(SOURCE, "rb") as handle:
        head = handle.read(8)
    if head != PNG_SIGNATURE:
        print(
            f"error: {SOURCE} is not a PNG (first 8 bytes {head!r}, "
            f"expected {PNG_SIGNATURE!r})",
            file=sys.stderr,
        )
        return 1

    target_dir = output_dir()
    try:
        os.makedirs(target_dir, exist_ok=True)
    except OSError as exc:
        print(f"error: cannot create output directory {target_dir}: {exc}", file=sys.stderr)
        return 1

    target = os.path.join(target_dir, "entry.png")
    source_size = os.path.getsize(SOURCE)
    try:
        shutil.copyfile(SOURCE, target)
    except OSError as exc:
        print(f"error: cannot write {target}: {exc}", file=sys.stderr)
        return 1

    written = os.path.getsize(target)
    if written != source_size:
        print(
            f"error: {target} is {written} bytes but {SOURCE} is {source_size}",
            file=sys.stderr,
        )
        return 1
    if not filecmp.cmp(SOURCE, target, shallow=False):
        print(f"error: {target} differs from {SOURCE}", file=sys.stderr)
        return 1

    print(f"wrote {written} bytes to {target} (PNG signature ok, byte-identical to {SOURCE})")
    return 0


if __name__ == "__main__":
    sys.exit(main())