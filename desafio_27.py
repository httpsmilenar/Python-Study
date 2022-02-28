# Escreva na tela um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint

computador = randint(0, 5)  # Faz o computador pensar
print("-=-" * 20)
print("vou pensar em um número entre 0 e 5. Tente advinhar...")
print("-=-" * 20)
jogador = int(input("em que número eu pensei? "))  # Jogador tenta advinhar
if jogador == computador:
    print("PARABÉNS, você conseguiu vencer!")
else:
    print(f"GANHEI! eu pensei no número {computador}, não no número {jogador}!")
