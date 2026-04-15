from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CashbackRequest(BaseModel):
    tipo_cliente: str
    valor_compra: float
    desconto_pct: Optional[float] = 0.0

class CashbackResponse(BaseModel):
    valor_compra: float
    desconto_pct: float
    valor_final: float
    cashback: float

class ConsultaHistorico(BaseModel):
    tipo_cliente: str
    valor_compra: float
    desconto_pct: float
    valor_final: float
    cashback: float
    criado_em: datetime

    model_config = {
        "from_attributes": True
    }
