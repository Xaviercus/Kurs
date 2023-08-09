def odleglosc_od_zera(liczba):
    odleglosc = abs(liczba)
    return odleglosc


print(odleglosc_od_zera(-20))
print(odleglosc_od_zera(0))
print(odleglosc_od_zera(88))

print("==========================")

lista = ['a', 'b', 'c', 'd']

for ind, war in enumerate(lista):
    print(f"Indeks: {ind}, Wartość: {war}")

print("==========================")


def idenks_lub_none(lista, element):
    for indeks, wartosc in enumerate(lista):
        if wartosc == element:
            return indeks
        return None


listam = [10, 15, 20, 30, 45]
element = 45

wynik = idenks_lub_none(listam, element)
if wynik is not None:
    print(f"Indeks elementu {element} w liście: {wynik}")
else:
    print(f"Element {element} nie istnieje w liście.")
