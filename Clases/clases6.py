from operator import truediv


class Coche():
    def __init__(self):
        self.__ruedas = 4;
        self.__color="Rojo";
        self.__enMarcha=False;
    def arrancar(self,arrancamos):
        self.__enMarcha=arrancamos;

        if(self.__enMarcha):
            chequeo = self.__chequeoInterno();
            if(self.__enMarcha and chequeo):
                return "El auto esta en marcha";
            elif(self.__enMarcha and chequeo == False):
                return "Algo anduvo mal en el chequeo";
        else:
            return "El auto esta apagado";
    def estado(self):
        print("ruedas: ", self.__ruedas, "color: ", self.__color);
    def __chequeoInterno(self):
        print("Realizando chequeo interno del auto");
        self.gasolina="Ok";
        self.aceite="Ok";
        self.puertas="Ok";

        if(self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Ok"):
            return True;
        else:
            return False;




miCoche1= Coche();
miCoche1.estado();
print(miCoche1.arrancar(True));
miCoche2= Coche();
miCoche2.estado();
print(miCoche2.arrancar(False));
