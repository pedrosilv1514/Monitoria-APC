
def escolhinha():

    numeros = []
    numeros_multiplos = []
    #Input dos números
    for i in input().split():
        numeros.append(int(i))
    
    numero_multiplo = int(input())

    for i in numeros:
        if i % numero_multiplo == 0:
            numeros_multiplos.append(i)

    
    print(*numeros_multiplos)


escolhinha()