#Clases
class Persona:
    #Constructor
    def __init__(self, param_nombre, param_email):
        self.nombre = param_nombre
        self.email = param_email
        self.asistencia = 0
    #Metodo
    def cambiar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre
    def asistencia_clase(self):
        self.asistencia += 1

class Profesor(Persona):
    #Constructor
    def __init__(self, param_nombre, param_email, legajo_empleado):
        self.legajo_empleado = legajo_empleado
        super().__init__(param_nombre, param_email)
class Alumno(Persona):
    def __init__(self, param_nombre, param_email, numero_alumno):
        self.numero_alumno = numero_alumno
        self.materias_cursando = []
        super().__init__(param_nombre, param_email)
    def cursando(self, materia):
        self.materias_cursando.append(materia)
#Objetos
profesor_rey = Profesor("Rey", "r.l@profesor.com", "123")
print(id(profesor_rey))
print(profesor_rey.nombre)
print(profesor_rey.email)
profesor_fran = Profesor("Fran", "f.pasqui@profesor.com", "212")
print(id(profesor_fran))
print(profesor_fran.nombre)
print(profesor_fran.email)
profesor_lucho = Profesor("Lucho", "l.toni@profesor.com", "152")
print(id(profesor_lucho))
print(profesor_lucho.nombre)
print(profesor_lucho.email)

print(" ")

profesor_rey.cambiar_nombre("Reynier")
print(profesor_rey.nombre)
profesor_fran.cambiar_nombre("Francisco")
print(profesor_fran.nombre)
profesor_lucho.cambiar_nombre("Luciano")
print(profesor_lucho.nombre)

print(" ")

profesor_rey.asistencia_clase()
print("Su asistencia es...")
print(profesor_rey.asistencia)
