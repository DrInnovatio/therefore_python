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


student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.

# TODO-2: Write your code below to add the grades to student_grades.👇

student_grades = {}

for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


# 🚨 Don't change the code below 👇
print(student_grades)

# Nesting dictionary in a dictionary

travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Australia": ["Sydney", "Perth", "Brisbane"],
    "Korea": {"cities_lived": ["Seoul", "Incheon", "Busan"]}
}
# Nesting dictionary in a list

travel_log_2 = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12},
    {"country": "Australia",
     "cities_visited": ["Sydney", "Perth", "Brisbane"],
     "total_visits": 5}
]

print(travel_log_2)