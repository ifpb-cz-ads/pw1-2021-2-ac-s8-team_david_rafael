def validar_string(letras, min, max):
    tamanho = len(letras)
    return min <= tamanho <= max


print(validar_string("", 1, 5))
print(validar_string("ABC", 2, 5))
print(validar_string("ABCEFG", 3, 5))
print(validar_string("ABCEFG", 1, 10))
