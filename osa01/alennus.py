# Alennus: halvempi tuote puoleen hintaan

hinta1 = 10
hinta2 = 12
alennusprosentti = 0.5

halvin = min(hinta1, hinta2)

hinta_alennuksen_jalkeen = hinta1 + hinta2 - halvin * 0.5

print(f"Yhteishinta: {hinta_alennuksen_jalkeen}")
