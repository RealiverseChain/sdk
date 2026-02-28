from fastapi import FastAPI
from api.routes import router

app = FastAPI(title="Realiverse API")

app.include_router(router)
