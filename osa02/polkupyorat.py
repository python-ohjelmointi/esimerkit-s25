maksiminopeus = int(input("Syötä maksiminopeus: "))
teho          = int(input("Syötä teho: "))
paino         = int(input("Syötä paino: "))

if maksiminopeus <= 25 and teho <= 250:
    print("Sähköavusteinen polkupyörä")

elif maksiminopeus <= 25 and teho <= 1_000:
    print("Moottorilla varustettu polkupyörä")

    if paino > 25:
        print("Vaatii vakuutuksen")

elif maksiminopeus <= 45:
    print("Sähkömopo")
    print("Vaatii mopo- tai moottoripyöräajokortin sekä rekisteröinnin ja liikennevakuutuksen")

else:
    print("Jokin muu ajoneuvoluokka")
