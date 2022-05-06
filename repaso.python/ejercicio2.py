print("escriba un año para daber si es bisiesto")


def año_bisiesto(año):
    div4 = año % 4
    div100 = año % 100
    div400 = año % 400
    if div4 & div100 & div400 == 0:
        print("es bisiesto")
    elif div4 & div400 == 0:
        print("es bisiesto")
    else:
        print("no es bisesto")


año = int(input())

print(año_bisiesto(año))
