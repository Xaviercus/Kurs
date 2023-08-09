def pokaz_parametry(**arg):
    for klucz, wartosc in arg.items():
        print(f"Arg kluczowy: {klucz}, Wartość: {wartosc}")

pokaz_parametry(imie="Piotr", wiek=30, miasto="Warszawa", panstwo = "Polska")
pokaz_parametry(imie="Adam", wiek=29)
