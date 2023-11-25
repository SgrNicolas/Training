# Write a function (you can name it whatever you want) that takes any word as a parameter, and returns all of its unique letters (without repetition) in alphabetical order.

def spell_function(word):
    letters = set()

    for char in word:
        char = char.lower()

        if char.isalpha():
            letters.add(char)

    sorted_letters = sorted(letters)
    return sorted_letters


function_1 = spell_function("Character")

print(function_1)
