#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida. Abaixo de 5.0: REPROVADO, entre 5.0 e 6.9: RECUPERAÇÃO e média 7.0 ou superior: APROVADO.
nota1 = float(input('primeira nota: '))
nota2 = float(input('segunda nota: '))
media = (nota1 + nota2) / 2
print(f'tirando {nota1:.1f} e {nota2:.1f}, a média do aluno é {media:.1f}')
if 7 > media >= 5:
    print('o aluno está em RECUPERAÇÃO.')
elif media < 5:
    print('o aluno está REPROVADO.')
else:
    print('o aluno está APROVADO.')