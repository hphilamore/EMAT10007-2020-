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
####################
# MAIN LOOP
####################
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 

  
    ########################
    # DRAW EVERYTHING
    ########################
    
    # Clear screen
    screen.fill(BLUE)
 

    # Flip screen
    pygame.display.flip()
 
    # Pause to have same FPS
    clock.tick(60)


# when main loop is finished, quit pygame 
pygame.quit()

