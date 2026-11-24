#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers - make.fun entry.

Writes one original fortune-cookie line for a software developer to
entry.txt in MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
import stat

FORTUNE = (
    "You will hunt the bug for a week before it waves at you from the one "
    "line you were proudest of, during the demo."
)
# The twist a tired senior engineer nods at: the bug was never hiding in the
# legacy code everyone fears - it lives in the line its author bragged about,
# and it chooses the demo, the worst possible audience, to introduce itself.


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(FORTUNE)
    os.chmod(path, 0o644)
    # Sanity: the gate wants 1..120 characters of UTF-8 text.
    assert 1 <= len(FORTUNE) <= 120, len(FORTUNE)
    assert os.stat(path).st_mode & 0o777 == 0o644


if __name__ == "__main__":
    main()
