# tela incial etc
import pygame

class Game:
    def __init__(self):
        self.window = None

    def run(self, ):
        print('Setup Started')
        pygame.init()
        window = pygame.display.set_mode(size=(600, 480))
        print('Setup Started')

        print('Loop Started')
        while True:
            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Quitting')
                    pygame.quit()  # Close Window
                    quit()  # end pygame
