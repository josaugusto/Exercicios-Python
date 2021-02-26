from random import choice
from time import sleep

lista = ['Pedra', 'Papel', 'Tesoura']

def jogador_venceu(computador, jogador):
    print('O Computador jogou {}'.format(computador))
    print('O jogador jogou {}'.format(lista[jogador]))
    print('O jogador VENCEU!!!')

def computador_venceu(computador, jogador):
    print('O Computador jogou {}'.format(computador))
    print('O jogador jogou {}'.format(lista[jogador]))
    print('O computador VENCEU!!!')

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

if lista[jogada] == 'Pedra' and computador == lista[2]:
    jogador_venceu(computador, jogada)
elif lista[jogada] == 'Papel' and computador == lista[0]:
    jogador_venceu(computador, jogada)
elif lista[jogada] == 'Tesoura' and computador == lista[1]:
    jogador_venceu(computador, jogada)
elif lista[jogada] == computador:
    print('O Computador jogou {}'.format(computador))
    print('O jogador jogou {}'.format(lista[jogada]))
    print('EMPATE entre o jogador e o computador!!!')
elif lista[jogada] == 'Tesoura' and computador == lista[0]:
    computador_venceu(computador, jogada)
elif lista[jogada] == 'Papel' and computador == lista[2]:
    computador_venceu(computador, jogada)
elif lista[jogada] == 'Pedra' and computador == lista[1]:
    computador_venceu(computador, jogada)