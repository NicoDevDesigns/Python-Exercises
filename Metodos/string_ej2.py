edad=input("Introduce tu edad: ");

while(edad.isdigit()==False):
    print("Por favor introduce un valor numerico");
    edad=input("Introduce tu edad: ");

if(int(edad)<18):
    print("No puedes pasar!");
else:
    print("Puedes pasar!");