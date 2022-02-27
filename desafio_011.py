# Faça um programa que leia a largura e altura de uma parede em metros. calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta 2m².
larg = float(input("largura da parede: "))
alt = float(input("altura da parede: "))
área = larg * alt
print(f"sua parede tem a dimensão de {larg*alt} em {área}m²")
tinta = área / 2
print(f"para pintar essa, parede você precisará de {tinta} litros de tinta ")
