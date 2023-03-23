


class cuadrado:
    def __init__(self,ancho,alto):
        self.ancho=ancho;
        self.alto=alto;
    def areaCuadrado(self):
        area = self.ancho*self.alto;
        return area;


figura = cuadrado(5,4);
print(figura.areaCuadrado());

