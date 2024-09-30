import random 
siffra1 = (random.randint(1, 9))
siffra2 = (random.randint(1, 9))
siffra3 = (random.randint(1, 9))
spel = str(input("vill du spela? (j/n) "))

while spel == "j" or spel == "J": 
    if siffra1 == siffra2 == siffra3: 
        print(siffra1, siffra2, siffra3)
        print("grattis, du vann")
        siffra1 = (random.randint(1, 9))
        siffra2 = (random.randint(1, 9))
        siffra3 = (random.randint(1, 9))
        spel = str(input("vill du spela? (j/n) "))

    elif siffra1 == 7 and siffra2 == 7 and siffra3 == 7:
        print(siffra1, siffra2, siffra3)
        print("grattis, du vann!")
        siffra1 = (random.randint(1, 9))
        siffra2 = (random.randint(1, 9))
        siffra3 = (random.randint(1, 9))
        spel = str(input("vill du spela? (j/n) "))
    else: 
        print(siffra1, siffra2, siffra3)
        print("du förlora")
        siffra1 = (random.randint(1, 9))
        siffra2 = (random.randint(1, 9))
        siffra3 = (random.randint(1, 9))
        spel = str(input("vill du spela? (j/n) "))

print("hejdå")



