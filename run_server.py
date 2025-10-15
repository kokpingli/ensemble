"""Quick script to test the API server locally."""

import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.presentation.main:app", host="127.0.0.1", port=8000, reload=True)
