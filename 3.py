def zlicz_samogloski(slowo):
    samogloski = "aeiou"
    ilosc_samoglosek = 0
    for litera in slowo:
        if litera in samogloski:
            ilosc_samoglosek += 1
    return ilosc_samoglosek

slowo_uzytkownika = input("Wprowadź słowo: ")
ilosc_samoglosek = zlicz_samogloski(slowo_uzytkownika)
print("Liczba samogłosek w słowie '{}' wynosi: {}".format(slowo_uzytkownika, ilosc_samoglosek))

print("Hello World !")



