from calculatum.datos import OPERATION

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