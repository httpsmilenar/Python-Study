#Crie um programa que leia dois valores e mostre o menu: [1]somar, [2]multiplicar, [3]maior, [4]novos números, [5]sair do programa. Seu programa deverá realizar a operação solicitada em cada caso.
numero1 = int(input('primeiro valor: '))
numero2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opcao = int(input('>>>>> qual é a sua opção? '))
    if opcao == 1:
        soma = numero1 * numero2
        print(f'a soma entre {numero1} e {numero2} é {soma}.')
    elif opcao == 2:
        produto = numero1 * numero2
        print(f'o resultado de {numero1} x {numero2} é {produto}.')
    elif opcao == 3:
        if numero1 > numero2:
            maior = numero1
        else:
            maior = numero2
        print(f'entre {numero1} e {numero2} o maior valor é {maior}')
    elif opcao == 4:
        print('informe os números novamente: ')
        numero1 = int(input('primeiro valor: '))
        numero2 = int(input('segundo valor: '))
    elif opcao == 5:
        print('finalizando...')
    else:
        print('opção inválida, tente novamente.')
    print('=-=' * 10)
print('fim do programa! volte sempre!')