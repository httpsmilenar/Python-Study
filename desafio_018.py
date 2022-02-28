# Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo.
import math

angulo = float(input("digiite o ângulo que você deseja: "))
seno = math.sin(math.radians(angulo))
print(f"o ângulo de {angulo} tem o SENO de {seno:.2f}")
cosseno = math.cos(math.radians(angulo))
print(f"o ângulo de {angulo} tem o COSSENO de {cosseno:.2f}")
tangente = math.tan(math.radians(angulo))
print(f"o ângulo de {angulo} tem a TANGENTE de {tangente:.2f}")
