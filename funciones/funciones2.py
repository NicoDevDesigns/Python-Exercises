def suma():
    valor1 = 10
    valor2 = 10
    valor3=60
    resultado = valor1 + valor2+valor3
    return resultado
def lista():
    return ("Nico",20,["Leo","mailo"],"Hermano")

def nuevaLista():
    lista1=("Hola","Soy el mundo")
    return lista1

print(nuevaLista())
dato = suma()
dato1= dato+(suma())
print(dato)
print(dato1)
print(lista())