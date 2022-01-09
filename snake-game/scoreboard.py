from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 275)
        self.report_score()
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def report_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
