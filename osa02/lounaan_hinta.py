"""
Laske kuvitteellisen lounasravintolan annoksen hinta annetun henkilön iän
perusteella. Lounas maksaa normaalisti 12,90 €,
mutta lapset maksavat lounaasta 0,5 € per ikävuosi 12:een ikävuoteen asti.

6-vuotiaan lounas maksaa siis 3 euroa ja 12-vuotiaan lounas 6 euroa.
"""

normaali_hinta = 12.90
hinta_per_lapsen_ikavuosi = 0.5
lastenannoksen_ikaraja = 12

ika = int(input("Kuinka vanha olet? "))

if ika <= lastenannoksen_ikaraja:
    print(f"{ika}-vuotiaan lounas maksaa {ika * hinta_per_lapsen_ikavuosi} euroa")
else:
    print(f"{ika}-vuotiaan lounas maksaa {normaali_hinta} euroa")
