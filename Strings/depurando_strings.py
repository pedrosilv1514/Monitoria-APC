def não_possui_a_letra_u(palavra):
    new_palavra = palavra.lower()
    for letra in new_palavra:
        if letra in 'uúûüù':
            return False
    return True


print(não_possui_a_letra_u("Universidade")) # False
print(não_possui_a_letra_u("sükûnet")) # False
print(não_possui_a_letra_u("Baú")) # False