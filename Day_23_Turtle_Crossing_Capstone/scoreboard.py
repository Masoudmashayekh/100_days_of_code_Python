from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-250, 270)
        self.write(f"Level: {self.level}", False, "center", ("Arial", 15, "bold"))

    def add_score(self):
        self.level += 1
        self.update_score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 35, "bold"))
