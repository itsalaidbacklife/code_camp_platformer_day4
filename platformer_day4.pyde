from groundClass import Ground
from characterClass import Player
def setup():
    size(1000, 1000)
    global grounds, guy
    guy_x = 500
    guy_y = 750
    vx = 0
    vy = 0
    guy = Player(500, 750)
    #Grounds: x,y of top corner, then width
    grounds = [Ground(-5, 900, 1005), Ground(500, 800, 100), Ground(600, 700, 50), Ground(500, 600, 50), Ground(400, 500, 25), Ground(300, 400, 25), Ground(450, 350, 50), Ground(550, 250, 50), Ground(650, 150, 25)]
    
def draw():
    global guy, grounds
    background(150)
    
    # Draw Ground
    guy.on_ground = False
    for ground in grounds:
        # rect(ground[0], ground[1], ground[2], 50)
        ground.display()
        #Check if guy is on this ground
        if guy.onGround(ground):
            guy.on_ground = True
            guy.y = ground.y - 150
    # Set guy's speed based on whether he is falling
    if guy.on_ground:
        guy.vy = 0
    else:
        guy.vy += 1
    # Move guy
    guy.y += guy.vy
    guy.x += guy.vx
    guy.display()
    
def keyPressed():
    global guy
    if key == 'a':
        guy.vx = -5
    elif key == 'd':
        guy.vx = 5
    elif key == 'w' and guy.on_ground:
        guy.vy = -15
        guy.y -= 10

def keyReleased():
    global guy
    if key == 'a' or key == 'd':
        guy.vx = 0


    
    
        