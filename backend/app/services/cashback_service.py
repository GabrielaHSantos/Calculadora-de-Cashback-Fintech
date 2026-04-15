def calcular_cashback(tipo_cliente: str, valor_compra: float, desconto_pct: float) -> dict:
    """
    Calcula o cashback com base nas regras:
    1. Base: 5% sobre o valor final.
    2. VIP: +10% sobre o valor do cashback base.
    3. Promoção: Dobro de cashback se valor > 500.
    """
    # 1. Valor Final
    desconto_valor = valor_compra * (desconto_pct / 100)
    valor_final = valor_compra - desconto_valor
    
    # 2. Cashback Base (5%)
    cashback_base = valor_final * 0.05
    
    # 3. Adicional VIP (10% sobre o base)
    cashback_vip = 0.0
    if tipo_cliente.upper() == "VIP":
        cashback_vip = cashback_base * 0.10
        
    cashback_total = cashback_base + cashback_vip
    
    # 4. Regra Diretoria: Dobro se > 500 
    # (Aplica sobre o total do cashback, já que o email diz "dobro de cashback para todos")
    if valor_final > 500:
        cashback_total *= 2
        
    return {
        "valor_compra": round(valor_compra, 2),
        "desconto_pct": round(desconto_pct, 2),
        "valor_final": round(valor_final, 2),
        "cashback": round(cashback_total, 2)
    }
