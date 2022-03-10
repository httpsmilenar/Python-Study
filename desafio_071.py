#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
print('='*30)
print('{:^30}'.format('BANCO MSR'))
print('='*30)
valor = int(input('que valor você quer sacar? R$'))
total = valor
cedulas = 50
totced = 0
while True:
    if total >= cedulas:
        total -= cedulas
        totced += 1
    else:
        if totced > 0:
            print(f'total de {totced} cédulas de R${cedulas} ')
        if cedulas == 50:
            cedulas = 20
        elif cedulas == 20:
            cedulas = 10
        elif cedulas == 10:
            cedulas = 1
        totced = 0
        if total == 0:
            break
print('='*30) 
print('volte sempre ao BANCO MSR! tenha um bom dia.')