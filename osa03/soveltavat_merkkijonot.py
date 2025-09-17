naytetaan = 5
luottokortti = "5555555555554444"

pituus = len(luottokortti)
sensuroitu = "*" * (pituus - naytetaan) + luottokortti[-naytetaan:]

print("Sensuroitu luottokortti:")
print(sensuroitu)

print()

vari = "#EDC9C5"
#          RRGGBB
#          rgb(237, 201, 197)

r = vari[1:3]
g = vari[3:5]
b = vari[5:]

print("HEX-muotoisen värin mmuuttaminen desimaaleiksi:")
print(r, g, b)
print(int(r, 16), int(g, 16), int(b, 16))
print()


url = "https://python-ohjelmointi.github.io"
print(url)
secure = url.startswith("https://")
print("Onko turvallinen?", secure)

print()

email = "noreply@example.com"
print(email)
at_merkki = email.index("@")

print("Tunnus:", email[: at_merkki])
print("Domain:", email[at_merkki+1 : ])


# kukin saa halutessaan tutkia päivämäärää :)
paivamaara = "2025-09-16"
