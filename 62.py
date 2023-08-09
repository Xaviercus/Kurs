import random


def generuj_losowe_liczby():
    return [random.randint(1, 49) for _ in range(6)]


def zgadnij_liczby(liczby):
    poprawnie_zagadniete = []
    for _ in range(6):
        zgadnij = int(input("Podaj swoją próbę: "))
        if zgadnij in liczby:
            poprawnie_zagadniete.append(zgadnij)

    return poprawnie_zagadniete


wylosowane_liczby = generuj_losowe_liczby()
poprawnie_zagadniete = zgadnij_liczby(wylosowane_liczby)

print("Poprawnie zgadnięte liczby:", poprawnie_zagadniete)
print("Ilość poprawnie zgadniętych liczb:", len(poprawnie_zagadniete))



