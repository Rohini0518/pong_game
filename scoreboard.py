from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()    
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score=0
        self.r_score=0
        self.update_score()
        
        
    def update_score(self):
        self.clear()
        self.goto(-100,340)
        self.write(f"Score :{self.l_score}", False, align="center", font=('Arial', 15, 'normal'))
        self.goto(100,340)
        self.write(f"Score :{self.r_score}", False, align="center", font=('Arial', 15, 'normal'))
        
    def left_score(self):
        self.l_score+=1
        self.update_score()
    def right_score(self):
        self.r_score+=1
        self.update_score()