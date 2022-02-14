#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
numero = int(input('digite um número: '))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f'analizando o número {numero}')
print(f'unidade {unidade}')
print(f'dezena {dezena}')
print(f'centena {centena}')
print(f'milhar {milhar}')