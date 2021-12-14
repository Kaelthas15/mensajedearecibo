import sys
import pygame
import numpy as np
import time
from pygame import mouse
from pygame import *


def paint_button(screen, button, text, colorT, colorF):
    if button.collidepoint(mouse.get_pos()):
        pygame.draw.rect(screen, (colorT), button, 0)
    else:
        pygame.draw.rect(screen, (colorF), button, 0)
    text1 = m1font.render(text, True, (255, 255, 255))
    postx = button.x+(button.width-text1.get_width())/2
    posty = button.y+(button.height-text1.get_height())/2
    screen.blit(text1, (postx, posty))


# empezamos
pygame.init()
# dimesionamos
width, height = 900, 900
size = (900, 900)
# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (25, 25, 25)
# pintamos la pantalla
screen.fill(bg)
# fuente de  letra
m1font = pygame.font.Font(None, 30)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
posb1 = (55*dimcw, 20*dimch)
dimb1 = (12*dimcw, 5*dimch)
# 0=apagado 1=pintado
gameState = np.zeros((nxC, nyC))
ers = Rect(posb1[0], posb1[1], dimb1[0], dimb1[1])

begdecod = Rect(posb1[0], posb1[1]+100, dimb1[0], dimb1[1])

limI = Rect(0, 0, 24*dimcw, height)
limD = Rect(47*dimcw, 0, 27*dimcw, height)
#numbers
rn1 = Rect (24*dimcw,0,1*dimcw,3*dimch)
rn2 = Rect (26*dimcw,0,1*dimcw,3*dimch)
rn3 = Rect (28*dimcw,0,1*dimcw,3*dimch)
rn4 = Rect (30*dimcw,0,1*dimcw,3*dimch)
rn5 = Rect (32*dimcw,0,1*dimcw,3*dimch)
rn6 = Rect (34*dimcw,0,1*dimcw,3*dimch)
rn7 = Rect (36*dimcw,0,1*dimcw,3*dimch)
rn8 = Rect (38*dimcw,0,2*dimcw,3*dimch)
rn9 = Rect (41*dimcw,0,2*dimcw,3*dimch)
rn10 = Rect (44*dimcw,0,2*dimcw,3*dimch)
#Ellements
eln1 = Rect(29*dimcw,5*dimch,2*dimcw,4*dimch)
eln2 = Rect(32*dimcw,5*dimch,2*dimcw,4*dimch)
eln3 = Rect(35*dimcw,5*dimch,2*dimcw,4*dimch)
eln4 = Rect(38*dimcw,5*dimch,2*dimcw,4*dimch)
eln5 = Rect(41*dimcw,5*dimch,2*dimcw,4*dimch)
#Numcleotides
nn11 = Rect(24*dimcw,11*dimch,5*dimcw,3*dimch)
nn12 = Rect(30*dimcw,11*dimch,5*dimcw,3*dimch)
nn13 = Rect(36*dimcw,11*dimch,5*dimcw,3*dimch)
nn14 = Rect(42*dimcw,11*dimch,5*dimcw,3*dimch)

nn21 = Rect(24*dimcw,16*dimch,5*dimcw,3*dimch)
nn24 = Rect(42*dimcw,16*dimch,5*dimcw,3*dimch)

nn31 = Rect(24*dimcw,21*dimch,5*dimcw,3*dimch)
nn32 = Rect(30*dimcw,21*dimch,5*dimcw,3*dimch)
nn33 = Rect(36*dimcw,21*dimch,5*dimcw,3*dimch)
nn34 = Rect(42*dimcw,21*dimch,5*dimcw,3*dimch)

nn41 = Rect(24*dimcw,26*dimch,5*dimcw,3*dimch)
nn44 = Rect(42*dimcw,26*dimch,5*dimcw,3*dimch)
#number of nucleotides
nof = Rect(34*dimcw,26*dimch,2*dimcw,16*dimch)
#beg people
bep = Rect(30*dimcw,46*dimch,9*dimcw,10*dimch)
#hepe
hp = Rect(25*dimcw,50*dimch,4*dimcw,1*dimch)
#ponum
pnu = Rect(41*dimcw,48*dimch,6*dimcw,6*dimch)
#ssol
ssol = Rect(25*dimcw,57*dimch,22*dimcw,4*dimch)
#foa
foa = Rect(25*dimcw,62*dimch,21*dimcw,9*dimch)
#soa
soa = Rect(33*dimcw,71*dimch,6*dimcw,2*dimch)

boolpaint = True

