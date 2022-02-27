# Escreva um programa que leia a velocidade de um carro. Se ultrapassar 80km/h, escreva uma mensagem dizendo que ele foi MULTADO. A multa vai custar R$7,00 por km acima do limite.
velocidade = float(input("qual é a velocidade atual do carro? "))
if velocidade > 80:
    print("MULTADO! você atingiu o limite permitido, que é de 80km/h.")
    multa = (velocidade - 80) * 7
    print(f"você deve pagar uma multa no valor de R${multa:.2f}")
print("tenha um bom dia! dirija com segurança.")
