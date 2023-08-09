def sumuj_elementy(*arg):
    return sum(arg)


print(sumuj_elementy(1, 2, 3))
print(sumuj_elementy(10, 20, 30, 40))
print(sumuj_elementy(5, -5, 10, -10))

print("===================")

def znajdz_najwieksza(*arg):
    return max(arg)


print(znajdz_najwieksza(1, 2, 3))
print(znajdz_najwieksza(10, 20, 30, 40))
print(znajdz_najwieksza(5, -5, 10, -10))

print("===================")

def srednia_aretmetyczna(*arg):
    return sum(arg) / len(arg)


print(srednia_aretmetyczna(1, 2, 3))
print(srednia_aretmetyczna(10, 20, 30, 40))
print(srednia_aretmetyczna(5, -5, 10, -10))
