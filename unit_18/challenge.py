import turtle as t

tim = t.Turtle()

num_sides = 5
angle = 360 / num_sides

for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)

t.done()
