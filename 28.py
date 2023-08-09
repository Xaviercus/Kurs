x = input("Podaj listę:  ")
y = x.split()

match y:
    case []:
        print("pusta lista")
    case ['a']:
        print("pojedynczy element")
    case ['a', 'b', *reszta]:
        print("wiele elementów")
    case _:
        print("bledna wartość")
