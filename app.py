from logging_demo import create_app

app = create_app()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(host="0.0.0.0", port=8000, reload=True, app="app:app")
