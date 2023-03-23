#importar un archivo externo binario a python para leerlo
import pickle

file_binario=open("database","rb");

lista=(pickle.load(file_binario));
print(lista);