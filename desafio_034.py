# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print("=-" * 20)
print("Analisador de Triângulos")
print("-=" * 20)
r1 = float(input("primeiro segmento: "))
r2 = float(input("segundo segmento: "))
r3 = float(input("terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("os segmentos acima PODEM formar um triângulo.")
else:
    print("os segmentos acima NÃO PODEM formar um triângulo. ")
