#Faça um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade: se ele ainda vai se alistar ao serviço militar, se é a hora ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date 
atual = date.today().year
nasc = int(input('ano de nascimento: '))
idade = atual - nasc
print(f'quem nasceu em {nasc} tem {idade} anos em {atual}')
if idade == 18:
    print('você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print(f'ainda faltam {saldo} para você sed alistar.')
elif idade > 18:
    saldo = idade - 18
    print(f'você já deveria ter se alistado há {saldo} anos!')