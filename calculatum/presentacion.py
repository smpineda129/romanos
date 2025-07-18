from roman_number import RomanNumber as rn

def input_romano(msg: str) -> rn:
    while True:
        numero = input(msg)
        try:
            numero = rn(numero)
            break
        except ValueError:
            print("Numero romano no valido")

        numero = rn(numero)
    return numero