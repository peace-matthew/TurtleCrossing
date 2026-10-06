import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("pink")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_up, key="Up")
screen.onkey(fun=player.move_left, key="Left")
screen.onkey(fun=player.move_right, key="Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_cars()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > FINISH_LINE_Y:
        player.level_up()
        car_manager.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()