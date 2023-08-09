def oblicz_srednia(liczby):
    suma = sum(liczby)
    ilosc = len(liczby)
    srednia = suma / ilosc
    return srednia

def wczytaj_liczby():
    liczby = []
    while True:
        wprowadzenie = input("Podaj liczbę (lub 'q' aby zakończyć): ")
        if wprowadzenie.lower() == 'q':
            break
        try:
            liczba = float(wprowadzenie)
            liczby.append(liczba)
        except ValueError:
            print("Niepoprawne dane. Podaj liczbę lub wpisz 'q' aby zakończyć.")
    return liczby

liczby_uzytkownika = wczytaj_liczby()
if len(liczby_uzytkownika) > 0:
    srednia = oblicz_srednia(liczby_uzytkownika)
    print("Średnia wynosi:", srednia)
else:
    print("Nie wprowadzono żadnych liczb.")
