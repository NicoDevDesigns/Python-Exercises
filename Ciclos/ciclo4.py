email = False;
texto = input("Ingrese una direccion de email: ");
for i in texto:
    if(i=="@"):
        email=True;
    
if(email == True):
    print("La direccion es un email");
else:
    print("La direccion no es un email");