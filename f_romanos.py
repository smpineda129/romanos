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

def de_romano_a_arabigo(romano: str) -> int:
    resultado = 0
    anterior = 0
    ultimo_par = ""
    for letra in romano:
        if letra in diccionario:
            valor_actual = diccionario[letra]
            ultimo_par += letra
            if len(ultimo_par) > 2:
                ultimo_par = ultimo_par[-2:]
            if anterior > 0 and valor_actual > anterior:
                resultado, anterior = valida_resta(ultimo_par, resultado, anterior)
            else:
                resultado += valor_actual
                anterior = valor_actual
        else:
            raise ValueError("Símbolo no permitido")
    return resultado

def valida_resta(cadena: str, resultado: int, anterior: int) -> tuple[int, int]:
    if cadena in diccionario:
        resultado = (resultado - anterior) + diccionario[cadena]
        anterior = diccionario[cadena]
        return resultado, anterior
    else:
        raise ValueError("Orden Incorrecto")

        