# Document Search Service

This is a FastAPI service for searching documents. It supports two types of document sources: local and Confluence.

## Setup
1. Create Python environment and install dependencies
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```
2. Create `.env` file in the root directory and add the following variables:
    ```bash
    CONFLUENCE_BASE_URL=
    CONFLUENCE_USERNAME=
    CONFLUENCE_TOKEN=
    DOCUMENT_DIRECTORY=
    ```

## Running the Service
To run the service, you need to set the `DOCUMENT_SOURCE` environment variable to either local or confluence.

Local Document Source
If you're using a local document source, run the service with:

```bash
export DOCUMENT_SOURCE=local
export DOCUMENT_DIRECTORY=/path/to/knowledge-base
python main.py
```

Confluence Document Source
If you're using a Confluence document source, run the service with:

```bash
export DOCUMENT_SOURCE=confluence
python main.py
```

The service will start and listen on http://0.0.0.0:8000. You can access the API documentation at http://localhost:8000/openapi.json.