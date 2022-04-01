list=[]

def orden(list):
    print("ingrese el tamaño que va a tener la lista")
    tamaño=int(input())
    for i in range(tamaño):
        print("agregue los numeros q va a contener esta lista")
        num=int(input())
        list.append(num)
    list.sort(reverse=True)
    print(list)

orden(list)



