from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
async def health():
    return {
        "message": "Hello!"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)