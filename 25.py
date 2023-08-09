typ_uzytkownika = []
for i in range(5):
    liczba = int(input(f"Podaj liczbę {i + 1}: "))
    typ_uzytkownika.append(liczba)

match typ_uzytkownika:
    case [7, 14, 22, 35, 42] | [1, 2, 3, 4, 5]:
        print("Gratulacje! Wygrałeś 1.000.000 zł!")
    case _:
        print("Niestety, nie udało Ci się wygrać. Spróbuj ponownie.")
print("Wygrane liczby to 7, 14, 22, 35, 42, 1, 2, 3, 4, 5,")
print("Twoje liczby", (typ_uzytkownika))
