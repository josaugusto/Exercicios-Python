import math
'''
    Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de 
    um triângulo retângulo, mostre o comprimento da hipotenusa 

    hipotenusa**2 = cateto_oposto**2 + cateto_adjacente**2

    hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
    ou
    math.hypot()
'''
cateto_oposto = float(input('Informe o comprimento do cateto oposto: '))
cateto_adjacente = float(input('Informe o comprimento do cateto adjacente: '))
#hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)
print('Hipotenusa: {:.2}'.format(hipotenusa))
