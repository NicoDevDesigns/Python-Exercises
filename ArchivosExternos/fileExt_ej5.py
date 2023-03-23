import pickle

class Persona:
    def __init__(self,nombre,genero,edad):
        self.nombre=nombre;
        self.genero=genero;
        self.edad=edad;
        print("Se ha creado una nueva persona ",self.nombre);
    def __str__(self):
        return "{} {} {}".format(self.nombre,self.genero,self.edad);

class ListaPersona:
    personas=[];
    def __init__(self):
        listaPersonas=open("ficheroExterno","ab+");
        listaPersonas.seek(0);

        try:
            self.personas=pickle.load(listaPersonas);
            print("Se cargaron {} personas al fichero".format(len(self.personas)));
        except:
            print("El fichero esta vacio");
        finally:
            listaPersonas.close();
            del(listaPersonas);
        
    def agregarPersona(self,p):
            self.personas.append(p);
            self.guardarPersonaFichero();

    def mostrarPersona(self):
        for p in self.personas:
                print(p);

    def guardarPersonaFichero(self):
        listaDePersonas=open("ficheroExterno","wb");
        pickle.dump(self.personas,listaDePersonas);
        listaDePersonas.close();
        del(listaDePersonas);
    def mostrarInfoficheroExterno(self):
        print("La informacion del fichero externo es la siguiente:");
        for p in self.personas:
            print(p);

miLista=ListaPersona();
persona2=Persona("leo","Masculino",35);
miLista.agregarPersona(persona2);
miLista.mostrarInfoficheroExterno();