while boolpaint:


    newgameState = np.copy(gameState)

    screen.fill(bg)
   
    ev = pygame.event.get()

    for event in ev:

        if event.type == pygame.QUIT:
            sys.exit()
        mouseclick = pygame.mouse.get_pressed()
        if sum(mouseclick) > 0:
            posx, posy = pygame.mouse.get_pos()
            celx, cely = int(np.floor(posx/dimcw)), int(np.floor(posy/dimch))
            newgameState[celx, cely] = mouseclick[0]
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                newgameState = np.zeros((nxC, nyC))
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if begdecod.collidepoint(mouse.get_pos()):
                boolpaint = False
                #newgameState= np.ones((nxC, nyC))
                
    


    pygame.draw.rect(screen, (128, 128, 128), limI, 0)
    pygame.draw.rect(screen, (128, 128, 128), limD, 0)

    #numbers
    pygame.draw.rect(screen,(255,255,255),rn1,3)
    pygame.draw.rect(screen,(255,255,255),rn2,3)
    pygame.draw.rect(screen,(255,255,255),rn3,3)
    pygame.draw.rect(screen,(255,255,255),rn4,3)
    pygame.draw.rect(screen,(255,255,255),rn5,3)
    pygame.draw.rect(screen,(255,255,255),rn6,3)
    pygame.draw.rect(screen,(255,255,255),rn7,3)
    pygame.draw.rect(screen,(255,255,255),rn8,3)
    pygame.draw.rect(screen,(255,255,255),rn9,3)
    pygame.draw.rect(screen,(255,255,255),rn10,3)
    #Ellements
    pygame.draw.rect(screen,(255,0,255),eln1,3)
    pygame.draw.rect(screen,(255,0,255),eln2,3)
    pygame.draw.rect(screen,(255,0,255),eln3,3)
    pygame.draw.rect(screen,(255,0,255),eln4,3)
    pygame.draw.rect(screen,(255,0,255),eln5,3)
    #nucleotides
    pygame.draw.rect(screen,(0,255,0),nn11,3)
    pygame.draw.rect(screen,(0,255,0),nn12,3)
    pygame.draw.rect(screen,(0,255,0),nn13,3)
    pygame.draw.rect(screen,(0,255,0),nn14,3)

    pygame.draw.rect(screen,(0,255,0),nn21,3)
    pygame.draw.rect(screen,(0,255,0),nn24,3)

    pygame.draw.rect(screen,(0,255,0),nn31,3)
    pygame.draw.rect(screen,(0,255,0),nn32,3)
    pygame.draw.rect(screen,(0,255,0),nn33,3)
    pygame.draw.rect(screen,(0,255,0),nn34,3)

    pygame.draw.rect(screen,(0,255,0),nn41,3)
    pygame.draw.rect(screen,(0,255,0),nn44,3)
    #number of nucleotides 
    pygame.draw.rect(screen,(255,255,0),nof,3)
    #beg people
    pygame.draw.rect(screen,(255,0,0),bep,3)
    #hepe
    pygame.draw.rect(screen,(255,255,255),hp,3)
    #ponum
    pygame.draw.rect(screen,(255,255,255),pnu,3)
    #ssol
    pygame.draw.rect(screen,(255,255,0),ssol,3)
    #foa
    pygame.draw.rect(screen,(255,0,255),foa,3)
    #soa
    pygame.draw.rect(screen,(255,255,255),soa,3)

    #numbers
    for z in range(24,40,2):
        newgameState [z,3]=1
    newgameState[z+3,3]=1
    newgameState[z+6,3]=1
    #Ellements
    newgameState[29,9]=1
    newgameState[32,9]=1
    newgameState[35,9]=1
    newgameState[38,9]=1
    newgameState[41,9]=1
    #Nucleotides
    newgameState[24,14]=1
    newgameState[25,14]=1
    newgameState[26,14]=1
    newgameState[27,14]=1
    newgameState[28,14]=1

    newgameState[30,14]=1
    newgameState[31,14]=1
    newgameState[32,14]=1
    newgameState[33,14]=1
    newgameState[34,14]=1

    newgameState[36,14]=1
    newgameState[37,14]=1
    newgameState[38,14]=1
    newgameState[39,14]=1
    newgameState[40,14]=1

    newgameState[42,14]=1
    newgameState[43,14]=1
    newgameState[44,14]=1
    newgameState[45,14]=1
    newgameState[46,14]=1

    newgameState[24,19]=1
    newgameState[25,19]=1
    newgameState[26,19]=1
    newgameState[27,19]=1
    newgameState[28,19]=1

    newgameState[42,19]=1
    newgameState[43,19]=1
    newgameState[44,19]=1
    newgameState[45,19]=1
    newgameState[46,19]=1

    newgameState[24,24]=1
    newgameState[25,24]=1
    newgameState[26,24]=1
    newgameState[27,24]=1
    newgameState[28,24]=1

    newgameState[30,24]=1
    newgameState[31,24]=1
    newgameState[32,24]=1
    newgameState[33,24]=1
    newgameState[34,24]=1

    newgameState[36,24]=1
    newgameState[37,24]=1
    newgameState[38,24]=1
    newgameState[39,24]=1
    newgameState[40,24]=1

    newgameState[42,24]=1
    newgameState[43,24]=1
    newgameState[44,24]=1
    newgameState[45,24]=1
    newgameState[46,24]=1

    newgameState[24,29]=1
    newgameState[25,29]=1
    newgameState[26,29]=1
    newgameState[27,29]=1
    newgameState[28,29]=1

    newgameState[42,29]=1
    newgameState[43,29]=1
    newgameState[44,29]=1
    newgameState[45,29]=1
    newgameState[46,29]=1
    #number of nucleotides
    newgameState[34,42]=1
    #hepe
    newgameState[24,50]=1
    #ponum
    newgameState[40,48]=1
    #soa
    newgameState[39,72]=1



    for x in range(0, nxC):
        for y in range(0, nyC):
            
                


            poly = [((x) * dimcw, y * dimch),
                    ((x+1) * dimcw, (y) * dimch),
                    ((x+1) * dimcw, (y+1) * dimch),
                    ((x) * dimcw, (y+1) * dimch)]
            # if gameState[x,y]==0:
            #    pygame.draw.polygon(screen,(255,0,0),poly,0)
            if newgameState[x, y] == 0:
                pygame.draw.polygon(screen, (128, 128, 128), poly, 1)
            else:
                if(newgameState[x, y] == 1 and y < 4 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y < 10 and y != 4 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (255, 0, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y > 10 and y < 25 and y != 10 and y != 15 and y != 20 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                elif(newgameState[x, y] == 1 and y > 25 and y < 30 and x > 23 and x <= 33):
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                elif(newgameState[x, y] == 1 and y > 25 and y < 30 and x > 36 and x < 47):
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                elif(newgameState[x, y] == 1 and y > 25 and y < 43 and x > 33 and x <= 36):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y > 30 and y < 46 and x > 23 and x < 47 and x != 34 and x != 35 and x != 36):
                    pygame.draw.polygon(screen, (0, 0, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y == 45 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
                elif(newgameState[x, y] == 1 and y > 45 and x > 29 and x < 39 and y < 56):
                    pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
                elif(newgameState[x, y] == 1 and y > 48 and y < 52 and x > 23 and x < 29):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y > 47 and y < 56 and x > 39 and x < 47):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y > 56 and y < 61 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (255, 255, 0), poly, 0)
                elif(newgameState[x, y] == 1 and y > 61 and y < 71 and x > 24 and x < 46):
                    pygame.draw.polygon(screen, (255, 0, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y == 72 and x > 24 and x < 30):
                    pygame.draw.polygon(screen, (0, 0, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y == 72 and x > 40 and x < 46):
                    pygame.draw.polygon(screen, (0, 0, 255), poly, 0)
                elif(newgameState[x, y] == 1 and y > 70 and y < 73 and x > 30 and x < 40):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                else:
                    pygame.draw.polygon(screen, (128, 128, 128), poly, 0)
    

    # texto del boton 1 borrar
    colorT = (93, 116, 219)
    colorF = (255, 0, 0)
    textb = "Borrar Todo"
    paint_button(screen, ers, textb, colorT, colorF)
    # texto del boton 2 pintar todo
    textb = "Traducir"
    paint_button(screen, begdecod, textb, colorT, colorF)

    # reiniciando las variables
    gameState = np.copy(newgameState)

    pygame.display.flip()
pygame.quit()

booldecodnumb = True


# empezamos
pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
#decod numb
numdecod1=int(gameState[24,2]*1+gameState[24,1]*2+gameState[24,0]*4)
numdecod2 = int(gameState[26,2]*1+gameState[26,1]*2+gameState[26,0]*4)
numdecod3 = int(gameState[28,2]*1+gameState[28,1]*2+gameState[28,0]*4)
numdecod4 = int(gameState[30,2]*1+gameState[30,1]*2+gameState[30,0]*4)
numdecod5 = int(gameState[32,2]*1+gameState[32,1]*2+gameState[32,0]*4)
numdecod6 = int(gameState[34,2]*1+gameState[34,1]*2+gameState[34,0]*4)
numdecod7 = int(gameState[36,2]*1+gameState[36,1]*2+gameState[36,0]*4)
numdecod8 = int(gameState[38,2]*1+gameState[38,1]*2+gameState[38,0]*4+gameState[39,2]*8+gameState[39,1]*16+gameState[39,0]*32)
numdecod9 = int(gameState[41,2]*1+gameState[41,1]*2+gameState[41,0]*4+gameState[42,2]*8+gameState[42,1]*16+gameState[42,0]*32)
numdecod10 = int(gameState[44,2]*1+gameState[44,1]*2+gameState[44,0]*4+gameState[45,2]*8+gameState[45,1]*16+gameState[45,0]*32)
#decod Ellements
elna_1 = int(gameState[29,8]*1+gameState[29,7]*2+gameState[29,6]*4+gameState[29,5]*8+gameState[30,8]*16+gameState[30,7]*32+gameState[30,6]*64+gameState[30,5]*128)
elna_2 = int(gameState[32,8]*1+gameState[32,7]*2+gameState[32,6]*4+gameState[32,5]*8+gameState[33,8]*16+gameState[33,7]*32+gameState[33,6]*64+gameState[33,5]*128)
elna_3 = int(gameState[35,8]*1+gameState[35,7]*2+gameState[35,6]*4+gameState[35,5]*8+gameState[36,8]*16+gameState[36,7]*32+gameState[36,6]*64+gameState[36,5]*128)
elna_4 = int(gameState[38,8]*1+gameState[38,7]*2+gameState[38,6]*4+gameState[38,5]*8+gameState[39,8]*16+gameState[39,7]*32+gameState[39,6]*64+gameState[39,5]*128)
elna_5 = int(gameState[41,8]*1+gameState[41,7]*2+gameState[41,6]*4+gameState[41,5]*8+gameState[42,8]*16+gameState[42,7]*32+gameState[42,6]*64+gameState[42,5]*128)
#decod nucleotides
#el11
el11h = int(gameState[24,13]*1+gameState[24,12]*2+gameState[24,11]*4)
el11c = int(gameState[25,13]*1+gameState[25,12]*2+gameState[25,11]*4)
el11n = int(gameState[26,13]*1+gameState[26,12]*2+gameState[26,11]*4)
el11o = int(gameState[27,13]*1+gameState[27,12]*2+gameState[27,11]*4)
el11p = int(gameState[28,13]*1+gameState[28,12]*2+gameState[28,11]*4)
#el12
el12h = int(gameState[30,13]*1+gameState[30,12]*2+gameState[30,11]*4)
el12c = int(gameState[31,13]*1+gameState[31,12]*2+gameState[31,11]*4)
el12n = int(gameState[32,13]*1+gameState[32,12]*2+gameState[32,11]*4)
el12o = int(gameState[33,13]*1+gameState[33,12]*2+gameState[33,11]*4)
el12p = int(gameState[34,13]*1+gameState[34,12]*2+gameState[34,11]*4 )
#el13
el13h = int(gameState[36,13]*1+gameState[36,12]*2+gameState[36,11]*4)
el13c = int(gameState[37,13]*1+gameState[37,12]*2+gameState[37,11]*4)
el13n = int(gameState[38,13]*1+gameState[38,12]*2+gameState[38,11]*4)
el13o = int(gameState[39,13]*1+gameState[39,12]*2+gameState[39,11]*4)
el13p = int(gameState[40,13]*1+gameState[40,12]*2+gameState[40,11]*4)
#el14
el14h = int(gameState[42,13]*1+gameState[42,12]*2+gameState[42,11]*4)
el14c = int(gameState[43,13]*1+gameState[43,12]*2+gameState[43,11]*4)
el14n = int(gameState[44,13]*1+gameState[44,12]*2+gameState[44,11]*4)
el14o = int(gameState[45,13]*1+gameState[45,12]*2+gameState[45,11]*4)
el14p = int(gameState[46,13]*1+gameState[46,12]*2+gameState[46,11]*4)
#el21
el21h = int(gameState[24,18]*1+gameState[24,17]*2+gameState[24,16]*4)
el21c = int(gameState[25,18]*1+gameState[25,17]*2+gameState[25,16]*4)
el21n = int(gameState[26,18]*1+gameState[26,17]*2+gameState[26,16]*4)
el21o = int(gameState[27,18]*1+gameState[27,17]*2+gameState[27,16]*4)
el21p = int(gameState[28,18]*1+gameState[28,17]*2+gameState[28,16]*4)
#el24
el24h = int(gameState[42,18]*1+gameState[42,17]*2+gameState[42,16]*4)
el24c = int(gameState[43,18]*1+gameState[43,17]*2+gameState[43,16]*4)
el24n = int(gameState[44,18]*1+gameState[44,17]*2+gameState[44,16]*4)
el24o = int(gameState[45,18]*1+gameState[45,17]*2+gameState[45,16]*4)
el24p = int(gameState[46,18]*1+gameState[46,17]*2+gameState[46,16]*4)
#el31
el31h = int(gameState[24,23]*1+gameState[24,22]*2+gameState[24,21]*4)
el31c = int(gameState[25,23]*1+gameState[25,22]*2+gameState[25,21]*4)
el31n = int(gameState[26,23]*1+gameState[26,22]*2+gameState[26,21]*4)
el31o = int(gameState[27,23]*1+gameState[27,22]*2+gameState[27,21]*4)
el31p = int(gameState[28,23]*1+gameState[28,22]*2+gameState[28,21]*4)
#el32 
el32h = int(gameState[30,23]*1+gameState[30,22]*2+gameState[30,21]*4)
el32c = int(gameState[31,23]*1+gameState[31,22]*2+gameState[31,21]*4)
el32n = int(gameState[32,23]*1+gameState[32,22]*2+gameState[32,21]*4 )
el32o = int(gameState[33,23]*1+gameState[33,22]*2+gameState[33,21]*4)
el32p = int(gameState[34,23]*1+gameState[34,22]*2+gameState[34,21]*4 )
#el33
el33h = int(gameState[36,23]*1+gameState[36,22]*2+gameState[36,21]*4)
el33c = int(gameState[37,23]*1+gameState[37,22]*2+gameState[37,21]*4)
el33n = int(gameState[38,23]*1+gameState[38,22]*2+gameState[38,21]*4)
el33o = int(gameState[39,23]*1+gameState[39,22]*2+gameState[39,21]*4)
el33p = int(gameState[40,23]*1+gameState[40,22]*2+gameState[40,21]*4)
#el34
el34h = int(gameState[42,23]*1+gameState[42,22]*2+gameState[42,21]*4)
el34c = int(gameState[43,23]*1+gameState[43,22]*2+gameState[43,21]*4)
el34n = int(gameState[44,23]*1+gameState[44,22]*2+gameState[44,21]*4)
el34o = int(gameState[45,23]*1+gameState[45,22]*2+gameState[45,21]*4)
el34p = int(gameState[46,23]*1+gameState[46,22]*2+gameState[46,21]*4)
#el41
el41h = int(gameState[24,28]*1+gameState[24,27]*2+gameState[24,26]*4)
el41c = int(gameState[25,28]*1+gameState[25,27]*2+gameState[25,26]*4)
el41n = int(gameState[26,28]*1+gameState[26,27]*2+gameState[26,26]*4)
el41o = int(gameState[27,28]*1+gameState[27,27]*2+gameState[27,26]*4)
el41p = int(gameState[28,28]*1+gameState[28,27]*2+gameState[28,26]*4)
#el44
el44h = int(gameState[42,28]*1+gameState[42,27]*2+gameState[42,26]*4)
el44c = int(gameState[43,28]*1+gameState[43,27]*2+gameState[43,26]*4)
el44n = int(gameState[44,28]*1+gameState[44,27]*2+gameState[44,26]*4)
el44o = int(gameState[45,28]*1+gameState[45,27]*2+gameState[45,26]*4)
el44p = int(gameState[46,28]*1+gameState[46,27]*2+gameState[46,26]*4)
#cantnuc
canuc = gameState[34,41]*(2**0)+gameState[34,40]*(2**1)+gameState[34,39]*(2**2)+gameState[34,38]*(2**3)+gameState[34,37]*(2**4)+gameState[34,36]*(2**5)+gameState[34,35]*(2**6)+gameState[34,34]*(2**7)+gameState[34,33]*(2**8)+gameState[34,32]*(2**9)+gameState[34,31]*(2**10)+gameState[34,30]*(2**11)+gameState[34,29]*(2**12)+gameState[34,28]*(2**13)+gameState[34,27]*(2**14)+gameState[34,26]*(2**15)+gameState[35,41]*(2**16)+gameState[35,40]*(2**17)+gameState[35,39]*(2**18)+gameState[35,38]*(2**19)+gameState[35,37]*(2**20)+gameState[35,36]*(2**21)+gameState[35,35]*(2**22)+gameState[35,34]*(2**23)+gameState[35,33]*(2**24)+gameState[35,32]*(2**25)+gameState[35,31]*(2**26)+gameState[35,30]*(2**27)+gameState[35,29]*(2**28)+gameState[35,28]*(2**29)+gameState[35,27]*(2**30)+gameState[35,26]*(2**31)
#soper
soper = (gameState[25,50]*1+gameState[26,50]*2+gameState[27,50]*4+gameState[28,50]*8)*126
#capob
capobl = gameState[41,48]*(2**0) + gameState[42,48]*(2**1) + gameState[43,48]*(2**2) + gameState[44,48]*(2**3) + gameState[45,48]*(2**4) + gameState[46,48]*(2**5) + gameState[41,49]*(2**6) + gameState[42,49]*(2**7) + gameState[43,49]*(2**8)+gameState[44,49]*(2**9)+gameState[45,49]*(2**10)+gameState[46,49]*(2**11)+gameState[41,50]*(2**12)+gameState[42,50]*(2**13)+gameState[43,50]*(2**14)+gameState[44,50]*(2**15)+gameState[45,50]*(2**16)+gameState[46,50]*(2**17)+gameState[41,51]*(2**18)+gameState[42,51]*(2**19)+gameState[43,51]*(2**20)+gameState[44,51]*(2**21)+gameState[45,51]*(2**22)+gameState[46,51]*(2**23)+gameState[41,52]*(2**24)+gameState[42,52]*(2**25)+gameState[43,52]*(2**26)+gameState[44,52]*(2**27)+gameState[45,52]*(2**28)+gameState[46,52]*(2**29)+gameState[41,53]*(2**30)+gameState[42,53]*(2**31)+gameState[43,53]*(2**32)+gameState[44,53]*(2**33)+gameState[45,53]*(2**34)+gameState[46,53]*(2**35)
#soa
soadec = gameState[38,72]*(2**0) + gameState[37,72]*(2**1)+ gameState[36,72]*(2**2)+gameState[35,72]*(2**3)+gameState[34,72]*(2**4)+gameState[33,72]*(2**5)+gameState[38,71]*(2**6)+gameState[37,71]*(2**7)+gameState[36,71]*(2**8)+gameState[35,71]*(2**9)+gameState[34,71]*(2**10)+gameState[33,71]*(2**11)
soadec = (soadec*126)/1000

#rect numbers
recnumsup= Rect(0,0,width,19*dimch)
recnumizq = Rect(0,19*dimch,10*dimcw,height)
recnumder= Rect(60*dimcw,19*dimch,27*dimcw,height)
recnuminf = Rect(0,50*dimch,width,height)
bordercolor = (46, 21, 103)
m1font = pygame.font.Font(None, 22)


textnumb = "El sistema de numeración que maneja en decimal es: " + str(numdecod1) + ", " + str(numdecod2) + ", " + str(numdecod3) + ", " + str(numdecod4) + ", " + str(numdecod5) + ", " + str(numdecod6) + ", " + str(numdecod7) + ", " + str(numdecod8) + ", " + str(numdecod9) + ", " + str(numdecod10) + ", "
text1 = m1font.render(textnumb, True, (0,0,0))


ers = Rect(int(width/2.5),55*dimch,200,100)


while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y+25) * dimch),
                    ((x+1) * dimcw, (y+25) * dimch),
                    ((x+1) * dimcw, (y+1+25) * dimch),
                    ((x) * dimcw, (y+1+25) * dimch)]
            
            if(newgameState[x, y] == 1 and y < 4 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((12*dimcw),(35*dimch)))    


    
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)            
        
    pygame.display.flip()
