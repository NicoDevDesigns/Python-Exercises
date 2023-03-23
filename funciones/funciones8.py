def infinito(*args):
    print(args)
def infinito2(*args):
    for args in args:
        print(args)
def infinito3(**kwargs):
    print(kwargs)
infinito("Nicolas",20,["Hola","Mundo"])
infinito2("Nicolas",20,["Hola","Mundo"])
infinito3(a="Nico",b=66,c=["Nico","Leo"])

