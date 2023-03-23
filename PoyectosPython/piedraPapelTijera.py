import random

def jugar():

    usuario=input("Escoja: piedra=pi, papel=pa, tijera=ti\n").lower()
    computadora=random.choice(['pi','pa','ti'])

    print('La eleccion de la computadora es: ',computadora)

    if usuario==computadora:
        return 'Empate!'
    
    if ganador(usuario,computadora):
        return 'Ganaste!!'
    
    return 'Perdiste!!'

def ganador(jugador,oponente):
    if((jugador=='pi' and oponente=='ti')
       or(jugador=='ti' and oponente=='pa')
        or(jugador=='pa' and oponente=='pi')):
        return True
    else:
        return False
   
print(jugar())