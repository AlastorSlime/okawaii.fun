from app import create_app

if __name__ == '__main__':
    import uvicorn

    app = create_app()
    uvicorn.run(
        app,
        host="0.0.0.0", # For production.
    )
