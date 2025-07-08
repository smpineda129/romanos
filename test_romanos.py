from f_romanos import de_arabigo_a_romano
from f_romanos import descomponer   

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
