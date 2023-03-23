class padre():
    def __init__(self,nombre):
        self.nombre=nombre;

    def estado(self):
        print("Hola mundo mi nombre es: ",self.nombre);

class hijo(padre):
    pass
hijoNico=hijo("Nico");
hijoNico.estado();
