from re import X
from turtle import Screen
from numpy import blackman
import pygame
import random
import cv2
import mediapipe as mp  
  
vid = cv2.VideoCapture(0)
mp_Hands = mp.solutions.hands
hands = mp_Hands.Hands()
mpDraw = mp.solutions.drawing_utils

WINDOW_W = 1000
WINDOW_H = 641
WINDOW_SIZE = (WINDOW_W, WINDOW_H)

pygame.init()



screen = pygame.display.set_mode(WINDOW_SIZE)
bg = pygame.image.load("spongback.jpg")
bg = pygame.transform.scale(bg,(WINDOW_W,WINDOW_H))

Rbotton = pygame.image.load("botton.png")
Rbotton =  pygame.transform.scale(Rbotton,(235,235))
Gbotton = pygame.image.load("Gbotton.png")
Gbotton =  pygame.transform.scale(Gbotton,(215,215))
gameover = pygame.image.load("gameover.png")
gameover =  pygame.transform.scale(gameover,(800,500))


time = 0


score = 0
tedfont = pygame.font.SysFont("Comic Sans MS" , 30)
 

play = True
is_red = False
switch_time = random.randint(10,28)
while play:


    ret, frame = vid.read(0)
    frame = cv2.flip(frame, 1)
    RGB_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(RGB_image)
    multiLandMarks = results.multi_hand_landmarks

    if multiLandMarks:
        for handLms in multiLandMarks:
            mpDraw.draw_landmarks(frame, handLms, mp_Hands.HAND_CONNECTIONS)
        y8 = multiLandMarks[0].landmark[8].y
        y5 = multiLandMarks[0].landmark[5].y
        y12 = multiLandMarks[0].landmark[12].y
        y9 = multiLandMarks[0].landmark[9].y
        y16 = multiLandMarks[0].landmark[16].y
        y13 = multiLandMarks[0].landmark[13].y
        y20 = multiLandMarks[0].landmark[20].y
        y17 = multiLandMarks[0].landmark[17].y
        under1 = y8 > y5 
        under2 = y12 > y9
        under3 = y16 > y13
        under4 = y20 > y17
        all_y = under1 and under2 and under3 and under4 
        semi_y = under1 and under2 and under3
        if all_y == True and not is_red:
            score += 1
        elif all_y == True and is_red:
                score = 0
                screen.blit(gameover,(100,70))
                pygame.display.flip()
                pygame.time.delay(3000)
                pygame.event.get()
        elif under4 == True and semi_y == False:
            break
    cv2.imshow('frame', frame)
      

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


    scor_text = tedfont.render("SCORE: " + str(score), True, (202,225,255))
    screen.blit(bg,(0,0))
    screen.blit(scor_text, (410, 100))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_red:
                score += 1
            if event.key == pygame.K_SPACE and is_red:
                score = 0
                screen.blit(gameover,(100,70))
                pygame.time.delay(3000)
                pygame.event.get()
    time = time + 1
    if is_red:
        screen.blit(Rbotton,(389,200))
    else:
        screen.blit(Gbotton,(395,210))

   

    if time>=switch_time:
        is_red = not is_red
        time=0
        switch_time = random.randint(10,28)

    pygame.display.flip()

pygame.quit()      
  
vid.release()

cv2.destroyAllWindows()
