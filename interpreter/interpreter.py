def main():
    n=input("EXPRESSION:")
    x,y,z=n.split(" ")
    x= float(x)
    z=float(z)
    if y=='+':
        ans=add(x,z)
        print(f"{ans:.1f}")
    elif y=='-':
        ans=sub(x,z)
        print(f"{ans:.1f}")
    elif y=='*':
        ans=mul(x,z)
        print(f"{ans:.1f}")
    elif y=='/':
        if x!=0 and z!=0:
            ans=div(x,z)
            print(f"{ans:.1f}")
        else:
            print("number not divisible by zero")
    else:
        print("error")

    return 0

def add(x,y):
    return x+y
def mul(x,y):
    return x*y
def sub(x,y):
    return x-y
def div(x,y):
    return x/y


if __name__ == "__main__":
    main()


