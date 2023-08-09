def dodawanie(a, b):
    return a + b

try:
    liczba1 = float(input("Podaj pierwszą liczbę: "))
    liczba2 = float(input("Podaj drugą liczbę: "))
    wynik = dodawanie(liczba1, liczba2)
    print("Wynik dodawania: {:.2f}".format(wynik))
except ValueError:
    print("Niepoprawne dane. Wprowadź dwie liczby.")