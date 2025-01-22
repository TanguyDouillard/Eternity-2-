import pygame
from pygame.locals import *
from sys import exit
from random import randint
import math
import os

###############################################################
def inArea(gX,gY,pointX, pointY,pointX2, pointY2):
    if pointX<gX<pointX2 and pointY<gY<pointY2:
        return True
    else:
        return False

def inCircle(pointX, pointY,gX,gY,distance):
    xDist = pointX-gX
    xDist=math.fabs(xDist)
    yDist = pointY-gY
    yDist=math.fabs(yDist)
    xyDist = (xDist*xDist)+(yDist*yDist)
    if distance >= math.sqrt(xyDist):
        return True
    else:
        return False
############################################################

imagestring= ""
endstring= ""
secendstring=""
scene=0
keyonce=1
text=""
blink=0
caps=0
imageOn=0
col=0
row=0
hit=-1
offsetX=0
offsetY=0
pix = 1




clock=pygame.time.Clock()
pygame.mixer.init(44100, 16, 2, 4096)
pygame.init()


screen = pygame.display.set_mode((960,640), 0, 32)
pygame.display.set_caption('JigSaw Puzzle Maker')

icon = pygame.image.load("icon32.png").convert_alpha()
pygame.display.set_icon(icon)

#pygame.scrap.init()

font1= pygame.font.Font("etobicoke.ttf",16)

bg= pygame.image.load("bg.png").convert()
MAIN= pygame.image.load("MAIN.png").convert()

gray= pygame.image.load("gray.png").convert()

bas= pygame.image.load("bas.png").convert()

p= pygame.image.load("sp50.png").convert_alpha()

look= pygame.image.load("look.png").convert()
returnx= pygame.image.load("return.png").convert()

WELLDONE = pygame.image.load("WELLDONE.png").convert()


green = pygame.image.load("green.png").convert_alpha()

snip = pygame.mixer.Sound("SNIP1.ogg")
bambam = pygame.mixer.Sound("bambam.ogg")


b1= pygame.image.load("baseimages/sr1.png").convert()
b2= pygame.image.load("baseimages/wh.png").convert()
b3= pygame.image.load("baseimages/jw1.png").convert()
b4= pygame.image.load("baseimages/jw2.png").convert()
b5= pygame.image.load("baseimages/sr2.png").convert()
b6= pygame.image.load("baseimages/bub.png").convert()
b7= pygame.image.load("baseimages/doa1.png").convert()
b8= pygame.image.load("baseimages/gun.png").convert()
b9= pygame.image.load("baseimages/rh.png").convert()
b10 = pygame.image.load("baseimages/bl.png").convert()
b11 = pygame.image.load("baseimages/elk.png").convert()
b12 = pygame.image.load("baseimages/tor.png").convert()
b13 = pygame.image.load("baseimages/bldr.png").convert()
b14 = pygame.image.load("baseimages/val2.png").convert()
b15 = pygame.image.load("baseimages/elv.png").convert()
b16 = pygame.image.load("baseimages/cat.png").convert()
b17 = pygame.image.load("baseimages/mars.png").convert()
b18 = pygame.image.load("baseimages/rum.png").convert()
b19 = pygame.image.load("baseimages/cab.png").convert()
b20 = pygame.image.load("baseimages/three.png").convert()

d_list=[]
e_list=[]

class PP():
    def piece(self, img,col,row,x,y,s):
        self.img=img
        self.col=col
        self.row=row
        self.x=x
        self.y=y
        self.s=s

for i in range(13):
    for ii in range(10):
        b=PP()
        b.piece(pygame.image.load("bas.png").convert(),i,ii,0,0,0)
        d_list.append(b)
 

text = font1.render(imagestring, True, (0,0,0))
text2 = font1.render("Load failed", True, (255,0,0))
textF = font1.render("Open the folder 'yourimage'", True, (0,0,0))
textE = font1.render("Drop the image in the folder.", True, (0,0,0))
textP = font1.render("Enter the name of the file with the keyboard below.", True, (0,0,0))
textL = font1.render("Click the Load button.", True, (0,0,0))
textLB = font1.render("LOAD", True, (255,255,255))
textME = font1.render("MAIN    EXIT", True, (255,255,255))


