from random import shuffle

lista = list(range(10))
shuffle(lista)
print(lista)
lista_ordenada = []
n = len(lista)

def m(lista):
  x = lista[0]
  for i in lista:
    if i < x:
      x = i
  return x  

def sorted_test(lista, lista_ordenada):
    for i in range(n):
      minimo = m(lista)
      lista_ordenada.append(minimo)
      lista.remove(minimo)
    print(lista_ordenada)

sorted_test(lista, lista_ordenada)
