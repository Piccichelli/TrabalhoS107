import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api:app", port=7999, reload=True)