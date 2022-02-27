#Escreva um  programa que leia dois números inteiros e  compare-os mostrando na tela: O PRIMEIRO VALOR É MAIOR, O SEGUNDO VALOR É MAIOR e NÃO EXISTE VALOR MAIOR, OS DOIS SÃO IGUAIS.
numero1 = int(input('primeiro número: '))
numero2 = int(input('segundo número: '))
if numero1 > numero2:
    print('o PRIMEIRO valor é maior.')
elif numero2 < numero1:
    print('o SEGUNDO valor é maior.')
elif numero1 == numero2:
    print('os dois valores são IGUAIS.')