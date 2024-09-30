import random

print("Välkommen, du kommer få kasta 2 tärningar, varje spel kostar 1kr. Om du kastar 2 6or vinner du 5kr, om du får en stege vinner du 2kr och om du får en dubeltt vinner du 3kr. Spelet avslutas när du har förlorat alla pengar eller väljer att avsluta det själv. Du kan när som helst sätta in mer pengar genom att tryvka på (i)")

pengar = int(input("ange belopp du vill sätta in: "))
spel = str(input("välj spela (s), insättning (i) eller avsluta (a) "))
tärning1 = (random.randint(1, 6))
tärning2  = (random.randint(1, 6))

while pengar > 0:
    if spel == "s": 
        pengar = pengar -1
        if tärning1 == tärning2 + 1 or tärning1 == tärning2 - 1:
            print(tärning1, tärning2, "stegvinst +2kr")
            pengar = pengar + 2
            print("pengar att spela för:", pengar)
            spel = str(input("välj spela (s), insättning (i) eller avsluta (a) "))
            tärning1 = (random.randint(1, 6))
            tärning2 = (random.randint(1, 6))
        else:
            if tärning1 == 6 and tärning2 == 6:
                print(tärning1, tärning2, "sex-vinst, +5kr")
                pengar = pengar + 5
                print("pengar att spela för:", pengar)
                spel = str(input("välj spela (s), insättning (i) eller avsluta (a) "))
                tärning1 = (random.randint(1, 6))
                tärning2 = (random.randint(1, 6))
            else:
                if tärning1 == tärning2:
                    print(tärning1, tärning2, "vinst, +3kr")
                    pengar = pengar + 3
                    print("pengar att spela för:", pengar)
                    spel = str(input("välj spela (s), insättning (i) eller avsluta (a) "))
                    tärning1 = (random.randint(1, 6))
                    tärning2 = (random.randint(1, 6))
                else: 
                    print(tärning1, tärning2, "ingen vinst")
                    print("pengar att spela för:", pengar)
                    spel = str(input("välj spela (s), insättning (i) eller avsluta (a) "))
                    tärning1 = (random.randint(1, 6))
                    tärning2 = (random.randint(1, 6))
    elif spel == "i":
        pengar = pengar + int(input("ange belopp att sätta in: "))
        print("du har", pengar, "kr att spela för")
        spel = str(input("välj spela (s), insättning (i) eller avsluta (a) "))
        tärning1 = (random.randint(1, 6))
        tärning2 = (random.randint(1, 6))

    elif spel == "a":
        break
    

print("du har", pengar, "kr")