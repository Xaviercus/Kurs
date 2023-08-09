oceny = {}

while True:
    imie = input("Podaj imię ucznia ('q' aby zakończyć): ")

    if imie.lower() == 'q':
        break

    ocena = float(input("Podaj ocenę ucznia: "))
    oceny[imie] = ocena

srednia = sum(oceny.values()) / len(oceny)
print("Średnia ocen wszystkich uczniów:", srednia)

# najlepszy = max(oceny, key=oceny.get)

najlepszy = None
najwyzsza = True

for imie, ocena in oceny.items():
    if ocena > najwyzsza:
        najlepszy = imie
        najwyzsza = ocena

# print("Najlepszy uczeń to:", najlepszy, "z oceną:", oceny[najlepszy])
print("Najlepszy uczeń to:", najlepszy, "z oceną:", najwyzsza)
print(oceny)
