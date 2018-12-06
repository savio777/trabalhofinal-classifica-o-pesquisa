# -*- coding: utf-8 -*-
import random

vetor = []

for i in range(21):
    vetor.append(random.randrange(21)) 

numero = int(input('qual numero deseja procurar no vetor? '))

def procurarNum(num, vet, e, d):
    if(d >= e):
        i = int(e + (d - e)/2)
        if(vet[i] == num):
            return i
        elif(vet[i] > num):
            return procurarNum(num, vet, e, i-1)
        else:
            return procurarNum(num, vet, i+1, d)
    else:
        return -1

print(vetor)

if(procurarNum(numero, vetor, 0, len(vetor)-1) > -1):
    print(numero,' contem no vetor')
else:
    print(numero,' não contem no vetor')