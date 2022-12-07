from sudoku_generator import generate_sudoku
from cell import Cell
import pygame


class Board:    # Constructtor for the Board class and creates a variable, mode, for the difficulty of the sudoku board
    def __init__(self, width, height, screen, mode):        #initilizes for this class function similar to what we did in the other classes
        self.width = width
        self.height = height
        self.screen = screen
        self.selected_cell = None


        if mode == 1:           #mode is easy
            self.removed_cells = 30                 #removes 30 cells
        elif mode == 2:     #mode is medium
            self.removed_cells = 40                 #removes 40 cells
        else:              #mode is automatically considered hard
            self.removed_cells = 50             #removes 50 cells


        self.board, self.solved_board = generate_sudoku(9, self.removed_cells)


        self.board_list = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board_list.append(Cell(self.board[i][j], i, j, self.screen))



    def draw(self):         #is the function used to draw the outline of the Sudoku grid and a line to delineate the 3x3 boxes
        self.screen.fill((72, 72, 72))
        image = pygame.image.load('assets/reddit.png')      #this is the image we used in the GUI, it is named reddit becasue that is where we got the image from
        image = pygame.transform.scale(image, (self.width, self.height))
        self.screen.blit(image, (-50,0))


        for i in range(1, 3):
             pygame.draw.line(self.screen, (255, 255, 255), (0, i * 150),(450, i * 150), 5)
        for j in range(1, 3):
             pygame.draw.line(self.screen,(255, 255, 255),(j * 150, 0),(j * 150, 450), 5)

        font_button = pygame.font.SysFont('Times New Roman', 30)        #font for button

        resetButtonText = font_button.render("Reset", False, (64, 255, 25))
        resetButton = pygame.draw.rect(self.screen, (0, 0, 0), [35, 485, 110, 70], 5)
        self.screen.blit(resetButtonText, (resetButton.x + 18, resetButton.y + 12.5))

        restartButtonText = font_button.render("Restart", False, (255, 255, 25))
        restartButton = pygame.draw.rect(self.screen, (0, 0, 0), [172.5, 485, 110, 70], 5)    # placings for boxes and buttons
        self.screen.blit(restartButtonText, (restartButton.x + 10, restartButton.y + 12.5))

        exitButtonText = font_button.render("Exit", False, (255, 25, 25))
        exitButton = pygame.draw.rect(self.screen, (0, 0, 0), [310.5, 485, 110, 70], 5)
        self.screen.blit(exitButtonText, (exitButton.x + 30, exitButton.y + 12.5))


        for cell in self.board_list:
            cell.draw()
        if self.selected_cell != None:
            self.selected_cell.draw(True)


    def select(self, row, col):  #Marks the cell at the row column intersection for the current selection, allows editing of that cell
        try:
            self.selected_cell = self.board_list[(row * 9) + col]
        except IndexError:
            return None

    def click(self, x, y):  # returns a tuple of the row and column if applicable in the displayed board.
        if x <= 450 and y <= 450:
            return (x // 50, y // 50)


    def clear(self):   # Clears the cell value
        if self.selected_cell.return_value() != self.selected_cell.return_sketch():
            self.selected_cell.set_sketched_value(0)


    def sketch(self, value):    # Sets the sketched value to the current selected cell equal to user entered value, displayed at top left using draw() function.
        if self.selected_cell.return_value() == 0:
            self.selected_cell.set_sketched_value(value)


    def place_number(self):    # sets the current selected cell to the user input
        if self.selected_cell.return_value() != self.selected_cell.return_sketch():
            self.selected_cell.set_cell_value(self.selected_cell.return_sketch())


    def reset_to_original(self):    # Resets all cells on the sudoku board to their original values
        self.board_list = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                self.board_list.append(Cell(self.board[i][j], i, j, self.screen))
        self.selected_cell = None
        self.draw()
        self.selected_cell = self.board_list[45]

    def is_full(self):   # Returns a Boolean value indicating whether the board is full or not
        for cell in self.board_list:
            if cell.return_value() == 0:
                return False
        return True

    def find_empty(self):   # Finds an empty cell amd returns its row and col as a tuple
        return self.selected_cell.return_row_and_col()


    def check_board(self):   # checks whether the board is solved correctly or not and if it is solved correctly returns True otherwise it returns False
        user_nums = [cell.return_value() for cell in self.board_list]
        if user_nums == self.solved_board:
            return True
        else:
            return False



