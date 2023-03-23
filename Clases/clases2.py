class Persona:
    def __init__(self,nombre,edad,sexo):
     self.nombre=nombre
     self.edad=edad
     self.sexo=sexo

    def datosPersonales(self):
        print("El nombre es ",self.nombre)
        print("La edad es: "+self.edad)
        print("El sexo es: ",self.sexo)

    def calculoPeso(self):
            peso = 10*self.edad
            print("El peso es: ",peso)

miPersona = Persona("Nicolas","35","Masculino")
miPersona2 = Persona("Veronica","35","femenino")
mipersona3=Persona("Jorge",33,"Masculino")

miPersona.datosPersonales()
miPersona.datosPersonales()
mipersona3.calculoPeso()


