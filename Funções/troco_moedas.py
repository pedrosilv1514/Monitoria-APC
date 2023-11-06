# A lógica para a resolução do problema é assim que for realizado o calculo da moeda, realiza-se a atualização do que restou faazendo o calculo do resto (%)
def troco (n):
    
    moedas_cinquenta = n // 50
    n = n % 50
    moedas_vinte = n // 25
    n = n % 25
    moedas_dez = n // 10
    n = n % 10
    moedas_cinco = n // 5
    n = n % 5
    moedas_um = n

    print(f'{moedas_cinquenta} moedas de 50 centavos')
    print(f'{moedas_vinte} moedas de 25 centavos')
    print(f'{moedas_dez} moedas de 10 centavos')
    print(f'{moedas_cinco} moedas de cinco centavos')
    print(f'{moedas_um} moedas de 1 centavo')

troco(567)