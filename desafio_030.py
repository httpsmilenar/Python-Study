#Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.
distancia = float(input('qual é a distância da sua viagem? '))
print(f'você está prestes a fazer uma viagem de {distancia}km. ')
if distancia <= 200:
    preço = distancia * 0.50 
else:
    preço = distancia * 0.45
print(f'o preço de sua passagem será de R${preço:.2f}')