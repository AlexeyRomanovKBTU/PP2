import functions1

# 1
grams = 100
print(f"{grams} grams is {functions1.grams_to_ounces(grams)} ounces.")

# 2
fahrenheit = 98
print(f"{fahrenheit}°F is {functions1.F_to_C(fahrenheit)}°C.")

# 3
heads, legs = 35, 94
chickens, rabbits = functions1.solve(heads, legs)
print(f"Chickens: {chickens}, Rabbits: {rabbits}")

# 4
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print("Prime numbers:", functions1.filter_prime(numbers))

# 5
word = "One"
print(functions1.string_permutations(word))

# 6
sentence = "We are ready"
print("Reversed sentence:", functions1.reverse_words(sentence))

# 7
nums = [1, 3, 3]
print(functions1.has_33(nums))

nums = [1, 3, 1, 3]
print(functions1.has_33(nums))

nums = [3, 1, 3]
print(functions1.has_33(nums))

# 8
spy_nums = [1, 2, 4, 0, 0, 7, 5]
print(functions1.spy_game(spy_nums))

spy_nums = [1, 0, 2, 4, 0, 5, 7]
print(functions1.spy_game(spy_nums))

spy_nums = [1, 7, 2, 0, 4, 5, 0]
print(functions1.spy_game(spy_nums))

# 9
radius = 5
print(f"Volume of sphere with radius {radius}:", functions1.sphere_volume(radius))

# 10
number_list = [1, 2, 3, 0, 1, 2, 4]
print("Unique elements:", functions1.unique_elements(number_list))

# 11
word = "abcacba"
print(f"Is '{word}' a palindrome?", functions1.is_palindrome(word))

# 12
print("Histogram:")
functions1.histogram([4, 9, 7])

# 13
functions1.guess_the_number()