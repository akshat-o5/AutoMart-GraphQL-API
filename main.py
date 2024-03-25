from fastapi import FastAPI
from app.routes import router

app = FastAPI()

app.include_router(router)










# API Documentation: https://documenter.getpostman.com/view/23129267/2sA35Bd4zW