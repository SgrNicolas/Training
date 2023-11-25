from random import *

################# Logical Operators Practice #################

num1 = 36
num2 = 72/2
num3 = 48
my_bool = num1 > num2 and num1 < num3

#################

num1 = 36
num2 = 72/2
num3 = 48
my_bool = num1 > num2 or num1 < num3

#################

text = "When something is important enough, you do it even if the odds are against you"

word1 = "success"
word2 = "technology"

my_bool = (not word1 in text) and (not word2 in text)

################# Decision Making Practice #################

# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
elif num1 == num2:
    print(f"{num1} and {num2} are equal")

#################

age = 16
has_license = False
if age > 18 and has_license:
    print("You can drive")
elif age < 18 and has_license == False:
    print("You can't drive yet. You must be 18 years old and have a license")
elif age > 18 and has_license == False:
    print("You can't drive. You need to have a license")

#################

speak_french = True
knows_python = False
if speak_french and knows_python:
    print("You meet the requirements to apply")
elif speak_french == False and knows_python == False:
    print("To apply, you need to know how to program in Python and speak French")
elif speak_french == False:
    print("To apply, you need to speak French")
elif knows_python == False:
    print("To apply, you need to know how to program in Python")

################# For Loops Practice #################

students = ["Norville", "Fred", "Velma", "Daphne"]
for student in students:
    print(f"Hello {student}")

#################

