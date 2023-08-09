def max_num(lista):
    if len(lista) == 0:
        return None
    return max(lista)

moja_lista = [10, 20, 5, 40, 30]
najwieksza = max_num(moja_lista)

print(najwieksza)

print("========================")

def min_num(lista):
    if len(lista) == 0:
        return None
    return min(lista)

moja_lista = [10, 20, 5, 40, 30]
najmniej = min_num(moja_lista)

print(najmniej)

print("========================")

def max_abs(lista):
    if len(lista) == 0:
        return None
    return max(lista, key=abs)

moja_lista = [-10, 20, 5, -20, -30]
mxabs = max_abs(moja_lista)

print(mxabs)

print("========================")

def min_len(lista_napisow):
    if len(lista_napisow) == 0:
        return None
    return min(lista_napisow, key=len)

napisy = ["jabłko", "gruszka", "banan", "śliwka", "malina"]
napis = min_len(napisy)

print(napis)




