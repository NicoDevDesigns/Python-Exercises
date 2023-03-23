from cProfile import label
from cgitb import text
from sqlite3 import Row
from tkinter import*
raiz= Tk();
miFrame=Frame(raiz, width=1200,height=600)
miFrame.pack();
miNombre=StringVar();

cuadroNombre = Entry(miFrame,textvariable=miNombre);
cuadroNombre.grid(row=0,column=1);
cuadroApellido = Entry(miFrame);
cuadroApellido.grid(row=1,column=1);
cuadroDireccion = Entry(miFrame);
cuadroDireccion.grid(row=2,column=1);
cuadroPass = Entry(miFrame);
cuadroPass.grid(row=3,column=1);
textoCometario=Text(miFrame,width=16,height=5);
textoCometario.grid(row=4,column=1,padx=10,pady=10);
scrollVertical=Scrollbar(miFrame,command=textoCometario.yview);
scrollVertical.grid(row=4,column=2,sticky="nsew");
textoCometario.config(yscrollcommand=scrollVertical.set);


nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0,column=0,sticky="e",padx=10,pady=10);
apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1,column=0,sticky="e",padx=10,pady=10);
direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=2,column=0,sticky="e",padx=10,pady=10);
passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=3,column=0,sticky="e",padx=10,pady=10);
comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4,column=0,sticky="e",padx=10,pady=10);

def codigoBoton():
     miNombre.set("Nico");

botonEnvio=Button(raiz,text="Enviar",command=codigoBoton);
botonEnvio.pack();



raiz.mainloop()
