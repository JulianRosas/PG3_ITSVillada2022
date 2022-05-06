class triangulo:
    def trian(self, l1, l2, l3):
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def mayor(self):
        if self.l1 > self.l2 and self.l1 > self.l3:
            print("el mayor es: ", self.l1)
        elif self.l2 > self.l1 and self.l2 > self.l3:
            print("el mayor es: ", self.l2)
        else:
            print("el mayor es: ", self.l3)

    def imprimir(self):
        if self.l1 == self.l2 and self.l2 == self.l3:
            print("equilatero")
        else:
            print("no es quilatero")


triangulo1 = triangulo()
triangulo1.trian(
    input("ingrese lado 1: "), input("ingrese lado 2: "), input("ingrese lado 3: ")
)
triangulo1.imprimir()
triangulo1.mayor()
