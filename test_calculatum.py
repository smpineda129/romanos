import random
from roman_number import RomanNumber as rn
from calculatum.presentacion import input_romano, input_operaciones, continuar_o_salir
from calculatum.datos import OPERATION
from calculatum.logica import calcular
import pytest

@pytest.mark.parametrize(
    "lista_entradas, result",
    [
        (["I"], rn(1)),
        (["XII"], rn(12)),
        (["12"], rn(12)),
    ]
)

def test_input_romano(monkeypatch, lista_entradas, result):
    entradas = iter(lista_entradas)
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    assert input_romano("") == result

@pytest.mark.parametrize(
    "lista_entradas, result",
    [
        (["+"], OPERATION.ADD),
        (["-"], OPERATION.SUB),
        (["x"], OPERATION.MUL),
        (["/"], OPERATION.DIV),
        (["*", "x"], OPERATION.MUL),
    ]
)

def test_input_operaciones(monkeypatch, lista_entradas, result):
    entradas = iter(lista_entradas)
    monkeypatch.setattr("builtins.input", lambda _: next(entradas))
    assert input_operaciones("") == result

def test_varios_inputs_romanos(monkeypatch):
    entradas = iter(["XII"])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    assert input_romano("Numero") == rn(12)
    
@pytest.mark.parametrize(
    "num1, num2, op, result",
    [
        (rn(10), rn(5), OPERATION.ADD, rn(15)),
        (rn(10), rn(5), OPERATION.SUB, rn(5)),
        (rn(10), rn(5), OPERATION.MUL, rn(50)),
        (rn(10), rn(5), OPERATION.DIV, rn(2)),
    ]
)

def test_calculos(num1, num2, op, result):
    assert calcular(num1, num2, op) == result
    
@pytest.mark.parametrize(
    "respuesta, resultado",
    [
        ("S", True),
        ("s", True),
        ("N", False),
        ("n", False),
        ("12", False),
    ]
)

def test_continue(monkeypatch, respuesta, resultado):
    monkeypatch.setattr("builtins.input", lambda _: respuesta)
    continuar_o_salir("") == resultado
    