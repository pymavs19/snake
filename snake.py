from pygame.locals import *
from random import randint
import pygame
import time

class Apple:
    x = 0
    y = 0
    step = 44

    def __init__(self,x,y):
        self.x = x*self.step
        self.y = y*self.step

    def draw(self, surface, image):
        surface.blit(image, (self.x, self.y))

class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 3
 
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length):
       self.length = length
       for i in range(0,2000):
           self.x.append(-100)
           self.y.append(-100)
 
       # initial positions, no collision.
       self.x[1] = 1*44
       self.x[2] = 2*44
 
    def update(self):
        self.updateCount += 1
        if self.updateCount > self.updateCountMax:
            for i in range(self.length - 1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            d = self.direction

            if d == 0: #right
                self.x[0] += self.step

            elif d == 1: #left
                self.x[0] -= self.step

            elif d == 2: #up
                self.y[0] += self.step

            elif d == 3: #down
                self.y[0] -= self.step

            self.updateCount = 0

    def change_direction(self, dir):
        self.direction = dir

    def draw(self, surface, image):
        for i in range(self.length):
            surface.blit(image, (self.x[i], self.y[i]))
 
class Detector:
    def isCollision(self,x1,y1,x2,y2):
        return x1==x2 and y1==y2

    def isOut(self,x,y,xlimit,ylimit):
        return x < 0 or x > xlimit or y < 0 or y > ylimit

class App:
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
 
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.detector = Detector()
        self.player = Player(3) 
        self.apple = Apple(5,5)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('SNAKE!')
        self._running = True
        self._image_surf = pygame.image.load("snake.png").convert()
        self._apple_surf = pygame.image.load("apple.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()
 
        # does snake eat apple?
        if self.detector.isCollision(self.apple.x,self.apple.y,self.player.x[0], self.player.y[0]):
            self.player.length = self.player.length + 1
            self.apple.x = randint(0,9)*44
            self.apple.y = randint(0,9)*44
 
        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.detector.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i]):
                print("You lose! Collision!")
                exit(0)

        #does the snake go off bounds?
        x = self.player.x[0]
        y = self.player.y[0]
        if self.detector.isOut(x,y,self.windowWidth,self.windowHeight):
            print("You lose! Off bounds!")
            exit(0)

        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 

            if (keys[K_ESCAPE]):
                self._running = False

            if(keys[K_RIGHT]):
                self.player.change_direction(0)
            if(keys[K_LEFT]):
                self.player.change_direction(1)
            if(keys[K_DOWN]):
                self.player.change_direction(2)
            if(keys[K_UP]):
                self.player.change_direction(3)
 
            self.on_loop()
            self.on_render()
 
            time.sleep (50.0 / 1000.0)
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()