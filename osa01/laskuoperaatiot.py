# liittymän nopeus (Mbit/s, megabittiä sekunnissa)
nopeus_mbit = int(input("Syötä liittymän nopeus (Mbit/s): "))

# Tiedoston koko: 27,4 MB (28 815 360 bytes) (MB, megatavut ja tavut)
koko_tavuina = int(input("Syötä tiedoston koko (tavuina): "))

tavu = 8 # bittiä

nopeus_megatavuina = nopeus_mbit / tavu
nopeus_tavuina = nopeus_megatavuina * 1_000 * 1_000
print(f"Nopeus megatavuina {nopeus_megatavuina}")
print(f"Nopeus tavuina {nopeus_tavuina}")

print(f"Koko tavuina: {koko_tavuina}")
print(f"Koko kilotavuina: {(koko_tavuina / 1024):.2f}")
print(f"Koko megatavuina: {(koko_tavuina / 1024**2):.2f}")

kesto = koko_tavuina / nopeus_tavuina
print(f"Tiedoston lataaminen kestää (teoriassa) {kesto:.2f} sekuntia")
