year = int(input("enter year "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 200):
    print("leap")
else:
    print("not leap")
