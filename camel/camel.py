t=input("camelCase:")
print("snake_name:" , end="")
for n in t:
    if n.isupper():
        n=n.lower()
        print(f"_{n}" ,end="")
    elif n.islower():
        print(n ,end="")
    else:
        print("error")
