#Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora usando o laço FOR.
numero = int(input('digite um número para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{numero} x {c} = {numero*c}')