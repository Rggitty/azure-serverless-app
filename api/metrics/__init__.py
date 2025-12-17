import os
import json
import time
import uuid
from datetime import datetime, timezone

import azure.functions as func

# This lives only while the function instance is warm (good enough for a demo)
START_TIME = time.time()

def main(req: func.HttpRequest) -> func.HttpResponse:
    uptime_seconds = round(time.time() - START_TIME, 3)

    payload = {
        "requestId": str(uuid.uuid4()),
        "timestampUtc": datetime.now(timezone.utc).isoformat(),
        "region": os.environ.get("REGION_NAME") or os.environ.get("WEBSITE_REGION") or "unknown",
        "deployment": {
            "repo": os.environ.get("GITHUB_REPOSITORY", "unknown"),
            "sha": os.environ.get("GITHUB_SHA", "unknown")[:12]
        },
        "runtime": {
            "python": os.environ.get("PYTHON_VERSION", "unknown"),
            "uptimeSeconds": uptime_seconds
        }
    }

    return func.HttpResponse(
        json.dumps(payload),
        status_code=200,
        mimetype="application/json"
    )
