from turtle import Screen
from snake import Snake
from food import Food
from score_board import KeepScore
import time

screen = Screen()
screen.setup(width=600, height=600)

screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)

snake = Snake()
food = Food()
score = KeepScore()

snake.create_snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

snake_is_moving = True

while snake_is_moving:
    screen.update()
    time.sleep(0.15)

    snake.move_snake()

    if snake.snake_parts[0].distance(food) < 15:
        food.refresh()
        score.increase_score()

        snake.extend()

    if snake.snake_parts[0].xcor() > 280 or snake.snake_parts[0].xcor() < -280 or snake.snake_parts[0].ycor() > 280 or \
            snake.snake_parts[0].ycor() < -280:
        score.reset()
        snake.reset_game()
        score.update_score()

        # score.game_over()

    for snake_part in snake.snake_parts:
        if snake_part == snake.snake_parts[0]:
            pass
        elif snake.snake_parts[0].distance(snake_part) < 10:
            # score.game_over()
            score.reset()
            snake.reset_game()
            score.update_score()

screen.exitonclick()
