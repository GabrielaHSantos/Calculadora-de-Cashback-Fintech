from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class ConsultaCashback(Base):
    __tablename__ = "consultas_cashback"
    
    id = Column(Integer, primary_key=True, index=True)
    ip_usuario = Column(String, index=True)
    tipo_cliente = Column(String)
    valor_compra = Column(Float)
    desconto_pct = Column(Float)
    valor_final = Column(Float)
    cashback = Column(Float)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())
