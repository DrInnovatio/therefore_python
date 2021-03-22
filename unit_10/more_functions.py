# from typing import final


# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()

#     return (f"{formated_f_name} {formated_l_name}")


# p = format_name("park", "FOO")
# line = len(p)
# print(line)
# print(p)


# def new_members(f_name, l_name):
#     if f_name == "" or l_name == "":
#         return
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"The new customers name is {formated_f_name} {formated_l_name}"


# print(new_members(input("What is the first name : "),
#                   (input("What is the last name : "))))


diet = {"apple": 0, "banana": 0, "pizza": 1, "coke": 1}

for key in diet:
    grade = diet[key]
    if grade == 0:
        print(f"You can eat {key}")
    elif grade == 1:
        print(f"You should not eat {key}")

# dishes = ["pizza", "sauerkraut", "paella", "Hamburger"]
# countries = ["Italy", "Germany", "Spain", "USA"]
# number = [1, 2, 3, 4]
# money = ["$120", "210", "100", "410"]
# country_specialities = zip(countries, dishes, number, money)
# print(tuple(country_specialities))
