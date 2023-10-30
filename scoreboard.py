from turtle import Turtle

ALIGNMENT = "Center"
FONT = ("Courier", 15, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("green")
        self.ht()
        self.penup()
        self.score = 0
        with open("data.txt") as data:              
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 275)
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as new_data:    
                new_data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()