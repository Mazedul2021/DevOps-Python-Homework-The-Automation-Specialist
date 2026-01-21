port = input("Enter Your Port: ")

port = int(port)

if 1 <= port <= 65536:
    print("Your Port is Valid")
else:
    print("Your Port is Invalid")    