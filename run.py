import uvicorn

from app import app

# developer mode
if __name__ == "__main__":
    uvicorn.run(app, port=8000)
