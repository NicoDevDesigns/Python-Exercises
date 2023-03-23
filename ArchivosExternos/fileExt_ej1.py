from io import open

archivo_texto=open("datosAE.txt","w");
texto="Hoy es un buen dia para dormir";
archivo_texto.write(texto);
archivo_texto.close();
