class Vino:
    def __init__(self,volumen,precio,marca):
        self.volumen=volumen
        self.precio=precio
        self.marca=marca
    def imprimir(self):
        print("el precio es: ",self.precio)

class Cerveza:
    def __init__(self,sabor):
        self.sabor=sabor

    def imprimirCerveza(self):
     print("El gusto de la cerveza es: ",self.sabor)
        
norton=Vino(1000,200,"norton")
quilmes=Cerveza("Negra")
norton.imprimir()
quilmes.imprimirCerveza()