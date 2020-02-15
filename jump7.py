for x in range(1,101):
    if x%7==0 :
        continue
    elif x%10==7 or x//10==7:
        continue
    else:
        print(x)

