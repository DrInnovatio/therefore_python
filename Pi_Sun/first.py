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