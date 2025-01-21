from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial',16,'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.speed("fastest")
        self.goto(0,270)
        self.score = -1
        self.score_updater()
    def score_updater(self):
        self.score += 1
        self.clear()
        self.write(arg="Score: " + str(self.score),align=ALIGNMENT,font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over!",align=ALIGNMENT,font=FONT)
