from turtle import Turtle
import turtle
turtle.colormode(255)
import time
import random

class Snake:
    def __init__(self):
        self.snake = []
        self.sleep_parameter = 0.08
        self.initial_setup()
    def initial_setup(self):
        for i in range(3):
            self.create_snake_part()

    def create_snake_part(self):
        color = (random.randint(100,255),random.randint(100,255),random.randint(100,255))
        snake_part = Turtle()
        snake_part.up()
        snake_part.shape("square")
        snake_part.color(color)
        self.snake.append(snake_part)
        if len(self.snake) > 1:
            self.snake[-1].goto(self.snake[-2].pos())
            self.snake[-1].setheading(self.snake[-2].heading())
            self.snake[-1].backward(22)
        print(self.snake)
    def move_snake(self):
        idx = len(self.snake) - 1
        while idx > 0:
            self.snake[idx].forward(22)
            self.snake[idx].setheading(self.snake[idx - 1].heading())
            idx -= 1
        self.snake[0].forward(22)
        time.sleep(self.sleep_parameter)

    def turn_left(self):
        self.snake[0].setheading((self.snake[0].heading() + 90) % 360)

    def turn_right(self):
        self.snake[0].setheading((self.snake[0].heading() - 90) % 360)
