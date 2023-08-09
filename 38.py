
uczniowie = {}

while True:
    numer = input("Podaj numer indeksu ('q' aby zakończyć): ")

    if numer == 'q':
        break

    imie, nazwisko = input("Podaj imię i nazwisko ucznia oddzielone spacją: ").split()
    oceny = input("Podaj oceny ucznia oddzielone spacją: ").split()

    uczniowie[numer] = {"imię": imie, "nazwisko": nazwisko, "oceny": oceny}

for numer, dane in uczniowie.items():
    oceny_str = ", ".join(dane["oceny"])
    print(f"Num indeksu: {numer}, {imie} {nazwisko}, oceny: [{oceny_str}]")

print(uczniowie)

# {'123': {"imię": 'asd', "nazwisko": 'asd', "oceny": ['1', '2', '3', '4', '5']}}