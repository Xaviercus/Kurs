lista_slow = input("Podaj listę słów oddzielonych spacją: ").split()

slownik = {}
for slowo in lista_slow:
    if slowo in slownik:
        slownik[slowo] += 1
    else:
        slownik[slowo] = 1

print("Słownik:")
for slowo, liczba in slownik.items():
    print(f"{slowo}: {liczba}")

