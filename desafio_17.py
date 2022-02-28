# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
co = float(input("comprimento do cateto oposto: "))
ca = float(input("comprimento do cateto adjacente: "))
hi = (co**2 + ca**2) ** (1 / 2)
print(f"a hipotenusa vai medir {hi}")
