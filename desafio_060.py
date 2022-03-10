#Faça um programa que leia um número qualquer e mostre o seu fatorial.
n = int(input('digite um número para calcular seu fatorial: '))
c = n
f = 1
print(f'calculando {n}! = ', end='')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')