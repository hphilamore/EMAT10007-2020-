# First Python game

# import modules 
import pygame


# Our constants
# define a couple of colours 
WHITE   = (255, 255, 255)
BLUE    = (217, 231, 249)



################################# 
# Call this function so the Pygame library can initialize itself
pygame.init()

# init a clock
clock = pygame.time.Clock()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# Set the title of the window
pygame.display.set_caption('Our Game')
 

done = False
x=100
y=100
STEP = 5
####################
# MAIN LOOP
####################
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x = x -STEP  
            elif event.key == pygame.K_RIGHT:
                x = x + STEP 
            elif event.key == pygame.K_UP:
                y = y - STEP
            elif event.key == pygame.K_DOWN:
                y = y + STEP
 
    
    ########################
    # DRAW EVERYTHING
    ########################
    
    # Clear screen
    screen.fill(BLUE)
 
    pygame.draw.circle(screen,WHITE,[x,y],5)
    
    # Flip screen
    pygame.display.flip()
 
    # Pause to have same FPS
    clock.tick(60)


# when main loop is finished, quit pygame 
pygame.quit()

