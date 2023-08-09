class Kalkulator:
    nazwa = "prosty kalkulator"

kalkulator1 = Kalkulator()
kalkulator2 = Kalkulator()

print(kalkulator1.nazwa)
print(kalkulator2.nazwa)

print("++++++++++++++++++++++")
class LaptopNiedotykowy:
    ekran_dotykowy = False

class LaptopDotykowy:
    ekran_dotykowy = True

laptop_niedotykowy = LaptopNiedotykowy()
laptop_dotykowy = LaptopDotykowy()

print("Czy laptop niedotykowy ma ekran dotykowy?", laptop_niedotykowy.ekran_dotykowy)
print("Czy laptop dotykowy ma ekran dotykowy?", laptop_dotykowy.ekran_dotykowy)
