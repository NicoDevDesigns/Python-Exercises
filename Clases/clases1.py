#clase y objetos
class Gelatina:
    def __init__(self,sabor,color,tamaño):
        self.sabor=sabor
        self.color=color
        self.tamaño=tamaño

    def imprimir(self):
        print("El sabor es "+self.sabor)
        print("El color es "+self.color)
        print("el tamaño es "+self.tamaño)

gel1 = Gelatina("amago","azul","grande")
gel2 = Gelatina("dulce","rosa","mediano")

gel1.imprimir()
gel2.imprimir()