# Program to draw a line using Direct use of line equation algorithim
"""
    A class used to represent a line and draw it using Direct use of line equation algorithm.

    ...

    Attributes
    ----------
    x1 : int
        x-coordinate of the starting point of the line
    x2 : int
        x-coordinate of the ending point of the line
    y1 : int
        y-coordinate of the starting point of the line
    y2 : int
        y-coordinate of the ending point of the line

    Methods
    -------
    draw_line():
        Draws the line using Direct use of line equation algorithm.
"""

import pygame
import sys

import pygame
import sys

class Lineslop:


    def __init__(self, x1, x2, y1, y2):
        """
        Parameters
        ----------
        x1 : int
            x-coordinate of the starting point of the line
        x2 : int
            x-coordinate of the ending point of the line
        y1 : int
            y-coordinate of the starting point of the line
        y2 : int
            y-coordinate of the ending point of the line
        """
        self.x1, self.y1 = x1, y1
        self.x2, self.y2 = x2, y2
       
    def draw_line(self):
        """
        Draws the line using Direct use of line equation algorithm.
        """
        pygame.init()
        width, height = 800,600
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Line Slope")

        dx, dy = abs(self.x2 - self.x1), abs(self.y2 - self.y1)
        gradient = dy / dx if dx != 0 else float('inf') # avoids division by zero

        x,y = self.x1, self.y1
        xend = self.x2

        pygame.draw.circle(screen, (255, 0, 0), (x, y), 1)

        while x <= xend:
            pygame.display.flip()
            pygame.time.delay(100)
            x += 1
            y = round(gradient * (x - self.x1) + self.y1)
            pygame.draw.circle(screen, (255, 0, 0), (x, y), 1)


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        pygame.quit()

if __name__ == '__main__':
    try:
        x1, y1 = map(int, input("Enter the first point: ").replace(",", " ").split())
        x2, y2 = map(int, input("Enter the second point: ").replace(",", " ").split())
    except ValueError:
        print("Error: Invalid input")
        sys.exit()
    


    Lineslop = Lineslop(x1, x2, y1, y2)
    Lineslop.draw_line()
