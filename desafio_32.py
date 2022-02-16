#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
#verificando que é menor
menor = a 
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
#verificando que é maior
maior = a
if b > c and b > a:
    maior = b
if c > a and c > b:
    maior = c
print (f' o menor valor digitdo foi {menor}')
print(f'o maior valor digitado foi {maior}')