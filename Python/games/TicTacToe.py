""" Tic tac toe games in python (tutorial follow-up) """

import sys
import pygame


# ----------------------------------------------------------------------------------------------------------------------


class Grid:

    def __init__(self, screen):
        self.screen = screen
        self.line = [
            ((200, 0), (200, 600)),
            ((400, 0), (400, 600)),
            ((0, 200), (600, 200)),
            ((0, 400), (600, 400)),
        ]

        self.grid = [[None for x in range(0, 3)] for y in range(0, 3)]
        self.counter_on = False

    def display(self):
        for line in self.line:
            pygame.draw.line(self.screen, (0, 0, 0), line[0], line[1], 2)

        for y in range(0, len(self.grid)):
            for x in range(0, len(self.grid)):

                # Draw X
                if self.grid[y][x] == 'X':

                    pygame.draw.line(
                        self.screen, (0, 0, 0), (x * 200, y * 200),
                        (200 + (x * 200), 200 + (y * 200)), 3
                    )
                    pygame.draw.line(
                        self.screen, (0, 0, 0), ((x * 200), 200 + (y * 200)),
                        (200 + (x * 200), (y * 200)), 3
                    )

                # Draw O
                elif self.grid[y][x] == 'O':

                    pygame.draw.circle(
                        self.screen, (0, 0, 0), (100 + (x * 200), 100 + (y * 200)), 100, 3
                    )

    def fix_value(self, x, y, value):

        if self.grid[y][x] is None:
            self.grid[y][x] = value
            self.counter_on = True

    def fix_to_none(self, line, column, value):
        self.grid[line][column] = value


# ----------------------------------------------------------------------------------------------------------------------


class Game:

    def __init__(self):

        # Size of screen & title
        self.screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Tic Tac Toe')

        self.game_launched = True
        self.grid = Grid(self.screen)

        self.player_x = 'X'
        self.player_o = 'O'

        self.counter = 0

        self.start_screen = True

    def main_function(self):

        while self.game_launched:

            while self.start_screen:
                for event in pygame.event.get():

                    if event.type == pygame.QUIT:
                        sys.exit()

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            self.start_screen = False

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    sys.exit()

                # Right mouse click
                if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0]:

                    # Mouse position
                    position = pygame.mouse.get_pos()
                    position_x, position_y = position[0] // 200, position[1] // 200

                    if self.counter % 2 == 0:
                        self.grid.fix_value(position_x, position_y, self.player_x)
                    else:
                        self.grid.fix_value(position_x, position_y, self.player_o)

                    if self.grid.counter_on:
                        self.counter += 1
                        self.grid.counter_on = False

                # Keyboard key restart the game
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.restart()

            list_x = []
            list_o = []

            for line in range(0, len(self.grid.grid)):
                for column in range(0, len(self.grid.grid)):

                    if self.grid.grid[line][column] == 'X':
                        x_position = (line, column)
                        list_x.append(x_position)

                    elif self.grid.grid[line][column] == 'O':
                        o_position = (line, column)
                        list_o.append(o_position)

            list_line_x = []
            list_column_x = []

            list_line_o = []
            list_column_o = []

            # X win
            if len(list_x) >= 3:
                for (line, column) in list_x:
                    list_line_x.append(line)
                    list_column_x.append(column)

                if list_line_x.count(0) == 3 or list_line_x.count(1) == 3 or list_line_x.count(2) == 3:
                    return self.player_x

                if list_column_x.count(0) == 3 or list_column_x.count(1) == 3 or list_column_x.count(2) == 3:
                    return self.player_x

                if list_line_x == list_column_x or list_line_x == list_column_x[::-1]:
                    return self.player_x

            # O win
            if len(list_o) >= 3:
                for (line, column) in list_o:
                    list_line_o.append(line)
                    list_column_o.append(column)

                if list_line_o.count(0) == 3 or list_line_o.count(1) == 3 or list_line_o.count(2) == 3:
                    return self.player_o

                if list_column_o.count(0) == 3 or list_column_o.count(1) == 3 or list_column_o.count(2) == 3:
                    return self.player_o

                if list_line_o == list_column_o or list_line_o == list_column_o[::-1]:
                    return self.player_o

            # Screen color
            self.screen.fill((240, 240, 240))
            # Display grid
            self.grid.display()
            # Refresh screen
            pygame.display.flip()

    # Restart game
    def restart(self):
        for line in range(0, len(self.grid.grid)):
            for column in range(0, len(self.grid.grid)):

                self.grid.fix_to_none(line, column, None)


# ----------------------------------------------------------------------------------------------------------------------


if __name__ == '__main__':
    pygame.init()
    Game().main_function()
    pygame.quit()
