x = input("Podaj pierwszą liczbę: ")
y = input("Podaj drugą liczbę: ")
z = input("Podaj trzecią liczbę: ")

krotka = (x, y, z)

print("krotka", krotka)
print("posortowana", sorted(krotka))
print("nowa posortowana krotka", tuple(sorted(krotka)))

if krotka == tuple(sorted(krotka)):
    print("kolejność rosnąca.")
else:
    print("nie jest posortowana.")

z1, z2, z3 = krotka
print("wartość zmiennej 1:", z1, "wartosci zmiennej 2:", z2, "wartosci zmiennej 3:", z3)
