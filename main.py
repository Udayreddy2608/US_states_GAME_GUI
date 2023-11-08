import turtle
from turtle import Turtle,Screen
import pandas


screen = Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states=pandas.read_csv("50_states.csv")
all_states=states["state"].to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer = screen.textinput(title=f"You answered {len(guessed_states)}/50", prompt="What's another state name??").title()
    if answer=="Exit":
        missed = [i for i in all_states if i not in guessed_states]
        new_data = pandas.DataFrame(missed)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        t=Turtle()
        t.hideturtle()
        t.penup()
        state_data=states[states.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(arg={answer},font=("courier",14,"normal"))



screen.exitonclick()


























