# biblioteca para gerar numeros aleatorios
import random

# inicialização da variavel do vetor
vetor = []

# numero q deseja verificar se existe no vetor
numero = int(input('qual numero deseja procurar no vetor? '))

# encher o vetor com 20 numeros aleatorios 
for i in range(20):
    vetor.append(random.randrange(21)) 

# função sequencial para encontrar o numero desejado no vetor
def procurarNumero(num, vet):
    for i in range(20):
        #print(vet[i])
        if(vet[i]==num):
            return 'numero encontrado ', vet[i]
    return 'numero ', num,'não encontrado'

# utilizar a função
print(procurarNumero(numero, vetor))