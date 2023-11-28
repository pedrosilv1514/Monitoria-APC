def compressao():
    escolha = int(input())
    for i in range(escolha):
        texto = input()
        
        i = 0
        saida = ''
        while i < len(texto):
            if texto[i].isalpha():
                char = texto[i]
                i += 1
                num_str = ''
                while i <len(texto) and texto[i].isdigit():
                    num_str += texto[i]
                    i += 1
                
                if num_str:
                    repeat = int(num_str)
                
                else:
                    repeat = 1
                
                saida += char * repeat
            
            else:
                i += 1
        
        print(saida)

compressao()