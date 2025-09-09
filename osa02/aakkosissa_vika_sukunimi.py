from string import ascii_uppercase

# vakio:
kirjaimet = ascii_uppercase + "ÅÄÖ"

# "sopivimman säilyttäjä":
viimeinen = "Valtakari"

print("Syötä sukunimet, yksi per rivi. Tyhjä rivi lopettaa.")

while True:
    syote = input()

    if syote == "":
        break

    if syote[0] not in kirjaimet:
        continue

    if syote > viimeinen:
        viimeinen = syote


print(f"Aakkosissa viimeinen on {viimeinen}")   # Öörni
