class Vehiculo():
    def __init__(self,potencia,marca):
        self.potencia=potencia
        self.marca=marca
    
    def imprimirCaracteristicas(self):
        print("La marca es: ",self.marca,"La potencia es: ",self.potencia)

class Moto(Vehiculo):
    def __init__(self,marcaMoto,potenciaMoto,color):
        super().__init__(potenciaMoto,marcaMoto)
        self.color=color
    def imprimirCarateristicas(self):
        super().imprimirCaracteristicas()
        print("El color: ",self.color)

class Auto(Vehiculo):
    def __init__(self,marcaAuto,potenciaAuto,puertas):
        super().__init__(potenciaAuto,marcaAuto)
        self.puertas=puertas
    def imprimir(self):
        super().imprimirCaracteristicas()
        print("La cantidad de puertas son: ",self.puertas)

patagonia = Moto("patagonia eagle",150,"Negro")
patagonia.imprimirCarateristicas()
fordFocus = Auto("Focus",200,5)
fordFocus.imprimir()