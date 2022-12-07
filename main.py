from board import Board
import pygame           #imports

def main():

    image = 0
    pygame.init()
    height, width = 450, 600
    game = pygame.display.set_mode((height, width))
    backgroundColor = (72, 72, 72)
    boardimage = pygame.image.load('assets/background.png')    # allows for a imported png to be loaded onto the menu
    boardimage = pygame.transform.scale(boardimage,(width * 1.5, height * 1.5))
    mainboardimage = pygame.image.load('assets/emptyboard.png')      # sets png to sudoku background
    title_font = pygame.font.SysFont('Times New Roman', 50)
    button_font = pygame.font.SysFont('Times New Roman', 20)
    cell_font = pygame.font.SysFont('Times New Roman', 25)    # cell font and size
    pygame_icon = pygame.image.load('assets/uf.png') #sets the favicon in the pygame window
    pygame.display.set_icon(pygame_icon)
    pygame.display.set_caption('Sudoku') #sets the title in the pygame window
    x, y = 113, 230 #used for GUI to position all elements throughout the program for user appearance
    winner = False


    while True:
        cursor_spot = pygame.mouse.get_pos() #uses cursor_spot for interpretation throughout program

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if image == 0:
                game.blit(boardimage, (0, 0))
                pygame.draw.rect(game, (255, 255, 255), [130.5, 155, 180, 60])
                title = title_font.render("Sudoku", True, (0, 0, 0))
                game.blit(title, (142.5, 155))  # above 4 lines are for what sudoku looks like in the main screen

                pygame.draw.rect(game, (64, 255, 25), [148, 315, 140, 40])
                easyText = button_font.render("Easy Mode", True, (0, 0, 0))
                game.blit(easyText, (172.5, 325)) # above 4 lines are for what easy mode looks like in the main screen

                pygame.draw.rect(game, (255, 255, 25), [148, 365, 140, 40])
                mediumText = button_font.render("Medium Mode", True, (0, 0, 0))
                game.blit(mediumText, (157.5, 375))  # above 4 lines are for what medium mode looks like in the main screen

                pygame.draw.rect(game, (255, 25, 25), [148, 415, 140, 40])
                hardText = button_font.render("Hard Mode", True, (0, 0, 0))
                game.blit(hardText, (172.5, 425))  # above 4 lines are for what hard mode looks like in the main screen

            if image == 1:
                row_choice, column_choice = board.find_empty() # if image choice is 1 then runs board.find_empty()

            if image == 2:
                if board.check_board():
                    winner = True   # Prompts the user with the winning screen
                    game.blit(mainboardimage, (0, 0))
                    button = pygame.draw.rect(game, (50, 168, 82), [160, 225, 140, 40])
                    exitText = button_font.render("Exit", True, (255, 255, 255)) # sets exit to black text
                    title = title_font.render("Fantastic!", True, (255, 255, 255)) # sets fantastic to black text
                    game.blit(exitText, (210, 235)) # formats exit into place
                    game.blit(title, (140, 100)) # formats title into place
                elif not board.check_board():
                    winner = False     # Prompts the user with the losing screen and choice to restart
                    game.blit(mainboardimage, (0, 0))
                    game.fill(backgroundColor)
                    button = pygame.draw.rect(game, (50, 168, 82), [150, 225, 140, 40])
                    restartText = button_font.render("Restart", True, (255, 255, 255))      # restart button
                    title = title_font.render("Game Over!", True, (0, 0, 0))            # game over button
                    game.blit(restartText, (190, 235)) # formats restart into place
                    game.blit(title, (100, 100)) # formats title into place

            if event.type == pygame.MOUSEBUTTONDOWN:     #cursor code for position
                cursor_spot = pygame.mouse.get_pos()
                x, y = event.pos

                if image == 0: # sets all the button spaces into place so that when clicked with cursor they change page
                    if x <= cursor_spot[0] <= y and height / 2 + 90 <= cursor_spot[1] <= height / 2 + 130:
                        image = 1
                        board = Board(width, height, game, 1)
                    if x <= cursor_spot[0] <= y and height / 2 + 140 <= cursor_spot[1] <= height / 2 + 180:
                        image = 1
                        board = Board(width, height, game, 2)

                    if x <= cursor_spot[0] <= y and height / 2 + 190 <= cursor_spot[1] <= height / 2 + 230:
                        image = 1
                        board = Board(width, height, game, 3)

                if image == 1: # sets all the button spaces into place so that when clicked with cursor they change page
                    if 35 <= cursor_spot[0] <= 135 and 500 <= cursor_spot[1] <= 575:
                        board.reset_to_original()
                        board.draw()

                    if 187.5 <= cursor_spot[0] <= 287.5 and 500 <= cursor_spot[1] <= 575:
                        game.fill((255, 255, 255))
                        image = 0

                    if 337.5 <= cursor_spot[0] <= 437.5 and 500 <= cursor_spot[1] <= 575:
                        quit()

                    if board.click(x, y) != None:
                        board.select(board.click(x, y)[0], board.click(x, y)[1])
                        board.draw()
                    board.draw()

                if image == 2: # sets all the buttons on this page to clickable so that when you click on it, it'll switch pages
                    if x <= cursor_spot[0] <= y and height / 2 <= cursor_spot[1] <= height / 2 + 40:
                        if winner == False:
                            image = 0
                            game.fill((255, 255, 255))
                        if winner == True:
                            pygame.quit()

            if image == 1:    # this code breaks down all the key strokes and if up, down, left, and right are used then you can move around the board up, down, left, and right
                if event.type == pygame.KEYDOWN:
                    board.draw()
                    if event.key == pygame.K_UP: # if pressed then the selection will move up one block
                        if column_choice > 0:
                            board.select(row_choice, column_choice - 1)

                    if event.key == pygame.K_DOWN:          # if pressed then the selection will move down one block
                        if column_choice < 8:
                            board.select(row_choice, column_choice + 1)

                    if event.key == pygame.K_LEFT:     # if pressed then the selection will move left one block
                        if row_choice < 8:
                            board.select(row_choice - 1, column_choice)

                    if event.key == pygame.K_RIGHT:     # if pressed then the selection will move right one block
                        if row_choice > 0:
                            board.select(row_choice + 1, column_choice)

                    if event.key == pygame.K_1 or event.key == pygame.K_KP_1:   #if you input number 1 in it sketchs the number
                        board.sketch(1)

                    if event.key == pygame.K_2 or event.key == pygame.K_KP_2:   #if you input number 2 in it sketchs the number
                        board.sketch(2)

                    if event.key == pygame.K_3 or event.key == pygame.K_KP_3:   #if you input number 3 in it sketchs the number
                        board.sketch(3)

                    if event.key == pygame.K_4 or event.key == pygame.K_KP_4:    #if you input number 4 in it sketchs the number
                        board.sketch(4)

                    if event.key == pygame.K_5 or event.key == pygame.K_KP_5:  #if you input number 5 in it sketchs the number
                        board.sketch(5)

                    if event.key == pygame.K_6 or event.key == pygame.K_KP_6:  #if you input number 6 in it sketchs the number
                        board.sketch(6)

                    if event.key == pygame.K_7 or event.key == pygame.K_KP_7: #if you input number 7 in it sketchs the number
                        board.sketch(7)

                    if event.key == pygame.K_8 or event.key == pygame.K_KP_8: #if you input number 8 in it sketchs the number
                        board.sketch(8)

                    if event.key == pygame.K_9 or event.key == pygame.K_KP_9: #if you input number 9 in it sketchs the number
                        board.sketch(9)


                    if event.key == pygame.K_BACKSPACE: # if backspace is hit then it clears that option
                        board.clear()

                    if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER: # when return or enter are used hten it saves it in the board
                        board.place_number()
                        if board.is_full():
                            image = 2
                    board.draw()

        pygame.display.update()

if __name__ == "__main__":          #main function to process code
    main()
