count = 0

primtal = [True ]*101

primtal[0] = False
primtal[1] = False
# stryk tal som är delbara med 2 men ej 2
for tal in range(2 + 2, 101, 2):
    primtal[tal] = False
# nästa tal efter 2 som ej är struket
tal = primtal.index(True, 2 + 1) #3

# stryk tal som är delbara med 3 men ej 3
for tal in range(3+3, 101, 3):
    primtal[tal] = False

tal=primtal.index(True, 3+1)

for tal in range(4+4, 101, 4):
    primtal[tal] = False

tal=primtal.index(True, 4+1)

for tal in range(5+5, 101, 5):
    primtal[tal] = False

tal=primtal.index(True, 5+1)

for tal in range(6+6, 101, 6):
    primtal[tal] = False

tal=primtal.index(True, 6+1)

for tal in range(7+7, 101, 7):
    primtal[tal] = False

tal=primtal.index(True, 7+1)

for tal in range(8+8, 101, 8):
    primtal[tal] = False

tal=primtal.index(True, 8+1)

for tal in range(9+9, 101, 9):
    primtal[tal] = False

tal=primtal.index(True, 9+1)

print(primtal)
