print("ingrese una palabra")
palabra = str(input())


def vowels(palabra):
    count = 0
    for i in palabra:
        if i in "aeiou":
            count += 1
    return count


print(vowels(palabra))
