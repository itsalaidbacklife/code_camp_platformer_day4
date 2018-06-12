def setup():
    size(1000, 1000)
    global guy_x, guy_y, vx, vy, grounds, guy_on_ground
    guy_x = 500
    guy_y = 750
    vx = 0
    vy = 0
    guy_on_ground = True
    #Grounds: x,y of top corner, then width
    grounds = [(-5, 900, 1005), (500, 800, 100), (600, 700, 50), (500, 600, 50), (400, 500, 25), (300, 400, 25), (450, 350, 50), (550, 250, 50), (650, 150, 25)wd] 
def draw():
    global guy_x, guy_y, vx, vy, grounds, guy_on_ground
    background(150)
    
    # Draw Ground
    guy_on_ground = False
    for ground in grounds:
        rect(ground[0], ground[1], ground[2], 50)
        #Check if guy is on this ground
        if onGround(ground[0], ground[1], ground[0]+ground[2], ground[1]+50):
            guy_on_ground = True
            guy_y = ground[1] - 150
    # Set guy's speed based on whether he is falling
    if guy_on_ground:
        vy = 0
    else:
        vy += 1
    # Move guy
    guy_y += vy
    guy_x += vx
    # Draw guy
    ellipse(guy_x, guy_y, 50, 50) #head
    line(guy_x, guy_y + 25, guy_x, guy_y + 100) #body
    line(guy_x, guy_y + 50, guy_x-25, guy_y + 20) #left arm
    line(guy_x, guy_y + 50, guy_x+25, guy_y + 20) #right arm
    line(guy_x, guy_y+100, guy_x - 25, guy_y + 150) #left leg
    line(guy_x, guy_y+100, guy_x + 25, guy_y + 150) #right leg
    
def keyPressed():
    global vx, vy, guy_y, guy_on_ground
    if key == 'a':
        vx = -5
    elif key == 'd':
        vx = 5
    elif key == 'w' and guy_on_ground:
        vy = -15
        guy_y -= 10

def keyReleased():
    global vx
    if key == 'a' or key == 'd':
        vx = 0

def onGround(ground_x1, ground_y1, ground_x2, ground_y2):
    global guy_x, guy_y #Use x and y of guy to compare to ground
    if guy_x >= ground_x1 and guy_x <= ground_x2:
        if guy_y + 150 >= ground_y1 and guy_y + 150 <= ground_y2:
            return True
        else:
            return False
    
    
        