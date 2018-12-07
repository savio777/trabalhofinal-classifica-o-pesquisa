# -*- coding: utf-8 -*-

tamanho = int(input('tamanho do vetor~> '))

vetor = []

for i in range(tamanho):
    vetor.append(int(input('elemento para o vetor~> ')))

vetor = list(set(vetor))

print(vetor)