from io import open

archivo=open("datosAE.txt","r");

leer = archivo.read();

archivo.close();

print(leer);