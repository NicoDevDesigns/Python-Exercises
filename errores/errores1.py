def suma(num1,num2):
    return num1+num2
def dividir(num1,num2):
    try:

     return num1/num2
    except ZeroDivisionError:
        print("No se puede divir por cero")
        return "Operacion no valida"

op1 = int(input("Ingrese el primer valor: "))
op2 = int(input("Ingrese el segundo valor: "))

operacion = input("Ingrese la operacion: ")

if operacion == suma:
    print(suma(op1,op2))
elif operacion == dividir:
    print(dividir(op1,op2))
else:
    print("Error") 

print("Ejecutandose")       