from fastapi import FastAPI
from app.manager import Manager
import uvicorn

start = Manager()
app = FastAPI()

@app.get("/processed_data")
def get_processed_data():
    try:
        return start.run()
    except Exception as e:
        return {"error": str(e)}