# First Python game

# import modules 
import pygame
import random


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



################################# 
#  class for gold
################################# 
class Gold(pygame.sprite.Sprite):
    """ our gold class. """
 
    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()
 
        # Set height, width
        self.image = pygame.Surface([25, 15])
        self.image.fill(GOLD)
 
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
 

        
 
# Create the player object
Player1 = Player(50, 50)

# make a list of sprites and add Player1
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(Player1)


# init random positions for gold pieces
GoldNum = 100
ListofGold = pygame.sprite.Group();
for Index in range(0,GoldNum-1):
    x = random.randint(1,800)
    y = random.randint(1,600)
    c = Gold(x,y)
    all_sprites_list.add(c) 
    ListofGold.add(c)


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

    # check for collision between Players and Gold
    # remove Gold (True)
    Player1Hitlist = pygame.sprite.spritecollide(Player1, ListofGold, True)
    # increase score Check the list of collisions.
    for item in Player1Hitlist:
        Player1.score += 1
        print(Player1.score)
    
    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()
 
    # Pause to have same FPS
    clock.tick(60)

# when main loop is finished, quit pygame 
pygame.quit()

