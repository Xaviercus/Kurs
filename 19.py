pierwsze_wartosci = []
for x in range(5):
    wartosc = input("Podaj wartość {}: ".format(x + 1))
    pierwsze_wartosci.append(wartosc)

drugie_wartosci = []
for x in range(5):
    wartosc = input("Podaj kolejną wartość {}: ".format(x + 1))
    drugie_wartosci.append(wartosc)

if pierwsze_wartosci == drugie_wartosci:
    print("Wprowadzone wartości są identyczne.")
else:
    print("Wprowadzone wartości nie są identyczne.")
