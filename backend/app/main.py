from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1 import cashback
from app.core.database import engine, Base

# Cria as tabelas do banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Cashback API")

# Setup CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas
app.include_router(cashback.router, tags=["Cashback"])

@app.get("/")
def root():
    return {"message": "Cashback API is running"}
