#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela. abaixo de 18.5: ABAIXO DO PESO; entre 18.5 e 25: PESO IDEAL; 25 até 30: SOBREPESO; 30 até 40: OBESIDADE e acima de 40: OBESIDADE MÓRBIDA.
peso = float(input('qual é o seu peso? (kg) '))
altura = float(input('qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print(f'o IMC dessa pessoa é de {imc:.1f}')
if imc < 18.5:
        print('você está ABAIXO DO PESO normal.')
elif 18.5 <= imc < 25:
    print('você está na faixa de peso NORMAL.') 
elif 25 <= imc < 30:
    print('você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('você está em OBESIDADE.')