# ruudukko on sanakirja
ruudukko = {}

# nappula kohtaan (0, 3)
# avaimet voivat olla merkkijonoja, tupleja tai monia muita tyyppejä
ruudukko[(0, 3)] = "👑"
ruudukko[(0, 1)] = "🐴"

print(ruudukko)

# tulostetaan pelilauta
for y in range(8):
    for x in range(8):
        avain = (y, x)
        merkki = "."
        if avain in ruudukko:
            merkki = ruudukko[avain]

        print(merkki, end="")
    print()
