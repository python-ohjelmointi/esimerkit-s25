from pathlib import Path

def tallenna(tied: Path, sisalto: str):
    tied.write_text(sisalto, encoding="utf-8")

def main():
    tallennettava = Path(__file__).parent / "tallennettu.txt"

    hello_text = "hello world\n" * 100

    on_olemassa = tallennettava.exists()

    if on_olemassa:
        ylikirjoita = input(f"Tiedosto {tallennettava} on olemassa. Ylikirjoitetaanko? (k/e) ")

        if ylikirjoita == "k":
            tallenna(tallennettava, hello_text)
    else:
        tallenna(tallennettava, hello_text)


main()
