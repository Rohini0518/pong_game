from turtle import Screen
from paddle import Sidepaddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()
screen.bgcolor("black")
screen.screensize(700,700)
screen.title("Welcome to the Pong game!")
screen.tracer(0)


rightpaddel=Sidepaddle((350,0))

leftpaddel=Sidepaddle((-350,0))

ball=Ball()
score_board=Scoreboard()
screen.listen()
screen.onkey(rightpaddel.up,"Up")
screen.onkey(rightpaddel.down,"Down")

screen.onkey(leftpaddel.up,"w")
screen.onkey(leftpaddel.down,"s")



while True:
   
   time.sleep(0.12)
   ball.move()
   if ball.ycor()>340 or ball.ycor()<-340:
      ball.bounce_y()
   if ball.distance(rightpaddel)<30 or ball.distance(leftpaddel)<30:
       ball.bounce_x()
      
   if ball.xcor()>390:  
      ball.change_direction()
      score_board.left_score()
       
   if ball.xcor()<-390: 
      ball.change_direction()
      score_board.right_score()
      
   screen.update()
   





screen.exitonclick()