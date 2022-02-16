#Faça um programa que leia um frase pelo teclado e mostre: quantas vezes a aparece a letra A, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('digite uma frase: ')).upper()
print(f'a letra A aparece {frase.count("A")} vezes na frase')
print(f'a primeira letra A apareceu na posição {frase.find("A")+1}')
print(f'a última letra A apareceu na posição {frase.rfind("A")+1}')