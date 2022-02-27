# Faça um programa que leia um ano qualquer e diga se ele é BISSEXTO.
ano = int(input("que ano quer analisar? "))
if ano % 4 == 0:
    print(f"o ano {ano} é BISSEXTO.")
else:
    print(f"o ano {ano} NÃO é BISSEXTO.")
