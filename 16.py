pierwsze_wartosci = []
for x in range(5):
    wartosc = input("Podaj wartość {}: ".format(x + 1))
    pierwsze_wartosci.append(wartosc)

identyczne = True
for x in range(5):
    wartosc = input("Podaj kolejną wartość {}: ".format(x + 1))
    if wartosc != pierwsze_wartosci[x]:
        identyczne = False
        break

if identyczne:
    print("Wprowadzone wartości są identyczne.")
else:
    print("Wprowadzone wartości nie są identyczne.")
