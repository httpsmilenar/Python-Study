#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade; até 9 anos de idade: MIRIM; até 14 anos: INFANTIL; até 19: JUNIOR; até 25: SENIOR; acima: MASTER.
from datetime import date
atual = date.today().year
nascimento = int(input('ano de nascimento: '))
idade = atual - nascimento
print(f'o atleta tem {idade} anos')
if idade <= 9:
    print('classificação: MIRIM')
elif idade <= 14:
    print('classificação: INFANTIL')
elif idade <= 19:
    print('classificação: JUNIOR')
elif idade <= 25:
    print('classificação: SENIOR')
else:
    print('classificação: MASTER')