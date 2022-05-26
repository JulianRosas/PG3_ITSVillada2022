try:
    meses = ("enero", "febrero", "marzo","abril", "mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
    mes = int(input("Introduce un numero del 1 al 12: "))
    print(meses[mes-1])
except IndexError:
    print("ingrese un numero valido")