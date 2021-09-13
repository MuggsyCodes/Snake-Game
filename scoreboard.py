from turtle import Turtle

# Scoreboard is a turtle object that knows how to keep track of the score and how to display it
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.setposition(0, 280)
        self.score = 0
        self.highscore = self.read_score()
        self.update_score()
        # self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=("Calibri", 12, "normal"))


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align="center", font=("Calibri", 12, "normal"))


    def increase_score(self):
        self.score += 1

    def write_score(self):
        with open('data.txt', mode='w') as file:
            file.write(str(self.highscore))

    def read_score(self):
        with open('data.txt', mode = 'r') as file:
            high_score = file.read()
            # print(f'high_score: {high_score}')
        return int(high_score)

    def scoreboard_reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.write_score()
        self.score = 0
        self.update_score()

    # with open('my_file.txt') as new_file:
    #     contents = new_file.read()
    #     print(contents)

    # with open('data.txt', mode='w') as file:
    #     file.write(self.highscore)
        # contents = new_file.read()
        # print(contents)

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"Game over dood!", False, align="center", font=("Calibri", 24, "normal"))



