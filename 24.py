miesiac = input("Podaj numer miesiąca (1-12): ")

match miesiac:
    case '1':
        print("Styczeń")
    case '2':
        print("Luty")
    case '3':
        print("Marzec")
    case '4':
        print("Kwiecień")
    case '5':
        print("Maj")
    case '6':
        print("Czerwiec")
    case _:
        print("Błędna wartość. Podaj numer miesiąca od 1 do 12.")