class zwierze:
    def __init__(self, imie, gatunek):
        self._imie = imie
        self._gatunek = gatunek

class ptak(zwierze):
    def __init__(self, imie, gatunek, rodzaj_ptaka):
        super().__init__(imie, gatunek)
        self._rodzaj_ptaka = rodzaj_ptaka
        print(f"imie {imie}, gatunek {gatunek}, rodzaj ptaka {rodzaj_ptaka}")

class ssak(zwierze):
    def __init__(self, imie, gatunek, rodzaj_ssaka):
        super().__init__(imie, gatunek)
        self._rodzaj_ssaka = rodzaj_ssaka
        print(f"imie {imie}, gatunek {gatunek}, rodzaj ssaka {rodzaj_ssaka}")

ptak_obiekt = ptak("seagull", "Steven", "mewa")
ssak_obiekt = ssak("puma", "kociak", "drapieżnik")



