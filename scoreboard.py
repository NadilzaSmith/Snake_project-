from turtle import Turtle

class Scoreboard (Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("high_score.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updade_score()
        self.hideturtle()


    def updade_score(self):
        self.clear()
        self.write(f"Score : {self.score} High Score {self.high_score}", align="center", font=("Comic Sans", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.updade_score()


    def increase_score(self):
        self.score += 1
        self.updade_score()





