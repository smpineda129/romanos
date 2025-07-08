diccionario = {
    "M": 1000,
    "CM": 900,
    "DCCC": 800,
    "DCC": 700,
    "DC": 600,
    "D": 500,
    "CD": 400,
    "CCC": 300,
    "CC": 200,
    "C": 100,
    "XC": 90,
    "LXXX": 80,
    "LXX": 70,
    "LX": 60,
    "L": 50,
    "XL": 40,
    "XXX": 30,
    "XX": 20,
    "X": 10,
    "IX": 9,
    "VIII": 8,
    "VII": 7,
    "VI": 6,
    "V": 5,
    "IV": 4,
    "III": 3,
    "II": 2,
    "I": 1,
}

def de_arabigo_a_romano(n: int) -> str:
    componentes = descomponer(n)
    resultado = ""
    for n in componentes:
        for clave, valor in diccionario.items():
            if valor == n:
                resultado += clave
    return resultado

def descomponer(n: int) -> list:
    resultado = []
    opera = [1000, 100, 10]
    for valor in opera:
        if n >= valor:
            unidad = (n // valor) * valor
            resultado.append(unidad)
            n = n % valor
    resultado.append(n)
    return resultado

        