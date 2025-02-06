n = input("FILE NAME :").strip().lower()
e = n.rsplit(".",1)

if len(e)==2:
    a=e[1]
    if a== "gif":
        print("image/gif")
    elif a== "jpeg":
        print("image/jpeg")
    elif a == "jpg":
        print("image/jpeg")
    elif a== "png":
        print("image/png")
    elif a=="pdf":
        print("application/pdf")
    elif a== "zip":
        print("application/zip")
    elif a== "txt":
        print("text/plain")
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")


