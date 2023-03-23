#exportar e importar una clase en binario
import pickle

class datos:
    def __init__ (self,nombre):
        self.nombre=nombre;
    def mostrar(self):
        print("El datos es: ", self.nombre);

nico=datos("Nico");
leo=datos("Leo");

hermanos=[nico,leo];

file_binario=open("database2","wb");

pickle.dump(hermanos,file_binario);
file_binario.close();
del(file_binario);

file_binarioOpen=open("database2","rb");

leer=pickle.load(file_binarioOpen);
file_binarioOpen.close();

for r in leer:
    print(r.mostrar());
