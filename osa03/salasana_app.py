from salasanageneraattori import arvo_salasana

# paluuarvo voidaan ottaa muuttujaan
vastaus = int(input("Anna salasanan pituus: "))
salasana = arvo_salasana(vastaus)
# palautettua arvoa voidaan käyttää kuten mitä tahansa merkkijonoa
print(salasana)

# paluuarvot voidaan antaa myös suoraan toisen funktion parametreiksi
print(arvo_salasana(32))
print(arvo_salasana(64))
