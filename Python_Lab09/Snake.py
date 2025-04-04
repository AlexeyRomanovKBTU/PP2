#Imports
import pygame
import random

#Initializing
pygame.init()

#Window size
width = 600
height = 400

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (213, 50, 80)
orange = (255, 165, 0)
yellow = (255, 255, 0)

#Screen
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")

#Main Variables
clock = pygame.time.Clock()
cell_size = 20
speed = 5

#Font
font = pygame.font.SysFont("bahnschrift", 25)

#Display messages
def message(msg, color, x, y, isCentered):
    text = font.render(msg, True, color)
    if isCentered:
        text_width = text.get_width()
        x = (width - text_width) // 2
    screen.blit(text, [x, y])

#Generate random food position
def random_food_position(snake_body):
    while True:
        food_pos = [random.randrange(0, width // cell_size) * cell_size,
                    random.randrange(0, height // cell_size) * cell_size]
        if food_pos not in snake_body:
            return food_pos

#Food class
class Food:
    def __init__(self, snake_body):
        self.spawn(snake_body)

    def spawn(self, snake_body):
        self.position = random_food_position(snake_body)
        self.weight = random.choice([10, 20, 30])
        self.spawn_time = pygame.time.get_ticks()
        self.lifetime = 5000  #5 seconds

    def draw(self):
        if self.weight == 10:
            color = red
        elif self.weight == 20:
            color = orange
        else:
            color = yellow
        pygame.draw.rect(screen, color, pygame.Rect(self.position[0], self.position[1], cell_size, cell_size))

    def is_expired(self):
        return pygame.time.get_ticks() - self.spawn_time > self.lifetime

def game_loop():
    global speed
    game_over = False
    game_close = False

    #Initial snake position
    snake_pos = [width // 2, height // 2]
    snake_body = [[snake_pos[0], snake_pos[1]]]
    direction = 'RIGHT'
    change_to = direction

    #Initialize food
    food = Food(snake_body)
    
    #Initial score and level
    score = 0
    level = 1

    #Game Loop
    while not game_over:

        #Game over screen
        while game_close:
            screen.fill(black)
            message("Game Over!", red, 0, height // 4, True)
            message(f"Score: {score} Level: {level}", red, 0, height // 3, True)
            message("Press Q to Quit or R to Restart", red, 0, height // 2, True)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        #Main game screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_UP and direction != 'DOWN':
                    change_to = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    change_to = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    change_to = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    change_to = 'RIGHT'

        direction = change_to

        #Snake movement
        if direction == 'UP':
            snake_pos[1] -= cell_size
        elif direction == 'DOWN':
            snake_pos[1] += cell_size
        elif direction == 'LEFT':
            snake_pos[0] -= cell_size
        elif direction == 'RIGHT':
            snake_pos[0] += cell_size

        #Wall collision check
        if snake_pos[0] < 0 or snake_pos[0] >= width or snake_pos[1] < 0 or snake_pos[1] >= height:
            game_close = True

        #Update snake body
        snake_body.insert(0, list(snake_pos))

        #Check if snake has eaten food
        if snake_pos == food.position:
            score += food.weight
            if score % 40 == 0:
                level += 1
                speed += 2
            food = Food(snake_body)
        elif food.is_expired():
            food = Food(snake_body)
        else:
            snake_body.pop()

        #Collision check with itself
        for block in snake_body[1:]:
            if snake_pos == block:
                game_close = True

        #Drawing elements
        screen.fill(black)
        food.draw()
        for block in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(block[0], block[1], cell_size, cell_size))

        #Display score and level
        message(f"Score: {score} Level: {level}", white, 10, 10, False)

        pygame.display.flip()
        clock.tick(speed)

    pygame.quit()
    quit()

#Start the game
game_loop()