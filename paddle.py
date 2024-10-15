from turtle import Turtle




class Sidepaddle(Turtle):
    def __init__(self,p_position):
        super().__init__()
        self.p_position=p_position      
        self.create_paddel()
        
        
    def create_paddel(self):
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=4,stretch_len=1)
        self.penup()
        self.goto(self.p_position)
          
    
    
    def up(self):
        new_y=self.ycor()+40
        self.goto(self.p_position[0],self.p_position[1]+new_y)
    def down(self):
        new_y=self.ycor()-40
        self.goto(self.p_position[0],self.p_position[1]+new_y) 
            
              
      
          
        
        
        