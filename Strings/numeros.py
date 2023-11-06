frase = input()

contador_numeros = 0
for i in frase:
    if i.isnumeric():
        contador_numeros += 1
    else:
        pass

print(contador_numeros)