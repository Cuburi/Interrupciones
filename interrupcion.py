def suma(num1, num2):
    return num1+num2

def resta(num1, num2):
    return num1-num2

def multiplicacion(num1, num2):
    return  num1*num2

def divicion(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        print("No se puede divir entre 0. \nSe genero interrupción")

try:
    op1=(int(input("Introduce el primer número: ")))

    op2=(int(input("Introduce el segundo número: ")))

    operacion = input("Introduce la operación a realizar (suma,resta,multiplicacion,divicion):")

    if (operacion == "suma"):
        print(suma(op1, op2))

    elif (operacion == "resta"):
        print(resta(op1, op2))

    elif (operacion == "multiplicacion"):
        print(multiplicacion(op1, op2))

    elif (operacion == "divicion"):
        print(divicion(op1, op2))

    else:
        print("Operación invalida")

except ValueError:
    print("Los valores introducidos no son correctos \nSe genero interrupción")


print("Calculo finalizado.")