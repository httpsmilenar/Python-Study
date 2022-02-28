# Crie um programa que leia o nome de uma pessoa e diga se ela tem tem SILVA  no nome.
nome = str(input("qual o seu nome completo? ")).strip()
print(f'seu nome tem silva? {"SILVA" in nome.upper()}')
