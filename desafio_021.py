# Crie um programa que leia o nome completo de uma pessoa e mostre O NOME COM TODAS AS LETRAS MAIÚSCULAS E MINÚSCULAS, QUANTAS LETRAS AO TODO e QUANTAS LETRAS TEM O PRIMEIRO NOME.
nome = str(input("digite o seu nome: ")).strip()
print("analisando seu nome...")
print(f"seu nome em maiúsculas é {nome.upper()}")
print(f"seu nome em minúsculas é {nome.lower()}")
print(f'seu nome tem ao todo {len(nome) - nome.count(" ")} letras')
print(f'seu primeiro nome tem {nome.find(" ")} letras')
