valor1 = int(input("Ingresar el primer valor: "))
valor2 = int(input("Ingresar el segundo valor: "))

print("Los valors son iguales?",valor1==valor2)
print("Los valores son distintos?",valor1!=valor2)

print(not True)
print(not False)

string1 = input("Ingrese una palabra: ")
resultado = len(string1) > 10

print("La palabra tiene mas de 10 caracteres? ",resultado)
print("La palabra tiene: ",len(string1))

numero1 = 10
numero2 = 5
user_num = int(input("Ingrese un valor: "))
numero1 = numero1 * user_num
numero2 = numero2 + user_num
print("El nuevo valor de 1 es: ",numero1)
print("El nuevo valor de 2 es: ",numero2)


