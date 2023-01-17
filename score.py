from turtle import Turtle

FONT = ('Contour', 15, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.write_score()
        self.highscore = 0

    def write_score(self):
        self.goto(0, 270)
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.write(f"Score = {self.score} Highscore= {self.highscore} ", align='center', font=FONT)

    def game_over(self):
        if(self.score>self.highscore):
            with open("highscore.txt", mode="w") as file:
                file.write(f"{self.score}")
        self.clear()
        self.write_score()
        self.goto(0, 0)
        self.write(f"Game Over.",align='center',font = FONT)



    def increase_score(self):
        self.clear()
        self.score+=1
        self.write_score()

