class persona:
    def nombre(self, nom):
        self.nombre = nom

    def imprimir(self):
        print("El nombre es: ", self.nombre)


persona1 = persona()
persona1.nombre("Pedro")
persona1.imprimir()

persona2 = persona()
persona2.nombre(input("ingese nombre"))
persona2.imprimir()
