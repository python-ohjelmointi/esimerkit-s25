
valmis_lista = ["yes", "no", "maybe"]

tyhja_lista: list[int] = []
tyhja_lista.append(10)
tyhja_lista.append(20)

tekstit_listana = ["ma", "ti", "ke"]
teksti_listana = list("esimerkki")  # tekee merkkijonosta listan

print(f"{valmis_lista = }")
print(f"{tyhja_lista = }")
print(f"{tekstit_listana = }")
print(f"{teksti_listana = }")

email = "noreply@haaga-helia.fi"

tunnus, domain = email.split("@")

print(f"{tunnus = }")
print(f"{domain = }")
