#importing required modules
from random import randrange
import pygame
from pygame import Color, Surface, event, image, key
#initializing pygame
pygame.init()
#initializing variables
blue = (0, 0, 255)

red = (255, 0, 0)

yellow = (255, 255, 0)

forest_green = (34, 139, 34)

screen_size = (720, 600)

title = 'Snake Game'

vel = 0

vel_1 = 0

dim = (30, 30)

x = random.randrange(100, 690)

y = randrange(50, 550)

x_enemy = random.randrange(100, 690)

y_enemy = randrange(50, 550)
#setting game window where game will be played
screen = pygame.display.set_mode(screen_size)
#setting game name
caption = pygame.display.set_caption(title)

#function for blitting rectangle(snake)
def snake(surface, color):
    for p, z in snake_list:
        pygame.draw.rect(surface, color, [p, z, 30, 30])

#function for blitting circle(food)
def food(surface, color, centre, radius):
    pygame.draw.circle(surface, color, centre, radius)

#displaying score
def score_display():
    font = pygame.font.SysFont(None, 40)
    img = font.render("Score :" + str(score*10), True, forest_green)
    screen.blit(img, (10, 10))

#starting score
score = 0
#game state (True or false)
running = True
#default snake length
snake_head = 1
#list for appending snake heads as snake eats food
snake_list = []
#while loop for continuously until stopped
while running:
    #food position
    centre = (x_enemy, y_enemy)
    #initializing keyboard keys
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            vel = -0.7
            vel_1 = 0

        if keys[pygame.K_RIGHT]:
            vel = 0.7
            vel_1 = 0

        if keys[pygame.K_UP]:
            vel_1 = -0.7
            vel = 0

        if keys[pygame.K_DOWN]:
            vel_1 = 0.7
            vel = 0

        if keys[pygame.K_ESCAPE]:
            running = False

    if x >= 690:
        running = False

    if x <= 0:
        running = False

    if y >= 570:
        running = False

    if y <= 0:
        running = False
    #used for making the snake move continuously
    x += vel

    y += vel_1
    #if statement for collision when the position of snake and food equals or is nearby(set accordingly)
    if abs(x - x_enemy) < 18 and abs(y - y_enemy) < 18:
        #increment score when snake eats food
        score += 1
        #increase length of snake when snake eats food
        snake_head += 20
        #changing position of food when snake eats food
        x_enemy = random.randint(20, 690)

        y_enemy = random.randint(20, 550)

    #code for increasing snake length
    head = []

    head.append(x)

    head.append(y)

    snake_list.append(head)

    #code for cutting heads
    if len(snake_list) > snake_head:
   
        del snake_list[0]
    #end game if snake eats itself
    if head in snake_list[:-1]:
    
        running = False
    #filling colors on screen
    screen.fill((255, 255, 255))
    #calling functions
    snake(screen, blue)

    food(screen, red, centre, 7)

    score_display()
    #function for updating contents on screen
    pygame.display.update()
