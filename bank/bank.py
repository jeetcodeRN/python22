n = input("Greeting :")
n = n.strip().lower()

if n[0:5] == "hello":
    print("$0")
elif n[0]=="h"and n[1]!="e":
    print("$20")
else:
    print("$100")
