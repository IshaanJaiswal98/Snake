from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()


snake = Snake()
food = Food()
scoreboard = Score()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

is_game_on = True
score = 0
while is_game_on:
    screen.update()
    snake.move()

    time.sleep(0.0999)

    #snake collision with food
    if (snake.head.distance(food)<15):
        food.refresh()
        snake.create_new_body()
        scoreboard.increase_score()

    #snake collision with boundary wall
    if snake.head.xcor()>300 or snake.head.xcor()<-300 or snake.head.ycor()>270 or snake.head.ycor()<-290:
        is_game_on = False
        scoreboard.game_over()

    #snake collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) <10:
            is_game_on = False
            scoreboard.game_over()



screen.exitonclick()