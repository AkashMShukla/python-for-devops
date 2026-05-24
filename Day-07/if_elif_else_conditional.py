import sys

type = sys.argv[1]

if type == "t2.micro":
    print("It will charge you 2$/month")
elif type == "t2.medium":
    print("It will charge you 4$/month")
else:
    print("Please enter valid type")