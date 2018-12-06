#include <stdio.h>

int main(void)
{
    int tamanho, i, s, aux, cont = 0;

    printf("escolha o tamanho do vetor~> ");
    scanf("%d", &tamanho); 
    // tamanho do vetor
    int vetor[tamanho];

    printf("\nde os valores do vetor:\n");

    // dar valores ao vetor
    for(i=0;i<tamanho;i++)
    {
        scanf("%d", &vetor[i]);
    }

    // sobrescrever valores repetidos
    for(i=0;i<tamanho-1;i++)
    {
        if((vetor[i]==vetor[i+1])&&(i<tamanho))
        {
            cont++;
            vetor[i+1]=vetor[i+2];
        }
    }

    printf("\n");

    for(i=0;i<tamanho;i++)
    {
        printf("%d, ", vetor[i]);
    }

    printf("\n");

    return 0;
}