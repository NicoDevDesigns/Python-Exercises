def sumar(val1,val2):
    resultado = val1 + val2;
    print("El resultado es: ", resultado);

def restar(val1,val2):
    resultado = val1 - val2;
    print("El resultado es: ", resultado);

class datosPadre:
    def __init__ (self,nombre,edad):
        self.nombre = nombre;
        self.edad = edad;

    def mostrarDatos(self):
        print("nombre: ", self.nombre," edad: ", self.edad);

class datosHijo(datosPadre):
    def __init__(self,sexo,hijoNombre,hijoEdad):
        super().__init__(hijoNombre,hijoEdad);
        self.sexo=sexo;
    def mostrarDatos(self):
        super().mostrarDatos();
        print("El sexo es: ",self.sexo);
    





