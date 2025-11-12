kirjaimet = "ABCDEFGHIJ" #....

koko = 4

for etaisyys_y in range(-koko+1, koko):
    y = abs(etaisyys_y)

    for etaisyys_x in range(-koko+1, koko):
        x = abs(etaisyys_x)

        etaisyys = max(x, y)
        print(kirjaimet[etaisyys], end="")
    
    print() # rivinvaihto

