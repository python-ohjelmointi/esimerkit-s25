while True:
    try:
        nimi = input("Syötä tiedoston nimi:")
        with open(nimi, encoding="utf-8") as tiedosto:
            sisalto = tiedosto.read()
            print(sisalto)
            break

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("Cannot read the file")

    except OSError:
        print("Some other error")
