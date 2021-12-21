def pesquisa(lista, item):
    return item + ' tem na lista' if item in lista else 'não tem na lista'

lista = ['banana', 'laranja', 'uva']
item = str(input("Pesquise quais frutas tem na lista"))

print(pesquisa(lista, item))
