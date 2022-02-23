#Подключение модулей--------------------------------------------------
from cv2 import transform
import pygame
from pygame.constants import HIDDEN 
import sys
from random import randint
#Стат переменные--------------------------------------------------
run = True
w = 50
ws = 700
hs = 500
p1 = pygame.transform.scale(pygame.image.load('player1up.png'), (w,w))
p2 = pygame.transform.scale(pygame.image.load('player2up.png'), (w,w))
x1 = 0 + 10
x2 = ws - w - 10
y1 = 0 + 10
y2 = hs - w - 10
#Создание окна--------------------------------------------------
pygame.init()
scr = pygame.display.set_mode((ws, hs))
bg = pygame.transform.scale(pygame.image.load('bg.png'), (ws,hs))
pygame.display.set_caption('Maded by abik')
pygame.init()
#Цикл игры--------------------------------------------------
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    #Движение пsssssервого игрока--------------------------------------------------
    keys = pygame.key.get_pressed()
    #Лево
    if keys[pygame.K_LEFT] and x1 > 0:
        x1 -= 5
        p1 = pygame.transform.scale(pygame.image.load('player1left.png'), (w,w))
    #Право
    if keys[pygame.K_RIGHT] and x1 < ws - w:
        facing1 = 1
        x1 += 5
        p1 = pygame.transform.scale(pygame.image.load('player1right.png'), (w,w))
    #Верх
    if keys[pygame.K_UP] and y1 > 0: 
        y1 -= 5
        p1 = pygame.transform.scale(pygame.image.load('player1up.png'), (w,w))
    #Низ
    if keys[pygame.K_DOWN] and y1 < hs - w:
        y1 += 5
        p1 = pygame.transform.scale(pygame.image.load('player1down.png'), (w,w))
    #Движение второго игрока--------------------------------------------------
    #Лево
    if keys[pygame.K_a] and x2 > 0:
        x2 -= 5
        p2 = pygame.transform.scale(pygame.image.load('player2left.png'), (w,w))
    #Право
    if keys[pygame.K_d] and x2 < ws - w:
        x2 += 5
        p2 = pygame.transform.scale(pygame.image.load('player2right.png'), (w,w))
    #Верх
    if keys[pygame.K_w] and y2 > 0: 
        y2 -= 5
        p2 = pygame.transform.scale(pygame.image.load('player2up.png'), (w,w))
    #Низ
    if keys[pygame.K_s] and y2 < hs - w:
        y2 += 5
        p2 = pygame.transform.scale(pygame.image.load('player2down.png'), (w,w))
    #--------------------------------------------------
    r1 = (x1,y1, w, w)
    r2 = (x2,y2, w, w)
    player1 = pygame.draw.rect(scr, (255,0,0), r1)
    player2 = pygame.draw.rect(scr, (255,0,0), r2)
    scr.blit(bg, (0,0))
    scr.blit(p1,r1)
    scr.blit(p2,r2)
    #--------------------------------------------------
    if player1.colliderect(player2):
        print('Пойман')
    #Обновление екрана--------------------------------------------------
    pygame.display.update()
