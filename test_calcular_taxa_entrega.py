from calcular_taxa_entrega import calcular_taxa_entrega


def test_entrega_ate_3_km_custa_5_reais():
    assert calcular_taxa_entrega(2, 50) == 5.0


def test_entrega_acima_de_3_km_acrescenta_2_reais_por_km_excedente():
    assert calcular_taxa_entrega(4, 50) == 7.0


def test_pedido_a_partir_de_100_reais_tem_entrega_gratuita():
    assert calcular_taxa_entrega(5, 100) == 0.0
