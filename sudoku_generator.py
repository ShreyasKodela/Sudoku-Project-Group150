import random, math   # imports random and math to be used throughout the course of the program

class SudokuGenerator:   # Constructor for the SudokuGenerator class
    def __init__(self, row_length, removed_cells):    # init definition function
        self.row_length = row_length
        self.removed_cells = removed_cells   # initializes removes cells

        self.box_length = int(math.sqrt(row_length))
        self.winning_game = []
        self.board = []       # creates an empty list for the sudoku board
        self.selected = False

        for i in range(row_length):
            self.board.append([0] * row_length)

    def get_board(self):    # Returns a 2D python list of numbers
        return self.board    #definition function



    def print_board(self):          # this function prints and displays the board to the console
        for row in self.board:
            for col in row:
                print(col, end=" ")
            print()

    def valid_in_row(self, row, num):         # returns a Boolean value and determines if the num is contained in a given row the board
        for element in range(self.row_length):

            if self.board[row][element] == num:
                return False
        return True



    def valid_in_col(self, col, num):       # returns a Boolean value and determines if the num is contained in a given col the board
        for element in range(self.row_length):
            if self.board[element][col] == num:
                return False
        return True

    def valid_in_box(self, beginning_row, beginning_col, num):      #checks for the num in 3X3 grid to see if it is valid
        for element in range(3):
            for i in range(3):
                if num == self.board[beginning_row + element][beginning_col + i]:
                    return False                                                            #returns the output
        return True

    def is_valid(self, row, col, num):   # returns if it safe to enter a row at a row and column intersection in the board by checking the respective row, column, and box
        beginning_row = (row // 3) * 3
        beginning_col = (col // 3) * 3

        if self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(beginning_row, beginning_col, num):
            return True
        else:
            return False

    def fill_box(self, beginning_row, beginning_col):  # Randomly fills in values in the 3x3 box from the start of the 3x3 to the end. Checks if valid by using valid_in_box def function
        number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]   # a list of all possible board values horizontal and vertically
        quavo = 0
        takeoff = 0

        for element in range(9):
            option = random.choice(number_list)
            if self.is_valid(beginning_row + quavo, beginning_col + takeoff, option):

                number_list.remove(option)
                self.board[beginning_row + quavo][beginning_col + takeoff] = option
                if takeoff != 2:
                    takeoff += 1
                    continue
                else:
                    takeoff = 0
                    quavo += 1

    def fill_diagonal(self):     # fills the three boxes along the main diagonal of the board
        for i in range(3):
            self.fill_box(int(3 * i), int(3 * i))

    def fill_remaining(self, row, col):     # Returns a completely filled board
        if (col >= self.row_length and row < self.row_length - 1):
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):   # The second step for creating a sudoku board

                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0

                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length + 1): #
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    def fill_values(self):     # Calls fill_diagonal and fill_remaining to construct a solution
        self.fill_diagonal()
        self.winning_game = self.board
        self.fill_remaining(0, self.box_length)


    def remove_cells(self):  # Removes 30, 40, or 50 cells from the board
        i = 0

        while i < self.removed_cells:
            goal_cell = [random.randint(0, 8), random.randint(0, 8)]

            if self.board[goal_cell[0]][goal_cell[1]] != 0:
                self.board[goal_cell[0]][goal_cell[1]] = 0
                i += 1

def generate_sudoku(size, removed):   # Generates and returns a sudoku board with a cleared number of cells
        sudoku = SudokuGenerator(size, removed)
        sudoku.fill_values()
        winning_game = []     #list for winning game

        for element in range(len(sudoku.get_board())):
            for num in range(len(sudoku.get_board()[element])):
                winning_game.append(sudoku.get_board()[element][num])
        sudoku.remove_cells()

        puzzle = sudoku.get_board()
        return puzzle, winning_game    #returns puzzle which is an object of sudoku which gets the board and also returns winning_game which is the finalized list