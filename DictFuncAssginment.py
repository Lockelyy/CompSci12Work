#1 - b)

#2
dict2 = {'num1': 17, 'num2': 36, 'num3': 10928}
total = 0
for i in dict2.values():
    total += i
print("total is equal to: ", str(total))

#3
dict3a = {'item1a': 'something', 'item2a': 'other thing'}
dict3b = {'item1b': 'third thing', 'item2b': 'fourth thing'}
dict3complete = {}

for i in dict3a:
    dict3complete[i] = dict3a[i]

for x in dict3b:
    dict3complete[x] = dict3b[x]

print(dict3complete)

#4
dict4 = {'key1': 'potato', 'key2': 'tomato', 'key3': 'potato', 'key4': 'tomatoe', 'key5': 'tomato'}
dict4unique = {}



#5
# Lists contain single values not assocaited with a key and would therefore be used in a shopping list for example or just storing random numbers
# Dictionaries have key value pairs and this would be useful for storing values when you want to correspond them to each other such as usernames and passwords

#6 d)
def namefunc(fname, lname, nname, bname, gname):
  print(fname + lname + nname + bname + gname)

namefunc("Emil", "Refsnes", "Hi", "Bee", "welcome")

#7
def funky_func(name, age):
    print("Name is: ", name, "\nAge is: ", age)

funky_func("17", "John")

#8 the cool way
def num_func(num1, num2, num3):
    num_list = []
    num_list.append(num1)
    num_list.append(num2)
    num_list.append(num3)
    print(max(num_list))

num_func(75,34,103)

#9
a_list = [23, 35, 24134, 124]

def list_sum(listinp):
    sum = 0
    for i in listinp:
        sum += i
        print(sum)

list_sum(a_list)

#10/11 Because they organize specific code into more general terms and using variables thus making it easieer to read. This also makes long code shorter as functions take out the process
# of needing to repeat code every single time you want to do something. Say I want to add all the numbers inside of 30 lists, and say it took 20 lines of code to do so. Instead of writing 20 lines
# of code 30 times I could write those 20 lines of code inside of a function and then call that function 30 times reducing those 20 lines to 1.
