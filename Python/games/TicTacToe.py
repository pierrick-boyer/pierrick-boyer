""" Tic tac toe games in python (tutorial follow-up) """

import sys
import pygame


# Method that draws the grid on the screen
class Grid:

    def __init__(self, screen):
        self.screen = screen
        self.lines = [
            ((200, 0), (200, 600)),
            ((400, 0), (400, 600)),
            ((0, 200), (600, 200)),
            ((0, 400), (600, 400)),
        ]

    def display(self):
        for lines in self.lines:
            pygame.draw.line(self.screen, (0, 0, 0), lines[0], lines[1], 2)


class Game:

    def __init__(self):

        # Size of screen & title
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Tic Tac Toe')

        self.games_launched = True
        self.gate = Grid(self.screen)

    def main_function(self):
        while self.games_launched:

            for events in pygame.event.get():

                # User clicks the window's "X" button or when the system 'asks' for the process to quit
                if events.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((240, 240, 240))
            self.gate.display()

            # update screen
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    Game().main_function()
    pygame.quit()
