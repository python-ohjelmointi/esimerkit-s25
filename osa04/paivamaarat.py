
def muotoile_paiva(paivamaara: str):
    vuosi, kuukausi, paiva = paivamaara.split("-")

    return f"{int(paiva)}.{int(kuukausi)}.{int(vuosi)}"

print(muotoile_paiva("2025-09-30"))
print(muotoile_paiva("2025-12-24"))
print(muotoile_paiva("2026-01-01"))

print(f"<span class='date'>{ muotoile_paiva("2025-10-01") }</span>")
