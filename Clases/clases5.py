class Coche():
    largo = 200;
    ancho = 300;
    funcionamiento = False;
    
    def estado(self):
        self.funcionamiento=True;
    def estadoCoche(self):
        if(self.funcionamiento):
            return "El coche esta en marcha"
        else:
            return "El coche esta parado";

miCoche=Coche();
print("El largo del coche es: ",miCoche.largo);
print("El ancho del coche es: ",miCoche.ancho);
#miCoche.estado();   
print(miCoche.estadoCoche());


