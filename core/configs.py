# Configurações Gerais
from importlib.machinery import DEBUG_BYTECODE_SUFFIXES
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


# Simulaçao do Settings do Django
class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação.
    """
    
    API_V1_STR: str = '/api/v1'
    DB_URL: str = "postgresql+asyncpg://postgres:root@localhost:5432/postgres"
    DBBaseModel = declarative_base()
    
    
    class Config:
        case_sensitive = True
        
        
settings = Settings()