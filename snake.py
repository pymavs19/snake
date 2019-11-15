from pygame.locals import *
from random import randint
import pygame
import time

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
 
    # def update(self):

    # def change_direction(self, dir):

    # def draw(self, surface, image):
 
 
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
        #self.game = Game()
        self.player = Player(3) 
        #self.apple = Apple(5,5)
 
    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
 
        pygame.display.set_caption('SNAKE!')
        self._running = True
        self._image_surf = pygame.image.load("snake.png").convert()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        #self.player.update()
 
        # does snake eat apple?
        # if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
        #     self.player.length = self.player.length + 1
 
 
        # does snake collide with itself?
        # for i in range(2,self.player.length):
        #     if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
        #         print("You lose! Collision: ")
        #         exit(0)
 
        pass
 
    def on_render(self):
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        #self.apple.draw(self._display_surf, self._apple_surf)
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
 
            self.on_loop()
            self.on_render()
 
            time.sleep (50.0 / 1000.0)
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()