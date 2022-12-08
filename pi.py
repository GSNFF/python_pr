import turtle


gsn = turtle.Turtle()
# gsn.color('red' , 'blue')



# gsn.begin_fill()
# gsn.forward(100)
# gsn.left(90)
# gsn.forward(100)
# gsn.left(90)
# gsn.forward(100)
# gsn.left(90)
# gsn.forward(100)
# gsn.end_fill()

# gsn.penup() # if pen up and down will be use the gsn.format(100) will be invis.. and splits up 
# gsn.forward(100)
# gsn.pendown()


# gsn.begin_fill()
# gsn.forward(100)
# gsn.left(90)
# gsn.forward(100)
# gsn.left(90)
# gsn.forward(100)
# gsn.left(90)
# gsn.forward(100)
# gsn.end_fill()
gsn.color('red' , 'yellow')
gsn.begin_fill()
gsn.speed(20)
for i in range(100):
    gsn.forward(300)
    gsn.left(168.5)
gsn.end_fill()

turtle.done()