# -*- coding: utf-8 -*-
import random

vetor = []

numero = int(input('qual numero deseja encontrar no vetor? '))

# numero de elementos na lista (com -1)
test = 21

for i in range(test):
    vetor.append(random.randrange(test))

def procurarNum(num, vet):
    indexRand = []   # guardar index que já foram testados
    indexTotal = list(range(test))   # lista total
    while(indexRand != indexTotal):
        i = random.randrange(test)
        if(vet[i]==num):
            return 'numero encontrado ', vet[i]
        indexRand.append(i)
        # apagar elementos repetidos na lista indexRand
        indexRand = list(set(indexRand))
    return 'numero ', num,'não encontrado'

print(procurarNum(numero, vetor))