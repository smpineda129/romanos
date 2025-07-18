from roman_number import RomanNumber as rn

total = rn(0)
while True:

    numero = input("Numero: ")
    num1 = rn(numero.upper())

    numero2 = input("Segundo número: ")
    num2 = rn(numero2.upper())

    operacion = input("Operación (+, -, x , /): ")
    if operacion == "+":
      resultado = num1 + num2
    elif operacion == '-':
       resultado = num1 - num2
    elif operacion == 'x':
       resultado =  num1 * num2
    else:
       resultado =  num1 / num2

    print(f"Resultado: {resultado}")


    seguir = input("Otro calculo (s/n)? ")
    if seguir.lower() == 's':
      total = total + resultado
      print(f"Total acumulado = {total}")
    else:
      print(f'El resultado total es : {total}')
      print("Hasta luego")
      break