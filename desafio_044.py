#Elabore um programa ue calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento. À vista: 10% de desconto; em ate 2x no cartão: preço normal; à vista no cartão: 5% de desconto e 3x ou mais vezes no cartão: 20% de juros.
print('{:=^40}'.format(' LOJAS RODRIGUES '))
preco = float(input('preço das compras: R$'))
print('''
FORMAS DE PAGAMENTO
[1] à vista
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input('qual é a opção? '))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print (f'sua compra será parcelada de 2x de R${parcela:.2f}')
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totparc = int(input('quantas parcelas?'))
    parcela = total / totparc
    print (f'sua compra será parcelada de {totparc}x de R${parcela:.2f} COM JUROS.')
print(f'sua compra de R${preco:.2f} vai custar R${total:.2f} no final.')