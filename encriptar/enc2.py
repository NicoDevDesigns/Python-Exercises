
def encriptar(texto):
    print('Encriptar archivo');
    textoFinal='';
    for letra in texto:
        ascii=ord(letra);
        ascii+=1;
        textoFinal+=chr(ascii);
    return textoFinal;

def desencriptar(texto2):
    print('Desencriptar archivo');
    textoFinal='';
    for letra in texto2:
        ascii=ord(letra);
        ascii-=1;
        textoFinal+=chr(ascii);
   
    return textoFinal;

def encriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo,'r');
    texto =  archivo.read();
    archivo.close();
    textoEncriptado = encriptar(texto);

    archivo= open(rutaArchivo,'w');
    archivo.write(textoEncriptado);
    archivo.close();
    print('El archivo se encripto correctamente');

def desencriptarArchivo(rutaArchivo):
    archivo = open(rutaArchivo,'r');
    texto =  archivo.read();
    archivo.close();
    textoDesencriptado = desencriptar(texto);

    archivo= open(rutaArchivo,'w');
    archivo.write(textoDesencriptado);
    archivo.close();
    print('El archivo de desencripto correctamente');

respuestaUsuario = input('Presione "E" para encriptar o "D" para desencriptar');
rutaArchivo = 'C:/Users/sanch/Documents/txt/archivo.txt'

if (respuestaUsuario == 'e'):
    encriptarArchivo(rutaArchivo);
else:
    desencriptarArchivo(rutaArchivo);