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

    # Teste com tempo negativo
        with pytest.raises(ValueError, match="O tempo não pode ser negativo."):
            calcular_juros_compostos(capital_investido, taxa_juros, -2)   

    # test com valores com texto

    # capital_investido como texto
    with pytest.raises(TypeError, match="O capital investido deve ser um número \(int ou float\)."):
        calcular_juros_compostos("mil", taxa_juros, tempo)
    
    # taxa_juros como texto
    with pytest.raises(TypeError,match="O capital investido deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital_investido, "cinco", tempo)

    # tempo como texto
    with pytest.raises(TypeError, match="O tempo deve ser um número \(int ou float\)."):
        calcular_juros_compostos(capital_investido, taxa_juros, "dois")



            



    
    
