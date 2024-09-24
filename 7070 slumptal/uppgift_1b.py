import random
spel = str(input("vill du spela? (j/n)? "))
tärning1 = (random.randint(1, 6))
tärning2  = (random.randint(1, 6))

while spel == "j":
    if tärning1 == 6 and tärning2 == 6:
        print(tärning1, tärning2, "grattis, du fick sex-vinst")
        spel = str(input("vill du spela? (j/n) "))
        tärning1 = (random.randint(1, 6))
        tärning2 = (random.randint(1, 6))
    else:
        if tärning1 == tärning2:
            print(tärning1, tärning2, "Grattis, du vann")
            spel = str(input("vill du spela? (j/n) "))
            tärning1 = (random.randint(1, 6))
            tärning2 = (random.randint(1, 6))
        else: 
            print(tärning1, tärning2, "du förlora")
            spel = str(input("vill du spela? (j/n) "))
            tärning1 = (random.randint(1, 6))
            tärning2 = (random.randint(1, 6))
print("Hejdå")
