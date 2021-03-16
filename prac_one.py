# programming_dictionary = {"bug": "advertising that workers who make a product or provide a service are unionized",
#                           "function": "activity that is natural to or the purpose of a person or thing.",
#                           "AI": "artificial intelligence.", 123: "what's up?",
#                           "loop": "Loop is based in Melbourne, Australia. Founded in 2016, Loop was created when our "
#                                   "founders"}
#
# empty_dictionary = {}
#
#
# programming_dictionary["bug"] = ""
#
#
# print(programming_dictionary)
#
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# student_scores = {
#     "Harry": 81,
#     "Ron": 78,
#     "Hermione": 99,
#     "Draco": 74,
#     "Neville": 62,
# }
# # 🚨 Don't change the code above 👆
#
# # TODO-1: Create an empty dictionary called student_grades.
#
# # TODO-2: Write your code below to add the grades to student_grades.👇
#
# student_grades = {}
#
# for student in student_scores:
#     score = student_scores[student]
#     if score > 90:
#         student_grades[student] = "Outstanding"
#     elif score > 80:
#         student_grades[student] = "Exceeds expectation"
#     elif score > 70:
#         student_grades[student] = "Acceptable"
#     else:
#         student_grades[student] = "Fail"
#
#
# # 🚨 Don't change the code below 👇
# print(student_grades)
#
# # Nesting dictionary in a dictionary
#
# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Australia": ["Sydney", "Perth", "Brisbane"],
#     "Korea": {"cities_lived": ["Seoul", "Incheon", "Busan"]}
# }
# # Nesting dictionary in a list
#
# travel_log_2 = [
#     {"country": "France",
#      "cities_visited": ["Paris", "Lille", "Dijon"],
#      "total_visits": 12},
#     {"country": "Australia",
#      "cities_visited": ["Sydney", "Perth", "Brisbane"],
#      "total_visits": 5}
# ]
#
# print(travel_log_2)


travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}

    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


# 🚨 Do not change the code below

add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Japan", 11, ["Tokyo", "Osaka", "Kyoto"])
print(travel_log)

fruits = [{"name_of_the_fruits": "banana", "number_of_the_fruits": 45, "nutrition": ["vitamin a", "vitamin c"]}]

print(fruits)


def add_new_fruits(name, number, nutrition):
    new_fruits = {}
    new_fruits["name_of_the_fruits"] = name
    new_fruits["number_of_the_fruits"] = number
    new_fruits["nutrition"] = nutrition
    fruits.append(new_fruits)


add_new_fruits("orange", 91, ["fat", "fuel", "carb"])

print(fruits)
