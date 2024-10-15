from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.x_val=10
        self.y_val=10
        self.ball_speed=0.1
    def create_ball(self):
            self.shape("circle")
            self.color("white")
            self.penup()
            self.goto(0,0)
    
    def move(self):
        new_x=self.xcor()+ self.x_val
        new_y=self.ycor()+ self.y_val
        self.forward(10)  
        self.goto(new_x,new_y)
        
    def change_direction(self):
        self.goto(0,0)      
        self.bounce_x()
       
    # def speedup_ball(self):
    #         self.ball_speed*=0.9
    #         time.speed(self.ball_speed)
           
            
    def bounce_y(self):
        self.y_val*=-1
            
    def bounce_x(self):
        self.x_val*=-1      
        self.ball_speed*=0.9
        time.sleep(self.ball_speed) 
        print(self.ball_speed)     
            