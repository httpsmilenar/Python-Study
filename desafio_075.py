#Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre: A) Quantas vezes apareceu o valor 9, B) Em que posição foi digitado o primeiro valor 3 e C) Quais foram os números pares.
numero = (int(input('digite um número: ')),
          int(input('digite outro número: ')),
          int(input('digite mais um número: ')),
          int(input('digite o último número: ')))
print(f'você digitou os valores {numero}')
print(f'o valor 9 apareceu {numero.count(9)} vezes.')
if 3 in numero:
    print(f'o valor 3 apareceu na {numero.index(3)+1}ª posição.')
else:
    print('o valor 3 não foi digitado em nenhuma posição.')
print('os valores digitados foram ', end='')
for n in numero:
    if n % 2 == 0:
        print(n, end=' ')