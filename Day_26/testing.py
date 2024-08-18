# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# short_names = [name for name in names if len(name) <= 4]
# upper_names = [name.upper() for name in names if len(name) >= 5]
# print(upper_names)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 24, 55]

# squared_numbers = [n**2 for n in numbers]


# print(squared_numbers)

list_of_strings = input().split(",")

numbers = [len(x) for x in list_of_strings]

even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
