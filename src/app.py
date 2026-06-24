from fastapi import FastAPI
from src.core.conf import settings


def create_app() -> FastAPI:
    app = FastAPI(
        debug=settings.DEBUG,
        title=settings.APP_NAME,
        version="0.1.0",
        description="create short link"
    )

    @app.get("/health")
    async def health_check():
        return {"status": "ok", "service": settings.APP_NAME}

    return app

app = create_app()
