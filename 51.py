def odwracanie_napisu(napis):
    if len(napis) == 0: return " "
    return odwracanie_napisu(napis[1:]) + napis[0]


napis_do = "masło"
print(odwracanie_napisu(napis_do))
