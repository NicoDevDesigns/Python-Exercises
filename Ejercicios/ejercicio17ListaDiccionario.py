nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")
edad = input("Ingrese el edad: ")
telefono = input("Ingrese el telefono: ")

base_datos = {"nombre":nombre,"apellido":apellido,"edad":edad,"telefono":telefono}
print("El nombre es ",base_datos["nombre"]," su apellido es ",base_datos["apellido"],"su edad es ",base_datos["edad"]," y su telefono es ",base_datos["telefono"])
