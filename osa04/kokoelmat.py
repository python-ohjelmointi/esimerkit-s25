esimerkki = ["tammikuu", "helmikuu",  "maaliskuu", "huhtikuu", "toukokuu",
             "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu",
             "marraskuu", "joulukuu"]

pituus = len(esimerkki)

eka = esimerkki[0]
toka = esimerkki[1]
vika = esimerkki[-1]

ekat_viisi = esimerkki[:5]
vikat_viisi = esimerkki[-5:]

print(f"{pituus = }")
print(f"{eka = }")
print(f"{toka = }")
print(f"{vika = }")
print(f"{ekat_viisi = }")
print(f"{vikat_viisi = }")
