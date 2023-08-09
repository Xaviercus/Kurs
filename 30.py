krotka = (15, 7, 29, 42, 10, 3)

min_x = krotka[0]
max_y = krotka[0]

for liczba in krotka:
    if liczba < min_x:
        min_x = liczba
    if liczba > max_y:
        max_y = liczba

print("Najmniejsza liczba:", min_x)
print("Największa liczba:", max_y)

(z1, *z2, z3) = krotka

print("zmienna 1:", z1)
print("zmienna 2:", z2)
print("zmienna 3:", z3)

nowa_krotka = krotka + (z1, *z2, z3)
print(nowa_krotka)