pygame.quit()


booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="Los números atómicos de los que estan compuestos son : "+ str(elna_1)+", "+ str(elna_2)+", "+ str(elna_3)+", "+ str(elna_4)+", "+ str(elna_5)
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y+20) * dimch),
                    ((x+1) * dimcw, (y+20) * dimch),
                    ((x+1) * dimcw, (y+1+20) * dimch),
                    ((x) * dimcw, (y+1+20) * dimch)]
            
            if(newgameState[x, y] == 1 and y < 10 and y != 4 and x > 23 and x < 47 and y>4):
                    pygame.draw.polygon(screen, (255, 0, 255), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((12*dimcw),(35*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()



booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textcom1 = "Las formulas de los compuestos de la primera filas son: "+"H"+ str(el11h)+" C"+str(el11c)+" N"+str(el11n)+" O"+str(el11o)+" P"+str(el11p)
textcom2 = "Las formulas de los compuestos de la primera filas son: "+"H"+ str(el12h)+" C"+str(el12c)+" N"+str(el12n)+" O"+str(el12o)+" P"+str(el12p)
textcom3 = "Las formulas de los compuestos de la primera filas son: "+"H"+ str(el13h)+" C"+str(el13c)+" N"+str(el13n)+" O"+str(el13o)+" P"+str(el13p)
textcom4 = "Las formulas de los compuestos de la primera filas son: "+"H"+ str(el14h)+" C"+str(el14c)+" N"+str(el14n)+" O"+str(el14o)+" P"+str(el14p)
text1 = m1font.render(textcom1, True, (0,0,0))
text2 = m1font.render(textcom2, True, (0,0,0))
text3 = m1font.render(textcom3, True, (0,0,0))
text4 = m1font.render(textcom4, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y+10) * dimch),
                    ((x+1) * dimcw, (y+10) * dimch),
                    ((x+1) * dimcw, (y+1+10) * dimch),
                    ((x) * dimcw, (y+1+10) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 10 and y < 15 and y != 10 and y != 15 and y != 20 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((12*dimcw),(35*dimch)))   
    screen.blit(text2, ((12*dimcw),(37*dimch)))  
    screen.blit(text3, ((12*dimcw),(39*dimch)))  
    screen.blit(text4, ((12*dimcw),(41*dimch)))   

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()



booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textcom1 = "Las formulas de los compuestos de la segunda filas son: "+"H"+ str(el21h)+" C"+str(el21c)+" N"+str(el21n)+" O"+str(el21o)+" P"+str(el21p)
textcom2 = "Las formulas de los compuestos de la segunda filas son: "+"H"+ str(el24h)+" C"+str(el24c)+" N"+str(el24n)+" O"+str(el24o)+" P"+str(el24p)

text1 = m1font.render(textcom1, True, (0,0,0))
text2 = m1font.render(textcom2, True, (0,0,0))


while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y+10) * dimch),
                    ((x+1) * dimcw, (y+10) * dimch),
                    ((x+1) * dimcw, (y+1+10) * dimch),
                    ((x) * dimcw, (y+1+10) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 15 and y < 20 and y != 10 and y != 15 and y != 20 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((12*dimcw),(35*dimch)))   
    screen.blit(text2, ((12*dimcw),(37*dimch)))  
 

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()

booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textcom1 = "Las formulas de los compuestos de la tercera filas son: "+"H"+ str(el31h)+" C"+str(el31c)+" N"+str(el31n)+" O"+str(el31o)+" P"+str(el31p)
textcom2 = "Las formulas de los compuestos de la tercera filas son: "+"H"+ str(el32h)+" C"+str(el32c)+" N"+str(el32n)+" O"+str(el32o)+" P"+str(el32p)
textcom3 = "Las formulas de los compuestos de la tercera filas son: "+"H"+ str(el33h)+" C"+str(el33c)+" N"+str(el33n)+" O"+str(el33o)+" P"+str(el33p)
textcom4 = "Las formulas de los compuestos de la tercera filas son: "+"H"+ str(el34h)+" C"+str(el34c)+" N"+str(el34n)+" O"+str(el34o)+" P"+str(el34p)
text1 = m1font.render(textcom1, True, (0,0,0))
text2 = m1font.render(textcom2, True, (0,0,0))
text3 = m1font.render(textcom3, True, (0,0,0))
text4 = m1font.render(textcom4, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y+5) * dimch),
                    ((x+1) * dimcw, (y+5) * dimch),
                    ((x+1) * dimcw, (y+1+5) * dimch),
                    ((x) * dimcw, (y+1+5) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 20 and y < 25 and y != 10 and y != 15 and y != 20 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((12*dimcw),(35*dimch)))   
    screen.blit(text2, ((12*dimcw),(37*dimch)))  
    screen.blit(text3, ((12*dimcw),(39*dimch)))  
    screen.blit(text4, ((12*dimcw),(41*dimch)))   

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()

booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textcom1 = "Las formulas de los compuestos de la cuarta filas son: "+"H"+ str(el41h)+" C"+str(el41c)+" N"+str(el41n)+" O"+str(el41o)+" P"+str(el41p)
textcom2 = "Las formulas de los compuestos de la cuarta filas son: "+"H"+ str(el44h)+" C"+str(el44c)+" N"+str(el44n)+" O"+str(el44o)+" P"+str(el44p)

text1 = m1font.render(textcom1, True, (0,0,0))
text2 = m1font.render(textcom2, True, (0,0,0))


while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y) * dimch),
                    ((x+1) * dimcw, (y) * dimch),
                    ((x+1) * dimcw, (y+1) * dimch),
                    ((x) * dimcw, (y+1) * dimch)]
            if(newgameState[x, y] == 1 and y > 25 and y < 30 and x > 23 and x <= 33):
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
            if(newgameState[x, y] == 1 and y > 25 and y < 30 and x > 36 and x < 47):
                    pygame.draw.polygon(screen, (0, 255, 0), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((12*dimcw),(35*dimch)))   
    screen.blit(text2, ((12*dimcw),(37*dimch)))  
 

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()
booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="La cantidad de numeros de nucleotidos es : "+ str(canuc)
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y-5) * dimch),
                    ((x+1) * dimcw, (y-5) * dimch),
                    ((x+1) * dimcw, (y+1-5) * dimch),
                    ((x) * dimcw, (y+1-5) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 25 and y < 43 and x > 33 and x <= 36):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((17*dimcw),(40*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()

booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="Asi se ve una representacion del ADN "
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y-10) * dimch),
                    ((x+1) * dimcw, (y-10) * dimch),
                    ((x+1) * dimcw, (y+1-10) * dimch),
                    ((x) * dimcw, (y+1-10) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 30 and y < 46 and x > 23 and x < 47 and x != 34 and x != 35 and x != 36):
                    pygame.draw.polygon(screen, (0, 0, 255), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((17*dimcw),(40*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()

booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="Asi se ve una representacion de la persona o ente "
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y-20) * dimch),
                    ((x+1) * dimcw, (y-20) * dimch),
                    ((x+1) * dimcw, (y+1-20) * dimch),
                    ((x) * dimcw, (y+1-20) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 45 and x > 29 and x < 39 and y < 56):
                    pygame.draw.polygon(screen, (255, 0, 0), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((17*dimcw),(40*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()

booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="La estatura de la persona o ente es: "+str(soper)+" cm"
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x+10) * dimcw, (y-20) * dimch),
                    ((x+1+10) * dimcw, (y-20) * dimch),
                    ((x+1+10) * dimcw, (y+1-20) * dimch),
                    ((x+10) * dimcw, (y+1-20) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 48 and y < 52 and x > 23 and x < 29):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((17*dimcw),(40*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()

booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="La población actual es de: "+str(capobl)+" personas o entes"
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x-10) * dimcw, (y-20) * dimch),
                    ((x+1-10) * dimcw, (y-20) * dimch),
                    ((x+1-10) * dimcw, (y+1-20) * dimch),
                    ((x-10) * dimcw, (y+1-20) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 47 and y < 56 and x > 39 and x < 47):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((17*dimcw),(40*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()

booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="Así se ve una representacion del sistema solar donde el resaltado es donde viven"
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y-30) * dimch),
                    ((x+1) * dimcw, (y-30) * dimch),
                    ((x+1) * dimcw, (y+1-30) * dimch),
                    ((x) * dimcw, (y+1-30) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 56 and y < 61 and x > 23 and x < 47):
                    pygame.draw.polygon(screen, (255, 255, 0), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((11*dimcw),(40*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()


booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="Así se ve una representacion de la antena donde se recibe este mensaje"
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y-40) * dimch),
                    ((x+1) * dimcw, (y-40) * dimch),
                    ((x+1) * dimcw, (y+1-40) * dimch),
                    ((x) * dimcw, (y+1-40) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 61 and y < 71 and x > 24 and x < 46):
                    pygame.draw.polygon(screen, (255, 0, 255), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((12*dimcw),(40*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()

booldecodnumb = True


pygame.init()

# dimesionamos
width, height = 900, 900
size = (900, 900)

# creamos la pantalla
screen = pygame.display.set_mode(size)
# color de la pantalla
bg = (125, 206, 160)

# pintamos la pantalla
screen.fill(bg)
nxC, nyC = 73, 73
dimcw = width/nxC
dimch = height/nyC
m1font = pygame.font.Font(None, 22)
textnuma="El diámetro de la antena es de: "+str(soadec)+" m"
text1 = m1font.render(textnuma, True, (0,0,0))

while booldecodnumb:
    screen.fill(bg)
    ev = pygame.event.get()
    for event in ev:
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if ers.collidepoint(mouse.get_pos()):
                booldecodnumb = False
                #newgameState= np.ones((nxC, nyC))
    for x in range(0, nxC):
        for y in range(0, nyC):

            poly = [((x) * dimcw, (y-40) * dimch),
                    ((x+1) * dimcw, (y-40) * dimch),
                    ((x+1) * dimcw, (y+1-40) * dimch),
                    ((x) * dimcw, (y+1-40) * dimch)]
            
            if(newgameState[x, y] == 1 and y > 70 and y < 73 and x > 30 and x < 40):
                    pygame.draw.polygon(screen, (255, 255, 255), poly, 0)
                    pygame.draw.polygon(screen, (0,0,0), poly, 1)
    pygame.draw.rect(screen, (bordercolor),recnumsup)   
    pygame.draw.rect(screen, (bordercolor),recnumder)
    pygame.draw.rect(screen, (bordercolor),recnumizq)
    pygame.draw.rect(screen, (bordercolor),recnuminf)
    screen.blit(text1, ((12*dimcw),(40*dimch)))    

          
    textb = "Siguiente"
    paint_button(screen, ers, textb, colorT, colorF)     
    pygame.display.flip()
pygame.quit()