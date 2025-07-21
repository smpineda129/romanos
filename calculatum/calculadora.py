from roman_number import RomanNumber as rn
from calculatum.presentacion import input_romano, input_operaciones
from calculatum.logica import calcular

total = rn(0)
while True:

    numero = input_romano("Numero: ")
    numero2 = input_romano("Segundo número: ")
    operacion = input_operaciones("Operación (+, -, x , /): ")
    
    resultado = calcular(numero, numero2, operacion)

    print(f"Resultado: {resultado}")


    seguir = input("Otro calculo (s/n)? ")
    if seguir.lower() == 's':
      total = total + resultado
      print(f"Total acumulado = {total}")
    else:
      print(f'El resultado total es : {total}')
      print("Hasta luego")
      break