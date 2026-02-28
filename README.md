Image-IPFS Upload Service
=========================

A FastAPI service that accepts a file URL, downloads the file, validates its size
(maximum 1MB), and uploads it to an IPFS upload endpoint.

This service is designed for proxying external files into IPFS without writing
anything to disk.

Repository:
https://github.com/linxclaw/image-ipfs

thanks to: https://www.clanker.world/

------------------------------------------------------------

Features
--------

- Upload file to IPFS from a public URL
- Enforces maximum file size of 1MB
- In-memory streaming (no disk writes)
- Uses multipart/form-data
- Automatic filename and MIME type detection
- Built with FastAPI

------------------------------------------------------------

Tech Stack
----------

- Python 3.9 or newer
- FastAPI
- Uvicorn
- Requests
- Pydantic

------------------------------------------------------------

Installation
------------

1. Clone the repository

    git clone https://github.com/linxclaw/image-ipfs
    cd image-ipfs

2. Create and activate a virtual environment (optional)

    python -m venv venv
   
    source venv/bin/activate    (Linux / macOS)
   
    venv\Scripts\activate       (Windows)

4. Install dependencies

    pip install -r requirements.txt

------------------------------------------------------------

Running the Server
------------------

    uvicorn main:app --reload --host 0.0.0.0 --port 8000

Once running, the API will be available at:

    http://localhost:8000

------------------------------------------------------------

API Endpoint
------------

POST /upload-from-url

Uploads a file to IPFS using a public file URL.

Request Body (JSON):

    {
      "file_url": "https://example.com/image.png"
    }

Error Responses:

- 400 : Failed to download file
- 413 : File exceeds 1MB limit

------------------------------------------------------------

Testing with cURL
-----------------

    curl -X POST http://localhost:8000/upload-from-url \
      -H "Content-Type: application/json" \
      -d '{
        "file_url": "https://example.com/image.png"
      }'

------------------------------------------------------------

Notes
-----

- Files are never stored on disk
- Upload field name is assumed to be "file"
- No authentication headers are included by default
- File size limit is strictly enforced

------------------------------------------------------------

License
-------

Creative Commons Attribution 4.0 International (CC BY 4.0)

You are free to:
- Share — copy and redistribute the material in any medium or format
- Adapt — remix, transform, and build upon the material for any purpose

Under the following terms:
- Attribution — You must give appropriate credit, provide a link to the license,
  and indicate if changes were made.

License details:
https://creativecommons.org/licenses/by/4.0/
