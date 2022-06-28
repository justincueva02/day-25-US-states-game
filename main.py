import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S.A. States Game')
img = 'blank_states_img.gif'
screen.addshape(img)
turtle.shape(img)

data = pandas.read_csv('50_states.csv')
all_states = data.state.values
guessed_states = []

game_is_on = True
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50', prompt="What's another state name?").lower().capitalize()
    answered_correct = answer_state in all_states
    if answered_correct:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        print('CORRECT🎉')
        state_row = data.loc[data['state'] == answer_state]
        x_coor = state_row.x.values[0]
        y_coor = state_row.y.values[0]
        t.goto(x_coor, y_coor)
        t.write(answer_state)
        print(x_coor, y_coor)
    else:
        print('💥 WONG 💥')

turtle.mainloop()
