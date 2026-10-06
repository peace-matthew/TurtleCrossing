from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-200, 260)
        self.update_level()

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_level()

    def update_level(self):
        self.write(arg=f"Level = {self.level}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

