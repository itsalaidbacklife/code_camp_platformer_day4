def setup():
    size(1000, 1000)
    global guy_x, guy_y, vx, vy
    guy_x = 500
    guy_y = 750
    vx = 0
    vy = 0
def draw():
    global guy_x, guy_y, vx, vy
    background(150)
    
    # Draw Ground
    rect(-5, 900, 1005, 100)
    
    # Draw guy
    ellipse(guy_x, guy_y, 50, 50) #head
    line(guy_x, guy_y + 25, guy_x, guy_y + 100) #body
    line(guy_x, guy_y + 50, guy_x-25, guy_y + 20) #left arm
    line(guy_x, guy_y + 50, guy_x+25, guy_y + 20) #right arm
    line(guy_x, guy_y+100, guy_x - 25, guy_y + 150) #left leg
    line(guy_x, guy_y+100, guy_x + 25, guy_y + 150) #right leg
    
    # Move guy
    guy_x += vx
    #Gravity
    if guy_y < 750:
        vy += 1
    else:
        vy = 0
        guy_y = 750
    guy_y += vy

def keyPressed():
    global vx, vy, guy_y
    if key == 'a':
        vx = -5
    elif key == 'd':
        vx = 5
    elif key == 'w' and guy_y == 750:
        vy = -15
        guy_y -= 10

def keyReleased():
    global vx
    if key == 'a' or key == 'd':
        vx = 0
        