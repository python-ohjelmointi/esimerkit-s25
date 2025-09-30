
def muotoile_paiva(paivamaara: str):
    vuosi = paivamaara[0:4]
    kuukausi = paivamaara[5:7]
    paiva = paivamaara[8:]

    muotoiltu = f"{int(paiva)}.{int(kuukausi)}.{int(vuosi)}"

    return muotoiltu

print(muotoile_paiva("2025-09-30"))
print(muotoile_paiva("2025-12-24"))
print(muotoile_paiva("2026-01-01"))

print(f"<span class='date'>{ muotoile_paiva("2025-10-01") }</span>")
