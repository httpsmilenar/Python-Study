#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a BASE DE CONVERSÃO: 1 para BINÁRIO, 2 para OCTAL e 3 para HEXADECIMAL.
numero = int(input('digite um número inteiro: '))
print('''escolha uma das bases para conversão:
[ 1 ] conveter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao = int(input('digite a sua opção: '))
if opcao == 1:
    print(f'{numero} convertido para BINÁRIO é igual a {bin(numero)}')
elif opcao == 2:
    print(f'{numero} convertdido para OCTAL é igual a {oct(numero)}')
elif opcao == 3:
    print(f'{numero} convertido para HEXADECIMAL é igual a {hex(numero)}')  
else:
    print('opção inválida, tente novamente.')