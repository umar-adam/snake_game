import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.snake_head.distance(food) < 15:
        food.refresh_food()
        scoreboard.increase_score()
        snake.extend()

    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280
            or snake.snake_head.ycor() < -280):
        scoreboard.game_reset()
        snake.restart_game()

    for segments in snake.segments[1:]:
        if snake.snake_head.distance(segments) < 10:
            scoreboard.game_reset()
            snake.restart_game()

screen.exitonclick()
