list=[ 4,12,54,5,80,15,23 ]

print ("que numero busca?")
num=int(input())

 
def lista (list, num):
    for i in list:
        if i==num:
            n=list.index(num)
            print("el numero esta en la posicion: "+str(n))

lista(list, num)    