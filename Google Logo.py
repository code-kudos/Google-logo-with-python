# Hi, I'm code kudos.
## Create Google logo using Turtle in python
### Hope you like it!!!!
#### To see more like this Subscribe to 
##### Youtube: @codekudos
###### Instagram: @codekudos
####### Twitter: @code_kudos

import turtle
import time

if __name__ == "__main__":
    gLogo=turtle.Turtle()

    gRed='#DB4437'  #Defining Color
    gYellow='#F4B400'
    gGreen='#0F9D58'
    gBlue='#4285F4'

    gLogo.screen.setup(400, 500)
    gLogo.getscreen()
    time.sleep(5)
    gLogo.pensize(5)

    gLogo.speed(0)
    gLogo.penup()
    gLogo.forward(120)
    gLogo.right(90)
    gLogo.circle(-150,50)
    gLogo.circle(-150,100)
    gLogo.circle(-150,60)
    gLogo.pendown()

    gLogo.speed(1)
    gLogo.color(gRed) #Red Curve part
    gLogo.begin_fill()
    gLogo.circle(-150,100)
    gLogo.right(90)
    gLogo.forward(50)
    gLogo.right(90)
    gLogo.circle(100,100)
    gLogo.right(90)
    gLogo.forward(50)
    gLogo.end_fill()

    gLogo.begin_fill() #Yello Curve part
    gLogo.color(gYellow)
    gLogo.right(180)
    gLogo.forward(50)
    gLogo.right(90)
    gLogo.circle(100,60)
    gLogo.right(90)
    gLogo.forward(50)
    gLogo.right(90)
    gLogo.circle(-150,60)
    gLogo.end_fill() 
    gLogo.right(90)
    gLogo.forward(50)
    gLogo.right(90)
    gLogo.circle(100,60)

    gLogo.color(gGreen) #Green Curve part
    gLogo.begin_fill()
    gLogo.circle(100,100)
    gLogo.right(90)
    gLogo.forward(50)
    gLogo.right(90)
    gLogo.circle(-150,100)
    gLogo.right(90)
    gLogo.forward(50)
    gLogo.end_fill() 
    gLogo.right(90)
    gLogo.circle(100,100)

    gLogo.color(gBlue) # blue Curve part
    gLogo.begin_fill()
    gLogo.circle(100,25)
    gLogo.left(115)
    gLogo.forward(65)
    gLogo.right(90)
    gLogo.forward(42)
    gLogo.right(90)
    gLogo.forward(124)
    gLogo.right(90)
    gLogo.circle(-150,50)
    gLogo.right(90)
    gLogo.forward(50)
    gLogo.end_fill()

    turtle.done()