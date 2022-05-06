class operaciones:
    def __init__(self):
        self.num1 = int(input("ingrese numero 1: "))
        self.num2 = int(input("ingrese numero 2: "))
        self.sumar()
        self.restar()
        self.multiplicar()
        self.dividir()

    def sumar(self):
        print("La suma es: ", self.num1 + self.num2)

    def restar(self):
        print("La resta es: ", self.num1 - self.num2)

    def multiplicar(self):
        print("La multiplicacion es: ", self.num1 * self.num2)

    def dividir(self):
        print("La division es: ", self.num1 / self.num2)


operacion1 = operaciones()
operacion1.__init__()
