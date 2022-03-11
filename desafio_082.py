#Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
numero = list()
pares = list()
ímpares = list()
while True:
    numero.append(int(input('digite um número: ')))
    resp = str(input('quer continuar: [S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(numero):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        ímpares.append(v)
print('-=' * 30)
print(f'a lista completa é {numero}.')
print(f'a lista de pares é {pares}.')
print(f'a lista de ímpares é {ímpares}')