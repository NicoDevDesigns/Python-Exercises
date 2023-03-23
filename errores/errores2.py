try:
    c= int(input("Ingrese un valor: "))
    c/0
except:
    print("Error")

try:
    a= int(input("Ingrese segundo valor: "))
    a/0
except ValueError:
    print("Error! Ingresar un numero")
except Exception as a:
    print(type(a).__name__)