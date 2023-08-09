liczby = []

while True:
    wprowadzenie = input("Podaj liczbę lub wpisz 'stop' żeby zakończyć: ")
    if wprowadzenie.lower() == 's':
        break

    liczba = wprowadzenie

    if liczba in liczby:
        liczby.remove(liczba)
    else:
        liczby.append(liczba)

print("Wprowadzone liczby:")
print(liczby)
