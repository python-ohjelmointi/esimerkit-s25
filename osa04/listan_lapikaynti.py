kuukaudet = ["tammikuu", "helmikuu",  "maaliskuu", "huhtikuu", "toukokuu",
             "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu",
             "marraskuu", "joulukuu"]

print(" While-toistolause ".center(60, "*"))
print()

kk = 0 # askeltaja

while kk < len(kuukaudet): # toistoehto
    nimi = kuukaudet[kk]
    print(nimi)
    kk += 1 # kasvatus

print()
print(" For-toistolause ".center(60, "*"))
print()

for nimi in kuukaudet:
    print(nimi.title())
