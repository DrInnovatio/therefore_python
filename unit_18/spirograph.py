import turtle as t
import random

tim = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


tim.speed("fastest")
tim.shape("turtle")
tim.color(random_color())
tim.circle(100)
current_heading = tim.heading()
tim.setheading(current_heading + 10)
tim.circle(100)

screen = t.Screen()
screen.exitonclick()

# t.done()
