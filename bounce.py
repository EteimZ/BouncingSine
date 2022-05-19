import pygame
import math

pygame.init()

# color
BLACK = (0,0,0)
WHITE = (255,255,255)

SPEED = 50

class Bounce:
    
    def __init__(self, w=800, h=500):
        # height and width
        self.w = w
        self.h = h

        # define ball parameters
        self.centerY = self.h * .5
        self.centerX = self.w * .5
        self.angle = 0

        # init display
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Bouncing Sine')
        self.clock = pygame.time.Clock()

    
    def animate(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        self.bounce()
        self.clock.tick(SPEED)
    
    
    def bounce(self):
        offset = self.h * .4

        y = self.centerY + math.sin(self.angle) * offset

        self.display.fill(WHITE)

        pygame.draw.circle(self.display, BLACK, (self.centerX, y), 50 )

        self.angle += 0.1

        pygame.display.flip()    


if __name__ == '__main__':

    ball = Bounce()

    while True:
        ball.animate()
    
    pygame.quit()
