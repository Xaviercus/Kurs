wprowadzenie = input("Podaj liczbę całkowitą: ")
liczba = int(wprowadzenie)

match liczba:
    case x if x > 0:
        print("Liczba dodatnia")
    case 0:
        print("Liczba wynosi 0")
    case _:
        print("Liczba ujemna")
