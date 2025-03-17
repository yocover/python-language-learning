from fastapi import FastAPI

app = FastAPI()

print("Hello World")

@app.get("/")
async def root():
    return {"message": "Hello World"} 