def e_multiplo(x,y):
    if x % y == 0:
        return "True"
    else:
        return "False"

x = int(input("Escreve o primeiro numero: "))
y = int(input("Escreva o segundo numeor: "))

print(e_multiplo(x,y))