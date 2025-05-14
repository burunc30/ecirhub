from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Burunc30 is running on Render!"}
