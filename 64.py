class Prostokat:
    def pole(self, a, b):
        return a * b


prostokat = Prostokat()
dlu_b = 5
szer_b = 10
wynik = prostokat.pole(dlu_b, szer_b)
print("Pole prostokąta o długości boków", dlu_b, "i", szer_b, "wynosi:", wynik)

print("--------------------------------")


class Kwadrat:
    def obwod(self, a):
        return 4 * a


kwadrat = Kwadrat()
dlugosc_b = 7
wynik = kwadrat.obwod(dlugosc_b)
print("Obwód kwadratu o długości boku", dlugosc_b, "wynosi:", wynik)

print("--------------------------------")


class Pies:
    def daj_glos(self, tekst):
        print(tekst + " hau hau!")


pies = Pies()
tekst_do_wys = "Cześć, jestem pies"
pies.daj_glos(tekst_do_wys)

print("--------------------------------")


class Pies:
    def __init__(self, imie, wiek, rasa):
        self.imie = imie
        self.wiek = wiek
        self.rasa = rasa


imie_psa = "Lucky"
wiek_psa = 3
rasa_psa = "Spanile"

pies = Pies(imie_psa, wiek_psa, rasa_psa)
print("Imię psa:", pies.imie)
print("Wiek psa:", pies.wiek)
print("Rasa psa:", pies.rasa)

print("--------------------------------")


class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

    def informacje(self):
        return f"Tytuł: {self.tytul}, Autor: {self.autor}"


tytul_ksiazki = "Krew Elfów"
autor_ksiazki = "Andrzej Sapkowski"

ksiazka = Ksiazka(tytul_ksiazki, autor_ksiazki)
print(ksiazka.informacje())

print("--------------------------------")
