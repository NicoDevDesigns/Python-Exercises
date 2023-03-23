class coche:
    def __init__(self,velocidad,nombre,temperatura):
        self.velocidad=velocidad;
        self.nombre=nombre;
        self.temperatura=temperatura;

    def acelerar(self):
        self.velocidad +=1;
        print('La velocidad actual es de: '+str(self.velocidad));
    def frenar(self):
        if self.velocidad==0:
            print('El coche se ha detenido');
        else:
            self.velocidad -=1;
            print('La velocidad actual es: '+str(self.velocidad));

mercedez= coche(-1,'mercedez',100);
mercedez.acelerar();
mercedez.frenar();
