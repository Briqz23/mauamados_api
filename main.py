from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.user_route import user_api_router
from routes.chat_route import chat_api_router

app = FastAPI()

app.include_router(user_api_router)
app.include_router(chat_api_router)

origins = [
    "http://localhost",
    "http://localhost:8080",
    # Add more allowed origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
