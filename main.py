from fastapi import FastAPI
from routes.user_route import user_api_router

app = FastAPI()

app.include_router(user_api_router)