aux = numero = int(input('Informe um número inteiro: '))
binario = []
while True:
    binario.append(str(aux%2))
    quociente = aux//2
    aux = quociente
    if quociente == 0 and binario[-1] == '0':
        break
binario.reverse()
print(f'O número {numero} em binário é: '+''.join(binario))
