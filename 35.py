lista_zakupow = {}

while True:
    produkt = input("Podaj nazwę produktu (wpisz 'koniec' aby zakończyć, 'lista' aby wyświetlić listę): ")

    if produkt == 'koniec':
        break

    if produkt == 'lista':
        print("Lista zakupów:")
        for produkt, ilosc in lista_zakupow.items():
            print(f"{produkt}: {ilosc}")
    else:
        ilosc = int(input("Podaj ilość tego produktu: "))
        if produkt in lista_zakupow:
            lista_zakupow[produkt] += ilosc
        else:
            lista_zakupow[produkt] = ilosc
