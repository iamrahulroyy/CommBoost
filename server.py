import logging 
from fastapi import FastAPI
from helper.modelsApi import router

app = FastAPI()

logging.basicConfig(level=logging.INFO)

app.include_router(router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)