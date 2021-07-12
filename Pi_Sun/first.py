def greet_user(username):
    print("Hello, " + username.title() + "!")


greet_user("Karl")


def area(height, width):
    result = height * width
    print(f"The area is {result}.")


area(12.3, 11.01)


def cleaning_plan(venue, service):
    print(f"We are going to {service} at {venue}")


cleaning_plan("home cleaning", "Mel's Place")
cleaning_plan("gardening", "Wendy's place")


def sales(price, product):
    print(f"{product} is ${price}.")


sales(1354, "TV")
sales(318, "Nintendo")


def my_pet(name, breed="Mal"):
    print(f"My dog {name} is a big {breed}")


my_pet("Sparky")


def make_shirt(size, message):
    print(f"Your size is {size} and {message} will be printed on the front of it.")


make_shirt("L", "Pythonists")


def got_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


musician = got_formatted_name("John", "Lennon")
print(musician)


def create_people(first_name, last_name):
    person = {'first': first_name, 'last': last_name}
    return person


actor = create_people("John", "Dixie")


#If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


def triangle(*side):
    total_area = (side[0] * side[1]) * 0.5
    return total_area


result_1 = triangle(12, 22)
result_2 = triangle(9, 23)

print(f"{result_1} and {result_2}")

