import pytest
from app.services.cashback_service import calcular_cashback

def test_questao_1_vip_com_cupom_20():
    # 2) VIP comprar um produto de R$ 600 usando um cupom de 20% off
    resultado = calcular_cashback("VIP", 600, 20)
    assert resultado["valor_final"] == 480
    assert resultado["cashback"] == 26.40

def test_questao_2_regular_com_cupom_10():
    # 3) Cliente comprar um produto de R$ 600 usando um cupom de 10% off
    resultado = calcular_cashback("Regular", 600, 10)
    assert resultado["valor_final"] == 540
    # Base = 5% de 540 = 27. Maior que 500, então dobra: 54
    assert resultado["cashback"] == 54.0

def test_questao_3_suporte_vip_reclamacao():
    # 4) VIP comprou um produto de R$ 600 usando um cupom de 15% off. Recebeu 56.
    resultado = calcular_cashback("VIP", 600, 15)
    assert resultado["valor_final"] == 510
    # Base: 510 * 5% = 25.5
    # VIP Bonus: 10% sobre 25.5 = 2.55. Total base: 28.05
    # Dobro (>500): 28.05 * 2 = 56.10
    assert resultado["cashback"] == 56.10
