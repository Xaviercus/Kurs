def mniejsze_niz_10_wieksze_rowne_5(liczba):
    return -10 < liczba < 10

liczby_rzeczywiste = [3.5, 8.2, 9.7, 12.1, 6.0, 4.9, 10.5]

wynik = filter(mniejsze_niz_10_wieksze_rowne_5, liczby_rzeczywiste)
wynik_lista = list(wynik)

print(wynik_lista)
