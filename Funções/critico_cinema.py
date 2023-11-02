def nota(n):
    notas_restantes = 10 - n
    notas_ocupadas = '★'
    resto_notas = '☆'

    print(f"|{n*notas_ocupadas}{notas_restantes*resto_notas}| ")

# nota(0)
# nota(3)
# nota(7)
