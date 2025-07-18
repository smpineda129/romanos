import random
from roman_number import RomanNumber as rn
from calculatum.presentacion import input_romano

def test_input_romano(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "I")
    assert input_romano("Numero") == rn(1)

def test_varios_inputs_romanos(monkeypatch):
    entradas = iter(["doce", "-1", "XII"])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    assert input_romano("Numero") == rn(12)