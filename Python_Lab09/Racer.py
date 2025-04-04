#Imports
import pygame, sys, os
from pygame.locals import *
import random, time

#Change directory
os.chdir(r"C:\Users\Алексей\Desktop\KBTU\2 semester\PP2\Python_Lab09")

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Main Variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
COIN_SPEED = 5
SCORE = 0
COINS = 0
FPS = 60
COINS_FOR_SPEEDUP = 5
coin_spawn_delay = 2000
last_coin_spawn = pygame.time.get_ticks()
FramePerSec = pygame.time.Clock()

#Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

#Screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

#Classes
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

      def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)
        self.weight = random.randint(1, 3)

    def move(self):
        self.rect.move_ip(0, COIN_SPEED)
        if self.rect.bottom > 600:
            self.kill()

def spawn_coin():
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)
                  

#Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(C1)
all_sprites.add(E1)


# Game Loop
while True:
    for event in pygame.event.get():     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    DISPLAYSURF.blit(background, (0,0))
    scores = font_small.render("Score: " + str(SCORE), True, BLACK)
    coin_scores = font_small.render("Coins: " + str(COINS), True, BLACK)
    DISPLAYSURF.blit(scores, (10,10))
    DISPLAYSURF.blit(coin_scores, (SCREEN_WIDTH - 105,10))

    # Move and draw all sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Player and Enemy collision
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit()        

    # Player and Coin collision
    hit_coins = pygame.sprite.spritecollide(P1, coins, dokill=True)
    for coin in hit_coins:
        pygame.mixer.Sound('coin_pickup.mp3').play()
        COINS += coin.weight

        # Speed up enemy if enough coins collected
        if COINS % COINS_FOR_SPEEDUP == 0:
            SPEED += 1

    # Randomly spawn new coins over time
    current_time = pygame.time.get_ticks()
    if current_time - last_coin_spawn > coin_spawn_delay:
        spawn_coin()
        last_coin_spawn = current_time

    pygame.display.update()
    FramePerSec.tick(FPS)