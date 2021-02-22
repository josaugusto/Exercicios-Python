import math

'''
    Faça um programa que leia um ângulo qualquer
    e mostre na tela o valor do seno, cosseno e tangente desse ângulo

'''
angulo = float(input('Informe o angulo em graus: '))
rad = math.radians(angulo)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('O seno do {} ° é: {:.2f}'.format(angulo, seno))
print('O cosseno do {} ° é: {:.2f}'.format(angulo, cosseno))
print('A tangente do {} ° é: {:.2f}'.format(angulo, tangente))
