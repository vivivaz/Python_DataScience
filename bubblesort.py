from random import shuffle

lista = list(range(10))
shuffle(lista)
print(lista)

def Bubble_Sort(lista):
    a = len(lista) -1
    while a != 0:
        for i in range(a):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
        a -= 1
    print(lista)

Bubble_Sort(lista)