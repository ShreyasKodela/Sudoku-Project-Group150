import pygame

class Cell:  #
    def __init__(self, value, row, col, screen): #initializes variables that we will use
        self.value = value
        self.sketch_value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketch_value = value

    def set_cell_value(self, value):        #this is a setter for the cell value
        self.value = value

    def set_sketched_value(self, value):        # this is a setter for sketched value
        self.sketch_value = value

    def draw(self, statement=False):   # Draws the cell with the value inside it, outlines the currently selected cell in red.

        if statement:
            self.square = pygame.draw.rect(self.screen, (255, 0, 0), [self.row * 50, self.col * 50, 50, 50], 5)
        else:
            self.square = pygame.draw.rect(self.screen, (255, 255, 255), [self.row * 50, self.col * 50, 50, 50], 1)

        desired_font = pygame.font.SysFont('Times New Roman', 32) #sets the font for the whole system and is used in the below code
        fortnite = desired_font.render(str(self.value), False, (255, 255, 255))
        if self.value != 0:
            self.screen.blit(fortnite, (self.square.x + 15, self.square.y + 5))

        if self.sketch_value != self.value:
            cod = desired_font.render(str(self.sketch_value), False, (122, 118, 116))
            self.screen.blit(cod, (self.square.x + 15, self.square.y + 5))


    def return_row_and_col(self):
        return (self.row, self.col)

    def return_value(self):         #is a getter for return_value
        return self.value

    def return_sketch(self):            #is a getter for sketch_value
        return self.sketch_value
