'''
    Faça um programa que leia a largura e a
    altura de uma parede em metros, calcule a sua área e a quantidade
    de tinta necessária para pintá-la, sabendo que cada litro
    de tinta, pinta uma área de 2 m^2

'''
largura = float(input('largura da parede: '))
altura = float(input('Altura da parede: '))
area = largura*altura 
qtd_tinta = area/2

print('A área da parede é igual a {}x{} = {} m².'.format(largura, altura, area))
print('Para pintar essa área iremos necessitar de {} L de tinta'.format(qtd_tinta))