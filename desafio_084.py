#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre: A) Quantas pessoas foram cadastradas, B) Uma listagem com as pessoas mais pesadas e C) Uma listagem com as pessoas mais leves.
dados = list()
pessoas = list()
peso_total = list()
pessoas_maior_peso = list()
pessoas_menor_peso  = list()
#dados inseridos pelo usuário
while True: 
    dados.append(str(input('nome: ')).strip().capitalize())
    dados.append(float(input('peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    while True:
        proximo = str(input('quer continuar? (S/N):')).strip().upper()
        if proximo in 'SN':
            break
    if proximo == 'N':
        break
#separando todos os pesos na lista > peso_total
for peso in pessoas:
    peso_total.append(peso[1])
#checando o peso máximo e mínimo 
maior_peso = max(peso_total)
menor_peso = min(peso_total)
#identificando os respectivos nomes de peso max/min
for pes in pessoas:
    if pes[1] == maior_peso: # if True: nome, peso > max
        pessoas_maior_peso.append(pes[0]) 
    if pes[1] == menor_peso: #if True: nome, peso > min
       pessoas_menor_peso.append(pes[0]) 
print(f'{"=-"*20}\nAo todo, você cadastrou {len(pessoas)} pessoa{"s" if len(pessoas) > 1 else ""}.')
print(f'O maior peso foi de {maior_peso}Kg. Peso de {pessoas_maior_peso}')
print(f'O menor peso foi de {menor_peso}Kg. Peso de {pessoas_menor_peso}')