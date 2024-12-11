from fastapi import FastAPI
from rotas import webhook as webhook_router

app = FastAPI()

app.include_router(webhook_router.router, prefix="/webhook", tags=["webhook"])