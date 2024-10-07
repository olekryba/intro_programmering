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

    diff = spelare - dator

    if diff == 0:
        print("lika")
    elif diff == 1:
        print("jag vann :)")
    elif diff == 2:
        print("Du vann")
    elif diff == -1:
        print("Du vann")
    else:
        print("Jag vann :)")
        
    dator = (random.randint(1, 3))
    spela = str(input("vill du spela? (j/n) "))
    spel = str(input("sten, sax eller påse? "))

print("Hejdå!")
