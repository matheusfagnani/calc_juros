import pytest 
from calculadora_juros import calcular_juros_compostos


def test_calcular_juros_compostos(capital_investido, taxa_juros, tempo):
    #  valores valido
    capital_investido = 1000.0
    taxa_juros = 5.0
    tempo = 2  
    juros, montante = calcular_juros_compostos(capital_investido, taxa_juros, tempo)
    assert juros == pytest.approx(102.5, rel=1e-9)
    assert montante == pytest.approx(1102.5, rel=1e-9)

    # Teste com capital investido negativo
    with pytest.raises(ValueError, match="O capital investido não pode ser negativo."):
        calcular_juros_compostos(-1000.0, taxa_juros, tempo)   
    # Teste com taxa de juros negativa  
    with pytest.raises(ValueError, match="A taxa de juros não pode ser negativa."):
        calcular_juros_compostos(capital_investido, -5.0, tempo)             
            



    
    
