# WINTER BREAK TEST

# 1. C
# 2. False
# 3. B
# 4. True
# 5.
# 6. A
# 7:
dict7 = {1: 7, 8: 3, 5: 5}

max_key = max(dict7)
print("Largest Key is: ", max_key)

all_values = dict7.values()
max_value = max(all_values)
print("Largest Value is: ", max_value)

# 8:
dict8a = {'apples': 8, 'oranges': 4, 'peaches': 10}
dict8b = {'apples': 3, 'oranges': 9, 'peaches': 5}
dict8total = {}

global value
for key, value in dict8a.items():

    dict8total[key] = value

for key, val in dict8b.items():
    if key in dict8total:
        dict8total[key] = dict8total[key] + val


print(dict8total)


# 9: False
# 10: Defining a function is effectively making the function and calling it just you using that function
# 11: You can pass arguments directly into the brackets following the function name like this: def my_function(arg):
#     or by defining the argument inside of the function.
# 12: The syntax to do so is *args and this is useful as you may not know how many arguments you want to pass to the
#     function right away and this allows your function to be flexible.
# 13:


def numberfunc(first, second, third):
    arguments = locals()
    print(arguments)

    for values in arguments.values():
        max_valuee = max(arguments.values())
        min_valuee = min(arguments.values())
        if values != max_valuee:
            print("This is not the middle value")
            if values != min_valuee:
                print("The middle number is: ", values)


numberfunc(4, 16, 1)

# 15: Integers are immutable but effectively what is happening here is that the old a still technically exists in
#     memory you have just lost the binding to it. You can test this by using id()
a = 11
print(id(a))
a = a + 1
print(id(a))

# 14:

nums = [2, 4, 6]


def fourteenfunction(list):
    fourteen_dict = {}
    for i in list:
        fourteen_dict[i] = i*i*i
        print(fourteen_dict)


fourteenfunction(nums)

# 16: The problem here is the scope, it is not possible for func2 to print funclvar as it is defined inside of another
#     function and it is not global so in order to fix this all you have to do is what I did below.
def func1():
    global func1var
    func1var = 2

def func2():
    print(func1var)

func1()
func2()