list_numbers = [1, 5, 8, 7, 6, 8, 2, 5, 2,
                6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

sum_numbers = 0
for number in list_numbers:
    sum_numbers = sum_numbers + number

print(sum_numbers)

#################

list_numbers = [1, 5, 8, 7, 6, 8, 2, 5, 2,
                6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

sum_even = 0

sum_odd = 0

for number in list_numbers:
    if number % 2 == 0:
        sum_even = sum_even + number
    if number % 2 == 1:
        sum_odd = sum_odd + number

print(sum_even, sum_odd)

################# While Loops Practice #################

number = 10

while number >= 0:
    print(number)
    number -= 1

#################

number = 50

while number >= 0:
    print(number)
    number -= 5
    if number % 5 == True:
        print(number)
    else:
        continue

#################

list_numbers = [4, 5, 8, 7, 6, 9, 8, 2, 4,
                5, 7, 1, 9, 5, 6, -1, -5, 6, -6, -4, -3]

for number in list_numbers:
    if number > 0:
        print(number)
    else:
        break

################# Range Practice #################

# a list consisting of all numbers that are multiples of 3 from 3 to 300 (inclusive)
my_list = list(range(3, 301, 3))

#################

sum_squares = 0

for i in range(1, 16):
    # add the squares of all the numbers from 1 to 15 (inclusive).
    sum_squares += i**2

################# Enumerator Practice #################

list_names = ["Steven", "Jackie", "Donna",
              "Kelso", "Eric", "Fez", "Kitty", "Red"]

for index, name in enumerate(list_names):
    print(f'{name} is found at index {index}')

#################

indices_list = list(enumerate("Python"))
print(indices_list)

#################

list_names = ["Maverick", "Alice", "Madeline", "Hazel",
              "Jack", "Meadow", "Thomas", "Emily", "Mills"]

for index, name in enumerate(list_names):
    if name[0] == "M":  # controlls if the first letter equals "M"
        print(f"{index}")

################# Zip Practice #################

capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

combination = list(zip(capitals, countries))

for capital, country in combination:
    print(f"The capital of {country} is {capital}")

#################

spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]
english = ["one", "two", "three", "four", "five"]

numbers = list(zip(spanish, portuguese, english))

print(numbers)

################# Min & Max Practice #################

number_list = [44542247/2, 21310/5, 2134747*33, 44556475,
               121676, 6654067, 353254, 123134, 55**12, 611**5]

maximum_value = (max(number_list))  # Gets the biggest number

#################

number_list = [44542247, 21310, 2134747, 44556475,
               121676, 6654067, 353254, 123134, 552512, 611665]

number_range = (max(number_list))-(min(number_list))
print(number_range)  # gets the difference between max and min numbers

#################

dictionary_ages = {"Tony": 55, "Paulie": 42, "Meadow": 78, "Vito": 44,
                   "Ralph": 24, "Sarah": 35, "Evan": 19, "Jean": 2, "Ned": 49}

minimum_age = (min(dictionary_ages.values()))
last_name = (max(dictionary_ages.keys()))

################# Random methods Practice #################

random_number = randint(1, 10)

#################

random_number = random()
print(random_number)

#################

names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
raffle = choice(names)

print(raffle)

################# List Comprehension Practice #################

values = [1, 2, 3, 4, 5, 6, 9.5]

square_values = [n**2 for n in values]
print(square_values)

#################

values = [1, 2, 3, 4, 5, 6, 9.5]

even_values = [n for n in values if n % 2 == 0]

print(even_values)

#################

temperature_fahrenheit = [32, 212, 275]

degrees_celsius = [(temp-32)*(5/9) for temp in temperature_fahrenheit]

print(degrees_celsius)

################# Methods, Help & Documentation Practice #################

string = ",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#"

print(",:_#,,,,,,:::____##Total_ _Pyt%on,,,,,,::#".lstrip(f"#:_,"))

#################
# Add the element "orange" as the fourth element

fruits = ["mango", "banana", "cherry", "plum", "grapefruit"]

fruits.insert(3, "orange")

print(fruits)

#################

phone_brands = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
tv_brands = {"Sony", "Philips", "Samsung", "LG"}

isolated_sets = tv_brands.isdisjoint(phone_brands)
print(isolated_sets)

################# FUNCTIONS PRACTICE #################
# Declare a function called greet, which every time it is called prints "Hello world!"


def greet():
    print("Hello world!")

#################
# Declare a function called welcome, which takes a person's name as an argument, and every time it is called, it prints "Welcome {name}!"


def welcome(name):
    print(f"Welcome {name}!")


name = "Luke"

#################
# Declare a function called square, that takes any number as an argument, and each time it is called, it prints the square of that number on the screen (that is, the value to the second power).


def square(n):
    print(n*n)


number = 12

################# Return Statement Practice #################
# Create a function called power that takes two numeric values as arguments. It must return the number that results from solving a power, using the first number as the base, and the second as the exponent


def power(n1, n2):
    total = n1**n2
    return total

#################
# Create a function called usd_to_eur that takes a numeric value (an amount in US dollars) as its only parameter, and returns the equivalent amount in euros as a result


def usd_to_eur(n):
    return n * 0.90


dollars = usd_to_eur(20)

print(dollars)

#################
# Create a function called reverse_word that takes the characters of a given word as an argument, reverses the order of their characters, and returns them that way and in uppercase.


def reverse_word(a_string):
    return a_string[::-1].upper()


word = "Course"

print(reverse_word(word))


################# Dynamic Functions Practice #################
# Create a function (all_positives) that returns True if all the values in a list are positive, and False if at least one of the values is negative. Create a list named numbers with positive and negative values.

def all_positives(list1):
    for i in list1:
        if i < 0:
            return False
    return True


numbers = [12, 65, 35, 23, -12]

#################
# Create a function (sum_less) that adds the numbers of a list as long as they are greater than 0 and less than 1000, and returns the result of said sum. Create a numbers variable, storing a list of numbers so we can test it.


def sum_less(numbers):
    sum = 0
    for number in numbers:
        if number > 0 and number < 1000:
            sum += number
    return sum


numbers = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100]

#################
# Create a function (count_even) that counts the number of even numbers that exist in a list (numbers), and returns the result of said count.


def count_even(numbers):
    even_numbers = 0
    for number in numbers:
        if number % 2 == 0:
            even_numbers += 1
    return even_numbers


numbers = [1, 50, 502, 755, 34]

################# Function Interactions Practice #################
# Create a function (throw_dice) that "throws" two random dice and returns its results (the function MUST RETURN TWO VALUES AS A RESULT, both of which must be between 1 and 6, randomly). Pass the result of these two dice to a function called roll_result (meaning that this second function MUST RECEIVE TWO ARGUMENTS) and return -without printing it- a certain message according to the what the sum of these values results:


def throw_dice():
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    result = dice1, dice2
    return result


def roll_result(dice1, dice2):
    sum_dice = dice1 + dice2
    if sum_dice <= 6:
        return f"The sum of your dice is {sum_dice}. Unfortunate"
    elif sum_dice > 6 and sum_dice < 10:
        return f"The sum of your dice is {sum_dice}. You have a good chance"
    elif sum_dice >= 10:
        return f"The sum of your dice is {sum_dice}. It looks like a winning roll"


