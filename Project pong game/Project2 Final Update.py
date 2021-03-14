# images in this game are copyrighted by Lucas Films and Disney
import pygame
import random
pygame.init()
SCR_WID, SCR_HEI = 640, 480
screen = pygame.display.set_mode((SCR_WID, SCR_HEI))
pygame.mixer.init()
#sound fx
bouncefx = pygame.mixer.Sound("blip.wav")
bouncefx2 = pygame.mixer.Sound("coin.wav")
#background music
pygame.mixer.music.load("chillout.mp3")
pygame.mixer.music.play(-1)
#adding color
Red = (255,0,0)
Green = (0,255,0)
Blue = (0,0,255)
color_list = [Red, Green, Blue]

class Player1():
    def __init__(self):
        self.x, self.y = 16, SCR_HEI/2
        self.speed = 3
        self.padWid, self.padHei = 8, 64
        self.score = 0
        self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
               
    def scoring(self):
        scoreBlit = self.scoreFont.render(str(self.score), 1, (0, 255, 0))
        screen.blit(scoreBlit, (32, 20))
        if self.score == 20:
                print("Player 1 Wins!")
                exit()

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
                self.y -= self.speed
        elif keys[pygame.K_s]:
                self.y += self.speed
               
        if self.y <= 0:
                self.y = 0
        elif self.y >= SCR_HEI-64:
                self.y = SCR_HEI-64
               
    def draw(self):
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.padWid, self.padHei))
         
class Player2():
    def __init__(self):
        self.x, self.y = SCR_WID-16, SCR_HEI/2
        self.speed = 3 
        self.padWid, self.padHei = 8, 64
        self.score = 0
        self.scoreFont = pygame.font.Font("imagine_font.ttf", 64)
               
    def scoring(self):
        scoreBlit = self.scoreFont.render(str(self.score), 1, (0, 255, 0))
        screen.blit(scoreBlit, (SCR_HEI+92, 20))
        if self.score == 20:
                print("Player 2 Wins!")
                exit()

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
                self.y -= self.speed
        elif keys[pygame.K_DOWN]:
                self.y += self.speed
               
        if self.y <= 0:
                self.y = 0
        elif self.y >= SCR_HEI-64:
                self.y = SCR_HEI-64
               
    def draw(self):
                pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, self.padWid, self.padHei))


class Ball():
        #random ball spawn
        def __init__(self):
            self.x = random.randrange(SCR_WID)
            self.y = random.randrange(SCR_HEI)
            self.speed_x = -2
            self.speed_y = 2
            self.size = 3  
                
        def movement(self):
            self.x += self.speed_x
            self.y += self.speed_y                
            #wall col

            if self.y <= 0:
                    self.speed_y *= -1
                    if player1.score + player2.score >=5:
                        bouncefx.play()
                    else:
                        bouncefx2.play()
            elif self.y >= SCR_HEI-self.size:
                self.speed_y *= -1
                                 
            if self.x <= 0:
                self.__init__()
                player2.score += 1
                if player1.score + player2.score >=5:
                    bouncefx.play()
                else:
                    bouncefx2.play()
            elif self.x >= SCR_WID-self.size:
                self.__init__()
                self.speed_x = 3
                player1.score += 1
           
                
                       
            ##wall col      
            #paddle col
            #player
            for n in range(-self.size, player1.padHei):
                    if self.y == player1.y + n:
                            if self.x <= player1.x + player1.padWid:
                                    self.speed_x *= -1
                                    if player1.score + player2.score >=5:
                                        bouncefx.play()
                                    else:
                                        bouncefx2.play()
                                    break
                    n += 1
            #player2
            for n in range(-self.size, player2.padHei):
                    if self.y == player2.y + n:
                            if self.x >= player2.x - player2.padWid:
                                    self.speed_x *= -1
                                    if player1.score + player2.score >=5:
                                        bouncefx.play()
                                    else:
                                        bouncefx2.play()

                                    break
                    n += 1
            
                
                ##paddle col
                #ball color change after score of 10 
        def draw(self):
                pygame.draw.rect(screen, (0,0,255), (self.x, self.y, 8, 8))
                if player1.score >=10:
                    pygame.draw.rect(screen, (random.choice(color_list)), (self.x, self.y, 8, 8))
                    

                #second ball
class Ball2():
        
        def __init__(self):
            self.x = random.randrange(SCR_WID)
            self.y = random.randrange(SCR_HEI)
            self.speed_x = -2
            self.speed_y = 2
            self.size = 3  
                
        def movement(self):
            self.x += self.speed_x
            self.y += self.speed_y                
            #wall col

            if self.y <= 0:
                    self.speed_y *= -1
                    if player1.score + player2.score >=5:
                        bouncefx.play()
                        
                    else:
                        bouncefx2.play()
            elif self.y >= SCR_HEI-self.size:
                self.speed_y *= -1
                                 
            if self.x <= 0:
                self.__init__()
                player2.score += 1
                if player1.score + player2.score >=5:
                    bouncefx.play()
                    
                else:
                    bouncefx2.play()
            elif self.x >= SCR_WID-self.size:
                self.__init__()
                self.speed_x = 3
                player1.score += 1
                       
                
                       
            ##wall col      
            #paddle col
            #player
            for n in range(-self.size, player1.padHei):
                    if self.y == player1.y + n:
                            if self.x <= player1.x + player1.padWid:
                                    self.speed_x *= -1
                                    #sound change after score of 5
                                    if player1.score + player2.score >=5:
                                        bouncefx.play()
                                    else:
                                        bouncefx2.play()
                                    break
                    n += 1
            #player2
            for n in range(-self.size, player2.padHei):
                    if self.y == player2.y + n:
                            if self.x >= player2.x - player2.padWid:
                                    self.speed_x *= -1
                                    #sound change after score of 5
                                    if player1.score + player2.score >=5:
                                        bouncefx.play()
                                        
                                    else:
                                        bouncefx2.play()

                                    break
                    n += 1
          
                
                ##paddle col
                #ball color change after score of 10 
        def draw(self):
                pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, 8, 8))
                if player2.score >=10:
                    pygame.draw.rect(screen, (random.choice(color_list)), (self.x, self.y, 8, 8))
                        
SCR_WID, SCR_HEI = 640, 480

pygame.display.set_caption("Pong")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60

#player = Player()
player1 = Player1() 
ball = Ball()
player2 = Player2()
ball2 = Ball2()
def Main():
    while True:
            #process
            for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                    print ("Game exited by user")
                                    exit()
                            #background change after score of 5    
                            if player1.score + player2.score >=5:
                                background_image = pygame.image.load("pongbackground2.jpg").convert()
                            else:
                                background_image = pygame.image.load("pongbackground.jpg").convert()                                   
                                


            ##process
            #logic
            ball.movement()
            player1.movement()
            player2.movement()
            ball2.movement()
            ##logic
            #draw
            screen.blit(background_image, [0,0])
            ball.draw()
            ball2.draw()
            player1.draw()
            player1.scoring()
            player2.draw()
            player2.scoring()
            
            ##draw
            #_______
            pygame.display.flip()
            clock.tick(FPS)

Main()


