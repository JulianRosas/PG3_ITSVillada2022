print("ingrese el ancho que va a tener el rectangulo")
ancho = int(input())
print("ingrese el alto que va a tener el rectangulo")
alto = int(input())
print("ingrese el caractear que va a usar el rectangulo")
caracter = str(input())


def rectangulo(ancho, alto, caracter):
    for i in range(alto):
        print(ancho * caracter)


rectangulo(ancho, alto, caracter)
