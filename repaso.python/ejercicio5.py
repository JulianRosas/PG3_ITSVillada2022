print("ingrese una palabra para ver si es un palindromo")
palabra = str(input())


def palindromo(palabra):
    if palabra == palabra[::-1]:
        return True
    else:
        return False


print(palindromo(palabra))
