class Auto():
    def __init__(self):
        self.enMarcha= False
        self.color="Verde"
        self.puertas=0

    def datosEntregados(self,arrancar,colorAuto,CantPuertas):
        self.enMarcha=arrancar
        self.color=colorAuto
        self.puertas=CantPuertas

        if(self.enMarcha):
            print("El auto esta en marcha")
        else:
            print("El auto no arranca")

miAuto = Auto()
miAuto.datosEntregados(True,"Azul",5)

    
