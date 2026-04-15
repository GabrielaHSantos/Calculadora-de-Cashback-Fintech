from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.cashback import CashbackRequest, CashbackResponse, ConsultaHistorico
from app.models.consulta import ConsultaCashback
from app.services.cashback_service import calcular_cashback
from typing import List

router = APIRouter()

@router.post("/calcular", response_model=CashbackResponse)
def calcular_e_salvar(req: CashbackRequest, request: Request, db: Session = Depends(get_db)):
    # Pega o IP real do cliente (importante para o Docker usar o header X-Forwarded-For se tiver proxy)
    ip_usuario = request.headers.get("X-Forwarded-For", request.client.host if request.client else "unknown")
    
    # Calcular
    resultado = calcular_cashback(
        tipo_cliente=req.tipo_cliente,
        valor_compra=req.valor_compra,
        desconto_pct=req.desconto_pct
    )
    
    # Salvar no DB
    nova_consulta = ConsultaCashback(
        ip_usuario=ip_usuario,
        tipo_cliente=req.tipo_cliente,
        valor_compra=resultado["valor_compra"],
        desconto_pct=resultado["desconto_pct"],
        valor_final=resultado["valor_final"],
        cashback=resultado["cashback"]
    )
    db.add(nova_consulta)
    db.commit()
    db.refresh(nova_consulta)
    
    return resultado

@router.get("/historico", response_model=List[ConsultaHistorico])
def listar_historico(request: Request, db: Session = Depends(get_db)):
    ip_usuario = request.headers.get("X-Forwarded-For", request.client.host if request.client else "unknown")
    consultas = db.query(ConsultaCashback).filter(ConsultaCashback.ip_usuario == ip_usuario).order_by(ConsultaCashback.criado_em.desc()).all()
    return consultas
