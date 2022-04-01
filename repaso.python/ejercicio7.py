print("ingrese un numero")
num = int(input())


def step(num):
    a = map(int, str(num)[1:]) 
    b = map(int, str(num)[:-1])
    return all(abs(a_digit - b_digit) == 1 for a_digit, b_digit in zip(a, b))

if(step(num) == True):
    print("Es step ")
else:
    print("No es step ") 