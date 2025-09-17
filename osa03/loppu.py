# "kokoojamuuttuja"
sanat = ""

# "ikuinen luuppi"
while True:
    sana = input("Anna sana tarinaan: ")

    if sana== "loppu":
        break

    sanat += sana + " "

print(f"{sanat}")
