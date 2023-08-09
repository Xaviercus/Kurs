x = input("Podaj liczbę całkowitą: ")
y = int(x)

match y:
    case 0:
        print("zero")
    case 1:
        print("jeden")
    case 2:
        print("dwa")
    case _:
        print("inne")