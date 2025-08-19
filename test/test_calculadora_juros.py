import pytest 
from calculadora_juros import calcular_juros_compostos


def test_calcular_juros_compostos():
    # Teste com valores válidos
    capital_investido = 1000.0
    taxa_juros = 5.0
    tempo = 2
    juros, montante = calcular_juros_compostos(capital_investido, taxa_juros, tempo)
    assert juros == pytest.approx(102.5, rel=1e-9)
