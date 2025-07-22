from calculatum.datos import OPERATION, rn
from calculatum.presentacion import input_operaciones, input_romano, continuar_o_salir

def calcular(num1, num2, operacion):
    if operacion == OPERATION.ADD:
      resultado = num1 + num2
    elif operacion == OPERATION.SUB:
       resultado = num1 - num2
    elif operacion == OPERATION.MUL:
       resultado =  num1 * num2
    elif operacion == OPERATION.DIV:
       resultado =  num1 / num2
    
    return resultado

def mainLoop():
   total = rn(0)
   while True:

      numero = input_romano("Numero: ")
      numero2 = input_romano("Segundo número: ")
      operacion = input_operaciones("Operación (+, -, x , /): ")
      resultado = calcular(numero, numero2, operacion)

      print(f"Resultado: {resultado}")

      total = total + resultado
      if not continuar_o_salir("Otro calculo (s/n)? "):
         break

      print(f"Total acumulado = {total}")

   print("Hasta luego")
   print(f'El resultado total es : {total}')