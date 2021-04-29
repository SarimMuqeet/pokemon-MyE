#              setup            #

'''Instructions For Playing:'''
###IN ORDER TO PLAY THE GAME YOU MUST USE BOTH-
###THE WRITTEN OUTPUTS ON PYTHON AND PYGAME GRAPHICS-
###FOR EXAMPLE, IF YOU INTERACT WITH THE PROFESSOR, HIS TEXTS WILL-
###POP UP AS OUTPUTS ON THE WRITTEN MODULE SIMILAR TO THE-
###INSTRUCTIONS AT THE BEGINNING OF THE GAME.

#imports#
from colorama import init, Fore, Back, Style
from termcolor import colored
init(convert=True)

import pygame
import time
import shelve
import random

#assignments#
pygame.init()

win = pygame.display.set_mode((735, 720))
pygame.display.set_caption("My Culminating Game")

x = 200
y = 165
width = 50
height = 60
vel = 5
walkCount = 0
BwalkCount = 0
RwalkCount = 0


width2 = 20
height2 = 20

rivalx = 367
rivaly = 600
rivalvel = 6

#walking varibles#
left = False
right = False
up = False
down = False

left2 = False
right2 = False
up2 = False
down2 = False

left3 = False
right3 = False
up3 = False
down3 = False


life = True
start = True

starter = True
continueoldgame = False

yourpokemon = []
yourpokemonword = []
rivalpokemon = []
rivalpokemonword = []


myList = []


clock = pygame.time.Clock()

#                loads              #

#start screen
print("Would you like to recall a previously saved game?")
a = input()
if a == "yes" or a == "Yes":
    continueoldgame = True
while continueoldgame:
    shelfFile = shelve.open(myList[1])

    


bg = pygame.image.load(r"C:\Users\syedm\Desktop\Computer Science Culminating\CompSciCBackground.png")
pygame.display.update()
character = pygame.image.load("left1.png")
pygame.display.update()

#Main Character Sprites
walkup = [pygame.image.load("up1.png"), pygame.image.load("up2.png"), pygame.image.load("up3.png")]
walkdown = [pygame.image.load("standing1.png"), pygame.image.load("standing2.png"), pygame.image.load("standing3.png")]
walkright = [pygame.image.load("right1.png"), pygame.image.load("right2.png"), pygame.image.load("right3.png")]
walkleft = [pygame.image.load("left1.png"), pygame.image.load("left2.png"), pygame.image.load("left3.png")]


standstill = pygame.image.load("standing1.png")

#black Sprites
blackup = [pygame.image.load("Oup1.png"), pygame.image.load("Oup2.png"), pygame.image.load("Oup3.png")]
blackdown = [pygame.image.load("Odown1.png"), pygame.image.load("Odown2.png"), pygame.image.load("Odown3.png")]
blackright = [pygame.image.load("Oright1.png"), pygame.image.load("Oright2.png"), pygame.image.load("Oright3.png")]
blackleft = [pygame.image.load("Oleft1.png"), pygame.image.load("Oleft2.png"), pygame.image.load("Oleft3.png")]

Bstandstill = pygame.image.load("Odown1.png")

#Rival Sprites
rivalup = [pygame.image.load("Rup1.png"), pygame.image.load("Rup2.png"), pygame.image.load("Rup3.png")]
rivaldown = [pygame.image.load("Rdown1.png"), pygame.image.load("Rdown2.png"), pygame.image.load("Rdown3.png")]
rivalright = [pygame.image.load("Rright1.png"), pygame.image.load("Rright2.png"), pygame.image.load("Rright3.png")]
rivalleft = [pygame.image.load("Rleft1.png"), pygame.image.load("Rleft2.png"), pygame.image.load("Rleft3.png")]

Rstandstill = pygame.image.load("Rdown1.png")


#starters
charmander2 = pygame.image.load("charmander.png")
bulbasaur2 = pygame.image.load("bulbasaur.png")
squirtle2 = pygame.image.load("squirtle.png")


starterpokemon = ["charmander", "bulbasaur", "squirtle"]
starterpokemon2 = [charmander2, bulbasaur2, squirtle2]


charmanderback = pygame.image.load("charmanderback.png")
bulbasaurback = pygame.image.load("bulbasaurback.png")
squirtleback = pygame.image.load("squirtleback.png")

battlesprite = [charmanderback, bulbasaurback, squirtleback]


