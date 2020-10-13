# Simple-pygame
#Doge against objects and increase your points....!!!!

import pygame
import random
import time

pygame.init()

display_width=800
display_height=600
car_width=73
car_height=100

carIcon=pygame.image.load('racecar.png')

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A racey game')
#pygame.draw.set_icon(carIcon)
clock=pygame.time.Clock()

carImg=pygame.image.load('racecar.png')

black=(0,0,0)
white=(255,255,255)
block_color=(53,115,255)
red=(200,0,0)
green=(0,200,0)
bright_red=(255,0,0)
bright_green=(0,255,0)
blue=(0,0,255)

def quit_game():
     """
    quit_game quits the game
    """ 
    pygame.quit()
    quit()
    
def things_doged(count):
    font=pygame.font.Font(None,25)
    text=font.render("Doged:"+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def things(thingx,thingy,thingw,thingh,color):
    pygame.draw.rect(gameDisplay,color,[thingx,thingy,thingw,thingh])

def text_objects(text,font):
    textSurface=font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText=pygame.font.Font('freesansbold.ttf',115)
    TextSurf,TextRect=text_objects(text,largeText)
    TextRect.center=(display_width/2,display_height/2)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)



def button(message,x,y,w,h,active_color,inactive_color,active=None):
        mouse=pygame.mouse.get_pos()
        click=pygame.mouse.get_pressed()
        print(mouse)
        if x<mouse[0]<x+w and y<mouse[1]<y+h:
            pygame.draw.rect(gameDisplay,active_color,[x,y,w,h])
            if click[0]==1 and active!=None:
                if active=="play":
                    game_loop()
                elif active=="quit":
                    quit_game()
        else:
            pygame.draw.rect(gameDisplay,inactive_color,[x,y,w,h])
        font2=pygame.font.Font('freesansbold.ttf',25)
        textSurface2,textRect2=text_objects(message,font2)
        textRect2.center=(x+(w/2),y+(h/2))
        gameDisplay.blit(textSurface2,textRect2)


def pause():
    font=pygame.font.Font(None,115)
    TextSurface,TextRect=text_objects("Paused",font)
    TextRect.center=(display_width/2,display_height/2)
    gameDisplay.blit(TextSurface,TextRect)

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit_game()

            button("Continue",250,420,100,50,bright_green,green,"play")
            button("Quit",450,420,100,50,bright_red,red,"quit")

            pygame.display.update()
            clock.tick(60)

def crash():
    font=pygame.font.Font(None,115)
    TextSurface,TextRect=text_objects("You Crashed",font)
    TextRect.center=(display_width/2,display_height/2)
    gameDisplay.blit(TextSurface,TextRect)


    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit_game()

            button("Play Again",250,420,100,50,bright_green,green,"play")
            button("Quit",450,420,100,50,bright_red,red,"quit")

            pygame.display.update()
            clock.tick(60)
    

def game_intro():
    intro=True
    while intro:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                quit_game()

        gameDisplay.fill(white)
        font=pygame.font.Font('freesansbold.ttf',115)
        textSurface,textRect=text_objects("A bit Racey",font)
        textRect.center=((display_width/2),(display_height/2))
        gameDisplay.blit(textSurface,textRect)

        button("Go!!",250,420,100,50,bright_green,green,"play")
        button("Quit",450,420,100,50,bright_red,red,"quit")
        pygame.display.update()
        clock.tick(15)

def game_loop():
    x=(display_width*0.45)
    y=(display_height*0.8)
    doged=0
    x_change=0
    crashed=False

######
    thing_startx=random.randrange(0,display_width)
    thing_starty=-600
    thing_speed=7
    thing_width=100
    thing_height=100
######    
    while not crashed:

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                quit_game()

            if event.type==pygame.KEYDOWN:
               ## print(event)
                if event.key==pygame.K_LEFT:
                    x_change=-5-doged
                elif event.key==pygame.K_RIGHT:
                    x_change=5+doged
                elif event.key==pygame.K_p:
                    pause()

            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                    x_change=0
            

        x+=x_change

        gameDisplay.fill(white)
#########
        things(thing_startx,thing_starty,thing_width,thing_height,block_color)
        thing_starty+=thing_speed
        car(x,y)
        things_doged(doged)
#########
        if x>display_width-car_width or x<0:
            crash()
        if thing_starty>display_height:
            doged+=1
            thing_speed+=1
            thing_speed%=13
            thing_width+=(doged*1.2)
            thing_width=thing_width%107
            thing_starty=0-thing_height
            thing_startx=random.randrange(0,display_width)
        
        if y<thing_starty+thing_height:
            print('y crossover')

            if x > thing_startx and x<thing_startx + thing_width or x+car_width > thing_startx and x+car_width<thing_startx+thing_width:
                print('crashed')
                crash()

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__" :
    game_intro()
    game_loop()
    quit_game()
