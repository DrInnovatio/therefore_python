person = {}
keep_going = False

while not keep_going:

    name = input("Name? : ")
    age = int(input("age ? : "))
    should_continue = input("Keep going? yes or no : ")

    person[name] = age

    if should_continue == 'yes':
        keep_going = False
    elif should_continue == 'no':
        keep_going = True

print(person)
