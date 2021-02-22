'''
    Formula para converter graus para fanrenheit 

    °C/5 = F - 32/9
    9x°C = 5F - 160
    F = (9x°C + 160)/5

    é só reduzir a formula para uma forma mais simplificada da mesma 
'''
temperatura = float(input('Informe a temperatura em °C: '))
fahrenheit = (9 * temperatura + 160)/5 
print('{} °C em Fanrenheit é igual a: {} °F'.format(temperatura, fahrenheit))