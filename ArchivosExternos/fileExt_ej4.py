from io import open 

file = open("datosAE.txt","r");

print(file.read(6));#el numero posiciona el puntero hasta donde lee
file.seek(2);#posiciona el puntero hasta el lugar donde se quiere
print(file.read());

file.seek(0);
file.seek(len(file.read())/2);
print(file.read());

file.seek(0);
print(file.readline());
