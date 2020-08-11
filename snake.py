from random import randrange
import pygame
from pygame import Color, Surface, event, image, key
import random
import math
pygame.init()
icon = pygame.image.load(r"D:\\icon.png")
blue=(0,0,255)
red =(255,0,0)
yellow = (255,255,0)
forest_green = (34,139,34)
screen_size = (720,600)
title = 'Snake Game'
vel = 0
vel_1 = 0
dim = (30,30)
x = random.randrange(100,690)
y = randrange(50,550)
x_enemy = random.randrange(100,690)
y_enemy = randrange(50,550)
screen = pygame.display.set_mode(screen_size)
caption = pygame.display.set_caption(title)

def snake(surface,color):
    for p , z in snake_list:
       pygame.draw.rect(surface,color,[p,z,30,30])
def food(surface,color,centre,radius):
    pygame.draw.circle(surface,color,centre,radius)
def score_display():
    font = pygame.font.SysFont(None, 40)
    img = font.render("Score :" + str(score*10), True, forest_green )
    screen.blit(img, (10, 10))

score = 0              
running = True
snake_head = 1 
snake_list = [] 
while running:
    centre = (x_enemy,y_enemy)  
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
    if x >= 690 :
        running = False
    if x <= 0 :
        running = False
    if y >= 570:
        running = False
    if y <= 0 :
        running = False
    x += vel
    y += vel_1 
    if abs(x - x_enemy)< 18 and abs(y - y_enemy)< 18:
        score +=1
        snake_head +=20
        x_enemy = random.randint(20, 690)
        y_enemy = random.randint(20, 550)
    head = []
    head.append(x)
    head.append(y)
    snake_list.append(head)     
       
    if len(snake_list) > snake_head:
        del snake_list[0]   
    if head in snake_list[:-1]:
        running = False                   
    screen.fill((255, 255, 255))              
    snake(screen,blue)
    food(screen,red,centre,7)
    score_display()
    pygame.display.update() 