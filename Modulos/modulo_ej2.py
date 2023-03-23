class datos:
    def __init__ (self,dato1,dato2):
        self.dato1=dato1;
        self.dato2=dato2;
    def calculo(self):
        self.respuesta = self.dato1*self.dato2;
        print("El resultado es: ",self.respuesta);
