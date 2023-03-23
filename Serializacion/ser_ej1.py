#exportar una lista a un archivo externo en binario
import pickle

lista=["Nico","Leo","july","Mary"];

file_binario=open("database","wb");

pickle.dump(lista,file_binario);

file_binario.close();