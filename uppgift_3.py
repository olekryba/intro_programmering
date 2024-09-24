svar = int(input("Ange ett tal "))
count = 1
gissningar = 0
while svar != "42":
    if count < 3:
        if svar < 42:
            svar = int(input("för lågt, ange ett nytt tal "))
            gissningar = gissningar + 1
            count = count + 1
        elif svar > 42:
            svar = int(input("för högt, ange ett nytt tal "))
            gissningar = gissningar + 1
            count = count + 1
        else: 
            print("grattis, du vann, du behövde", gissningar , "gissningar.")
            break
    else: 
        print("du har gåssat 3 gånger, du har förlorat")
        break