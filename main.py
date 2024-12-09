import pygame
import time

pygame.init()

WIDTH = 600
HEIGHT = 600 

display_surface= pygame.display.set_mode((WIDTH,HEIGHT))

bg = pygame.image.load('bgpygame.jpg')
car1 = pygame.image.load("character_1.png")
car2 = pygame.image.load("character_2.png")

bg = pygame.transform.scale(bg,(WIDTH,HEIGHT))
car1= pygame.transform.scale(car1,(150,150))
car2= pygame.transform.scale(car2,(150,150))

car1_x = 100
car1_y = 10

car2_x = 500
car2_y = 10

keys1 = [False,False,False,False]
keys2 = [False,False,False,False]

while True :
    display_surface.blit(bg,(0,0))
    display_surface.blit(car1,(car1_x,car2_y))
    display_surface.blit(car2,(car2_x,car2_y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                keys1[0]=True
            if event.key == pygame.K_DOWN:
                keys1[2]=True
            if event.key == pygame.K_LEFT:
                keys1[1]=True 
            if event.key == pygame.K_RIGHT:
                keys1[3]=True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                keys1[0]=False
            if event.key == pygame.K_DOWN:
                keys1[2]=False 
            if event.key == pygame.K_LEFT:
                keys1[1]=False 
            if event.key == pygame.K_RIGHT: 
                keys1[3] = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keys2[0]=True
            if event.key == pygame.K_s:
                keys2[2]=True
            if event.key == pygame.K_a:
                keys2[1]=True 
            if event.key == pygame.K_d:
                keys2[3]=True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                keys2[0]=False
            if event.key == pygame.K_s:
                keys2[2]=False 
            if event.key == pygame.K_a:
                keys2[1]=False 
            if event.key == pygame.K_d: 
                keys2[3] = False
    
    if keys1[0]:
        if car1_y>0:
            car1_y -= 2 
    if keys1[1]:
        if car1_x>0:
            car1_x -= 2
    if keys1[2]:
        if car1_y<600:
            car1_y += 2
    if keys1[3]:
        if car1_x<600:
            car1_x += 2

    if keys2[0]:
        if car2_y>0:
            car2_y -= 2 
    if keys2[1]:
        if car2_x<600:
            car2_x -= 2
    if keys2[2]:
        if car2_y<600:
            car2_y += 2
    if keys2[3]:
        if car2_x>0:
            car2_x += 2
    
        