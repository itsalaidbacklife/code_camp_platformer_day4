class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.on_ground = False
        self.vy = 0
        self.vx = 0
        
    def display(self):
        ellipse(self.x, self.y, 50, 50) #head
        line(self.x, self.y + 25, self.x, self.y + 100) #body
        line(self.x, self.y + 50, self.x-25, self.y + 20) #left arm
        line(self.x, self.y + 50, self.x+25, self.y + 20) #right arm
        line(self.x, self.y+100, self.x - 25, self.y + 150) #left leg
        line(self.x, self.y+100, self.x + 25, self.y + 150) #right leg 
        
    def onGround(self, ground):
        if self.x >= ground.x and self.x <= ground.x + ground.w:
            if self.y + 150 >= ground.y and self.y + 150 <= ground.y + 50:
                return True
            else:
                return False    