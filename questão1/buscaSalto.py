# -*- coding: utf-8 -*-
import math

vetor = []

for i in range(21):
    vetor.append(random.randrange(21)) 

numero = int(input('qual numero deseja encontrar no vetor? '))

def procurarNum(num, vet):
    tamanho = len(vet)
    pulo = math.sqrt(tamanho)

    antes = 0
    while(vet[min(tamanho,pulo)-1] < num):
        antes = pulo
        pulo += math.sqrt(tamanho)
        if(antes >= tamanho):
            return num," não está no vetor"

    # percorrer normalmente até o numero desejado
    while(vet[antes] < num):
        antes += 1  
        if(antes == min(pulo, tamanho)):
            return num," não está no vetor"
        
    if(vet[antes] == num):
        return vet[antes]," está no vetor"
    
print(procurarNum(numero, vetor))