while True:

    mx, my = pygame.mouse.get_pos()
    timePassed = clock.tick(30)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


        elif scene==0:   ## main
            if event.type==MOUSEBUTTONDOWN:
                if inArea(mx,my,55, 257, 178, 325):
                    scene=1
                elif inArea(mx,my,82, 342, 142, 421):
                    os.startfile('README.txt')

                elif inArea(mx,my,471, 589, 504, 620):
                    pix -= 1
                    if pix<1:
                        pix=20

                elif inArea(mx,my,660, 589, 691, 620):
                    pix += 1
                    if pix>20:
                        pix=1

                elif inArea(mx,my,541, 590, 626, 617):
                    if pix==1:
                        puzzelbase = b1
                    elif pix==2:
                        puzzelbase = b2
                    elif pix==3:
                        puzzelbase = b3
                    elif pix==4:
                        puzzelbase = b4
                    elif pix==5:
                        puzzelbase = b5
                    elif pix==6:
                        puzzelbase = b6
                    elif pix==7:
                        puzzelbase = b7
                    elif pix==8:
                        puzzelbase = b8
                    elif pix==9:
                        puzzelbase = b9
                    elif pix==10:
                        puzzelbase = b10
                    elif pix==11:
                        puzzelbase = b11
                    elif pix==12:
                        puzzelbase = b12
                    elif pix==13:
                        puzzelbase = b13
                    elif pix==14:
                        puzzelbase = b14
                    elif pix==15:
                        puzzelbase = b15
                    elif pix==16:
                        puzzelbase = b16
                    elif pix==17:
                        puzzelbase = b17
                    elif pix==18:
                        puzzelbase = b18
                    elif pix==19:
                        puzzelbase = b19
                    elif pix==20:
                        puzzelbase = b20
                    

                    imageOn=1
                    scene=2
                        


            

            
                    

        elif scene==1:   ## Load own
            if event.type==MOUSEBUTTONDOWN:
                imageOn=0
                
                
                if inArea(mx,my,580, 22, 682, 88):
                    os.startfile('yourimage')

                elif inArea(mx,my,436, 433, 529, 577):
                    os.startfile('README.txt')
                

                elif inArea(mx,my,41, 471, 128, 501):
                    scene=0
                    
                elif inArea(mx,my,41, 520, 120, 550):
                    pygame.quit()
                    exit()
                    
                elif inArea(mx,my,247, 210, 284, 242):
                    imagestring += "1"
                    
                elif inArea(mx,my,289, 210, 325, 242):
                    imagestring += "2"  
                elif inArea(mx,my,332, 210, 365, 242):
                    imagestring += "3"                
                elif inArea(mx,my,373, 210, 407, 242):
                    imagestring += "4"                  
                elif inArea(mx,my,414, 210, 449, 242):
                    imagestring += "5"                
                elif inArea(mx,my,456, 210, 490, 242):
                    imagestring += "6"                 
                elif inArea(mx,my,498, 210, 531, 242):
                    imagestring += "7"                 
                elif inArea(mx,my,539, 210, 574, 242):
                    imagestring += "8"                 
                elif inArea(mx,my,582, 210, 615, 242):
                    imagestring += "9"                 
                elif inArea(mx,my,622, 210, 656, 242):
                    imagestring += "0" 
                

                elif inArea(mx,my,665, 210, 698, 242):
                    secstring=imagestring
                    imagestring=""
                    i=0
                    while i< len(secstring)-1:
                        imagestring += secstring[i]
                        i +=1
                                       
                elif inArea(mx,my,707, 210, 740, 242):  ##clear
                    imagestring = ""
                    endstring = ""

                elif inArea(mx,my,247, 250, 284, 282):
                    if caps==1:
                        imagestring += "Q"
                    else:
                        imagestring += "q"
                elif inArea(mx,my,289, 250, 325, 282):
                    if caps==1:
                        imagestring += "W"
                    else:
                        imagestring += "w"  
                elif inArea(mx,my,332, 250, 365, 282):
                    if caps==1:
                        imagestring += "E"
                    else:
                        imagestring += "e"                
                elif inArea(mx,my,373, 250, 407, 282):
                    if caps==1:
                        imagestring += "R"
                    else:
                        imagestring += "r"                  
                elif inArea(mx,my,414, 250, 449, 282):
                    if caps==1:
                        imagestring += "T"
                    else:
                        imagestring += "t"                
                elif inArea(mx,my,456, 250, 490, 282):
                    if caps==1:
                        imagestring += "Y"
                    else:
                        imagestring += "y"                 
                elif inArea(mx,my,498, 250, 531, 282):
                    if caps==1:
                        imagestring += "U"
                    else:
                        imagestring += "u"                 
                elif inArea(mx,my,539, 250, 574, 282):
                    if caps==1:
                        imagestring += "I"
                    else:
                        imagestring += "i"                 
                elif inArea(mx,my,582, 250, 615, 282):
                    if caps==1:
                        imagestring += "O"
                    else:
                        imagestring += "o"                 
                elif inArea(mx,my,622, 250, 656, 282):
                    if caps==1:
                        imagestring += "P"
                    else:
                        imagestring += "p"


                elif inArea(mx,my,247, 290, 284, 320):
                    if caps==1:
                        imagestring += "A"
                    else:
                        imagestring += "a"
                elif inArea(mx,my,289, 290, 325, 320):
                    if caps==1:
                        imagestring += "S"
                    else:
                        imagestring += "s"
                        
                elif inArea(mx,my,332, 290, 365, 320):
                    if caps==1:
                        imagestring += "D"
                    else:
                        imagestring += "d"                
                elif inArea(mx,my,373, 290, 407, 320):
                    if caps==1:
                        imagestring += "F"
                    else:
                        imagestring += "f"                  
                elif inArea(mx,my,414, 290, 449, 320):
                    if caps==1:
                        imagestring += "G"
                    else:
                        imagestring += "g"                
                elif inArea(mx,my,456, 290, 490, 320):
                    if caps==1:
                        imagestring += "H"
                    else:
                        imagestring += "h"                 
                elif inArea(mx,my,498, 290, 531, 320):
                    if caps==1:
                        imagestring += "J"
                    else:
                        imagestring += "j"                 
                elif inArea(mx,my,539, 290, 574, 320):
                    if caps==1:
                        imagestring += "K"
                    else:
                        imagestring += "k"                 
                elif inArea(mx,my,582, 290, 615, 320):
                    if caps==1:
                        imagestring += "L"
                    else:
                        imagestring += "l"                 


                elif inArea(mx,my,247, 328, 284, 360):
                    if caps==1:
                        imagestring += "Z"
                    else:
                        imagestring += "z"
                elif inArea(mx,my,289, 328, 325, 360):
                    if caps==1:
                        imagestring += "X"
                    else:
                        imagestring += "x"  
                elif inArea(mx,my,332, 328, 365, 360):
                    if caps==1:
                        imagestring += "C"
                    else:
                        imagestring += "c"                
                elif inArea(mx,my,373, 328, 407, 360):
                    if caps==1:
                        imagestring += "V"
                    else:
                        imagestring += "v"                  
                elif inArea(mx,my,414, 328, 449, 360):
                    if caps==1:
                        imagestring += "B"
                    else:
                        imagestring += "b"                
                elif inArea(mx,my,456, 328, 490, 360):
                    if caps==1:
                        imagestring += "N"
                    else:
                        imagestring += "n"                 
                elif inArea(mx,my,498, 328, 531, 360):
                    if caps==1:
                        imagestring += "M"
                    else:
                        imagestring += "m"                 
                elif inArea(mx,my,539, 328, 574, 360):
                    imagestring += "."
                    
                elif inArea(mx,my,582, 328, 615, 360):
                    imagestring += "_"

                elif inArea(mx,my,665, 328, 740, 360):
                    imagestring += " "


                elif inArea(mx,my,707, 250, 740, 280):
                    if caps==0:
                        caps=1
                    else:
                        caps=0



                elif inArea(mx,my,665, 291, 698, 321):   ## move cursor left
                    secstring=imagestring
                    secendstring=endstring
                    imagestring=""
                    i=0
                    ii=0
                    while i< len(secstring)-1:
                        imagestring += secstring[i]
                        i +=1
                    if len(imagestring)>0:    
                        endstring=secstring[len(secstring)-1]
                        endstring += secendstring


                elif inArea(mx,my,706, 291, 740, 321):   ## move cursor right
                    secendstring=endstring
                    if len(endstring)>0: 
                        imagestring += endstring[0]
                        endstring=""
                        i=1
                        while i< len(secendstring):
                            endstring += secendstring[i]
                            i +=1


                        


                elif inArea(mx,my,253, 148, 298, 192):  ## load

                    e_list *= 0
                    for i in range(130):
                        d_list[i].s=0
                    
                    try:
                        puzzelbase = pygame.image.load("yourimage/" + imagestring.strip() + endstring.strip()).convert()
                       
                        imageOn=1
                        scene=2
                        
                    except:
                        imageOn=2

                    



                
            

        elif scene==3:    ##   laying puzzle
            if event.type==MOUSEBUTTONDOWN:

                if inArea(mx,my,0, 568,120, 640):
                    scene=5
                
                for i in range((row*col)-1,-1,-1):
                    if 0<(mx-d_list[i].x)<50 and 0<(my-d_list[i].y)<50:
                        hit=i
                        offsetX=mx-d_list[i].x
                        offsetY=my-d_list[i].y
                        break


                if inArea(mx,my,145, 615, 177, 627):
                    e_list *= 0  #.clear()
                    for i in range(130):
                        d_list[i].s=0
                    scene=0
                        
                if inArea(mx,my,192, 616, 222, 627):
                    pygame.quit()
                    exit()


              
            if event.type==MOUSEBUTTONUP:
                hit=-1



                

        elif scene==4:   ##  finished
            if event.type==MOUSEBUTTONDOWN:
                if inArea(mx,my,827, 83, 896, 105):
                    e_list *= 0  #.clear()
                    for i in range(130):
                        d_list[i].s=0
                    scene=0

                if inArea(mx,my,833, 121, 895, 144):
                    pygame.quit()
                    exit()
                    
                
        elif scene==5:   ##  look
            if event.type==MOUSEBUTTONDOWN:
                if inArea(mx,my,0, 568,120, 640):
                    scene=3


