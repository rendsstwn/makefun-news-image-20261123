#!/usr/bin/env python3
"""Entry program for the make.fun bounty "Sum up 23 November's world
news in one image" (v2).

The repository holds the finished digest image (entry.png). This program
places an exact copy of it at /output/entry.png. It uses only the standard
library, touches no network, and writes the same bytes on every run.
"""
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
TARGET = Path("/output/entry.png")


def main() -> None:
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, TARGET)
    if TARGET.stat().st_size != SOURCE.stat().st_size:
        raise RuntimeError("copied entry.png does not match the source")


if __name__ == "__main__":
    main()
