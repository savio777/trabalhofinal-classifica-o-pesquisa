# -*- coding: utf-8 -*-

tamanho = int(input('tamanho da lista~> '))

lista = []

for i in range(tamanho):
    lista.append(int(input('elemento da lista~> ')))

x = int(input('elemento que deseja encontrar o index~> '))

index = -1

for i in range(tamanho):
    if(lista[i] == x):
        index = i

if(index > -1):
    print(x,' está em~> ', index)
else:
    print('esse valor não está na lista, ',index)