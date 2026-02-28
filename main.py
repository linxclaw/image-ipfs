from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
import requests
from io import BytesIO
import os
import mimetypes

app = FastAPI()

UPLOAD_URL = "https://www.clanker.world/api/ipfs/upload"
MAX_SIZE = 1 * 1024 * 1024 


class UploadFromURL(BaseModel):
    file_url: HttpUrl


@app.post("/upload-from-url")
def upload_from_url(payload: UploadFromURL):
    r = requests.get(payload.file_url, stream=True, timeout=20)
    if r.status_code != 200:
        raise HTTPException(status_code=400, detail="Failed to download file")

    content = r.content
    size = len(content)

    if size > MAX_SIZE:
        raise HTTPException(status_code=413, detail="File exceeds 1MB limit")

    filename = os.path.basename(str(payload.file_url).split("?")[0]) or "upload.bin"

    content_type = r.headers.get("Content-Type")
    if not content_type:
        content_type = mimetypes.guess_type(filename)[0] or "application/octet-stream"

    files = {
        "file": (filename, BytesIO(content), content_type)
    }

    upload_resp = requests.post(UPLOAD_URL, files=files)

    return {
        "status_code": upload_resp.status_code,
        "response": upload_resp.json() if upload_resp.headers.get("content-type", "").startswith("application/json") else upload_resp.text
    }
