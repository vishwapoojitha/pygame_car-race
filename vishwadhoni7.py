import pygame #the main library
import time
import random

pygame.init() #initialising pygame

#variables are good than assigning constant values each time
#crash_sound = pygame.mixer.Sound("crash.wav")
display_width= 800
display_height= 600
blue = (0,0,200)
black = (0,0,0)
white = (255,255,255)
red=(200,0,0)
green=(0,200,0)
bright_red=(255,0,0)
pause=True
bright_green=(0,255,0)
car_width=73
car_speed =0 #no use till now
gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('My_first_game')
clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png.jpg')
gameIcon = pygame.image.load('carIcon.png')
Highscore = 0
dodged=0

pygame.display.set_icon(gameIcon)

#functions
def paused():

    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.mixer.music.pause()

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        button("Continue",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
def unpause():
    pygame.mixer.music.unpause()
    game_loop()
def quitgame():
    pygame.quit()
    quit()
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    click = pygame.mouse.get_pressed()
    #print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac,(x,y,w,h))
        if click[0]==1 and action !=None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    gameDisplay.blit(textSurf, textRect)
def things_dodged(count):
    font=pygame.font.SysFont(None,25)
    text= font.render("Dodged: "+str(count), True , black)
    gameDisplay.blit(text, (0,0))
def things_Highscore(count):
    font=pygame.font.SysFont(None,25)
    text= font.render("Highscore: "+str(count), True , black)
    gameDisplay.blit(text, (0,25))
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
def car(x,y) :
    gameDisplay.blit(carImg, (x,y))
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
def crash():
    message_display('You Crashed')
    #pygame.mixer.Sound.play(crash_sound)
    pygame.mixer.music.stop()
    time.sleep(2)
    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)


        button("Play Again",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.SysFont('comicsansms',115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
def game_loop():
    global Highscore
    #pygame.mixer.music.load('jazz.wav')
    #pygame.mixer.music.play(-1)
    x =  (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    thing_startx= random.randrange(0,display_width)
    thing_starty= -600
    thing_speed= 7
    thing_width= 100
    thing_height= 100
    dodged=0
    gameExit= False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                quit()
                #instead of gameExit = True
                #and print(event)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -20
                elif event.key == pygame.K_RIGHT:
                    x_change = 20
                elif event.key == pygame.K_UP :
                    y_change = -10
                elif event.key == pygame.K_DOWN :
                    y_change = 10
                if event.key == pygame.K_p:
                    pause = True #not working if pause isn't a global variable
                    paused()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN :
                    y_change = 0

        if Highscore < dodged :
            Highscore = dodged
        x=x+x_change
        y=y+y_change
        gameDisplay.fill(white)
        #print Highscore
        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed
        things_dodged(dodged)
        things_Highscore(Highscore)
        car(x,y)
        if x>display_width-car_width or x<0 :
            crash()
        if thing_starty>display_height:
            thing_starty=0-thing_height
            thing_startx= random.randrange(0,display_width)
            dodged +=1
            thing_speed +=1
            thing_width += (dodged*1.01)
        if y<thing_starty+thing_height:
            #print('y crossover')
            if x>thing_startx and x<thing_startx+thing_width or x+car_width>thing_startx and x+car_width<thing_startx+thing_width:
                #print('x crossover')
                crash()
        pygame.display.update()
        clock.tick(60)
game_intro()
game_loop()
pygame.quit()
quit()