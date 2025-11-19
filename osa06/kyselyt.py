def kysy_luku(pyynto: str) -> int:
    while True:
        try:
            syote = input(pyynto)
            luku = int(syote)
            return luku

        except ValueError:
            print("Virheellinen numero!")

def kysy_luku_valilta(pyynto: str, minimi: int, maksimi: int) -> int:
    while True:
        luku = kysy_luku(pyynto)

        if minimi <= luku <= maksimi:
            return luku

        print("Luku ei ollut oikealla välillä!")
