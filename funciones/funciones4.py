def infinito(**kwargs):
    for kwarg in kwargs:
        print(kwarg,"---->",kwargs[kwarg])

infinito(a="nico",b = 66,c = ["Hola","Mundo"])