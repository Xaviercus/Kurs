def x(tFahr):
    tCels = 5 / 9 * (tFahr - 32)
    return tCels

tFahr = float(input("Podaj temperaturę w f: "))
tCels = x(tFahr)
print("Temperatura w c:", tCels)
