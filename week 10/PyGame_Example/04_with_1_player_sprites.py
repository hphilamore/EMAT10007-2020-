# First Python game

# import modules 
import pygame


# Our constants
# define a couple of colours 
BLACK   = (0  ,   0,   0)
WHITE   = (255, 255, 255)
BLUE    = (217, 231, 249)
GOLD    = (255, 255,   0)
PURPLE  = (202,  90, 155)
GREEN   = ( 23, 210, 155)

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
x_speed = 0
y_speed = 0
STEP = 5
SPEED = 5
################################# 
#  class for players
################################# 
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # Methods
    def __init__(self, x, y,color=PURPLE):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([15, 15])
        self.image.fill(color)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 
        # Set speed vector
        self.change_x = 0
        self.change_y = 0

        # score
        self.score = 0

    # increasing speed
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y
 
# Create the player object
Player1 = Player(50, 50)
# make a list of sprites and add Player1
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(Player1)


####################
# MAIN LOOP
####################
while not done:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player1.changespeed(-SPEED, 0)  
            elif event.key == pygame.K_RIGHT:
                Player1.changespeed(SPEED, 0)
            elif event.key == pygame.K_UP:
                Player1.changespeed(0, -SPEED)
            elif event.key == pygame.K_DOWN:
                Player1.changespeed(0, SPEED)
                
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                Player1.changespeed(SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                Player1.changespeed(-SPEED, 0)
            elif event.key == pygame.K_UP:
                Player1.changespeed(0, SPEED)
            elif event.key == pygame.K_DOWN:
                Player1.changespeed(0, -SPEED)

    
    ########################
    # DRAW EVERYTHING
    ########################
    
    # Clear screen
    screen.fill(BLUE)
    
    # This calls update on all the sprites
    # calls function update of all sprites
    all_sprites_list.update()

    
    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()
 
    # Pause to have same FPS
    clock.tick(60)

# when main loop is finished, quit pygame 
pygame.quit()

