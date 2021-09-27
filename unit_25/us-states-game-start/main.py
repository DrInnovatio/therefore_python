import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# don't need this any more.
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

# If answer_state is one of the states in all the states of the 50_states.csv
    # If they got it right:
    # create a turtle to write the name of the state at the state's x and y coordate.

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.goto(state_data.x, state_data.y)
    t.write(state_data.state)

screen.exitonclick()