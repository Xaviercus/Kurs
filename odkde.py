def sprawdz_parzystosc(liczba):
    if liczba % 2 == 0:
        print(f"Liczba {liczba} jest parzysta.")
    else:
        print(f"Liczba {liczba} jest nieparzysta.")

try:
    liczba = int(input("Podaj liczbe: "))
    sprawdz_parzystosc(liczba)
except ValueError:
    print("To nie jest poprawna liczb. Spróbuj ponownie.")