#################
# Create a function called reduce_list() that takes a list (numbers) as an argument, and returns also a list, but removing duplicates (leaving only one of the numbers if there are duplicates) and removing the highest value. The order of the elements can be changed. For example, if given the list [1,2,15,7,2] it should return [1,2,7]. Create a function called average() that can receive as an argument the list returned by the previous function, and that calculates the average of its values.

numbers = [1, 2, 15, 7, 2, 8]


def reduce_list(numbers):
    numbers = list(set(numbers))
    numbers.sort()
    numbers.pop(-1)
    return numbers


def average(numbers):
    avg_value = sum(numbers)/len(numbers)
    return avg_value


#################
# You must create a list with values and call it secret_codes.Create a function called toss_coin that returns the result of a random coin toss. Such a function must be able to return the results "Heads" or "Tails", and must not receive any arguments to work. Create a second function called luck, that takes two arguments: the first must be the result of the coin toss. The second argument will be any list (the secret_codes variable that was created at the beginning). If the coin comes up "Tails", luck should print this message to the user: "List will self-destruct", and return said list as empty list = [ ]. If the coin comes up "Heads", it should print to the screen: "List was saved" and return the list intact.

secret_codes = [1, 2, 3, 4]


def toss_coin():
    result = random.choice(["Heads", "Tails"])
    return result


def luck(coin, a_list):
    if coin == "Tails":
        print("List will self-destruct")
        return []
    elif coin == "Heads":
        print("List was saved")
        return a_list


################# Indefinite Args Practice #################
# Create a function called sum_squares that takes any number of numeric arguments, and returns the sum of their values squared.

def sum_squares(*args):
    total = 0
    for arg in args:
        total += arg * arg
    return total


#################
# Create a function called absolute_sum, which takes any number of arguments, and returns the sum of their absolute values (that is, it takes the non-negative values and adds them together, in other words, considers them all - negative and positive - as positive).

def absolute_sum(*args):
    total = 0
    for arg in args:
        total += abs(arg)
    return total


#################
# Create a function called personal_numbers that receives, as its first argument, a name, and then an indefinite number of values.

def personal_numbers(name, *args):
    sum_numbers = 0
    for arg in args:
        sum_numbers += arg
    return f"{name}, the sum of your numbers is {sum_numbers}"


################# Indefinite kwargs Practice #################
# Create a function called number_attributes that counts the number of parameters that are passed, and returns that number as the result.

def number_attributes(**kwargs):
    total_args = 0
    for arg in kwargs:
        total_args += 1
    return total_args


#################
# Create a function called list_attributes that returns in the form of a list the values of the attributes given in the form of keywords. The function must expect to receive any number of arguments of this type.

def list_attributes(**kwargs):
    result_list = []
    for value in kwargs.values():
        result_list.append(value)
    return result_list


#################
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments         This function should display on the screen:           Characteristics of {name}: {argument_name}: {argument_value} {argument_name}: {argument_value} etc...

def describe_person(name, **kwargs):
    print(f"Characteristics of {name}:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


################# PRACTICAL PROBLEMS Practice #################
# EX. 1
# Create a function called return_distincts() that receives 3 integers as parameters.

# If the sum of the 3 numbers is greater than 15, it must return the highest number.

# If the sum of the 3 numbers is less than 10, it must return the lowest number.

# If the sum of the 3 numbers is a value between 10 and 15 (included), then it must return the number with the intermediate value.

def return_different_values(a, b, c):

    a_sum = a + b + c
    a_list = [a, b, c]

    if a_sum > 15:
        return max(a_list)
    elif a_sum < 10:
        return min(a_list)
    else:
        a_list.sort()
        return a_list[1]


print(return_different_values(3, 2, 7))
#################

# EX. 2
# Write a function (you can name it whatever you want) that takes any word as a parameter, and returns all of its unique letters (without repetition) in alphabetical order


def unrepited_letters(word):

    my_set = set()

    for letter in word:
        my_set.add(letter)

    my_list = list(my_set)
    my_list.sort()

    return my_list


print(unrepited_letters('pineapple'))
#################

# EX. 3
# Create a function called describe_person, which takes his name as parameters and then an indeterminate number of arguments.


def describe_person(name, **kwargs):
    print(f"Characteristics of {name}:")

    for key, value in kwargs.items():
        print(f"{key}: {value}")
#################
