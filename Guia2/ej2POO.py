class alumno:
    def constr(self, nombre, nota):
        self.nombre = nombre
        self.nota = int(nota)

    def imprimir(self):
        print("El nombre es: ", self.nombre)
        print("La nota es: ", self.nota)

    def estado(self):
        if self.nota >= 4:
            print("regular")
        else:
            print("desaprobado")


alumno1 = alumno()
alumno1.constr("juansito", "6")
alumno1.imprimir()
alumno1.estado()

alumno2 = alumno()
alumno2.constr("josefina", "3")
alumno2.imprimir()
alumno2.estado()
