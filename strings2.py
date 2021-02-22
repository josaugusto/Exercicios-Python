'''
    faça um programa que leia uma frase pelo teclado e mostre:

    quantas vezes aparece a letra "A".
    
    em que posição ela aparece a primeira vez.

    Em que posição ela aparece a última vez.
'''
frase = input('Informe uma frase generica: ')
qtd = frase.lower().count('a')
print('A letra "A" apareceu {} '.format(qtd)+'vezes')
