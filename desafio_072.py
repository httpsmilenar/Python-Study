#Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quize', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    numero = int(input('digite um número entre 0 e 20: '))
    if 0 <= numero <= 20:
        break
    print('tente novamente.', end='')
print(f'você digitou o número {cont}')