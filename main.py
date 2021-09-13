from turtle import Screen, Turtle # module and class import
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width = 600, height= 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Scoreboard()
score.read_score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True

# rad_varb = 0
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        print("nom nom nom")
        score.increase_score()
        # score.reset()
        score.update_score()
        food.refresh()
        snake.extend()

    # Detect collisions with wall.
    if snake.head.xcor()>280 or snake.head.ycor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280:
        #print("You hit wall")
        #score.game_over()
        #game_is_on = False
        score.scoreboard_reset()
        snake.clear_snake()

    # Detect collision with self
    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            score.scoreboard_reset()
            snake.clear_snake()
            # print("Body collision yoself")
            # score.game_over()
            # game_is_on = False


screen.exitonclick()










