import turtle
import pandas

# Create the screen object with title
screen = turtle.Screen()
screen.title("I.R.R Province Game")

# Adding the image to set it as background
image = "./IRI_Blank.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=1024, height=914)

# Create a writer object from Turtle class
writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

# Using pandas to read the csv data file
data = pandas.read_csv("./IRAN.csv")
all_province = data.province.tolist()

# Game loop
guessed = []
while len(guessed) < 31:

    # Game's text box for getting user inputs
    answer = screen.textinput(title=f"{len(guessed)}/31 Province Correct",
                                    prompt="What's another province name?").title()

    # Write the name of the province if user guessed correctly
    if answer in all_province:
        guessed.append(answer)
        position = data[data.province == answer]
        writer.goto(int(position.x), int(position.y))
        writer.write(arg=position.province.item(), align="center")

# Using the mainloop function to avoid exiting the screen
turtle.mainloop()
