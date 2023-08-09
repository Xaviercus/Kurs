liczby = []

while True:
    wprowadzenie = input("Podaj liczbę lub wpisz 'stop' żeby zakończyć: ")

    if wprowadzenie.lower() == 'stop':
        break

    liczba = int(wprowadzenie)

    if liczba in liczby:
        liczby.remove(liczba)
    else:
        liczby.append(liczba)

print("Unikalne wartości:")
print(liczby)
