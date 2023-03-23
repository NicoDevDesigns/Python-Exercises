#Comparador de numeros

print('Comparador de numeros');

num1=int(input('Ingrese el primer numero: '));
num2=int(input('Ingrese el segundo numero: '));

if num1>num2:
    print('El primero es mayor'+str(num1));
elif num1<num2:
    print('El segundo es mayor'+str(num2));
else:
    print('Los numeros son iguales');
