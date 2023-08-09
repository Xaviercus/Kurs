wprowadzenie = input("Podaj listę liczb oddzielonych spacją: ")

lista_liczb = list(map(int, wprowadzenie.split()))

unikalne_liczby = []
for liczba in lista_liczb:
    if liczba not in unikalne_liczby:
        unikalne_liczby.append(liczba)

print("Unikalne wartości:")
print(unikalne_liczby)
