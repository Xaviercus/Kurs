slownik = {}

for i in range(2):
    numer = int(input("Podaj numer: "))
    imie = input("Podaj imię: ")
    slownik[numer] = imie

print("Klucze:")
for numer in slownik:
    print(numer)

print("Wartości:")
for imie in slownik.values():
    print(imie)