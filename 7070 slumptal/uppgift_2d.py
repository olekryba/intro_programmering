import random 
siffra1 = (random.randint(1, 9))
siffra2 = (random.randint(1, 9))
siffra3 = (random.randint(1, 9))
pengar = 50
print("pengar att spela för", pengar)
spel = str(input("vill du spela? (j/n) "))

while pengar > 0:
    if spel == "j" or spel == "J": 
        pengar = pengar -1
        if siffra1 == siffra2 == siffra3: 
            print(siffra1, siffra2, siffra3)
            print("grattis, du vann, +50kr")
            pengar = pengar + 50
            siffra1 = (random.randint(1, 9))
            siffra2 = (random.randint(1, 9))
            siffra3 = (random.randint(1, 9))
            print("du har", pengar, "kr att spela för")
            spel = str(input("vill du spela? (j/n) "))

        elif siffra1 == 7 and siffra2 == 7 and siffra3 == 7:
            print(siffra1, siffra2, siffra3)
            print("grattis, du vann!, +100kr")
            pengar = pengar + 100
            siffra1 = (random.randint(1, 9))
            siffra2 = (random.randint(1, 9))
            siffra3 = (random.randint(1, 9))
            print("du har", pengar, "kr att spela för")
            spel = str(input("vill du spela? (j/n) "))

        elif siffra1 == siffra2 or siffra1 == siffra3 or siffra2 == siffra3:
            print(siffra1, siffra2, siffra3)
            print("Minivinst!, +5kr")
            pengar = pengar +5
            siffra1 = (random.randint(1, 9))
            siffra2 = (random.randint(1, 9))
            siffra3 = (random.randint(1, 9))
            print("du har", pengar, "kr att spela för")
            spel = str(input("vill du spela? (j/n) "))

        elif siffra1 == 7 or siffra2 == 7 or siffra3 == 7:
            print(siffra1, siffra2, siffra3)
            print("sjuvinst!, +2kr") 
            pengar = pengar +2
            siffra1 = (random.randint(1, 9))
            siffra2 = (random.randint(1, 9))
            siffra3 = (random.randint(1, 9))
            print("du har", pengar, "kr att spela för")
            spel = str(input("vill du spela? (j/n) ")) 
        
        else: 
            print(siffra1, siffra2, siffra3)
            print("du förlora")
            siffra1 = (random.randint(1, 9))
            siffra2 = (random.randint(1, 9))
            siffra3 = (random.randint(1, 9))
            print("du har", pengar, "kr att spela för")
            spel = str(input("vill du spela? (j/n) "))


print("hejdå")
