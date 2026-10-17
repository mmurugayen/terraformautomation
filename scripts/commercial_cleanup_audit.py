#!/usr/bin/env python3
"""Read-only candidate report. Do not delete based on this report alone."""
import hashlib
import json
import logging
from collections import defaultdict
from pathlib import Path

logger = logging.getLogger(__name__)


def inventory(root):
    root = Path(root).resolve()
    hashes = defaultdict(list)
    empty = []
    ignore = {".git", ".venv", "venv", "node_modules", "__pycache__", "dist", "build"}
    for path in sorted(root.rglob("*")):
        if (
            not path.is_file()
            or path.is_symlink()
            or any(part in ignore for part in path.relative_to(root).parts)
        ):
            continue
        try:
            size = path.stat().st_size
            if size > 8388608:
                continue
            relative_path = path.relative_to(root).as_posix()
            if size == 0:
                empty.append(relative_path)
            else:
                digest = hashlib.sha256(path.read_bytes()).hexdigest()
                hashes[(size, digest)].append(relative_path)
        except OSError:
            continue
    result = {
        "empty_files": empty,
        "exact_duplicates": [paths for paths in hashes.values() if len(paths) > 1],
        "warning": "Manual dependency and regression review required.",
    }
    logger.info(
        "Cleanup inventory completed: empty_files=%d duplicate_groups=%d",
        len(result["empty_files"]),
        len(result["exact_duplicates"]),
    )
    return result


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    print(json.dumps(inventory(Path(__file__).resolve().parents[1]), indent=2))
