#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar. A prestação mensal não pode exceder 30% ou então o empréstimo será negado.
casa = float(input('valor da casa: R$'))
salario = float(input('salário do comprador: R$'))
anos = int(input('quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'para pagar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}')
if prestacao <= minimo:
    print('empréstimo pode ser condedido.')
else:
    print('empréstimo negado.')