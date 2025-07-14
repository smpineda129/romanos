from f_romanos import de_arabigo_a_romano
from f_romanos import descomponer   
from f_romanos import de_romano_a_arabigo
import pytest 

def test_1976():
    assert de_arabigo_a_romano(1976) == "MCMLXXVI"

def test_miles():
    assert de_arabigo_a_romano(1000) == "M"

def test_centenas():
    assert de_arabigo_a_romano(900) == "CM"

def test_decenas():
    assert de_arabigo_a_romano(70) == "LXX"

def test_unidades():
    assert de_arabigo_a_romano(6) == "VI"

def test_descomponer_numeros():
    assert descomponer(1976) == [1000, 900, 70, 6]
    assert descomponer(2984) == [2000, 900, 80, 4]

"""""
Test para romano a arabigo

Existen 3 reglas basicas:
-> regla de orden: los simbolos se suman y ordenan de mayor a menor
-> regla de las restas: 
    - los simbolos i x c m pueden restar si van delante de uno mayor
    los pares:
        - V, X para I
        - L, C para X
        - D, M para C
    - Solo se puede hacer una resta por grupo (no se puede escribir IVIV)

"""""

def test_orden_decreciente_romanos():
    assert de_romano_a_arabigo("XV") == 15

"""""
Excepciones con pytest
"""""

def test_orden_creciente_error():
    with pytest.raises(ValueError) as la_variable:
        de_romano_a_arabigo("VC")
    assert "Orden Incorrecto" == str(la_variable.value)

"""""
Comprobar que solo se pueden repetir los simbolos I, X, C, M hasta un maximo de 3 veces
"""""

def test_repeticiones_max_3():

    with pytest.raises(ValueError):
        de_romano_a_arabigo("MMMMCCCCXXXXIIII")
    with pytest.raises(ValueError):
        de_romano_a_arabigo("MMMM")
    with pytest.raises(ValueError):
        de_romano_a_arabigo("CCCC")
    with pytest.raises(ValueError):
        de_romano_a_arabigo("XXXX")
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IIII")

def test_VLD_no_repeticiones():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("DD")

    with pytest.raises(ValueError):
        de_romano_a_arabigo("MMMVV")

    with pytest.raises(ValueError):
        de_romano_a_arabigo("IVV")

def test_restas_repetidas():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IVIX")

def test_restas_desordenadas():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IXCM")

def test_restas_encadenadas_deben_fallar():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IXC")

def test_940():
    assert de_romano_a_arabigo("CMXL") == 940

def test_2():
    assert de_romano_a_arabigo("II") == 2

def test_mixto_valido():
    assert de_romano_a_arabigo("MCMXLIV") == 1944  # M (1000) + CM (900) + XL (40) + IV (4)

def test_resta_invalida_IC():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IC")  # I no puede restar a C

def test_resta_invalida_IL():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IL")  # I no puede restar a L

def test_resta_invalida_XD():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("XD")  # X no puede restar a D

def test_resta_encadenada():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IXC")  # IX seguido de C (no permitido)

def test_resta_desordenada():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("XLIXC")  # Dos restas seguidas y luego otro mayor

def test_resta_repetida_I():
    with pytest.raises(ValueError):
        de_romano_a_arabigo("IVIX")  # 'I' usado dos veces como restador

