import turtle
screen = turtle.Screen()
screen.setup(450,450)
screen.title('Winner')
screen.bgcolor('Blue')
t1 = turtle.Turtle()
t1.ht()
t1.up()
t1.goto(-250,0)
t1.write('Congratulation You WON!!', font=("Arial", 20, "normal"))

turtle.mainloop()