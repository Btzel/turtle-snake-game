from turtle import Screen

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.initial_setup()

    def initial_setup(self):
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)

    def event_listener(self,turn_left,turn_right):
        self.screen.listen()
        self.screen.onkey(key="a", fun=turn_left)
        self.screen.onkey(key="d", fun=turn_right)

    def screen_updater(self):
        self.screen.update()

    def exit_event(self):
        self.screen.exitonclick()