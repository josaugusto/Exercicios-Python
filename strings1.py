'''
    Crie um programa que leia o nome completo de uma pessoa e mostre

    o nome com todas as letras maiúsculas

    o nome com todas minúsculas.

    quantas letras ao todo(sem considerar espaços).

    quantas letras tem o primeiro nome

    jose augusto silva santos
'''

nome = input('Informe seu nome: ').strip()

print('Nome em maiúscula: '+nome.upper())
print('Nome em minúscula: '+nome.lower())
lista = nome.split()

i = 0
soma = 0
while i<len(lista):
    soma+=len(lista[i])
    i+=1 
print('O nome {} possui {} letras ao todo'.format(nome, soma))
primeiro = len(lista[0])
print('O primeiro nome possui {} letras ao todo'.format(primeiro))
