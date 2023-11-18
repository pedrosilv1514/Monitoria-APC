frase = input()

if 'zero' in frase:
    frase = frase.replace('zero', '0')

if 'um' in frase:
    frase = frase.replace('um', '1')

if 'dois' in frase:
    frase = frase.replace('dois', '2')

if 'três' in frase:
    frase = frase.replace('três', '3')

if 'quatro' in frase:
    frase = frase.replace('quatro', '4')

if 'cinco' in frase:
    frase = frase.replace('cinco', '5')

if 'seis' in frase:
    frase = frase.replace('seis', '6')

if 'sete' in frase:
    frase = frase.replace('sete', '7')

if 'oito' in frase:
    frase = frase.replace('oito', '8')

if 'nove' in frase:
    frase = frase.replace('nove', '9')

print(frase)