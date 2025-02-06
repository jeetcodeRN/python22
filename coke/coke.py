n=0
ad=50
while n<=25:
    n=int(input("insert coin:"))
    if n==25 or n==10 or n==5:
        ad=ad-n
        if ad>0:
            print("Amount Due:",ad)
        elif ad<=0:
            break
        else:
           print("error")
    else:
     print("Amount Due:",ad)
print("Change Owed:",abs(ad))
