
# First Python game

# import modules
import pygame
import random

# Our constants
# We define a number of colours
# RGB values (Red, Green, Blue) 0...255
BLACK   = (0  ,   0,   0)
WHITE   = (255, 255, 255)
BLUE    = (217, 231, 249)
GOLD    = (255, 255,   0)
PURPLE  = (202,  90, 155)
GREEN   = ( 23, 210, 155)
RED     = (255,   0,   0)

# set speed
SPEED = 15

#################################
#  class for players
#  derived from class: pygame.sprite.Sprite
#################################
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """

    # Methods
    def __init__(self, x, y, color=PURPLE):
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

    # function to change speed of Player
    def changeSpeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y

    # update position (will be called every time we go through the
    # while loop (see below)
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

#################################
#  class for enemies
#  derived from class: pygame.sprite.Sprite
#################################
class Enemy(pygame.sprite.Sprite):
    """ This class is for a random enemy """

    delay = 0

    # Methods
    def __init__(self, x, y, size, color=RED):
        """ Contructor for the Enemy class """
        # Call the parent constructor first (the Sprite constructor)
        super().__init__()

        # Set height, width
        self.size = size
        self.image = pygame.Surface([size, size])
        self.image.fill(color)

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # Set speed vector
        self.change_x = 0
        self.change_y = 0

    # update position (will be called every time we go through the
    # while loop (see below)
    def update(self):
        """ Find a new position for the enemy"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def moveRandomly(self, speed, xLimit, yLimit):

        if self.delay == 0:
            randomDirection = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"][random.randint(0,7)]
            if randomDirection == "N":
                self.change_x, self.change_y = 0, -speed
            elif randomDirection == "NE":
                self.change_x, self.change_y = speed, -speed
            elif randomDirection == "E":
                self.change_x, self.change_y = speed, 0
            elif randomDirection == "SE":
                self.change_x, self.change_y = speed, speed
            elif randomDirection == "S":
                self.change_x, self.change_y = 0, speed
            elif randomDirection == "SW":
                self.change_x, self.change_y = -speed, speed
            elif randomDirection == "W":
                self.change_x, self.change_y = -speed, 0
            elif randomDirection == "NW":
                self.change_x, self.change_y = -speed, -speed

            self.delay = random.randint(5,100)

        else:
            self.delay -= 1

        if self.rect.x + self.change_x < 0 or (self.rect.x + self.size) + self.change_x > xLimit:
            self.change_x *= -1
        if self.rect.y + self.change_y < 0 or (self.rect.y + self.size) + self.change_y > yLimit:
            self.change_y *= -1

#################################
#  class for gold pieces
#  derived from class: pygame.sprite.Sprite
#################################
class Gold(pygame.sprite.Sprite):
    """ our gold class. """

    # -- Methods
    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pygame.Surface([25, 15]) # rectangle size
        self.image.fill(GOLD) # colore defined above

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#################################
# Call this function so the Pygame library can initialize itself
pygame.init()

# init font
# this is needed to render fonts on the screen (e.g., to show the score)
pygame.font.init()
myfont = pygame.font.SysFont("Helvetica", 24)

# init a clock
# need to keep a constant FPS (frames per second)
clock = pygame.time.Clock()

# Create an 800x600 sized screen
Screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Our Game')

# Create the players (instances of the class Player)
Player1 = Player(50, 50)       # at position x=50, y=50 and default color
Player2 = Player(700, 50,GREEN)

# Create enemy (instance of the class Enemy)
Enemy1 = Enemy(400, 400, 30)

# list of all sprites in the game
AllSpritesList = pygame.sprite.Group()

PlayerList = pygame.sprite.Group()

# add players to the list
AllSpritesList.add(Player1)
AllSpritesList.add(Player2)

# list of all players in the game
PlayerList = pygame.sprite.Group()
PlayerList.add(Player1)
PlayerList.add(Player2)

# add enemy to the game
AllSpritesList.add(Enemy1)

