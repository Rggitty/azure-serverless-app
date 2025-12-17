import os
import json
import logging
import azure.functions as func
from azure.storage.blob import BlobServiceClient

CONTAINER_NAME = "appdata"
BLOB_NAME = "status.json"

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # IMPORTANT: we'll store the Storage connection string in this setting
        conn_str = os.environ.get("STORAGE_CONN_STR")
        if not conn_str:
            return func.HttpResponse("Missing STORAGE_CONN_STR app setting", status_code=500)

        bsc = BlobServiceClient.from_connection_string(conn_str)
        blob_client = bsc.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

        data = blob_client.download_blob().readall()
        payload = json.loads(data)

        return func.HttpResponse(
            json.dumps(payload),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.exception("Failed to load status.json from blob storage")
        return func.HttpResponse(f"Error: {str(e)}", status_code=500)
