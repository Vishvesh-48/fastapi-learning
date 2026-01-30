from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "My first FastAPI server is running 🎉"}

@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/doc")
def doc():
    return {"status": "Welcome to the doc"}