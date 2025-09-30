import random

kirjaimet = "abcdefghjkmnopqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789#$%&()*+,-./:;<=>?@[]^_"


def arvo_salasana(pituus):
    arvotut = ""
    while len(arvotut) < pituus:
        arvotut += random.choice(kirjaimet)
    return arvotut
