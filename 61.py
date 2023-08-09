import random

liczbadz = random.randint(1, 100)
liczbap = 0

print("Witaj w grze zgadnij liczbę!")

while True:
    zgadnij = int(input("Podaj swoją liczbę: "))
    liczbap += 1

    if zgadnij < liczbadz:
        print("Za mała liczba!")
    elif zgadnij > liczbadz:
        print("Za duża liczba!")
    else:
        print(f"Brawo! Zgadłeś liczbę {liczbadz} po {liczbap} próbach.")
        break