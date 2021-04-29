#sgnwrgqeog#
'''
def count(a):
    start = 1
    if a > 0:
        for i in range(start, a + 1, 1):
            print(i)
    elif a < 0:
        for i in range(start, a - 1, -1):
            print(i)
count(-9)
'''

#setup#
import pygame
pygame.init()

win = pygame.display.set_mode((800, 740))
pygame.display.set_caption("My Culminating Game")

x = 200
y = 165
width = 40
height = 60
vel = 5

#loads#
life = True

bg = pygame.image.load("grassbackground.png")
pygame.display.update()
character = pygame.image.load("standing1.png")
#pygame.display.update()

keys = pygame.key.get_pressed()


#main game function#
while life == True:
    win.blit(bg, (0, 0))
    pygame.display.update()
    pygame.time.delay(100)
    pygame.display(character, (x, y))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            life = False
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 300 - width - vel:
        x += vel
    if keys[pygame.K_UP] and y < vel:
        y -= vel
    if keys[pygame.K_DOWN] and y > 300 - height - vel:
        y += vel



#pygame.image.load(r"C:\Users\syedm\Desktop\Computer Science Culminating\sideimage.png", (win, (0, 225, 0), (x, y, width, height)))#

pygame.quit()
