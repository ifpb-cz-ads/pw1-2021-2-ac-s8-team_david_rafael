def pesquise(lista, valor):
    if valor in lista:
        return lista.index(valor)
    return None
    
L1 = [10, 20, 25, 30]
print(pesquise(L1, 25))
print(pesquise(L1, 27))