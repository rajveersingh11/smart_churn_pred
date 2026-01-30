from fastapi import FastAPI

from app.api import churn, auth, health

def creat_app():

    app = FastAPI(
        titel="Smart Churn Prediction API",
        version="1.0"
    )

    app.include_router(auth.router, prefix="/auth")
    app.include_router(churn.router, prefix="/churn")
    app.include_router(health.router, prefix="/health")

    return app

app = creat_app()

if __name__ == "__main__":

    import uvicorn
    uvicorn.run("app.main:app", reload=True)