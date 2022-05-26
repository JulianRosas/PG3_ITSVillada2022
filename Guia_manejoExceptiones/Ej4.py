try:
    num1 = int(input("ingrese un numero: "))
    num2 = int(input("ingrese otro  numero: "))

    div = num1 / num2
    print("la division es: ",div)
except ZeroDivisionError:  
    print("no se puede dividir por cero")
    pass
except ValueError:
    print("ingrese un numero")
    pass