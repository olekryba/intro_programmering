svar = int(input("Ange ett tal "))
gissningar = 0
while svar != "42":
    if svar < 42:
        svar = int(input("för lågt, ange ett nytt tal "))
        gissningar = gissningar + 1
    elif svar > 42:
        svar = int(input("för högt, ange ett nytt tal "))
        gissningar = gissningar + 1
    else: 
        print("grattis, du vann, du behövde", gissningar , "gissningar.")
        break
    



        