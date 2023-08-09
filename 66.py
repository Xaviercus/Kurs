class KontoBankowe:
    def __init__(self, numer_konta, saldo):
        self._saldo = saldo
        self._numer_konta = numer_konta


class KontoOszczednosciowe(KontoBankowe):
    def __init__(self, numer_konta, saldo, oprocentowanie):
        super().__init__(numer_konta, saldo)
        self._oprocentowanie = oprocentowanie

    def oblicz_odsetki(self):
        return self._saldo * (self._oprocentowanie / 100)


konto_oszczednosciowe = KontoOszczednosciowe("12345", 1000, 2.5)

odsetki = konto_oszczednosciowe.oblicz_odsetki()
print(f"Odsetki: {odsetki}")


