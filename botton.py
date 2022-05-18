from re import X
from turtle import Screen
from numpy import blackman
import pygame
import random

WINDOW_W = 1000
WINDOW_H = 641
WINDOW_SIZE = (WINDOW_W, WINDOW_H)
BLACK = (0, 0, 0)
score = 0
pygame.init()

font = pygame.font.SysFont("Arial", 50, bold = True, italic = True)
Press_text = font.render("PRESS", True, BLACK)
dont_Press_text = font.render("DONT PRESS", True, BLACK)
scor_text = font.render("SCORE: " + str(score), False, BLACK)






screen = pygame.display.set_mode(WINDOW_SIZE)
bg = pygame.image.load("spongback.jpg")
bg = pygame.transform.scale(bg,(WINDOW_W,WINDOW_H))

Rbotton = pygame.image.load("botton.png")
Rbotton =  pygame.transform.scale(Rbotton,(300,300))
Gbotton = pygame.image.load("Gbotton.png")
Gbotton =  pygame.transform.scale(Gbotton,(215,215))
gameover = pygame.image.load("gameover.png")
gameover =  pygame.transform.scale(gameover,(800,500))


time = 0





play = True
is_red = False
switch_time = random.randint(100, 500)
while play:
    screen.blit(bg,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_red:
                score += 1
                scor_text = font.render("SCORE: " + str(score), False, BLACK)
                print(score)
            if event.key == pygame.K_SPACE and is_red:
                score = 0
                scor_text = font.render("SCORE: " + str(score), False, BLACK)
                screen.blit(gameover,(100,70))
                pygame.display.flip()
                pygame.time.delay(5000)
                pygame.event.get()
    time = time + 1
    if is_red:
        screen.blit(Rbotton,(350,170))
    else:
        screen.blit(Gbotton,(395,210))

    if time>=switch_time:
        is_red = not is_red
        time=0
        switch_time = random.randint(100,500)

    pygame.display.flip()

pygame.quit()
