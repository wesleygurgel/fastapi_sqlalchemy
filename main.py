from fastapi import FastAPI
from core.configs import settings
from api.v1.api import api_router


app = FastAPI(title='Cursos API - FastAPI + SQLAlchemy')
app.include_router(api_router, prefix=settings.API_V1_STR)

# /api/v1/imovel
# /api/v1/carteira


if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8001, log_level='info', reload=True)