###################################################################

    if scene==0:   ## main
        screen.blit(MAIN,(0,0))


        if pix==1:
            screen.blit(b1,(300,65))
        elif pix==2:
            screen.blit(b2,(300,65))
        elif pix==3:
            screen.blit(b3,(300,65))
        elif pix==4:
            screen.blit(b4,(300,65))
        elif pix==5:
            screen.blit(b5,(248,207))
        elif pix==6:
            screen.blit(b6,(300,65))
        elif pix==7:
            screen.blit(b7,(300,65))
        elif pix==8:
            screen.blit(b8,(360,65))
        elif pix==9:
            screen.blit(b9,(330,65))
        elif pix==10:
            screen.blit(b10,(300,65))
        elif pix==11:
            screen.blit(b11,(300,65))
        elif pix==12:
            screen.blit(b12,(300,65))
        elif pix==13:
            screen.blit(b13,(252,207))
        elif pix==14:
            screen.blit(b14,(300,65))
        elif pix==15:
            screen.blit(b15,(300,65))
        elif pix==16:
            screen.blit(b16,(300,65))
        elif pix==17:
            screen.blit(b17,(360,100))
        elif pix==18:
            screen.blit(b18,(275,167))
        elif pix==19:
            screen.blit(b19,(300,65))
        elif pix==20:
            screen.blit(b20,(390,35))
                    

    elif scene==1:   ##  enter load

        blink+=1
        text = font1.render(imagestring + " " + endstring, True, (0,0,0))
        if blink>14:
            text = font1.render(imagestring + '|' + endstring, True, (0,0,0))
        if blink>29:
            blink=0

        
        screen.blit(bg,(0,0))
        if caps==1:
            screen.blit(green,(753, 255))
        screen.blit(text, [376, 175])
            
        if imageOn==2:
            screen.blit(text2, [376, 150])

        screen.blit(textL, [376, 125])
        screen.blit(textP, [376, 100])
        screen.blit(textE, [376, 75])
        screen.blit(textF, [376, 50])
        screen.blit(textLB, [260, 166])


            


    elif scene==2:   ## setup play



        col= int((puzzelbase.get_width()-12)/50)
        row= int((puzzelbase.get_height()-12)/50)

        if col>13:
            col=13

        if row>10:
            row=10



        for i in range(col):
            for ii in range(row):
                d_list[(ii*col)+i].img.blit(puzzelbase,(-i*50,-ii*50))
                d_list[(ii*col)+i].img.blit(p,(0,0))
                d_list[(ii*col)+i].img.set_colorkey((255,0,255))
                d_list[(ii*col)+i].col=i
                d_list[(ii*col)+i].row=ii

                d_list[(ii*col)+i].x=randint(700, 860)
                d_list[(ii*col)+i].y=randint(20, 570)
                d_list[(ii*col)+i].s=1



        scene=3  ## play




    elif scene==3:   ###

        if hit>-1:
            d_list[hit].x = mx - offsetX
            d_list[hit].y = my - offsetY

        for i in range(col*row):
            if inCircle(d_list[i].x, d_list[i].y, d_list[i].col*50+20, d_list[i].row*50+20, 10) and hit==-1 and d_list[i].s==1:
                d_list[i].s=0
                e_list.append(d_list[i])
                channel=snip.play(0)
                break
            
        screen.blit(gray,(0,0))

        for i in range(col):
            for ii in range(row):
                screen.blit(bas,(i*50 + 20,ii*50 + 20))


        for i in range(len(e_list)):
            screen.blit(e_list[i].img,(e_list[i].col*50 + 20, e_list[i].row*50 + 20))

        for i in range(col):
            for ii in range(row):
                if d_list[(ii*col)+i].s==1:
                    screen.blit(d_list[(ii*col)+i].img,(d_list[(ii*col)+i].x,d_list[(ii*col)+i].y))

        screen.blit(look,(0,568))

        screen.blit(textME, (145, 615))

        if len(e_list) == row*col:
            channel=bambam.play(0)
            scene=4

    elif scene==4:   ### win
        screen.blit(gray,(0,0))
        screen.blit(puzzelbase, (20, 20))
        screen.blit(WELLDONE, (686, 0))

    elif scene==5:   ### look
        screen.blit(gray,(0,0))
        screen.blit(puzzelbase, (20, 20))
        screen.blit(returnx,(0,568))

            
    #screen.blit(font1.render(str(len(e_list)) + ":" + str(q), True, (255,0,0)), [300, 600])
    pygame.display.update()
