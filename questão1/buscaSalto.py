# -*- coding: utf-8 -*-
import math
import random

vetor = []

for i in range(21):
    vetor.append(random.randrange(21)) 

numero = int(input('qual numero deseja encontrar no vetor? '))

def procurarNum(num, vet):
    tamanho = len(vet)
    pulo = math.sqrt(tamanho)

    comeco = 0
    while(vet[int(min(pulo, tamanho)-1)] < num):
        comeco = pulo
        pulo += math.sqrt(tamanho)
        if(comeco >= tamanho):
            return -1
        
    while(vet[int(comeco)] < num):
        comeco += 1
        if(comeco == min(pulo, tamanho)):
            return -1
    
    if(vet[int(comeco)] == num):
        return comeco
    
    return -1

print(vetor)
print(int(procurarNum(numero, vetor)))
''' ficou bugado, não consegui concertar o bug '''
'''if(procurarNum(numero, vetor) > -1):
    print(numero,' está no vetor')
else:
    print(numero,' não está no vetor')'''