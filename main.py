from scoreboard import ScoreBoard
from screen import GameScreen
from snake import Snake
from food import Food
from wall import Wall


screen = GameScreen()
snake = Snake()
food = Food()
scoreboard = ScoreBoard()
wall = Wall()

screen.event_listener(snake.turn_left,snake.turn_right)

start = True
game_over = False

while not game_over:
    snake.move_snake()
    #detect collision with foods
    if snake.snake[0].distance(food) < 20:
        scoreboard.score_updater()
        snake.create_snake_part()
        food.spawner(snake.snake)
        if 0.03 < snake.sleep_parameter:
            snake.sleep_parameter -= snake.sleep_parameter*scoreboard.score/100
            print(snake.sleep_parameter)

    #detect collision with walls
    if snake.snake[0].xcor() > 240 or snake.snake[0].xcor() < -240 or snake.snake[0].ycor() > 240 or snake.snake[0].ycor() < -240:
        game_over = True
        scoreboard.game_over()
    #detect collision with tail
    for i in snake.snake[1:]:
           if snake.snake[0].distance(i) < 10:
                game_over = True
                scoreboard.game_over()
                break
    screen.screen_updater()

screen.exit_event()

