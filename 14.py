liczby = []


while True:
    wprowadzenie = input("Podaj liczbe lub wpisz 'stop' żeby zakończyć: ")
    if wprowadzenie.lower() == 's':
        break
    liczba = float(wprowadzenie)
    liczby.append(liczba)


if len(liczby) > 0:
    print("Największa liczba:", max(liczby))
    print("Najmniejsza liczba:", min(liczby))
else:
    print("Nie wprowadzono żadnych liczb.")