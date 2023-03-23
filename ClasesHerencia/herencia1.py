class persona:
    def __init__(self,nombre,edad,sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo

    def datosPersonales(self):
        print("El nombre es ",self.nombre)
        print("La edad es: ",self.edad)
        print("El sexo es: ",self.sexo)

miPersona = persona("Nicolas",35,"Masculino")
miPersona.datosPersonales()

print("***********************")

class empleado(persona):
    def datosEmpleado(self,vacaciones,salario):
        print("Los dias de vacaciones son: ",vacaciones)
        print("El salario es: ",salario)

miPersona2 = empleado("Leo",34,"Masculino")
miPersona2.datosPersonales()
miPersona2.datosEmpleado(5,5000) 
    
