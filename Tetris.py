import pygame, random

pygame.init()

#Set up display window
screenSize = (800, 600)
display = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Tetris Game")
centerX = (800 / 2)
centerY = (600 / 2)

#Colors
black = (0, 0, 0)
white = (255, 255, 255)
gray = (192, 192, 192)
red = (255, 0, 0)
darkGreen = (0, 102, 0)
green = (0, 255, 0)
lightBlue = (0, 128, 255)
blue = (0, 0, 255)
pink = (255, 0, 255)
yellow = (255, 255, 0)

#Fonts
bigArialFont = pygame.font.SysFont("arial", 75, bold = True)
mediumArialFont = pygame.font.SysFont("arial", 45)
smallArialFontBold = pygame.font.SysFont("arial", 30, bold = True)
smallArialFont = pygame.font.SysFont("arial", 30)

#10x20 game board
grid = []
for row in range(20):
    grid.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
grid.append([2, 2, 2, 2, 2, 2, 2, 2, 2, 2])

score = 0
ticks = 0
running = True
menu = True
game = False
final = False

def block_draw(color, x, y):
    pygame.draw.rect(display, color, (x, y, 30, 30))
    pygame.draw.rect(display, black, (x, y, 30, 30), 2)

def menu_display():
    global playButton

    playButton = pygame.Rect(centerX - 80, 320, 160, 100)
    pygame.draw.rect(display, white, (playButton), 5)

    textMenu1 = bigArialFont.render("TETRIS", False, white)
    textMenu2 = mediumArialFont.render("PLAY", False, white)
    menuRect1 = textMenu1.get_rect()
    menuRect2 = textMenu2.get_rect()
    menuRect1.center = (centerX, 150)
    menuRect2.center = playButton.center
    display.blit(textMenu1, menuRect1)
    display.blit(textMenu2, menuRect2)

    #Draw 'I' piece
    i = 100
    for block in range(4):
        block_draw(red, 150, i)
        i += 30

    #Draw 'L' piece
    l = 275
    for block in range(3):
        block_draw(green, 50, l)
        l += 30
    block_draw(green, 80, 335)

    #Draw 'S' piece
    s = 125
    for block in range(2):
        block_draw(lightBlue, s, 450)
        s += 30
    s = 155
    for block in range(2):
        block_draw(lightBlue, s, 420)
        s += 30

    #Draw 'Z' piece
    z = 580
    for block in range(2):
        block_draw(pink, z, 100)
        z += 30
    z = 610
    for block in range(2):
        block_draw(pink, z, 130)
        z += 30

    #Draw 'T' piece
    t = 650
    for block in range(3):
        block_draw(blue, t, 225)
        t += 30
    block_draw(blue, 680, 255)

    #Draw 'O' piece
    o = 580
    for block in range(2):
        block_draw(darkGreen, o, 340)
        o += 30
    o = 580
    for block in range(2):
        block_draw(darkGreen, o, 370)
        o += 30

    #Draw 'J' piece
    j = 430
    for block in range(3):
        block_draw(yellow, 700, j)
        j += 30
    block_draw(yellow, 670, 490)

def draw_square(x, y, gridRow, gridColumn):
    if grid[gridRow][gridColumn] == 0:
        pygame.draw.rect(display, black, (x, y, 25, 25))
        pygame.draw.rect(display, white, (x, y, 25, 25), 1)

    elif grid[gridRow][gridColumn] == 1:
        pygame.draw.rect(display, white, (x, y, 25, 25))
        pygame.draw.rect(display, white, (x, y, 25, 25), 1)

    elif grid[gridRow][gridColumn] == 2:
        pygame.draw.rect(display, gray, (x, y, 25, 25))
        pygame.draw.rect(display, white, (x, y, 25, 25), 1)

def game_display():
    x = 275
    y =  50
    for row in range(20):
        for column in range(10):
            draw_square(x, y, row, column)
            x += 25       
        y += 25
        x = 275

    pygame.draw.rect(display, lightBlue, (275, 50, 250, 500), 3)

    textScore1 = smallArialFontBold.render("Score", True, white)
    textScore2 = smallArialFont.render(str(score), False, white)
    scoreRect1 = textScore1.get_rect()
    scoreRect2 = textScore2.get_rect()
    scoreRect1.center = (650, 125)
    scoreRect2.center = (650, 175)
    display.blit(textScore1, scoreRect1)
    display.blit(textScore2, scoreRect2)

