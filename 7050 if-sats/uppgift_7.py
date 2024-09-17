månad = int(input("vilken månad är du född i? (1-12)"))

if månad in [12, 1, 2]: 
    årstid= "vintern"

elif månad in [3, 4, 5]:
    årstid = "våren"

elif månad in [6, 7, 8]:
    årstid = "sommaren"

elif månad in [9, 10, 11]:
    årstid = "hösten"

else: 
    årstid = "ogiltig månad"

print("du är förr på", årstid)

