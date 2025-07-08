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
    assert "orden incorrecto" == str(la_variable.value)