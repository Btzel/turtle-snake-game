from screen import GameScreen
from snake import Snake

screen = GameScreen()
snake = Snake()

screen.event_listener(snake.turn_left,snake.turn_right)

start = True
game_over = False

while not game_over:
    snake.move_snake()
    screen.screen_updater()
screen.exit_event()