#                functions               #
def redraw():
    global walkCount
    global standstill
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 9:
        walkCount = 0

    if left:
        win.blit(walkleft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkright[walkCount//3], (x, y))
        walkCount += 1
    elif up:
        win.blit(walkup[walkCount//3], (x, y))
        walkCount += 1
    elif down:
        win.blit(walkdown[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(standstill, (x, y))
    
    pygame.display.update()

def Oredraw():
    global BwalkCount
    global Bstandstill
    win.blit(bg, (0, 0))
    if BwalkCount + 1 >= 9:
        BwalkCount = 0

    elif left2:
        win.blit(blackleft[BwalkCount//3], (blackx, blacky))
        BwalkCount += 1

    elif right2:
        win.blit(blackright[BwalkCount//3], (blackx, blacky))
        BwalkCount += 1

    elif up2:
        win.blit(blackup[BwalkCount//3], (blackx, blacky))
        BwalkCount += 1

    elif down2:
        win.blit(blackdown[BwalkCount//3], (blackx, blacky))
        BwalkCount += 1
    else:
        win.blit(Bstandstill, (blackx, blacky))

    pygame.display.update()


def Rredraw():
    global RwalkCount
    global Rstandstill
    win.blit(bg, (0, 0))
    if RwalkCount + 1 > 9:
        RwalkCount = 0

    elif left3:
        win.blit(rivalleft[RwalkCount//3], (rivalx, rivaly))
        RwalkCount += 1

    elif right3:
        win.blit(rivalright[RwalkCount//3], (rivalx, rivaly))
        RwalkCount += 1

    elif up3:
        win.blit(rivalup[RwalkCount//3], (rivalx, rivaly))
        RwalkCount += 1

    elif down3:
        win.blit(rivaldown[RwalkCount//3], (rivalx, rivaly))
        RwalkCount += 1
    else:
        win.blit(Rstandstill, (rivalx, rivaly))

    pygame.display.update()

def boundaries(xpos, ypos):
    global x
    global y
    pygame.draw.rect(win, (0, 0, 0), (xpos, ypos, width2, height2))
    if xpos == x - width:
        xpos == x - width - 10
    elif ypos == y:
        vel = 0
    pygame.display.update()
    

'''def collision(xpos, ypos, width, height, x, y, width2, height2):
    if(x+'''

def changebackground(newbackground):
    global win
    bg = pygame.image.load(newbackground)
    pygame.display.update()
    win.blit(bg, (0, 0))

'''def obstacle1(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)    
'''




#main game function#
win.blit(bg, (0, 0))
pygame.display.update()
while life == True:
    #starting test...wait a total of 4 seconds before character appears on screen
    while start == True:
        print("Welcome to your first Pokemon Adventure")
        print("")
        time.sleep(2)
        print("You have just been reincarnated. Don't ask why you didn't start in a house.")
        print("")
        time.sleep(2)
        print("Your first task is to visit the Professor's House to get your first Pokemon")
        print("")
        print("")
        print("Hint: Professor Black's House is at the end of the street you are currently on")
        print("It is isolated from the rest of the houses in the town")
        start = False

    clock.tick(36)
    #win.blit(bg, (0, 0))
    #pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            life = False
    
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_a] and x > 0 + width + vel:
        x -= vel
        left = True
        right = False
        if right == False:
            standstill = pygame.image.load("left1.png")
        pygame.display.update()
    
    elif keys[pygame.K_d] and x < 735 - width - vel:
        x += vel
        right = True
        left = False
        pygame.display.update()
        
    elif keys[pygame.K_w] and y > 64:
        y -= vel
        up = True
        down = False
        right = False
        left = False
        pygame.display.update()
        
    elif keys[pygame.K_s] and y < 740 - height - vel:
        y += vel
        down = True
        up = False
        right = False
        left = False
        pygame.display.update()
        

    else:
        walkCount = 0
        
    redraw()



    #collisions/identifying boundaries
    '''boundaries (480, 146)'''

    if 480>= x >= 445 and 150 >= y >= 130:
        bg = pygame.image.load("Laboratory.png")
        pygame.display.update()
        win.blit(bg, (0, 0))
        x = 367
        y = 600
        blackx = 300
        blacky = 250
        
        win.blit(Bstandstill, (blackx, blacky))
        win.blit(standstill, (x, y))
        pygame.display.update()
        print("")
        print("Black: Hey there! You must be the new trainer!1")
        print("Black: I have something very special to show you. Follow me.")
        print("")
        
        #PKMN Trainer Black interaction
        while y >= 300:
            y -= vel
            up = True
            redraw()
            win.blit(Bstandstill, (blackx, blacky))
            pygame.display.update()
            win.blit(standstill, (x, y))
        time.sleep(2)
        while blackx != 150:
            blackx -= vel
            left2 = True
            right2 = False
            up2 = False
            down2 = False
            if right2 == False:
                Bstandstill = pygame.image.load("Oleft1.png")
            win.blit(Bstandstill, (blackx, blacky))
            x -= vel
            left = True
            right = False
            up = False
            down = False
            if right == False:
                standstill = pygame.image.load("left1.png")
            Oredraw()
            redraw()
            pygame.display.update()
        win.blit(Bstandstill, (blackx, blacky))
        pygame.display.update()
        win.blit(standstill, (x, y))
        pygame.display.update()

        time.sleep(3)            
        print("")
        print("Black: Look inside in this object. I've got three pokeballs ready for you.")
        time.sleep(2)

        win = pygame.display.set_mode((500, 200))
        changebackground("Battle1.png")
        

        #starter pics - can have 45 pixels of space between them, y value will be 500

        print("")
        print("Each one contains either a grass, water, or fire type pokemon")
        print("")

        win.blit(charmander2, (0, 100))
        pygame.display.update()
        print(colored("Black: This is 'CHARMANDER', the fire type pokemon", "red"))
        time.sleep(2)
        win.blit(bulbasaur2, (165, 100))
        pygame.display.update()
        print("Black: This is 'BULBASAUR', the grass type pokemon")
        time.sleep(2)
        win.blit(squirtle2, (330, 100))
        pygame.display.update()
        print("Black: This is 'SQUIRTLE', the water type pokemon")
        time.sleep(2)
        starter = True
        while starter:
            print("")
            print("Type in the name of whichever pokemon you'd like to select")
            pokemonchoice = input()

            time.sleep(2)

            win = pygame.display.set_mode((735, 720))
            changebackground("Laboratory.png")
            pygame.display.update()
            win.blit(blackdown[1], (120, 350))
            win.blit(walkdown[1], (170, 350))
            pygame.display.update()

            
            print("Excellent choice. Would you like to give a nickname to your new pokemon?")
            choice = input()
            if choice == "yes" or choice == "Yes":
                print("What would you like to name it?")
                nickname = input()
            else:
                nickname = pokemonchoice
            print("Your " + "'" + str(nickname) + "'" + " has safely been stored in its pokeball")

            time.sleep(2)
            #Introduce Rival

            print("Black: Now that I recall, there was another kid that was supposed to show up today...")
            time.sleep(4)
            print("Black: ...")
            time.sleep(3)
            print("You: ????")
            for i in range(35):
                up3 = True
                down3 = False
                right3 = False
                left3 = False
                rivaly -= rivalvel
                Rredraw()
                win.blit(Rstandstill, (rivalx, rivaly))
                win.blit(blackright[1], (120, 350))
                win.blit(walkright[1], (170, 350))
                pygame.display.update()
            win.blit(rivalleft[1], (rivalx, rivaly))
            win.blit(blackright[1], (120, 350))
            win.blit(walkright[1], (170, 350))
            pygame.display.update()
            
            #Rival dialogue scene
            print("Rival: HEY! HEY! YOUR GREATEST PROSPECT HAS FINALLY SHOWED UP!")
            time.sleep(3)
            print("Black: About time you came")
            time.sleep(2)
            print("Black: Well since you were late, you have to pick out of the two pokemon left")
            time.sleep(3)
            print("Rival: ...")
            time.sleep(2)
            print("Rival: Well thats fine by me.. better actually cuz know I'll just take the stronger type!")
            time.sleep(3)
            print("Rival: Since my rival here chose " + pokemonchoice + "...")
            time.sleep(2)
            #pick fire type
            if pokemonchoice == "charmander" or pokemonchoice == "Charmander" or pokemonchoice == "fire" or pokemonchoice == "Fire":
                yourpokemonword.append(str(starterpokemon[0]))
                yourpokemon.append(charmanderback)
                rivalpokemon.append(squirtle2)
                rivalpokemonword.append(str(starterpokemon[2]))
                
            #pick grass type
            elif pokemonchoice == "bulbasaur" or pokemonchoice == "Bulbasaur" or pokemonchoice == "grass" or pokemonchoice == "Grass":
                yourpokemonword.append(str(starterpokemon[1]))
                yourpokemon.append(bulbasaurback)
                rivalpokemon.append(charmander2)
                rivalpokemonword.append(str(starterpokemon[0]))
                
            #pick water type
            elif pokemonchoice == "squirtle" or pokemonchoice == "Squirtle" or pokemonchoice == "water" or pokemonchoice == "Water":
                yourpokemonword.append(str(starterpokemon[2]))
                yourpokemon.append(squirtleback)
                rivalpokemon.append(bulbasaur2)
                rivalpokemonword.appen(str(starterpokemon[1]))
                
            #invalid pick
            else:
                starter = False
                print("Invalid option. Please pick again")
                starter = True
            print("Rival: I'll choose... " + str(rivalpokemonword[0]) + "!")
            time.sleep(2)
            print("Rival: With the type advantage, I'm sure to beat you in battle!")
            time.sleep(2)
            print("Black: Are you ready for your first battle?")
            print("")
            time.sleep(2)
            print("Answer with either a 'yes' or a 'no'")
            b = input()
            if b == "Yes" or b == "yes":
                print("very well. Here we go!!!")
            else:
                print("Well, thats too bad. Can't back out of this one!")
            starter = False
        time.sleep(2.5)

        
        win = pygame.display.set_mode((400, 240))
        changebackground("battle.png")
        pygame.display.update()
        win.blit(rivalpokemon[0], (250, 20))
        win.blit(yourpokemon[0], (50, 80))
        pygame.display.update()

        print("What would you like to do?")
        print("HP - 40/40", "Foe HP - 55/55")

        def options():
            print("A - Battle", "B - Flee", "C - Bag", "D - Party")
        options()
        HP = 40
        FoeHP = 50
        Ember = 10
        squirtlemoveset = ["Water Gun", "Leer", "Water Gun", "Leer"]
        if pokemonchoice == "charmander":
            bchoice = input()
            if bchoice == "a" or bchoice == "A":
                print("Which attack would you like to use?")
                time.sleep(1)
                print("A - Ember", "B - Leer")
                bchoice = input()
                if bchoice == "a" or bchoice == "A":
                    print("")
                    print("It's not very effective")
                    FoeHP = FoeHP - Ember
                    move = random.randint[4]
                    print("The opposing Squirtle used " + str(squirtlemoveset[move]))
                    if move == 1 or move == 3:
                        HP = HP - 23
                        print("It's Super Effective!")
                        time.sleep(1)
                        print("Charmander lost 23 Health Points")
                        print("")
                        time.sleep(1.5)
                        print("HP - " + str(HP) +", Foe HP - " + str(FoeHP))
                    else:
                        print("The opposing Squirtle used " + str(squirtlemoveset[move]))
                elif bchoice == "b" or bchoice == "B":
                    print("")
                    print("The opposing Squirtle's defense harshly fell!")
                    print("")
                    time.sleep(1)
                    #turn 2
                    options()
                    print("")
                    bchoice = input()
            elif bchoice == "":
                print("Your attempt to flee has failed")
                time.sleep(1.5)
                print("As a result, you lose your chance to attack")
                time.sleep(1)
                print("The opposing Squirtle used water gun!")
                time.sleep(1)
                print("It's Super Effective!")
                time.sleep(1)
                print("Charmander lost 23 HP points!")
                time.sleep(1)
            elif bchoice == "":
                print("Which item would you like to use?")
                time.sleep(1)
                print("A - Pokeball")
                bchoice = input()
                if bchoice == "A" or bchoice == "a":
                    print("You cannot catch another trainer's Pokemon!")
                    time.sleep(2)
                    print("As a result of your ridiculous attempt, you lose the chance to attack!")
                    time.sleep(1)
                    print("The opposing squirtle used water gun!")
                    time.sleep(1)
                    print("It's Super Effective!")
                    time.sleep(1)
                    print("Charmander lost 23 HP points!")
            elif bchoice == "":
                print("")

        
            #if a == "W" or a == "w" or a == "water" or a == "Water":
                

        print("Would you like to save your game?")
        save = input()
        if save == "yes" or save == "Yes":
            save = True
    
    
    
    #entering houses
    '''if 490 >= x >= 465 and 150 >= y >= 130:
        pygame.image.load("Laboratory.png")
        win.blit("Laboratory.png", (0, 0))'''
       #changebackground("Laboratory.png")
       #pygame.display.update()

pygame.quit()






































































































































































































