while True:
    a = str(input()) + " "
    if a == "quit! ":
        break
    elif len(a) > 4:
        if a[a.find("or") - 1] not in "ueoaiy" and a[a.find("or") + 2] == " ": # or could've used a.endswith("or")
            a = a[:-1].replace("or", "our")
            print(a)
        else:
            print(a)
    else:
        print(a)