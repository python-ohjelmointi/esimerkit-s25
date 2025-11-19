from kyselyt import kysy_luku_valilta

paivat = "ma ti ke to pe la su".split(" ")
numero = kysy_luku_valilta("Syötä viikonpäivän numero (0-6): ", 0, 6)

print(paivat[numero])

vuosi = kysy_luku_valilta("Syötä vuosi: ", 0, 3000)
print(vuosi)
