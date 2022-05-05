

class familia:
    def __init__(self):
        self.padre=(input("el nombre del padre es: "))
        self.madre=(input("el nombre de la madre es: "))
        self.hijos = List = []
        self.cantHijos= int(input("cuantos hijos tenes: "))
        for i in range (self.cantHijos):
            self.nombres=str(input("ingrese el nombre de su hijo: "))
            self.hijos.append(self.nombres)

    def __str__(self) -> str:
        return "Padre: " + self.padre + "\nMadre: " + self.madre + "\nHijos: " + str(self.hijos)

familia1=familia()
print(familia1)
