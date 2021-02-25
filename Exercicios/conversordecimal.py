'''
    rascunho:

    6 na base 2
    divisões consecutivas
        6|2
        0 3|2
        ...
        pegar os restos de trás pra frente

    binario: 0 e 1
'''
numero = int(input('Informe um número decimal inteiro: '))
i = 1
resto = []
while i != 0:
    resto.append(numero%2)
    quociente = numero//2
    numero = quociente
    if quociente == 0 and resto[-1] == 0:
        i = 0
resto.reverse()

print(resto)