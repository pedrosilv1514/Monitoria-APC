frase_inicial = input()

nova_string = ''

indice = 0
for i in frase_inicial:
    if indice % 2 == 0:
        pass
    else:
        if frase_inicial[indice] != ' ':
            nova_string += i
        else:
            pass
    indice += 1


print(nova_string.replace(' ', ''))