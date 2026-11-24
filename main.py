#!/usr/bin/env python3
"""Write one short roast line to entry.txt for a make.fun bounty."""

from __future__ import annotations

import os
import sys
from pathlib import Path

TEXT = "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."

DEFAULT_OUT_DIR = "/output"


def resolve_out_dir() -> Path:
    """Return the folder the entry file belongs in.

    MAKEFUN_OUTPUT_DIR wins; OUTPUT_DIR is accepted as a fallback; /output last.
    """
    for name in ("MAKEFUN_OUTPUT_DIR", "OUTPUT_DIR"):
        chosen = os.environ.get(name)
        if chosen:
            return Path(chosen)
    return Path(DEFAULT_OUT_DIR)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be between 1 and 280 characters"

    out_dir = resolve_out_dir()
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))

    print(f"{len(TEXT)} characters", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
