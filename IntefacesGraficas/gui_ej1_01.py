from tkinter import *

raiz=Tk()
raiz.title("Hola nico, soy el Mundo")

raiz.config(bg="red")
raiz.config(bd=22)
#raiz.config(relief="groove")
raiz.config(cursor="hand2")
raiz.geometry("700x500")

miFrame=Frame()
miFrame.pack(side="top",anchor="n")
miFrame.config(bg="blue")
miFrame.config(width="650",height="350")
miFrame.config(bd=40)
#miFrame.config(relief="sunken")
miFrame.config(cursor="pirate")

raiz=mainloop()