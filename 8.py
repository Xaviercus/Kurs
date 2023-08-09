# liczba1 = float(input("Podaj pierwszą liczbę: "))
# liczba2 = float(input("Podaj drugą liczbę: "))
#
# suma = liczba1 + liczba2
#
# print("Suma dwóch liczb wynosi:", suma)


while True:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))

    suma = liczba1 + liczba2

    print("Suma dwóch liczb wynosi:", suma)

    kontynuacja = input("Czy chcesz kontynuować? (Tak/Nie): ")
    if kontynuacja.lower()!= 'tak':
       break
