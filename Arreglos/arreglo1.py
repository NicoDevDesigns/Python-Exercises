arreglo=['lunes','martes','miercoles','jueves','viernes'];

for dias in arreglo:
    print('El dia es '+dias);

for dias in arreglo:
    if(dias.endswith('nes')):
     print('El dia es '+dias);

for dias in arreglo:
    if dias=='martes':
     break
    print('El dia es '+dias);

arreglo.reverse();
for dias in arreglo:
    print('El dia es '+dias);

texto = 'Hola Nico';
for recorrer in texto:
    print(recorrer);

for numero in range(20):
    print(numero);