import pygame
import random
import math

#myhang 1204

def distance(p1,p2):
    return  math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

pygame.init()

screen = pygame.display.set_mode((1200,700))

pygame.display.set_caption('Kmeans project')

clock = pygame.time.Clock()




#Colours
BACKGROUND = (214,214,214)
YELLOW = (249,255,230)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
VIOLET = (138,43,226)
BROWN = (210,105,30)
ORANGE = (255,140,0)

COLOR = [RED, BLUE, GREEN, VIOLET, BROWN, ORANGE]

#Font
font = pygame.font.SysFont('sans', 40)
Smallfont = pygame.font.SysFont('sans', 10)

fontPlus = font.render('+', True, WHITE)
fontMinus = font.render('-', True, WHITE)
fontRun = font.render('Run', True, WHITE)
fontRandom = font.render('Random', True, WHITE)
fontAlgorithm = font.render('Algorithm', True, WHITE)
fontReset = font.render('Reset', True, WHITE)

K = 0
Error = 0
points = []
clusters = []
labels = []


running = True
while running:
    clock.tick(60)
    
    #Dặt sai vị trí nên nó không nhận
    [mouse_x,mouse_y] = pygame.mouse.get_pos()

    #Draw interface
    screen.fill(BACKGROUND)
    #Draw pannel
    
    pygame.draw.rect(screen,BLACK, [50,50,700,500])
    pygame.draw.rect(screen,YELLOW, [50+5,50+5,700-10,500-10])


    #Draw button
    #K +
    pygame.draw.rect(screen,BLACK, [800,50,50,50])
    screen.blit(fontPlus, (815, 50))
    #K -
    pygame.draw.rect(screen,BLACK, [900,50,50,50])
    screen.blit(fontMinus, (920, 50))

    #Random
    pygame.draw.rect(screen,BLACK, [800,150,150,50])
    screen.blit(fontRandom, (813, 150))

    #Run
    pygame.draw.rect(screen,BLACK, [800,250,150,50])
    screen.blit(fontRun, (840, 250))

    #Algorithm
    pygame.draw.rect(screen,BLACK, [800,450,200,50])
    screen.blit(fontAlgorithm, (830, 450))

    #Reset
    pygame.draw.rect(screen,BLACK, [800,550,150,50])
    screen.blit(fontReset, (835, 550))

    #K
    fontK = font.render('K = ' + str(K), True, BLACK)
    screen.blit(fontK, (1000, 50))
    #Error
    fontError = font.render('Error = ' + str(Error), True, BLACK)
    screen.blit(fontError, (815, 350))

    #Create position of mouse in panel
    if (50<mouse_x<700) and (50<mouse_y<500):
        Mousefont = Smallfont.render('('+str(mouse_x-50)+","+str(mouse_y-50)+")", True, BLACK)
        screen.blit(Mousefont, (mouse_x+10, mouse_y))

    #End draw interface


    

    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN:

            #Create points in panel
            if (50<mouse_x<750) and (50<mouse_y<550):
                point = [mouse_x-50,mouse_y-50]
                points.append(point)
                print(points)
                # labels.append(point)
                # min = 9999999
                # for j in range(len(clusters)):
                #     d = math.sqrt((points[i][0]-clusters[j][0])**2 + (points[i][1]-clusters[j][1])**2)
                #     if (d<min):
                #         min = d
                #         labels[len(points)]=j
                #         print(labels)
                #         print("j = ",j)



            #K+
            if (800<mouse_x<850) and (50<mouse_y<100):
                K +=1
                if(K>6):
                    print("Max K = 6")
                    K-=1

            #K-
            if (900<mouse_x<950) and (50<mouse_y<100):
                K -=1
                if (K<1):
                    print("Min K = 1")
                    K+=1

            #Ranđom
            if (800<mouse_x<950) and (150<mouse_y<200):
                clusters = []
                for i in range(K):
                    pos_x = random.randint(50,700)
                    pos_y = random.randint(50,500)
                    p = [pos_x,pos_y]
                    clusters.append(p)
                    print(clusters)

                print("Press Random")
            #Run
            if (800<mouse_x<950) and (250<mouse_y<300):
                labels = [0]*len(points)
                for i in range(len(points)):
                    min = 999999
                    for j in range(len(clusters)):
                        d = math.sqrt((points[i][0]-clusters[j][0])**2 + (points[i][1]-clusters[j][1])**2)
                        if (d<min):
                            min = d
                            labels[i]=j
                


          


                # for i in range(len(labels)):
                #     pygame.draw.circle(screen,COLOR[labels[i]], [points[i][0]+50,points[i][1]+50],5)

            #Algorithm
            if (800<mouse_x<1000) and (450<mouse_y<500):
                print("Press Algorithm")

            #Reset
            if (800<mouse_x<950) and (550<mouse_y<600):
                print("Press Reset")
            
    for i in range(len(points)):
        pygame.draw.circle(screen,BLACK, [points[i][0]+50,points[i][1]+50],7) #Sai dimension vì lấy từ 0 chứ không phải từ 1
        pygame.draw.circle(screen,YELLOW, [points[i][0]+50,points[i][1]+50],5)

    for i in range(len(clusters)):
        pygame.draw.circle(screen,COLOR[i], [clusters[i][0],clusters[i][1]],10) #Sai dimension vì lấy từ 0 chứ không phải từ 1

    for i in range(len(labels)):
        pygame.draw.circle(screen,COLOR[labels[i]], [points[i][0]+50,points[i][1]+50],5)
        


        for j in range(len(clusters)):
            if labels[i] == 


        

    pygame.display.flip() # thiếu dấu ()




pygame.quit()