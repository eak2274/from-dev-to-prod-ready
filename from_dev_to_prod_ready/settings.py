"""
Settings
"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """class Settings"""
    main_url: str

settings = Settings()
