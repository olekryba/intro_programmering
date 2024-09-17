i = 1
tal_1 = 1
tal_2 = 1
while i < 30:
    print(tal_1)
    tal_1_backup = tal_1
    tal_1 = tal_2
    tal_2 = tal_1_backup + tal_2
    i = i+1
print("klar")