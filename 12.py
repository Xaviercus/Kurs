wartosci = []

for x in range(10):
    wartosc = input("Podaj wartość nr {}: ".format(x + 1))
    wartosci.append(wartosc)

print("Wprowadzone wartości (co druga):")
for x in wartosci[::2]:
    print(x)
