from cProfile import label
from tkinter import*

#creacion de raiz
root=Tk();
#Creacion del frame
miFrame=Frame(root,width=500,height=400);
miFrame.pack();#Encasulamiento
#Creacion del label texto
miLabel=Label(miFrame, text="Hola mundo soy Nico",fg="red",font=("Comic Sans MS",40));
miLabel.place(x=100,y=200);#posicionamiento del label
#Label(miFrame, text="Hola mundo soy Nico").place(x=100,y=200);#Lo mismo que lo anterior pero menos codigo en caso de no usar label

#Creacion de label imagen
#miImagen=PhotoImage(file="ejemplo.png");
#Label(miFrame,image=miImagen).place(x=100,y=200);

root.mainloop();#Bucle
