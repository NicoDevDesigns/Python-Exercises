numeros = {
    "1":"uno",
    "2":"Dos",
    "3":"Tres",
}

texto= input('Ingrese un numero: ');
textoFinal = '';
for letra in texto:
    textoFinal+=numeros[letra]+' ';
print(textoFinal);
