while True:
    edad = int(input("Cual es tu edad: "))
    salario =int(input("Cual es tu salario: "))
    if edad > 18 and salario > 1000 :
        print("Ingreso al sistema")
        break;
    print("No se le permite el ingreso!")
    print("Ingrese los datos nuevamente.....")