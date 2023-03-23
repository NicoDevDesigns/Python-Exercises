from dataclasses import replace


chateando = True;
while chateando:
    texto = input('>');
    if(texto=='salir'):
        chateando = False;
    texto=texto.replace(':)','😁');
    texto=texto.replace(':(','🥺')
    print(texto);

