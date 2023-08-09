def suma_elementow(lista):
    if len(lista) == 0: return 0
    return lista[0] + suma_elementow(lista[1:])

lista_liczb = [1, 2, 3, 4, 8]
print(suma_elementow(lista_liczb))
