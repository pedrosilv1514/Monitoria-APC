texto = input()
palavra_censurada = input()

if palavra_censurada in texto:
    texto_formatado = texto.replace(palavra_censurada, '*')
    print(texto_formatado)
    
else:
    print('tudo certo :)')