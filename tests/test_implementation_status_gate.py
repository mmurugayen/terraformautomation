import json,subprocess,sys
from pathlib import Path
S=Path("scripts/implementation_status_gate.py")
def run(t,p,*x):
 f=t/"s.json";f.write_text(json.dumps(p));return subprocess.run([sys.executable,str(S),"--file",str(f),*x],capture_output=True,text=True)
def test_evidence_required(t): assert run(t,{"items":[{"id":"x","status":"implemented","evidence":[]}]}).returncode!=0
def test_evidenced_complete(t): assert run(t,{"items":[{"id":"x","status":"implemented","evidence":["test"]}]},"--require-complete").returncode==0
def test_native_pending_fails_release(t): assert run(t,{"items":[{"id":"x","status":"native_pending","native_required":True}]},"--require-complete").returncode==2
