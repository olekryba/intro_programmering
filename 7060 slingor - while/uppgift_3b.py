i = 1
hur_många = int(input("hur många tal ska skrivas ut?"))
tal_1 = 1
tal_2 = 1
while i <= hur_många:
    print(tal_1)
    tal_1_backup = tal_1
    tal_1 = tal_2
    tal_2 = tal_1_backup + tal_2
    i = i+1
    print("kvot", tal_2 / tal_1)
print("klar")