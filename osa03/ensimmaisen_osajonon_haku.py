sana = "python"
merkki = "y"

indeksi = sana.find(merkki)

osajono = sana[indeksi: indeksi + 3]

if len(osajono) == 3:
    print(osajono)
