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

orden_romano = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

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
    repeticiones = 1
    restadores_usados = set()  # Aquí guardamos los símbolos que ya han sido usados en una resta

    for i, letra in enumerate(romano):
        if letra in diccionario:
            valor_actual = diccionario[letra]
            ultimo_par = cadena_max_2(ultimo_par, letra)

            if ultimo_par in ("IV", "IX", "XL", "XC", "CD", "CM"):
                restador = ultimo_par[0]  # El símbolo que está restando

                if restador in restadores_usados:
                    raise ValueError("No se permiten restas repetidas con el mismo símbolo")

                restadores_usados.add(restador)

                if i + 1 < len(romano):
                    siguiente = romano[i + 1]
                    if orden_romano.index(siguiente) > orden_romano.index(letra):
                        raise ValueError("No se permite encadenar restas o símbolos mayores después de una resta")

            repeticiones = contador_repeticiones_max_3(valor_actual, anterior, repeticiones, letra)
            resultado, anterior = calcula_numero(anterior, valor_actual, ultimo_par, resultado, letra)
        else:
            raise ValueError("Símbolo no permitido")

    return resultado

    
def cadena_max_2(cadena: str, letra: str) -> str:
    cadena += letra
    if len(cadena) > 2:
        return cadena[-2:]
    else:
        return cadena
    
def contador_repeticiones_max_3(valor_actual: int, anterior: int, repeticiones: int, letra: str) -> int:
    if valor_actual == anterior:
        repeticiones += 1
        if letra in ("V", "L", "D") and repeticiones > 1 or repeticiones > 3:
            raise ValueError(f"No se admiten mas de {repeticiones - 1} repeticiones de {letra}")
    else:
        repeticiones = 1
    return repeticiones 

def calcula_numero(anterior: int, valor_actual: int, ultimo_par: str, resultado: int, letra:str) -> tuple[int, int]:
    if anterior > 0 and valor_actual > anterior:
        resultado, anterior = valida_resta(ultimo_par, resultado, anterior, letra) # Valida si es resta valida
    else:
        resultado += valor_actual
        anterior = valor_actual
    return resultado, anterior

def valida_resta(cadena: str, resultado: int, anterior: int, letra:str) -> tuple[int, int]:
    if cadena in diccionario:
        resultado = (resultado - anterior) + diccionario[cadena]
        anterior = diccionario[cadena]
        return resultado, anterior
    else:
        raise ValueError("Orden Incorrecto")