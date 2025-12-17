import os
import json
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

import azure.functions as func

START_TIME = time.time()

def _load_build_info():
    try:
        p = Path(__file__).resolve().parent.parent / "shared" / "build_info.json"
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception:
        return {"version": "unknown", "buildTimeUtc": "unknown", "commitSha": "unknown"}

def main(req: func.HttpRequest) -> func.HttpResponse:
    uptime_seconds = round(time.time() - START_TIME, 3)
    build = _load_build_info()

    payload = {
        "requestId": str(uuid.uuid4()),
        "timestampUtc": datetime.now(timezone.utc).isoformat(),
        "region": os.environ.get("WEBSITE_REGION") or os.environ.get("REGION_NAME") or "unknown",
        "build": build,
        "runtime": {
            "uptimeSeconds": uptime_seconds
        }
    }

    return func.HttpResponse(
        json.dumps(payload),
        status_code=200,
        mimetype="application/json"
    )
