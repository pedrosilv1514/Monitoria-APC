def busca_impostor():
    quantidade_jogadores = int(input())
    lista_jogadores = []
    lista_impostores = []

    for i in range(quantidade_jogadores):
        jogador = input()
        lista_jogadores.append(jogador)
    
    for i in input().split():
        lista_impostores.append(i)
    
    for jogador in lista_jogadores:
         if not( jogador in lista_impostores):
                 print(jogador, end=' ')

busca_impostor()