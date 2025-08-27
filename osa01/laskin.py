# --- EI TOIMI --- #
# Error
# > Tehtävän src.laskin suorittaminen epäonnistui.
# > Varmista, että saat ohjelman suoritettua loppuun.
yksi = int(input("Luku 1: "))
kaksi = int(input("Luku 2: "))
komento = input("Komento: ")  # summa, erotus, tulo, tai jotain muuta

if komento == "summa":
    vastaus = yksi+kaksi
    print(f'{yksi} + {kaksi} = {vastaus}')

elif komento == "tulo":
    vastaus = yksi*kaksi
    print(f'{yksi} * {kaksi} = {vastaus}')

elif komento == "erotus":
    vastaus = yksi-kaksi
    print(f'{yksi} - {kaksi} = {vastaus}')
