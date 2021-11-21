# List Comprehension

numbers = [1, 2, 3, 5, 6, 7, 8]
new_list = [n + 1 for n in numbers]

print(new_list)

# name = "Angela"
# letters_list = [letter for letter in name]
# print(letters_list)

range_list = [num * 2 for num in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "James", "Jully", "Harry", "Freddie", "Dave"]
short_names = [name for name in names if len(name) < 5]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

number_a = [1,1,2,3,5,8,13,21,34,55]
squared_numbers = [num * num for num in number_a]
print(squared_numbers)
