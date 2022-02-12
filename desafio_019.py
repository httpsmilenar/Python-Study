#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
nome1 = str(input('primeiro aluno: '))
nome2 = str(input('segundo aluno: '))
nome3 = str(input('terceiro aluno: '))
nome4 = str(input('quarto aluno: '))
lista = [nome1, nome2, nome3, nome4]
escolhido = random.choice(lista)
print(f'o aluno escolhido foi {escolhido}')