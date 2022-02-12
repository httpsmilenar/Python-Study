#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
nome1 = str(input('primeiro aluno: '))
nome2 = str(input('segundo aluno: '))
nome3 = str(input('terceiro aluno: '))
nome4 = str(input('quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print('a ordem de apresentação será ')
print(lista)