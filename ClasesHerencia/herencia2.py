class persona():
    def __init__(self,nombre,edad):
        self.nombre=nombre;
        self.edad=edad;
    def descripcion(self):
        print("nombre: ",self.nombre," Edad: ",self.edad);
class empleado(persona):
    def __init__(self,salario,nombreEmpleado,edadEmpleado):
       super().__init__(nombreEmpleado,edadEmpleado);
       self.salario=salario;
    def descripcion(self):
        super().descripcion();
        print("Salario: ", self.salario);

nico=empleado(70,"Nico",36);
nico.descripcion();
        