# init random positions for gold pieces
GoldNum = 100  # number of pieces
# make another sprite list only with gold pieces
# this is need to check if a player has touched a gold
ListofGold = pygame.sprite.Group();
for Index in range(0,GoldNum-1):
    x = random.randint(1,800) # random positions on the screen
    y = random.randint(1,600)
    c = Gold(x,y)
    AllSpritesList.add(c) # also add them to the list of all sprites
    ListofGold.add(c)


done = False
####################
# MAIN LOOP
####################
while not done:

    # check if there as been any evetn
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close window button has been pressed
            done = True

        # Set speed  to SPEED if a key pressed
        # object will keep this speed until key is released (see below)
        elif event.type == pygame.KEYDOWN:
                #################################
                # player 1 uses arrow keys
                #################################
            if event.key == pygame.K_a:
                Player1.changeSpeed(-SPEED, 0)
            elif event.key == pygame.K_d:
                Player1.changeSpeed(SPEED, 0)
            elif event.key == pygame.K_w:
                Player1.changeSpeed(0, -SPEED)
            elif event.key == pygame.K_s:
                Player1.changeSpeed(0,SPEED)
                #################################
                # player 2 uses keys a,d,w and s
                #################################
            elif event.key == pygame.K_LEFT:
                Player2.changeSpeed(-SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                Player2.changeSpeed(SPEED, 0)
            elif event.key == pygame.K_UP:
                Player2.changeSpeed(0, -SPEED)
            elif event.key == pygame.K_DOWN:
                Player2.changeSpeed(0, SPEED)

        # Reset speed when key goes up
        # set speed back to zero, when button is released
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                Player1.changeSpeed(SPEED, 0)
            elif event.key == pygame.K_d:
                Player1.changeSpeed(-SPEED, 0)
            elif event.key == pygame.K_w:
                Player1.changeSpeed(0, SPEED)
            elif event.key == pygame.K_s:
                Player1.changeSpeed(0, -SPEED)
                 ############################
            elif event.key == pygame.K_LEFT:
                Player2.changeSpeed(SPEED, 0)
            elif event.key == pygame.K_RIGHT:
                Player2.changeSpeed(-SPEED, 0)
            elif event.key == pygame.K_UP:
                Player2.changeSpeed(0, SPEED)
            elif event.key == pygame.K_DOWN:
                Player2.changeSpeed(0, -SPEED)

    # Invoke the random movement of the enemy
    Enemy1.moveRandomly(15, 800, 600)

    # This calls update on all the sprites
    # calls function update of all sprites
    AllSpritesList.update()

    # check for collision between Players and gold pieces
    # remove Gold if touched by player (True)
    Player1HitList = pygame.sprite.spritecollide(Player1, ListofGold, True)
    Player2HitList = pygame.sprite.spritecollide(Player2, ListofGold, True)

    # increase score by checking list of collisions.
    # if there has been now collision the list will be empty
    for item in Player1HitList:
        Player1.score += 1
    for item in Player2HitList:
        Player2.score += 1

    # Detect if Enemy1 is touching either of the players

    EnemyHitList = pygame.sprite.spritecollide(Enemy1, PlayerList, False)
    print(EnemyHitList)

    # If so, decrease the player's score
    stealAmount = random.randint(1,5)
    for player in EnemyHitList:
        player.score -= stealAmount
        if player.score < 0:
            player.score = 0

    ########################
    # DRAW EVERYTHING
    ########################

    # Clear screen
    # redraw the background
    Screen.fill(BLUE)

    # Draw sprites
    # including players and gold
    AllSpritesList.draw(Screen)


    # Show score for players online
    # checkout http://www.pygame.org/docs/ref/font.html
    ScoreText1 = myfont.render("Player 1:  "+str(Player1.score), 1, (0,0,0))
    ScoreText2 = myfont.render("Player 2:  "+str(Player2.score), 1, (0,0,0))
    Screen.blit(ScoreText1, (100, 10)) # add on top of screen
    Screen.blit(ScoreText2, (600, 10)) # add on top of screen


    # Flip screen
    pygame.display.flip()

    # Pause to have same FPS
    clock.tick(60)


# when main loop is finished, quit pygame
pygame.quit()
