from turtle import Turtle

with open("text.txt") as file:
    initial_highscore = file.read()


class KeepScore(Turtle):
    def __init__(self):
        super().__init__()
        self.game_score = 0
        self.high_score = int(initial_highscore)
        self.color("white")
        self.penup()
        self.setposition(x=0, y=260)

        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(arg=f"SCORE: {self.game_score}   HIGH_SCORE: {self.high_score}", align="center",
                   font=('Courier', 17, 'bold'))

    def reset(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score
        self.game_score = 0
        with open("text.txt", mode="w") as data:
            data.write(str(self.high_score))

        self.update_score()

    def increase_score(self):
        self.game_score += 1
        self.update_score()
