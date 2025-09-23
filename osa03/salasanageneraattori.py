from random import choice

kirjaimet = "abcdefghjkmnopqrstuvwxyzABCDEFGHJKMNPQRSTUVWXYZ23456789#$%&()*+,-./:;<=>?@[]^_"

def arvo_salasana(pituus):
    arvotut = ""
    while len(arvotut) < pituus:
        arvotut += choice(kirjaimet)
    return arvotut
