"""Main module"""
from fastapi import FastAPI
from pydantic import BaseModel
from .settings import settings

print(settings.main_url)
app = FastAPI()

class Status(BaseModel):
    """class Status"""
    status: str = "ok"

@app.get(settings.main_url)
async def status():
    """function Status"""
    return Status()
