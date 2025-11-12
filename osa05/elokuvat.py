elokuvat = """Avatar (2009)
Avengers: Endgame (2019)
Titanic (1997)
Star Wars: The Force Awakens (2015)
Avengers: Infinity War (2018)
Spider-Man: No Way Home (2021)
Jurassic World (2015)
The Lion King (2019)
The Avengers (2012)
Furious 7 (2015)
Frozen II (2019)
Top Gun: Maverick (2022)
Oppenheimer (2023)
Barbie (2023)
Harry Potter and the Deathly Hallows: Part 2 (2011)""".splitlines()

tulosteet: list[str] = []

for elokuva in elokuvat:
    nimi = elokuva[0:-7]
    vuosi = elokuva[-5:-1]

    rivi = f"{vuosi}: {nimi}"
    tulosteet.append(rivi)


jarjestetty = sorted(tulosteet)

for leffa in jarjestetty:
    print(leffa)
