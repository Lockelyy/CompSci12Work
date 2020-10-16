import random

# QUESTION 1

# a) Integer
# b) Integer
# c) Boolean
# d) String
# e) Boolean
# f) Integer

# QUESTION 2

# You can use" "

# QUESTION 3

a_var = "7"
b_var = 100
a_var = int(a_var)
b_var = str(b_var)
print(type(a_var))
print(type(b_var))

# QUESTION 4

# c)

# QUESTION 5

# A single equals sign is used when you are defining something like a variable or a list (ex: name = "Bill",
# list = []. A double equal sign is used when you are comparing two things, a double equals sign in this context just
# means that you are checking if the two things are equal to each other.

# QUESTION 6

# Infinite ifs (Infinite in a block)
# Infinite but there has to be an if statement in front of them (infinite in a block)
# Else statements must link up to if statements so there can only be as many else statements as there are if statements.
# (1 else statement in a block)

# QUESTION 7

# A + sign placed in between two integers adds the two integers. However, if it is placed in between two strings it
# combines the two strings with no space in between them. Examples below:
print(1 + 1)
print("Hi" + "no")

# QUESTION 8

userinput = input("Please enter a number: ")
userinput = int(userinput)
print(userinput + 1)

# QUESTION 9

numero = random.randint(1, 100)
print("The random number is: ", numero)

if numero <= 49:
    print("YOU FAIL")

if numero == 100:
    print("ACE")

if numero >= 50:
    print("YOU PASS")

# QUESTION 10

while True:
    nameinput = input("Please enter your name: ")

    if nameinput == "Bob":
        print("Hello", nameinput)
        break

    else:
        print("Hello", nameinput)

# QUESTION 11

colorlist = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
print(colorlist[0])
print(colorlist[-1])

colorlist.remove("green")
colorlist.insert(3, "blurple")

last_3 = colorlist[4:7]
print("The last_3 variable looks like this:",last_3)
print(colorlist)

# QUESTION 12

def createList(no1, no2):
    list12 = []
    while (no1 < no2 + 1):
        list12.append(no1)
        no1 += 1
        print(list12)

    for i in list12:
        print(i + 10)

createList(1,5)

