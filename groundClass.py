class Ground:
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        
    def display(self):
        rect(self.x, self.y, self.w, 50)