
gräns = int(input("ange en övre gräns:"))
tal_1 = 1
tal_2 = 1
while tal_1 < gräns:
    print(tal_1)
    tal_1_backup = tal_1
    tal_1 = tal_2
    tal_2 = tal_1_backup + tal_2

    
    
print("klar")