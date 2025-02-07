import random
import math
from itertools import permutations

# 1
def grams_to_ounces(grams):
    return 28.3495231 * grams

# 2
def F_to_C(F):
    return (5 / 9) * (F - 32)

# 3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return None

# 4
def filter_prime(numbers):
    is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))
    return list(filter(is_prime, numbers))

# 5
def string_permutations(s):
    return list(permutations(s))

# 6
def reverse_words(sentence):
    return " ".join(sentence.split()[::-1])

# 7
def has_33(nums):
    return any(nums[i] == nums[i+1] == 3 for i in range(len(nums) - 1))

# 8
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
            
        if not code:
            return True
    return False

# 9
def sphere_volume(r):
    return (4/3) * math.pi * r**3

# 10
def unique_elements(list_):
    unique_list = []
    for elements in list_:
        if elements not in unique_list:
            unique_list.append(elements)
    return unique_list

# 11
def is_palindrome(word):
    return word == word[::-1]

# 12
def histogram(lst):
    for num in lst:
        print("*" * num)
    
# 13
def guess_the_number():
    name = input("Hello! What is your name?\n")
    number = random.randint(1, 20)

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0

    while True:
        guess = int(input("Take a guess.\n"))
        guesses += 1

        if guess < number:
            print("Your guess is too low.")

        elif guess > number:
            print("Your guess is too high.")

        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break
