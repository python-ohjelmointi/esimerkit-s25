paivat = "ma ti ke to pe la su"

osat = paivat.split(" ")

ekat = osat[:-1]
vika = osat[-1]

print(", ".join(ekat) + " ja " + vika)

# toivottu tulos: ma, ti, ke, to, pe, la ja su
