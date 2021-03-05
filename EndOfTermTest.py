#1 b)

#2 a)

#3 True

#4 False

#5  True

#6 Dunder methods are internally called when you perform a certaion action, like when you do 10 + 10 the __add__()
#  method will be called meanwhile regular methods have to be phyiscally called. 

#7 You create an instance of an object by first giving the instance a name then writing the name of the class and then writing brackets
# and within those brackets writing the values for the variables defined in the __init__ method. 
# Example: John = Person("17", "Likes Dogs")

#8 \n

#9 No you should not use print with __str__

#10 Inheriting a class allows you to have all the features of the parent class including its methods of course while
#   having the ability to add methods of your own in the new child class. Basically just building on another class with a new class.

#11
class Dog:
    def __init__(self, favourite_food):
        self.favourite_food = favourite_food

class Boy:
    def __init__(self, pet):
        self.pet = pet

spot = Dog('steak')
fred = Boy(spot)

print()

# 12
class Ball:
    def __init__(self, colour, size, material):
        self.colour = colour
        self.size = size
        self.material = material
    
    def deflate(self):
        self.size -= 1
        print(str(self.size))

soccerball = Ball("white", 8, "leather")
soccerball.deflate()

# 13 ends up at 1
class FunnyNumbers:
    def __init__(self, starting_number):
        self.number = starting_number
    
    def halve(self):
        self.number //= 2

    def triple_and_one(self):
        self.number = 3*self.number + 1

    def next_step(self):
        if self.number % 2 == 0:
            self.halve()
            print(str(self.number))
        else:
            print(str(self.number))
            self.triple_and_one()

Yolo = FunnyNumbers(13)
for i in range(10):
    Yolo.next_step()

# 14
class Square:
    def __init__(self, side_length):
        self.sl = side_length
        self.area = 0

    def grow_bigger(self):
        self.sl += 1
        print(str(self.sl))

    def calculate_area(self):
        self.area = self.sl * self.sl
        return f"{self.area}"

Bob = Square(5)
Bob.grow_bigger()
print(Bob.calculate_area())

# 15
class Athlete:
    def __init__(self, name, weight, original_height):
            self.name = name
            self.weight = weight
            self.original_height = original_height
    
    def __str__(self):
        return f'name is {self.name}, weight is {self.weight}, original height is {self.original_height}'
    
    def eat_lots(self):
        print(str(self.weight + 10))

    def stretch(self):
        self.original_height += 3
        print(self.original_height)

dude = Athlete("Bill", 100, 180)
print(dude.__str__())
dude.eat_lots()
dude.stretch()


# 16
class Wizard:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.spellbooks = 1

    def __repr__(self):
        if self.health > 0:
            return f'{self.name} is alive'
        if self.health <= 0:
            return f'{self.name} is dead'

    def get_hit_with_books(self):
        self.health -= self.spellbooks
        print(str(self.health))

    def learn_things(self):
        self.spellbooks += 2

Mary = Wizard("Mary", 100)
Mary.learn_things()
Mary.get_hit_with_books()
print(Mary.__repr__())

# 17
test_string = 'Fast 5'
if test_string.startswith("F") and test_string.isalpha():
    print("True")
else:
    print("False")

# 18
start_list = ['one', 'two', 'three', 'four']
start_string = ' potato '

end_string = 'four potato three potato twoandahalf potato two potato one potato none' 

start_list.append(start_string)
start_list.reverse()
