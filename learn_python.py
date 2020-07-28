# https://www.youtube.com/watch?v=rfscVS0vtbw #

# SETUP AND HELLO WORLD #

print("Hello, world!")

a = 1
b = 3
c = 8
d = a + b + c
print(d)

# DRAWING A SHAPE #

print("   /|")
print("  /_|")
print(" /__|")
print("/___|")

# VARIABLES AND DATA TYPES #

print("There was a man named John, ")
print("he was 35 years old. ")
print("He really liked the name John, ")
print("but didn't like being 35.")

character_name = "John"
character_age = "35"

print("There was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("He really liked the name " + character_name + ", ")
print("but didn't like being " + character_age + ".")

character_name = "Tom"  # string
character_age = 50  # integer
character_age = 50.12313123  # numeric, float
is_male = True  # boolean (can be False)

# WORKING WITH STRINGS #

print("Giraffe Academy")
print("Giraffe\Academy")
print("Giraffe\nAcademy")
print("Giraffe\"Academy")

phrase = "Giraffe Academy"
print(phrase)
print(phrase + " is cool.")
print(phrase.lower())
print(phrase.upper())
print(phrase.isupper())
print(phrase.upper().isupper())
print(len(phrase))

print(phrase[0])
# python index starts from 0
phrase = "Giraffe Academy"
#         0123456789
print(phrase[2])
print(phrase.index("G"))
print(phrase.index("Acad"))
print(phrase.index("a"))
# print(phrase.index("z")) will create error
print(phrase.replace("Giraffe", "Elephant"))

# WORKING WITH NUMBERS #

print(2)
print(3 * 4.5)
print(4 * 5 + 6)
print(4 * (5 + 6))
print(10 % 3)  # modulo function use % sign
my_num = 5
print(my_num)
print(str(my_num))
print(str(my_num) + " my favorite number.")
# print(my_num + " my favorite number.") will create error
my_num2 = -5
print(abs(my_num2))
print(pow(my_num2, 2))  # equal to square of my_num2
print(max(1, 2, 3, 4, 5))
print(min(1, 2, 3, 4, 5))
print(round(1.1231231321))

from math import *
print(floor(1.2312312312))
print(ceil(1.21312312312))
print(sqrt(36))

# GETTING INPUT FROM USERS #

enter_name = input("Enter your name: ")
print("Hello " + enter_name + "!")

enter_age = input("Enter your age: ")
print("Hello " + enter_name + "! You are " + enter_age + "!")

# BUILDING A BASIC CALCULATOR #

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
result = float(num1) + float(num2)
print(result)

# MAD LIBS GAME #

print("Roses are red")
print("Violets are blue")
print("I love you")

enter_color = input("Enter a color: ")
enter_plural_noun = input("Enter a plural noun: ")
enter_celebrity = input("Enter a celebrity: ")

print("Roses are " + enter_color)
print(enter_plural_noun + " are blue")
print("I love " + enter_celebrity)

# LISTS #

datatype_list = ["Kevin", 2, True]
friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends_list[0])
print(friends_list[-1])
print(friends_list[1:])
print(friends_list[1:3])
friends_list[1] = "Mike"
print(friends_list)
print(friends_list[1])

# LIST FUNCTIONS #

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends_list.extend(lucky_numbers)
print(friends_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list.append("Creed")
print(friends_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list.insert(1, "Kelly")
print(friends_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list.remove("Jim")
print(friends_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list.clear()
print(friends_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list.pop()
print(friends_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Jim", "Toby"]
print(friends_list.index("Kevin"))
# print(friends_list.index("Kautzar")) will error because no "Kautzar" in friends_list
print(friends_list.count("Jim"))

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list.sort()
print(friends_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list.reverse()
print(friends_list)

friends_list = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends_list2 = friends_list.copy()
print(friends_list2)

# TUPLES #

coordinates = (4, 5)
print(coordinates[0])
# coordinates[1] = 10 will result error because tuple immutable
coordinates2 = [(4, 5), (6, 7), (8, 9), (10, 11)]
print(coordinates2)

# FUNCTIONS #

def say_hi():
    print("Hello, User!")
say_hi()

print("Top")
say_hi()
print("Bottom")

def say_hi2(name, age):
    print("Hello, " + name + "! You are " + age)
say_hi2("Kautzar", "28")

def say_hi3(name, age):
    print("Hello, " + name + "! You are " + str(age))
say_hi3("Kautzar", 28)

# RETURN STATEMENT #

def cube(num):
    num * num * num
cube(3)
print(cube(3))

def cube2(num):
    return num * num * num
cube2(3)
print(cube2(3))
result = cube2(4)
print(result)
# use return means break the function code, can't add more code below the return keyword

# IF STATEMENTS #

is_male = True
if is_male:
    print("You are a male")

is_male = False
if is_male:
    print("You are a male")

is_male = False
if is_male:
    print("You are a male")
else:
    print("You are not a male")

is_male = True
is_tall = False
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither male nor tall")
if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")

is_male = True
is_tall = True
if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a male, but not tall")
elif not(is_male) and is_tall:
    print("You are either not male or not tall or both")

# IF STATEMENTS AND COMPARISONS #

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3,4,5))
# comparison signs: > < != == and others

# BUILDING A BETTER CALCULATOR #

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")"

# DICTIONARIES # key: value

monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

print(monthConversions["Nov"])
print(monthConversions.get("Dec"))
print(monthConversions.get("Luv"))
print(monthConversions.get("Luv", "Not a valid key"))

monthConversions2 = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    4: "May",
    5: "June",
    6: "July",
    7: "August",
    8: "September",
    9: "October",
    10: "November",
    11: "December"
}

print(monthConversions2.get(1))

# WHILE LOOP #

i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop")

# BUILDING A GUESSING GAME #

secret_word = "giraffe"
guess_word = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess_word != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess_word = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you lose!")
else:
    print("You win!")