print(
    """" ******** TREASURE GAME ******* 
********  FIND A RIGHT PATH******* """
)
print("welcome skull island")
p = input("you are at crossroad choose a path , type right or left \n")
r = input("you are at the river , wait for the boat or swim \n")
d = input("you are at the door, choose red ,green,blue \n")

if p == "left" and r == "swim" and d == "green":
    print("treasure is yours $$$$$$$$$")
elif p == "right" and r == "boat" and d == "red":
    print("treasure is yours $$$$$$$$$")
else:
    print("GAME OVER")
