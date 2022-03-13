#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado. EQUILÁTERO: todos são iguais; ISÓCELES: dois lados iguais; ESCALENO: todos os lados diferentes.
print('=-'* 20)
print('Analisador de Triângulos')
print('-=' * 20)
r1 = float(input('primeiro segmento: '))
r2 = float(input('segundo segmento: '))
r3 = float(input('terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('os segmentos acima PODEM formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO!')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO!')
    else:
        print('ISÓCELES!')
else:
    print('os segmentos acima NÃO PODEM formar um triângulo. ')