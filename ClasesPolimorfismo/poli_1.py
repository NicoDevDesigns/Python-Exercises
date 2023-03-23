class coche():
    def desplazamiento(self):
        print("El coche se desplaza en 4 ruedas");
class moto():
    def desplazamiento(self):
        print("La moto se desplaza en 2 ruedas");
class camion():
    def desplazamiento(self):
        print("El camion se desplaza en 6 ruedas");

def desplazamientoVehiculo(vehiculo):
    vehiculo.desplazamiento();

miVehiculo=coche();
desplazamientoVehiculo(miVehiculo);
