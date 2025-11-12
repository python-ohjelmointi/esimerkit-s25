# sanakirja:
kurssi = {
    "nimi": "Python-ohjelmointi",
    "tunnus": "SOF004AS2A"
}

print(kurssi)

print(kurssi["nimi"])
print(kurssi["tunnus"])

print(kurssi.keys())
print(kurssi.values())

# lista voi sisältää myös sanakirjoja, tai toisin päin:
kurssit = [kurssi, kurssi, kurssi]

print(kurssit)


print(kurssit[1]["nimi"])
