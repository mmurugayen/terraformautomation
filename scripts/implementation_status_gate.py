#!/usr/bin/env python3
"""Fail-closed implementation/qualification status gate."""
import argparse,json
from pathlib import Path
VALID={"implemented","partial","not_implemented","native_pending"}
def main():
 p=argparse.ArgumentParser();p.add_argument("--file",default="implementation-status.json");p.add_argument("--require-complete",action="store_true");a=p.parse_args()
 items=json.loads(Path(a.file).read_text()).get("items",[])
 if not items: raise SystemExit("items must be non-empty")
 seen=set()
 for x in items:
  i=x.get("id");s=x.get("status")
  if not i or i in seen or s not in VALID: raise SystemExit("invalid implementation status record")
  seen.add(i)
  if s=="implemented" and not x.get("evidence"): raise SystemExit(f"{i}: implemented requires evidence")
  if s=="native_pending" and x.get("native_required") is not True: raise SystemExit(f"{i}: native_pending requires native_required=true")
 print(json.dumps({"counts":{s:sum(x["status"]==s for x in items) for s in sorted(VALID)},"complete":all(x["status"]=="implemented" for x in items)},sort_keys=True))
 if a.require_complete and any(x["status"]!="implemented" for x in items): raise SystemExit(2)
if __name__=="__main__": main()
