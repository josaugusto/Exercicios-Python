from random import choice
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']

print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogada = int(input('Qual é a sua jogada? '))
computador = choice(lista)
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')
sleep(1)
print('O Computador jogou {}'.format(computador))
print('O jogador jogou {}'.format(lista[jogada]))

if lista[jogada] == 'Pedra' and computador == lista[2]:
    print('O jogador VENCEU!!!')
elif lista[jogada] == 'Papel' and computador == lista[0]:
    print('O jogador VENCEU!!!')
elif lista[jogada] == 'Tesoura' and computador == lista[1]:
    print('O jogador VENCEU!!!')
elif lista[jogada] == computador:
    print('EMPATE entre o jogador e o computador!!!')
elif lista[jogada] == 'Tesoura' and computador == lista[0]:
    print('O computador VENCEU!!!')
elif lista[jogada] == 'Papel' and computador == lista[2]:
     print('O computador VENCEU!!!')
elif lista[jogada] == 'Pedra' and computador == lista[1]:
     print('O computador VENCEU!!!')