kraje_stolice = {
    "Polska": "Warszawa",
    "Niemcy": "Berlin",
    "Francja": "Paryż",
    "Włochy": "Rzym",
}


nazwa_kraju = input("Podaj nazwę kraju: ")


if nazwa_kraju in kraje_stolice:
    stolica = kraje_stolice[nazwa_kraju]
    print(f"Stolica {nazwa_kraju} to {stolica}.")
else:
    print(f"Brak informacji o stolicy kraju {nazwa_kraju} w słowniku.")
