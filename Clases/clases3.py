class Coche():
    def __init__(self):
        self.marca = "Audi"
        self.color = "Rojo"
        self.__ruedas = 4
        self.enmarcha = False

    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos
        if(self.enmarcha):
            return "El coche esta en marcha"
        else:
            return "El coche se encuentra apagado"
        
    def __str__(self):
        return "Este auto es marca {}, de color {} y tiene {} ruedas".format(self.marca,self.color,self.__ruedas)

miCoche = Coche()
print(str(miCoche))
print(miCoche.arrancar(True))

print("******Coche nuevo**********")
miCoche2=Coche()
miCoche2.__ruedas =5
miCoche2.color="Verde"
print(str(miCoche2))
