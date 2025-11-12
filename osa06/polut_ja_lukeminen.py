from pathlib import Path

print(f"{__file__=}")

polku = Path(__file__)
print(f"{polku=}")

ylahakemisto = polku.parent
print(f"{ylahakemisto=}")

zen_tiedosto = ylahakemisto / "zen.txt"
print(f"{zen_tiedosto=}")

sisalto = zen_tiedosto.read_text(encoding="utf-8")

# tästä eteenpäin sisalto on ihan vain merkkijono, jolla ei ole mitään yhteyttä tiedostoon

print(sisalto)
