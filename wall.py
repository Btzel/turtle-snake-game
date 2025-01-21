from turtle import Turtle

class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("maroon")
        self.pensize(width=2)
        self.hideturtle()
        self.goto(-250,250)
        self.draw_wall()
    def draw_wall(self):
        self.pendown()
        self.goto(250,250)
        self.goto(250,-250)
        self.goto(-250,-250)
        self.goto(-250,250)
        self.penup()