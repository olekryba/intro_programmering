import random

dator = (random.randint(1, 3))
spela = str(input("vill du spela? (j/n) "))

spel = str(input("sten, sax eller påse? "))

while spela == "j" or spela == "J":

    if spel == "sten":
        spelare = 1
    elif spel == "sax":
        spelare = 2
    elif spel == "påse":
        spelare = 3

    if dator == 1 and spelare == 1:
        print("sten, lika")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

    elif dator == 1 and spelare == 2:
        print("sten, jag vann :)")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

    elif dator == 1 and spelare == 3:
        print("sten, du vann")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

    elif dator == 2 and spelare == 1: 
        print("sax, du vann")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

    elif dator == 2 and spelare == 2:
        print("sax, lika")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

    elif dator == 2 and spelare == 3: 
        print("sax, jag vann :)")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

    elif dator == 3 and spelare == 1: 
        print("påse, jag vann :)")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

    elif dator == 3 and spelare == 2:
        print("påse, du vann")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

    elif dator == 3 and spelare == 3: 
        print("påse, lika")
        dator = (random.randint(1, 3))
        spela = str(input("vill du spela? (j/n) "))
        spel = str(input("sten, sax eller påse? "))

print("Hejdå!")





