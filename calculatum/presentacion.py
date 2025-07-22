from roman_number import RomanNumber as rn
from calculatum.datos import OPERATION as op

def input_romano(msg: str) -> rn:
    while True:
        numero = input(msg)
        try:
            if numero.isdigit():
                numero = int(numero)
            numero = rn(numero)
            break
        except ValueError:
            print("Numero romano no valido")

        numero = rn(numero)
    return numero

def input_operaciones(msg:str) -> op:
    while True:
        cadena = input(msg)
        try:
            return op(cadena)
        except ValueError: 
            print("Cadena no valida")

def continuar_o_salir(msg: str) -> bool:
    return input(msg).lower() == "s"