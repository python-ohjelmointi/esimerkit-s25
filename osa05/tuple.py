from collections import namedtuple

Elokuva = namedtuple("Elokuva", ["nimi", "vuosi"])

elokuvat = [
    Elokuva("Avatar", 2009),
    Elokuva("Avengers: Endgame", 2019),
    Elokuva("Titanic", 1997),
    Elokuva("Star Wars: The Force Awakens", 2015),
    Elokuva("Avengers: Infinity War", 2018),
    Elokuva("Spider-Man: No Way Home", 2021),
    Elokuva("Jurassic World", 2015),
    Elokuva("The Lion King", 2019),
    Elokuva("The Avengers", 2012),
    Elokuva("Furious 7", 2015),
    Elokuva("Frozen II", 2019),
    Elokuva("Top Gun: Maverick", 2022),
    Elokuva("Oppenheimer", 2023),
    Elokuva("Barbie", 2023),
    Elokuva("Harry Potter and the Deathly Hallows: Part 2", 2011)
]

def tulosta_elokuva(leffa: Elokuva):
    print(f"{leffa.vuosi}: {leffa.nimi}")

def anna_vuosi(leffa: Elokuva):
    return leffa.vuosi

jarjestetty = sorted(elokuvat, key=anna_vuosi)

for elokuva in jarjestetty:
    tulosta_elokuva(elokuva)
