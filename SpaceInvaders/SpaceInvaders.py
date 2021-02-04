import turtle
import os

#Screen Setup
ms = turtle.Screen() # screen
ms.bgcolor("black")
ms.title("Space Invaders")

#Border Creation
border = turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range (4): 
    border.forward(600)
    border.left(90)
border.hideturtle()
##### END BORDER CREATION #####


#Player Creation
player = turtle.Turtle() 
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)
##### END PLAYER CREATION #####

#Player Movements
playerspeed = 15

def move_left():
    if player.xcor() <= -285: #check if hit bounds of border
        player.setx(-285)
    else: 
        x = player.xcor()
        x -= playerspeed
        player.setx(x)
        print(player.xcor())
 
def move_right(): 
    if player.xcor() >= 285: #check if hit bounds of border
        player.setx(285)
    else: 
        x = player.xcor()
        x += playerspeed
        player.setx(x)
        print(player.xcor())


ms.listen() 

ms.onkey(move_left, "Left")
ms.onkey(move_right, "Right")

#### END PLAYER MOVEMENTS ####


ms.mainloop()
