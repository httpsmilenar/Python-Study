#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último separadamente.
n = str(input('digite seu nome completo: ')).strip()
nome = n.split()
print(f'seu primeiro nome é {nome[0]}')
print(f'seu último nome é {nome[len(nome)-1]}')