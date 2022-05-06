
respuesta = int(input("ingrese un  1-si quire sumar  2-si quiere terminar el programa: "))
while respuesta == 1:
    try:
        n1 = int(input("ingrese un numero: "))
        n2 =int(input("ingrese otro numero: "))
        suma1 = n1 + n2
        print("la suma de los dos numeros es : ",suma1)
        respuesta = int(input("desea continuar sumando? 1-si 2-no: "))
    except ValueError:
        print("ingrese un numero valido")
        pass