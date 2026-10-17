#!/usr/bin/env python3
"""Read-only candidate report. Do not delete based on this report alone."""
import hashlib
import json
from collections import defaultdict
from pathlib import Path
def inventory(root):
    root=Path(root).resolve()
    hashes=defaultdict(list)
    empty=[]
    ignore={".git",".venv","venv","node_modules","__pycache__","dist","build"}
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.is_symlink() or any(x in ignore for x in p.relative_to(root).parts): continue
        try:
            size=p.stat().st_size
            if size>8388608: continue
            rel=p.relative_to(root).as_posix()
            if size==0: empty.append(rel)
            else: hashes[(size,hashlib.sha256(p.read_bytes()).hexdigest())].append(rel)
        except OSError: continue
    return {"empty_files":empty,"exact_duplicates":[v for v in hashes.values() if len(v)>1],"warning":"Manual dependency and regression review required."}
if __name__=="__main__":
    print(json.dumps(inventory(Path(__file__).resolve().parents[1]),indent=2))
