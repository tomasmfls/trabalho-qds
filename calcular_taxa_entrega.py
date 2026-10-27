def calcular_taxa_entrega(distancia_km, total_pedido):
    """Calcula a taxa de entrega conforme a distância e o valor do pedido."""
    if total_pedido >= 100:
        return 0.0

    if distancia_km <= 3:
        return 5.0

    return 5.0 + (distancia_km - 3) * 2.0
