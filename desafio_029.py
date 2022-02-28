# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
numero = int(input("digite um número qualquer: "))
resultado = numero % 2
if resultado == 0:
    print(f"o número {numero} é PAR.")
else:
    print(f"o n´mero {numero} é ÍMPAR.")
