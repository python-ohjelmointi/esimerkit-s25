# Tämä esimerkki on tarina-tehtävän inspiroima:
teksti = "Olipa kerran pieni talo preerialla loppu"

tekstin_pituus = len(teksti)

i = 0

while i < len(teksti):
    print(i, teksti[i])
    i += 1


# tulostetaan vain alkuosa, jätetään pois "loppu":

alkuosa = teksti[:-5]
print(alkuosa)
