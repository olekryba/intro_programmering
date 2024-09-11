tal = int(input("mata in ett tal:"))

if tal < 0:
    print("Talet är negativt")
elif 0 <= tal <= 9:
    print("Talet är ensiffrigt")
elif 10 <= tal <= 99:
    print("Talet är tvåsiffrigt")
elif 100 <= tal <= 999:
    print("Talet är tresiffrigt")
else: print("Talet är fyrsiffrigt eller större")
