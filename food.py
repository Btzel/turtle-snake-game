from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.shapesize(stretch_wid=.5, stretch_len=.5)
        self.spawner([])

    def spawner(self,snake):
        is_spawn = False
        while not is_spawn:
            is_initial_collision = False
            random_x = random.randint(-240,240)
            random_y = random.randint(-240,240)
            self.goto(random_x, random_y)
            if len(snake) > 0:
                for i in snake:
                    if i.distance(self) < 30:
                        is_initial_collision = True
                if not is_initial_collision:
                    is_spawn = True
            else:
                is_spawn = True





