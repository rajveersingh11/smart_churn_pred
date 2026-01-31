from fastapi import FastAPI

from app.api import churn, auth, health
from app.core.logging import setup_logger
from app.core.config import validate_config


# Setup Logging (FIRST)


logger = setup_logger()
logger.info("Churn API Started")


# Validate Config

validate_config()


# Create App


def create_app():

    app = FastAPI(
        title="Smart Churn Prediction API",
        version="1.0"
    )

    app.include_router(auth.router, prefix="/auth")
    app.include_router(churn.router, prefix="/churn")
    app.include_router(health.router, prefix="/health")

    return app


app = create_app()


# Run Server (Local Only)

if __name__ == "__main__":

    import uvicorn

    uvicorn.run("app.main:app", reload=True)
