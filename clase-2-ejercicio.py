class Persona:
    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    
    def mostrar_persona(self):
        print('Persona')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'DNI: {self.dni}')

class Estudiante(Persona):
    def __init__(self, nombre, apellido, dni, legajo, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.legajo = legajo
        self.carrera = carrera
        
    def mostrar_estudiante(self):
        print('Estudiante')
        print(f'Nombre: {self.nombre}')
        print(f'Apellido: {self.apellido}')
        print(f'DNI: {self.dni}')
        print(f'Legajo: {self.legajo}')
        print(f'Carrera: {self.carrera}')
        
    def cambiar_carrera (self, nueva_carrera):
        self.carrera = nueva_carrera

print()        
persona1 = Persona('Marcos', 'Sanchez', 8143859)
persona1.mostrar_persona()       
print()
persona2 = Persona('Graciela', 'Martinez', 14354985)
persona2.mostrar_persona()
print()
persona3 = Estudiante('Julian', 'Flores', '37654043', '16345', 'Licenciatura en Composicion Musical')
persona3.mostrar_estudiante()
print()
persona4 = Estudiante('Ailen', 'Rivero', '34954334', '8713', 'Tecnicatura en Programación')
persona4.mostrar_estudiante()

persona4.cambiar_carrera ("contador")
persona4.mostrar_estudiante()


