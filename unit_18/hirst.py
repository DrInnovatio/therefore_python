import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()


color_list = [(253, 253, 249), (251, 244, 248), (247, 252, 250), (236, 246, 250), (243, 234, 76), (211, 158, 93),
              (188, 12, 69), (111, 179, 208), (25, 116, 169), (172, 172, 31), (221, 128, 166), (160, 78, 35),
              (128, 186, 146), (10, 32, 76), (235, 73, 41), (217, 67, 108), (31, 135, 83), (176, 48, 95), (234, 165, 194),
              (79, 13, 63), (12, 55, 34), (236, 228, 6), (29, 164, 207), (15, 42, 132), (58, 165, 95), (135, 213, 228),
              (9, 102, 63), (134, 36, 21), (93, 29, 12), (156, 211, 190)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(10):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)




screen = turtle_module.Screen()
screen.exitonclick()