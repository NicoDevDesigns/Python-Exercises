def consulta(nombre):
    print("Bienvenidos!!");
    print("Como estas ",nombre);

    edad = int(input("dime tu edad: "));
    if(edad<18):
        print("No puedes ver esta peli");
    else:
        print("Tremenda peli");