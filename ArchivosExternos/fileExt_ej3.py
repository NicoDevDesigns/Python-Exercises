from io import open

file = open("datosAE.txt","a");

textoAgregar=" Hoy me veo una peli";

file.write(textoAgregar);

file.close();

