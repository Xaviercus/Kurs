class Zwierze:
    def __init__(self, imie_zwierzecia):
        self.imie_zwierzecia = imie_zwierzecia

    def daj_glos(self):
        print(f"Zwierze {self.imie_zwierzecia} wydaje dzwiek")


zwierze1 = Zwierze("Papuga")
zwierze2 = Zwierze("Kapibara")

zwierze1.daj_glos()
zwierze2.daj_glos()


class Pies(Zwierze):
    def __init__(self, imie_zwierzecia, rasa):
        super().__init__(imie_zwierzecia)
        self.rasa_psa = rasa

    def daj_glos(self):
        print(f"Pies {self.imie_zwierzecia} rasy {self.rasa_psa} wydaje szczekanie.")


# Tworzenie obiektu klasy Pies
pies1 = Pies("Burek", "Owczarek")
pies2 = Pies("Azor", "Labrador")

# Wywołanie metody daj_glos na obiekcie pies1 i pies2
pies1.daj_glos()
pies2.daj_glos()