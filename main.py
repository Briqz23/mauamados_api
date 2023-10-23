from fastapi import FastAPI
from routes.user_route import user_api_router
from routes.chat_route import chat_api_router

app = FastAPI()

app.include_router(user_api_router)
app.include_router(chat_api_router)