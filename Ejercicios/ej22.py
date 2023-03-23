nombre = input('Dime tu nombre mortal?: ');
edad = int(input('Dime tu edad?: '))
texto= 'Hola mundo soy '+ nombre +' y mi edad es: '+str(edad);
print(texto); 

preguntaHijo = input('sos hijo del jefe? ');
EsHijoJefe = preguntaHijo == 'si';
puedeSubir = edad>15 or EsHijoJefe;
if(puedeSubir):
    print('Sos mayor de edad puedes entrar');
else:
    print('Sos menor de edad no puedes entrar');

