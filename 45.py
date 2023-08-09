def x():
    liczba = int(input("Podaj liczbę: "))
    if liczba == 0:
        return None
    return liczba % 2 == 0


while True:
    wynik = x()
    print("Czy wynik jest parzysty?", wynik)
1

