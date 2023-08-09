def parzyste(element):
    return element % 2 == 0
def liczby_parzyste(lista):
    p_lista = filter(parzyste, lista)
    return list(p_lista)

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p_liczby = liczby_parzyste(liczby)
print("Liczby parzyste:", p_liczby)

print("=====================")