def final_display():
    textFinal1 = mediumArialFont.render("Game Over!", True, white)
    textFinal2 = smallArialFont.render("Your score was: " + str(score), False, white)
    finalRect1 = textFinal1.get_rect()
    finalRect2 = textFinal2.get_rect()
    finalRect1.center = (centerX, 200)
    finalRect2.center = (centerX, 350)
    display.blit(textFinal1, finalRect1)
    display.blit(textFinal2, finalRect2)

def get_piece():
    global activePiece
    pieceList = ["I", "L", "S", "Z", "T", "O", "J"]
    activePiece = random.choice(pieceList)
    return activePiece

def start_piece(piece):
    global rotation
    rotation = 1

    if piece == "I":
        grid[0] = [0, 0, 0, 1, 1, 1, 1, 0, 0, 0]
    elif piece == "J":
        grid[0] = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
        grid[1] = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]
    elif piece == "L":
        grid[0] = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0]
        grid[1] = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]   
    elif piece == "O":
        grid[0] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        grid[1] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]   
    elif piece == "S":
        grid[0] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0]
        grid[1] = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]  
    elif piece == "T":
        grid[0] = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0]
        grid[1] = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0] 
    elif piece == "Z":
        grid[0] = [0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
        grid[1] = [0, 0, 0, 0, 1, 1, 0, 0, 0, 0] 

def index_all(array, value):
    indexArray = []
    for index in range(10):
        if array[index] == value:
            indexArray.append(index)
    return indexArray

def check_under():
    for row in range(20):
        activeBlocks = grid[row].count(1)
        if activeBlocks != 0:
            for slot in index_all(grid[row], 1):
                if grid[row + 1][slot] >= 2:
                    return False
    return True

def block_drop(row, column, value):
    grid[row][column] = 0
    grid[row + 1][column] = value

def game_over():
    topRowCount = grid[0].count(2)
    if topRowCount != 0:
        return True
    else:
        return False

def piece_drop():
    global game, final
    empty = check_under()

    if empty:
        for row in range(20, -1, -1):
            activeBlocks = grid[row].count(1)
            if activeBlocks != 0:
                indexList = index_all(grid[row], 1)
                for index in indexList:
                    block_drop(row, index, 1)
    elif not empty:
        for row in range(20):
            activeBlocksList = index_all(grid[row], 1)
            for value in activeBlocksList:
                grid[row][value] = 2
        if game_over():
            game = False
            final = True
        else:
            start_piece(get_piece())

def row_drop(row, value):
    indexList = index_all(grid[row], 2)
    for index in indexList:
        block_drop(row, index, 2)

def row_clear():
    global score
    rowsCleared = 0

    for row in range(20):
        count = grid[row].count(2)
        if count == 10:
            grid[row] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            for higherRow in range(row - 1, -1, -1):
                row_drop(higherRow, 2)
            rowsCleared += 1

    score += rowsCleared * 10

def can_move(direction):
    if direction == "left":
        for row in range(20):
            rowCount = grid[row].count(1)
            if rowCount != 0:
                leftmostIndex = grid[row].index(1)
                if leftmostIndex == 0 or grid[row][leftmostIndex - 1] == 2:
                    return False
        
    elif direction == "right":
        for row in range(20):
            rowCount = grid[row].count(1)
            if rowCount != 0:
                grid[row].reverse() 
                reversedRow = grid[row].copy()
                grid[row].reverse()
                rightmostIndex = reversedRow.index(1)
                if rightmostIndex == 0 or reversedRow[rightmostIndex - 1] == 2:
                    return False
    return True

def piece_move(direction):
    empty = can_move(direction)
    if empty:
        if direction == "left":
            for row in range(20):
                rowCount = grid[row].count(1)
                if rowCount != 0:
                    rowIndex = index_all(grid[row], 1)
                    for index in rowIndex:
                        grid[row][index] = 0
                        grid[row][index - 1] = 1


        if direction == "right":
            for row in range(20):
                rowCount = grid[row].count(1)
                if rowCount != 0:
                    rowIndex = index_all(grid[row], 1)
                    rowIndex.reverse()
                    for index in rowIndex:
                        grid[row][index] = 0
                        grid[row][index + 1] = 1

def is_occupied(row, column, value):
    if grid[row][column] == value:
        return True
    else:
        return False

def any_occupied(firstInstance, pairsList, value):
    length = len(pairsList)
    for pair in range(length):
        result = is_occupied(firstInstance[0] + pairsList[pair][0], firstInstance[1] + pairsList[pair][1], value)
        if result:
            return True

    return False

def find_top_left(value):
    for row in range(20):
        valueCount = grid[row].count(value)
        if valueCount != 0:
            horizontalIndex = grid[row].index(value)
            return row, horizontalIndex

def can_rotate(): 
    firstInstance = find_top_left(1)

    if activePiece == "I":
        if rotation == 1:
            checklist = [(-2, 2), (-1, 2), (0, 2), (1, 2)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        elif rotation == 2:
            #1
            #1
            #1
            #1
            if firstInstance[1] < 2 or firstInstance[1] > 8:
                return False

            checklist = [(2, -2), (2, -1), (2, 0), (2, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False
            
    elif activePiece == "J":
        if rotation == 1:
            #1
            #1 1 1
            checklist = [(0, 1), (0, 2), (1, 1), (2, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False
            
        elif rotation == 2:
            #1 1
            #1
            #1
            if firstInstance[1] == 0:
                return False

            checklist = [(0, -1), (0, 0), (0, 1), (1, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False
            
        elif rotation == 3: 
            #1 1 1
            #    1
            checklist = [(-1, 1), (0, 1), (1, 1), (1, 0)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        elif rotation == 4:
            #  1
            #  1
            #1 1
            if firstInstance[1] == 9:
                return False

            checklist = [(1, -1), (2, -1), (2, 0), (2, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False
        
    elif activePiece == "L":
        if rotation == 1:
            #    1
            #1 1 1
            checklist = [(-1, -1), (0, -1), (1, -1), (1, 0)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        elif rotation == 2:
            #1
            #1
            #1 1
            if firstInstance[1] == 0:
                return False

            checklist = [(1, -1), (1, 0), (1, 1), (2, -1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        elif rotation == 3:
            #1 1 1
            #1
            checklist = [(-1, 0), (-1, 1), (0, 1), (1, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        elif rotation == 4:
            #1 1
            #  1
            #  1
            if firstInstance[1] == 0:
                return False

            checklist = [(1, 1), (2, -1), (2, 0), (2, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

    elif activePiece == "O":
        #O shape has no rotations
        return False
    
    elif activePiece == "S":
        if rotation == 1:
            #  1 1
            #1 1
            checklist = [(0, 0), (1, 0), (1, 1), (2, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        if rotation == 2:
            #1
            #1 1
            #  1
            if firstInstance[1] == 0:
                return False

            checklist = [(0, 0), (0, 1), (1, -1), (1, 0)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

    elif activePiece == "T":
        if rotation == 1:
            #  1
            #1 1 1
            checklist = [(0, 0), (1, 0), (1, 1), (2, 0)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        elif rotation == 2:
            #1
            #1 1
            #1
            if firstInstance[1] == 0:
                return False

            checklist = [(1, -1), (1, 0), (1, 1), (2, 0)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        elif rotation == 3:
            #1 1 1
            #  1
            checklist = [(-1, 1), (0, 0), (0, 1), (1, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        elif rotation == 4:
            #  1
            #1 1
            #  1
            if firstInstance[1] == 9:
                return False

            checklist = [(0, 0), (1, -1), (1, 0), (1, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

    elif activePiece == "Z":
        if rotation == 1:
            #1 1
            #  1 1
            checklist = [(0, 2), (1, 1), (1, 2), (2, 1)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False

        if rotation == 2:
            #  1
            #1 1
            #1
            if firstInstance[1] == 0:
                return False

            checklist = [(0, -2), (0, -1), (1, -1), (1, 0)]
            result = any_occupied(firstInstance, checklist, 2)
            if result:
                return False
    return True

def blink_piece(tupleList):
    firstInstance = find_top_left(1)

    for row in range(20):
        rowCount = grid[row].count(1)
        if rowCount != 0:
            for num in range(10):
                if grid[row][num] == 1:
                    grid[row][num] = 0

    length = len(tupleList)
    for each in range(length):
        change = tupleList[each]
        grid[firstInstance[0] + change[0]][firstInstance[1] + change[1]] = 1

def rotate_piece():
    global rotation

    for row in range(20):
        rowCount = grid[row].count(1)
        if rowCount != 0:
            highestRow = row
    
    if highestRow >= 2:
        if can_rotate():
            if activePiece == "I":
                if rotation == 1:
                    blink_piece([(-2, 2), (-1, 2), (0, 2), (1, 2)])
                    rotation = 2

                elif rotation == 2:
                    blink_piece([(2, -2), (2, -1), (2, 0), (2, 1)])
                    rotation = 1

            elif activePiece == "J":
                if rotation == 1:
                    blink_piece([(0, 1), (0, 2), (1, 1), (2, 1)])
                    rotation = 2

                elif rotation == 2:
                    blink_piece([(0, -1), (0, 0), (0, 1), (1, 1)])
                    rotation = 3

                elif rotation == 3:
                    blink_piece([(-1, 1), (0, 1), (1, 1), (1, 0)])
                    rotation = 4

                elif rotation == 4:
                    blink_piece([(1, -1), (2, -1), (2, 0), (2, 1)])
                    rotation = 1

            elif activePiece == "L":
                if rotation == 1:
                    blink_piece([(-1, -1), (0, -1), (1, -1), (1, 0)])
                    rotation = 2

                elif rotation == 2:
                    blink_piece([(1, -1), (1, 0), (1, 1), (2, -1)])
                    rotation = 3

                elif rotation == 3:
                    blink_piece([(-1, 0), (-1, 1), (0, 1), (1, 1)])
                    rotation = 4

                elif rotation == 4:
                    blink_piece([(1, 1), (2, -1), (2, 0), (2, 1)])
                    rotation = 1

            elif activePiece == "S":
                if rotation == 1:
                    blink_piece([(0, 0), (1, 0), (1, 1), (2, 1)])
                    rotation = 2

                elif rotation == 2:
                    blink_piece([(0, 0), (0, 1), (1, -1), (1, 0)])
                    rotation = 1

            elif activePiece == "T":
                if rotation == 1:
                    blink_piece([(0, 0), (1, 0), (1, 1), (2, 0)])
                    rotation = 2

                elif rotation == 2:
                    blink_piece([(1, -1), (1, 0), (1, 1), (2, 0)])
                    rotation = 3

                elif rotation == 3:
                    blink_piece([(-1, 1), (0, 0), (0, 1), (1, 1)])
                    rotation = 4

                elif rotation == 4:
                    blink_piece([(0, 0), (1, -1), (1, 0), (1, 1)])
                    rotation = 1

            elif activePiece == "Z":
                if rotation == 1:
                    blink_piece([(0, 2), (1, 1), (1, 2), (2, 1)])
                    rotation = 2

                elif rotation == 2:
                    blink_piece([(0, -2), (0, -1), (1, -1), (1, 0)])
                    rotation = 1

#Main program
start_piece(get_piece())

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #Menu loop
    while menu:
        display.fill(black)
        menu_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if playButton.left <= mouseX and mouseX <= playButton.right:
                    if playButton.top <= mouseY and mouseY <= playButton.bottom:
                        menu = False
                        game = True

        pygame.display.update()

    #Game loop
    while game:
        display.fill(black)

        if ticks == 10:
            piece_drop()
            ticks = 0

        clock = pygame.time.Clock()
        clock.tick(30)
        ticks += 1

        row_clear()
        game_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_r:
                    rotate_piece()
                elif event.key == pygame.K_LEFT:
                    piece_move("left")
                elif event.key == pygame.K_RIGHT:
                    piece_move("right")
 
        pygame.display.update()

    #End screen loop
    while final:
        display.fill(black)
        final_display()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                final = False
        
        pygame.display.update()

pygame.quit()