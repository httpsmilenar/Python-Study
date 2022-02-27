# Faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto.
preço = float(input("qual é o preço do produto? R$"))
novo = preço - (preço * 5 / 100)
print(f"o produto que custava R${preço}, com o desconto de 5% vai custar R${novo}")
