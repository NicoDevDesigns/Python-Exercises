def calculadoraPeso(nombre):
    print('Bienvenido '+ nombre);
    peso = int(input('Ingrese su peso: '));
    altura = int(input('Ingrese su altura: '));

    altura = altura/100;
    imc= peso/(altura*altura);

    print('Su IMC es de: '+str(imc));

    if(imc<20):
        print('Se encuentra delgado!');
    if(imc>=20 and imc<=26):
        print('Nivel normal');
    if(imc>26 and imc<=30):
        print('Estado de sobrepeso');
    if(imc>30):
        print('Estado de obesidad');

nombre = input('Ingrese su nombre: ');
calculadoraPeso(nombre);
