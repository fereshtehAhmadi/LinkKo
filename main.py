import uvicorn
from src.core.conf import settings


def main():

    uvicorn.run(
        app="src.app:app",
        host=settings.APP_HOST,
        port=settings.APP_PORT,
        reload=settings.RELOAD,
    )


if __name__ == "__main__":
    main()

