#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por km rodado.
dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
pago = dias * 60
print(f'o total a pagar é de {pago:.2f}')

dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'o total a pagar é de {pago:.2f}')