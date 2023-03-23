from tkinter import *

#Creacion de raiz
raiz = Tk();
raiz.title("Hola nico");
#raiz.resizable(True,False);

#raiz.iconbitmap("michi.ico");
#raiz.geometry("500x400");
raiz.config(bg="red");
raiz.config(bd=20);#Dimension del borde
raiz.config(relief="groove");#Estilo del borde
raiz.config(cursor="hand2");#Estilo del cursor

#creacion de frame
miFrame=Frame();#Construir el frame
miFrame.pack(side="top",anchor="n");#Empaquetar o meterlo dentro de la raiz/posicionamiento del frame
miFrame.config(bg="blue");#color del frame
miFrame.config(width="650",height="350");#dimensiones del frame
miFrame.config(bd=40);#Dimension del borde
miFrame.config(relief="sunken");#Estilo del borde
miFrame.config(cursor="pirate");#Estilo del cursor

raiz.mainloop();
 