from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.ht()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"SCORE:  {self.score}", align="center", font=('courier', 14, 'bold'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("ariel", 28, "bold"))
