# import relevant modules
import turtle
import random
import time
#setting screen
screen = turtle.Screen()
screen.bgcolor("black")

# we want 2 players!
#player 1
playerOne = turtle.Turtle()
playerOne.color("red")
#making shape of player
playerOne.shape('turtle')

#player 2
playerTwo = playerOne.clone()
playerTwo.color("magenta")

#positions!
playerOne.penup()
playerOne.goto(-300,250)

playerTwo.penup()
playerTwo.goto (-300,-250)

# finish line drawing using commands
playerOne.goto(300,250)
playerOne.right(90)
playerOne.pendown()
playerOne.forward(500)
playerOne.write("Finsh Line!",font = 20, align = "center")
#let's player one go back to original psoition
playerOne.penup()
playerOne.goto(-300,250)
playerOne.left(90)

#make sure both players have their pens down
playerOne.pendown()
playerTwo.pendown()

#let's make die values
die = [1,2,3,4,5,6]

#let's make the game!
for i in range(30):
    if playerOne.pos() >= (300, 250):
        print("Player One wins!")
        break
    elif playerTwo.pos() >= (300, -250):
        print("Player Two wins!")
        break
    else:
        dieRoll = random.choice(die)
        playerOne.forward(dieRoll*25)
        time.sleep(2)
        dieRolls = random.choice(die)
        playerTwo.forward(dieRolls * 25)
        time.sleep(2)
#put this in personal turtle game! It keeps turtle drawing on screen!
# turtle.done()






