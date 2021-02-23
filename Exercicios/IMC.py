nome = input('Informe seu nome: ')
altura = float(input('Digite sua altura(cm): '))
peso = float(input('Digite seu peso(Kg): '))
altura = altura/100
indice_corporal = peso / altura**2

if indice_corporal < 16:
    print('{} possui índice de massa corporal igual a {:.2f}, sendo classificado como: Baixo peso muito grave'
    .format(nome, indice_corporal))
elif indice_corporal >= 16 and  indice_corporal <= 16.99:
    print('{} possui índice de massa corporal igual a {:.2f}, sendo classificado como: Baixo peso grave'
    .format(nome, indice_corporal))
elif indice_corporal >= 18.50 and  indice_corporal <= 24.99:
     print('{} possui índice de massa corporal igual a {:.2f}, sendo classificado como: Peso normal'
    .format(nome, indice_corporal))
elif indice_corporal >= 25 and  indice_corporal <= 29.99:
    print('{} possui índice de massa corporal igual a {:.2f}, sendo classificado como: Sobrepeso'
    .format(nome, indice_corporal))
elif indice_corporal >= 30 and indice_corporal <= 34.99:
     print('{} possui índice de massa corporal igual a {:.2f}, sendo classificado como: Obesidade grau I'
    .format(nome, indice_corporal))
elif indice_corporal >= 35 and indice_corporal <= 39.99:
    print('{} possui índice de massa corporal igual a {:.2f}, sendo classificado como: Obesidade grau II'
    .format(nome, indice_corporal))
else:
     print('{} possui índice de massa corporal igual a {:.2f}, sendo classificado como: Obesidade grau III'
    .format(nome, indice_corporal))
