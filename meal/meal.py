def main():
    time=input("what time is it?")

    nt=convert(time)

    if nt>=7 and nt<=8:
        print("breakfast time")
    elif nt>=12 and nt<=13:
        print("lunch time")
    elif nt>=18 and nt<19:
        print("dinner time")
    else :
        print("error")

    return 0


def convert(time):
    h,m=time.split(':')
    h=int(h)
    m=int(m)
    newtime=h+m/60
    return newtime


if __name__ == "__main__":
    main()
