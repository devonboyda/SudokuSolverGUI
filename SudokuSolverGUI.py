import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption("Sudoku Solver")
clock = pygame.time.Clock()
font = pygame.font.SysFont("stencil", 60)

running = True
isPressed = False
is_pressed_reset = False
no_solution = False
currNum = None  # testing

# boolean collection for block coordinates

b1_1 = False
b1_2 = False
b1_3 = False
b1_4 = False
b1_5 = False
b1_6 = False
b1_7 = False
b1_8 = False
b1_9 = False

b2_1 = False
b2_2 = False
b2_3 = False
b2_4 = False
b2_5 = False
b2_6 = False
b2_7 = False
b2_8 = False
b2_9 = False

b3_1 = False
b3_2 = False
b3_3 = False
b3_4 = False
b3_5 = False
b3_6 = False
b3_7 = False
b3_8 = False
b3_9 = False

b4_1 = False
b4_2 = False
b4_3 = False
b4_4 = False
b4_5 = False
b4_6 = False
b4_7 = False
b4_8 = False
b4_9 = False

b5_1 = False
b5_2 = False
b5_3 = False
b5_4 = False
b5_5 = False
b5_6 = False
b5_7 = False
b5_8 = False
b5_9 = False

b6_1 = False
b6_2 = False
b6_3 = False
b6_4 = False
b6_5 = False
b6_6 = False
b6_7 = False
b6_8 = False
b6_9 = False

b7_1 = False
b7_2 = False
b7_3 = False
b7_4 = False
b7_5 = False
b7_6 = False
b7_7 = False
b7_8 = False
b7_9 = False

b8_1 = False
b8_2 = False
b8_3 = False
b8_4 = False
b8_5 = False
b8_6 = False
b8_7 = False
b8_8 = False
b8_9 = False

b9_1 = False
b9_2 = False
b9_3 = False
b9_4 = False
b9_5 = False
b9_6 = False
b9_7 = False
b9_8 = False
b9_9 = False


class numberObject:
    def __init__(self, x, y, num=None):
        self.num = None
        self.x = x
        self.y = y
        self.height = 58
        self.width = 58
        self.filled = 0
        self.color = (255, 255, 255)

    def draw(self, num):
        global currNum
        currNum = num
        if num is not None:
            idText = str(num).rjust(3)
            screen.blit(font.render(idText, True, (0, 0, 0)), (self.x, self.y))

    def get_num(self):
        return self.num

    def num_reset(self, num):
        self.num = None

    def set_num(self):
        if self.num is None:
            self.num = 1
        elif self.num == 1:
            self.num = 2
        elif self.num == 2:
            self.num = 3
        elif self.num == 3:
            self.num = 4
        elif self.num == 4:
            self.num = 5
        elif self.num == 5:
            self.num = 6
        elif self.num == 6:
            self.num = 7
        elif self.num == 7:
            self.num = 8
        elif self.num == 8:
            self.num = 9
        elif self.num == 9:
            self.num = None

    def set_solution(self, newNum):
        self.num = newNum


class gameBoardLittleBoxes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 70
        self.width = 70
        self.color = (0, 0, 0)
        self.filled = 1

    def draw(self):
        i = 0
        while i <= 590:
            j = 0
            while j <= 590:
                pygame.draw.rect(screen, self.color, (self.x + j, self.y + i, self.height, self.width), self.filled)
                j += 70
            i += 70


class gameBoardBigBoxes:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 210
        self.width = 210
        self.color = (0, 0, 0)
        self.filled = 5

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width), self.filled)
        pygame.draw.rect(screen, self.color, (self.x + self.width, self.y, self.height, self.width), self.filled)
        pygame.draw.rect(screen, self.color, (self.x + (self.width * 2), self.y, self.height, self.width), self.filled)

        pygame.draw.rect(screen, self.color, (self.x, self.y + self.height, self.height, self.width), self.filled)
        pygame.draw.rect(screen, self.color, (self.x + self.width + self.height, self.y, self.height, self.width),
                         self.filled)
        pygame.draw.rect(screen, self.color, (self.x + (self.width * 2), self.y + self.height, self.height, self.width),
                         self.filled)

        pygame.draw.rect(screen, self.color, (self.x, self.y + (self.height * 2), self.height, self.width), self.filled)
        pygame.draw.rect(screen, self.color, (self.x + self.width, self.y + (self.height * 2), self.height, self.width),
                         self.filled)
        pygame.draw.rect(screen, self.color,
                         (self.x + (self.width * 2), self.y + (self.height * 2), self.height, self.width), self.filled)


# Redo Button

class resetButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 256
        self.color = (0, 0, 0)
        self.filled = 5

    def draw(self):
        this = pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width), self.filled)
        screen.fill("red", this, 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width), self.filled)
        text = str("R").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 25, self.y + 4))
        text = str("e").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 25, self.y + self.height + 4))
        text = str("s").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 25, self.y + (self.height * 2) + 4))
        text = str("e").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 25, self.y + (self.height * 3) + 4))
        text = str("t").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 25, self.y + (self.height * 4) + 4))

    def is_pressed(self, corx, cory):
        x = corx
        y = cory

        global is_pressed_reset

        if self.x < x < self.x + self.height:
            if self.y < y < self.y + self.width:
                is_pressed_reset = True

class solveButton:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 50
        self.width = 256
        self.color = (0, 0, 0)
        self.filled = 5

    def draw(self):
        this = pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width), self.filled)
        screen.fill("red", this, 0)
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.height, self.width), self.filled)
        text = str("S").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 22, self.y + 4))
        text = str("o").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 23, self.y + (self.height) + 4))
        text = str("l").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 22, self.y + (self.height * 2) + 4))
        text = str("v").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 22, self.y + (self.height * 3) + 4))
        text = str("e").rjust(3)
        screen.blit(font.render(text, True, (255, 255, 255)), (self.x - 22, self.y + (self.height * 4) + 4))

    def is_pressed(self, corx, cory):
        x = corx
        y = cory

        global isPressed

        if self.x < x < self.x + self.height:
            if self.y < y < self.y + self.width:
                isPressed = True

    def make_grid(self):
        global grid
        grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

        # converting gui to grid

        grid[0][0] = box1_1.get_num()
        grid[0][1] = box1_2.get_num()
        grid[0][2] = box1_3.get_num()
        grid[0][3] = box1_4.get_num()
        grid[0][4] = box1_5.get_num()
        grid[0][5] = box1_6.get_num()
        grid[0][6] = box1_7.get_num()
        grid[0][7] = box1_8.get_num()
        grid[0][8] = box1_9.get_num()

        grid[1][0] = box2_1.get_num()
        grid[1][1] = box2_2.get_num()
        grid[1][2] = box2_3.get_num()
        grid[1][3] = box2_4.get_num()
        grid[1][4] = box2_5.get_num()
        grid[1][5] = box2_6.get_num()
        grid[1][6] = box2_7.get_num()
        grid[1][7] = box2_8.get_num()
        grid[1][8] = box2_9.get_num()

        grid[2][0] = box3_1.get_num()
        grid[2][1] = box3_2.get_num()
        grid[2][2] = box3_3.get_num()
        grid[2][3] = box3_4.get_num()
        grid[2][4] = box3_5.get_num()
        grid[2][5] = box3_6.get_num()
        grid[2][6] = box3_7.get_num()
        grid[2][7] = box3_8.get_num()
        grid[2][8] = box3_9.get_num()

        grid[3][0] = box4_1.get_num()
        grid[3][1] = box4_2.get_num()
        grid[3][2] = box4_3.get_num()
        grid[3][3] = box4_4.get_num()
        grid[3][4] = box4_5.get_num()
        grid[3][5] = box4_6.get_num()
        grid[3][6] = box4_7.get_num()
        grid[3][7] = box4_8.get_num()
        grid[3][8] = box4_9.get_num()

        grid[4][0] = box5_1.get_num()
        grid[4][1] = box5_2.get_num()
        grid[4][2] = box5_3.get_num()
        grid[4][3] = box5_4.get_num()
        grid[4][4] = box5_5.get_num()
        grid[4][5] = box5_6.get_num()
        grid[4][6] = box5_7.get_num()
        grid[4][7] = box5_8.get_num()
        grid[4][8] = box5_9.get_num()

        grid[5][0] = box6_1.get_num()
        grid[5][1] = box6_2.get_num()
        grid[5][2] = box6_3.get_num()
        grid[5][3] = box6_4.get_num()
        grid[5][4] = box6_5.get_num()
        grid[5][5] = box6_6.get_num()
        grid[5][6] = box6_7.get_num()
        grid[5][7] = box6_8.get_num()
        grid[5][8] = box6_9.get_num()

        grid[6][0] = box7_1.get_num()
        grid[6][1] = box7_2.get_num()
        grid[6][2] = box7_3.get_num()
        grid[6][3] = box7_4.get_num()
        grid[6][4] = box7_5.get_num()
        grid[6][5] = box7_6.get_num()
        grid[6][6] = box7_7.get_num()
        grid[6][7] = box7_8.get_num()
        grid[6][8] = box7_9.get_num()

        grid[7][0] = box8_1.get_num()
        grid[7][1] = box8_2.get_num()
        grid[7][2] = box8_3.get_num()
        grid[7][3] = box8_4.get_num()
        grid[7][4] = box8_5.get_num()
        grid[7][5] = box8_6.get_num()
        grid[7][6] = box8_7.get_num()
        grid[7][7] = box8_8.get_num()
        grid[7][8] = box8_9.get_num()

        grid[8][0] = box9_1.get_num()
        grid[8][1] = box9_2.get_num()
        grid[8][2] = box9_3.get_num()
        grid[8][3] = box9_4.get_num()
        grid[8][4] = box9_5.get_num()
        grid[8][5] = box9_6.get_num()
        grid[8][6] = box9_7.get_num()
        grid[8][7] = box9_8.get_num()
        grid[8][8] = box9_9.get_num()

        for i in range(9):
            for j in range(9):
                if grid[i][j] is None:
                    grid[i][j] = 0

        # print(grid)
        return grid

    def error_checker(self, grid):
        global no_solution
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    tempNum = grid[i][j]
                    if self.is_in_row_checker(grid, i, j + 1, tempNum):
                        no_solution = True
                        return True
                    if self.is_in_column_checker(grid, i + 1, j, tempNum):
                        no_solution = True
                        return True
                    if self.is_in_box_checker(grid, i, j, tempNum):
                        no_solution = True
                        return True
                    else:
                        continue
        return False

    def empty_index(self, grid, a):
        for row in range(9):
            for column in range(9):
                if grid[row][column] == 0:
                    a[0] = row
                    a[1] = column
                    return True
        return False

    def is_in_row(self, grid, row, num):
        for i in range(9):
            if grid[row][i] == num:
                return True
        return False

    def is_in_row_checker(self, grid, row, column, num):
        for column in range(column, 9):
            if grid[row][column] == num:
                return True
        return False

    def is_in_column(self, grid, column, num):
        for i in range(9):
            if grid[i][column] == num:
                return True
        return False

    def is_in_column_checker(self, grid, row, column, num):
        for row in range(row, 9):
            if grid[row][column] == num:
                return True
        return False

    def is_in_box(self, grid, row, column, num):
        for i in range(3):
            for j in range(3):
                if grid[i + row][j + column] == num:
                    return True
        return False

    def is_in_box_checker(self, grid, row, column, num):
        counter = 0
        if row <= 2:
            row = 0
        elif row <= 5:
            row = 3
        else:
            row = 6
        if column <= 2:
            column = 0
        elif column <= 5:
            column = 3
        else:
            column = 6
        for i in range(3):
            for j in range(3):
                if grid[i + row][j + column] == num:
                    counter += 1
                    if counter > 1:
                        return True
        return False

    def location_checker(self, grid, row, column, num):
        return not self.is_in_row(grid, row, num) and not self.is_in_column(grid, column, num) and not self.is_in_box(
            grid, row - row % 3, column - column % 3, num)

    def solve(self, grid):
        a = [0, 0]
        if not self.empty_index(grid, a):
            return True

        row = a[0]
        column = a[1]
        for num in range(1, 10):
            if self.location_checker(grid, row, column, num):
                grid[row][column] = num
                if self.solve(grid):
                    return True
                grid[row][column] = 0
        return False

    def print_grid(self, grid):
        for i in range(9):
            print(grid[i][0], grid[i][1], grid[i][2], grid[i][3], grid[i][4], grid[i][5], grid[i][6], grid[i][7],
                  grid[i][8])

    def show_solution(self, grid):

        # Set's new numbers in GUI

        box1_1.set_solution(grid[0][0])
        box1_2.set_solution(grid[0][1])
        box1_3.set_solution(grid[0][2])
        box1_4.set_solution(grid[0][3])
        box1_5.set_solution(grid[0][4])
        box1_6.set_solution(grid[0][5])
        box1_7.set_solution(grid[0][6])
        box1_8.set_solution(grid[0][7])
        box1_9.set_solution(grid[0][8])

        box2_1.set_solution(grid[1][0])
        box2_2.set_solution(grid[1][1])
        box2_3.set_solution(grid[1][2])
        box2_4.set_solution(grid[1][3])
        box2_5.set_solution(grid[1][4])
        box2_6.set_solution(grid[1][5])
        box2_7.set_solution(grid[1][6])
        box2_8.set_solution(grid[1][7])
        box2_9.set_solution(grid[1][8])

        box3_1.set_solution(grid[2][0])
        box3_2.set_solution(grid[2][1])
        box3_3.set_solution(grid[2][2])
        box3_4.set_solution(grid[2][3])
        box3_5.set_solution(grid[2][4])
        box3_6.set_solution(grid[2][5])
        box3_7.set_solution(grid[2][6])
        box3_8.set_solution(grid[2][7])
        box3_9.set_solution(grid[2][8])

        box4_1.set_solution(grid[3][0])
        box4_2.set_solution(grid[3][1])
        box4_3.set_solution(grid[3][2])
        box4_4.set_solution(grid[3][3])
        box4_5.set_solution(grid[3][4])
        box4_6.set_solution(grid[3][5])
        box4_7.set_solution(grid[3][6])
        box4_8.set_solution(grid[3][7])
        box4_9.set_solution(grid[3][8])

        box5_1.set_solution(grid[4][0])
        box5_2.set_solution(grid[4][1])
        box5_3.set_solution(grid[4][2])
        box5_4.set_solution(grid[4][3])
        box5_5.set_solution(grid[4][4])
        box5_6.set_solution(grid[4][5])
        box5_7.set_solution(grid[4][6])
        box5_8.set_solution(grid[4][7])
        box5_9.set_solution(grid[4][8])

        box6_1.set_solution(grid[5][0])
        box6_2.set_solution(grid[5][1])
        box6_3.set_solution(grid[5][2])
        box6_4.set_solution(grid[5][3])
        box6_5.set_solution(grid[5][4])
        box6_6.set_solution(grid[5][5])
        box6_7.set_solution(grid[5][6])
        box6_8.set_solution(grid[5][7])
        box6_9.set_solution(grid[5][8])

        box7_1.set_solution(grid[6][0])
        box7_2.set_solution(grid[6][1])
        box7_3.set_solution(grid[6][2])
        box7_4.set_solution(grid[6][3])
        box7_5.set_solution(grid[6][4])
        box7_6.set_solution(grid[6][5])
        box7_7.set_solution(grid[6][6])
        box7_8.set_solution(grid[6][7])
        box7_9.set_solution(grid[6][8])

        box8_1.set_solution(grid[7][0])
        box8_2.set_solution(grid[7][1])
        box8_3.set_solution(grid[7][2])
        box8_4.set_solution(grid[7][3])
        box8_5.set_solution(grid[7][4])
        box8_6.set_solution(grid[7][5])
        box8_7.set_solution(grid[7][6])
        box8_8.set_solution(grid[7][7])
        box8_9.set_solution(grid[7][8])

        box9_1.set_solution(grid[8][0])
        box9_2.set_solution(grid[8][1])
        box9_3.set_solution(grid[8][2])
        box9_4.set_solution(grid[8][3])
        box9_5.set_solution(grid[8][4])
        box9_6.set_solution(grid[8][5])
        box9_7.set_solution(grid[8][6])
        box9_8.set_solution(grid[8][7])
        box9_9.set_solution(grid[8][8])

    def no_solution(self):
        string = "No Solution"
        text = str(string).rjust(3)
        nsFont = pygame.font.SysFont("stencil", 110)
        screen.blit(nsFont.render(text, True, (0, 0, 0)), (95, 310))


def coordinate_checker(coorx, cory):
    x = coorx
    y = cory

    # boolean collection for block coordinates
    global b1_1
    global b1_2
    global b1_3
    global b1_4
    global b1_5
    global b1_6
    global b1_7
    global b1_8
    global b1_9

    global b2_1
    global b2_2
    global b2_3
    global b2_4
    global b2_5
    global b2_6
    global b2_7
    global b2_8
    global b2_9

    global b3_1
    global b3_2
    global b3_3
    global b3_4
    global b3_5
    global b3_6
    global b3_7
    global b3_8
    global b3_9

    global b4_1
    global b4_2
    global b4_3
    global b4_4
    global b4_5
    global b4_6
    global b4_7
    global b4_8
    global b4_9

    global b5_1
    global b5_2
    global b5_3
    global b5_4
    global b5_5
    global b5_6
    global b5_7
    global b5_8
    global b5_9

    global b6_1
    global b6_2
    global b6_3
    global b6_4
    global b6_5
    global b6_6
    global b6_7
    global b6_8
    global b6_9

    global b7_1
    global b7_2
    global b7_3
    global b7_4
    global b7_5
    global b7_6
    global b7_7
    global b7_8
    global b7_9

    global b8_1
    global b8_2
    global b8_3
    global b8_4
    global b8_5
    global b8_6
    global b8_7
    global b8_8
    global b8_9

    global b9_1
    global b9_2
    global b9_3
    global b9_4
    global b9_5
    global b9_6
    global b9_7
    global b9_8
    global b9_9

    if 130 < x < 195:
        if 25 < y < 92:
            box1_1.set_num()
            b1_1 = True
        elif 95 < y < 160:
            box2_1.set_num()
            b2_1 = True
        elif 165 < y < 230:
            box3_1.set_num()
            b3_1 = True
        elif 235 < y < 300:
            box4_1.set_num()
            b4_1 = True
        elif 305 < y < 370:
            box5_1.set_num()
            b5_1 = True
        elif 375 < y < 440:
            box6_1.set_num()
            b6_1 = True
        elif 445 < y < 510:
            box7_1.set_num()
            b7_1 = True
        elif 515 < y < 580:
            box8_1.set_num()
            b8_1 = True
        elif 585 < y < 650:
            box9_1.set_num()
            b9_1 = True
    elif 200 < x < 265:
        if 25 < y < 92:
            box1_2.set_num()
            b1_2 = True
        elif 95 < y < 160:
            box2_2.set_num()
            b2_2 = True
        elif 165 < y < 230:
            box3_2.set_num()
            b3_2 = True
        elif 235 < y < 300:
            box4_2.set_num()
            b4_2 = True
        elif 305 < y < 370:
            box5_2.set_num()
            b5_2 = True
        elif 375 < y < 440:
            box6_2.set_num()
            b6_2 = True
        elif 445 < y < 510:
            box7_2.set_num()
            b7_2 = True
        elif 515 < y < 580:
            box8_2.set_num()
            b8_2 = True
        elif 585 < y < 650:
            box9_2.set_num()
            b9_2 = True
    elif 270 < x < 335:
        if 25 < y < 92:
            box1_3.set_num()
            b1_3 = True
        elif 95 < y < 160:
            box2_3.set_num()
            b2_3 = True
        elif 165 < y < 230:
            box3_3.set_num()
            b3_3 = True
        elif 235 < y < 300:
            box4_3.set_num()
            b4_3 = True
        elif 305 < y < 370:
            box5_3.set_num()
            b5_3 = True
        elif 375 < y < 440:
            box6_3.set_num()
            b6_3 = True
        elif 445 < y < 510:
            box7_3.set_num()
            b7_3 = True
        elif 515 < y < 580:
            box8_3.set_num()
            b8_3 = True
        elif 585 < y < 650:
            box9_3.set_num()
            b9_3 = True
    elif 340 < x < 405:
        if 25 < y < 92:
            box1_4.set_num()
            b1_4 = True
        elif 95 < y < 160:
            box2_4.set_num()
            b2_4 = True
        elif 165 < y < 230:
            box3_4.set_num()
            b3_4 = True
        elif 235 < y < 300:
            box4_4.set_num()
            b4_4 = True
        elif 305 < y < 370:
            box5_4.set_num()
            b5_4 = True
        elif 375 < y < 440:
            box6_4.set_num()
            b6_4 = True
        elif 445 < y < 510:
            box7_4.set_num()
            b7_4 = True
        elif 515 < y < 580:
            box8_4.set_num()
            b8_4 = True
        elif 585 < y < 650:
            box9_4.set_num()
            b9_4 = True
    elif 410 < x < 475:
        if 25 < y < 92:
            box1_5.set_num()
            b1_5 = True
        elif 95 < y < 160:
            box2_5.set_num()
            b2_5 = True
        elif 165 < y < 230:
            box3_5.set_num()
            b3_5 = True
        elif 235 < y < 300:
            box4_5.set_num()
            b4_5 = True
        elif 305 < y < 370:
            box5_5.set_num()
            b5_5 = True
        elif 375 < y < 440:
            box6_5.set_num()
            b6_5 = True
        elif 445 < y < 510:
            box7_5.set_num()
            b7_5 = True
        elif 515 < y < 580:
            box8_5.set_num()
            b8_5 = True
        elif 585 < y < 650:
            box9_5.set_num()
            b9_5 = True
    elif 480 < x < 545:
        if 25 < y < 92:
            box1_6.set_num()
            b1_6 = True
        elif 95 < y < 160:
            box2_6.set_num()
            b2_6 = True
        elif 165 < y < 230:
            box3_6.set_num()
            b3_6 = True
        elif 235 < y < 300:
            box4_6.set_num()
            b4_6 = True
        elif 305 < y < 370:
            box5_6.set_num()
            b5_6 = True
        elif 375 < y < 440:
            box6_6.set_num()
            b6_6 = True
        elif 445 < y < 510:
            box7_6.set_num()
            b7_6 = True
        elif 515 < y < 580:
            box8_6.set_num()
            b8_6 = True
        elif 585 < y < 650:
            box9_6.set_num()
            b9_6 = True
    elif 550 < x < 615:
        if 25 < y < 92:
            box1_7.set_num()
            b1_7 = True
        elif 95 < y < 160:
            box2_7.set_num()
            b2_7 = True
        elif 165 < y < 230:
            box3_7.set_num()
            b3_7 = True
        elif 235 < y < 300:
            box4_7.set_num()
            b4_7 = True
        elif 305 < y < 370:
            box5_7.set_num()
            b5_7 = True
        elif 375 < y < 440:
            box6_7.set_num()
            b6_7 = True
        elif 445 < y < 510:
            box7_7.set_num()
            b7_7 = True
        elif 515 < y < 580:
            box8_7.set_num()
            b8_7 = True
        elif 585 < y < 650:
            box9_7.set_num()
            b9_7 = True
    elif 620 < x < 685:
        if 25 < y < 92:
            box1_8.set_num()
            b1_8 = True
        elif 95 < y < 160:
            box2_8.set_num()
            b2_8 = True
        elif 165 < y < 230:
            box3_8.set_num()
            b3_8 = True
        elif 235 < y < 300:
            box4_8.set_num()
            b4_8 = True
        elif 305 < y < 370:
            box5_8.set_num()
            b5_8 = True
        elif 375 < y < 440:
            box6_8.set_num()
            b6_8 = True
        elif 445 < y < 510:
            box7_8.set_num()
            b7_8 = True
        elif 515 < y < 580:
            box8_8.set_num()
            b8_8 = True
        elif 585 < y < 650:
            box9_8.set_num()
            b9_8 = True
    elif 690 < x < 755:
        if 25 < y < 92:
            box1_9.set_num()
            b1_9 = True
        elif 95 < y < 160:
            box2_9.set_num()
            b2_9 = True
        elif 165 < y < 230:
            box3_9.set_num()
            b3_9 = True
        elif 235 < y < 300:
            box4_9.set_num()
            b4_9 = True
        elif 305 < y < 370:
            box5_9.set_num()
            b5_9 = True
        elif 375 < y < 440:
            box6_9.set_num()
            b6_9 = True
        elif 445 < y < 510:
            box7_9.set_num()
            b7_9 = True
        elif 515 < y < 580:
            box8_9.set_num()
            b8_9 = True
        elif 585 < y < 650:
            box9_9.set_num()
            b9_9 = True


gbbb = gameBoardBigBoxes(125, 25)
gblb = gameBoardLittleBoxes(125, 25)
solveButton = solveButton(50, 200)
resetButton = resetButton(780, 200)

# box objects

box1_1 = numberObject(113, 35)
box1_2 = numberObject(184, 35)
box1_3 = numberObject(250, 35)
box1_4 = numberObject(327, 35)
box1_5 = numberObject(392, 35)
box1_6 = numberObject(461, 35)
box1_7 = numberObject(532, 35)
box1_8 = numberObject(601, 35)
box1_9 = numberObject(668, 35)

box2_1 = numberObject(113, 105)
box2_2 = numberObject(184, 105)
box2_3 = numberObject(250, 105)
box2_4 = numberObject(327, 105)
box2_5 = numberObject(392, 105)
box2_6 = numberObject(461, 105)
box2_7 = numberObject(532, 105)
box2_8 = numberObject(601, 105)
box2_9 = numberObject(668, 105)

box3_1 = numberObject(113, 175)
box3_2 = numberObject(184, 175)
box3_3 = numberObject(250, 175)
box3_4 = numberObject(327, 175)
box3_5 = numberObject(392, 175)
box3_6 = numberObject(461, 175)
box3_7 = numberObject(532, 175)
box3_8 = numberObject(601, 175)
box3_9 = numberObject(668, 175)

box4_1 = numberObject(113, 248)
box4_2 = numberObject(184, 248)
box4_3 = numberObject(250, 248)
box4_4 = numberObject(327, 248)
box4_5 = numberObject(392, 248)
box4_6 = numberObject(461, 248)
box4_7 = numberObject(532, 248)
box4_8 = numberObject(601, 248)
box4_9 = numberObject(668, 248)

box5_1 = numberObject(113, 312)
box5_2 = numberObject(184, 312)
box5_3 = numberObject(250, 312)
box5_4 = numberObject(327, 312)
box5_5 = numberObject(392, 312)
box5_6 = numberObject(461, 312)
box5_7 = numberObject(532, 312)
box5_8 = numberObject(601, 312)
box5_9 = numberObject(668, 312)

box6_1 = numberObject(113, 383)
box6_2 = numberObject(184, 383)
box6_3 = numberObject(250, 383)
box6_4 = numberObject(327, 383)
box6_5 = numberObject(392, 383)
box6_6 = numberObject(461, 383)
box6_7 = numberObject(532, 383)
box6_8 = numberObject(601, 383)
box6_9 = numberObject(668, 383)

box7_1 = numberObject(113, 453)
box7_2 = numberObject(184, 453)
box7_3 = numberObject(250, 453)
box7_4 = numberObject(327, 453)
box7_5 = numberObject(392, 453)
box7_6 = numberObject(461, 453)
box7_7 = numberObject(532, 453)
box7_8 = numberObject(601, 453)
box7_9 = numberObject(668, 453)

box8_1 = numberObject(113, 525)
box8_2 = numberObject(184, 525)
box8_3 = numberObject(250, 525)
box8_4 = numberObject(327, 525)
box8_5 = numberObject(392, 525)
box8_6 = numberObject(461, 525)
box8_7 = numberObject(532, 525)
box8_8 = numberObject(601, 525)
box8_9 = numberObject(668, 525)

box9_1 = numberObject(113, 595)
box9_2 = numberObject(184, 595)
box9_3 = numberObject(250, 595)
box9_4 = numberObject(327, 595)
box9_5 = numberObject(392, 595)
box9_6 = numberObject(461, 595)
box9_7 = numberObject(532, 595)
box9_8 = numberObject(601, 595)
box9_9 = numberObject(668, 595)
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
            break
        if e.type == pygame.MOUSEBUTTONDOWN:
            posX, posY = pygame.mouse.get_pos()
            solveButton.is_pressed(posX, posY)
            resetButton.is_pressed(posX, posY)
            if not isPressed:
                coordinate_checker(posX, posY)
            if isPressed:
                if not solveButton.error_checker(solveButton.make_grid()):
                    if solveButton.solve(grid):
                        # solveButton.print_grid(grid)
                        solveButton.show_solution(grid)
                        # Make all tiles true
                        b1_1 = True
                        b1_2 = True
                        b1_3 = True
                        b1_4 = True
                        b1_5 = True
                        b1_6 = True
                        b1_7 = True
                        b1_8 = True
                        b1_9 = True

                        b2_1 = True
                        b2_2 = True
                        b2_3 = True
                        b2_4 = True
                        b2_5 = True
                        b2_6 = True
                        b2_7 = True
                        b2_8 = True
                        b2_9 = True

                        b3_1 = True
                        b3_2 = True
                        b3_3 = True
                        b3_4 = True
                        b3_5 = True
                        b3_6 = True
                        b3_7 = True
                        b3_8 = True
                        b3_9 = True

                        b4_1 = True
                        b4_2 = True
                        b4_3 = True
                        b4_4 = True
                        b4_5 = True
                        b4_6 = True
                        b4_7 = True
                        b4_8 = True
                        b4_9 = True

                        b5_1 = True
                        b5_2 = True
                        b5_3 = True
                        b5_4 = True
                        b5_5 = True
                        b5_6 = True
                        b5_7 = True
                        b5_8 = True
                        b5_9 = True

                        b6_1 = True
                        b6_2 = True
                        b6_3 = True
                        b6_4 = True
                        b6_5 = True
                        b6_6 = True
                        b6_7 = True
                        b6_8 = True
                        b6_9 = True

                        b7_1 = True
                        b7_2 = True
                        b7_3 = True
                        b7_4 = True
                        b7_5 = True
                        b7_6 = True
                        b7_7 = True
                        b7_8 = True
                        b7_9 = True

                        b8_1 = True
                        b8_2 = True
                        b8_3 = True
                        b8_4 = True
                        b8_5 = True
                        b8_6 = True
                        b8_7 = True
                        b8_8 = True
                        b8_9 = True

                        b9_1 = True
                        b9_2 = True
                        b9_3 = True
                        b9_4 = True
                        b9_5 = True
                        b9_6 = True
                        b9_7 = True
                        b9_8 = True
                        b9_9 = True
                    else:
                        no_solution = True
        screen.fill((176,224,230))
        #screen.fill((255, 255, 255))
        gbbb.draw()
        gblb.draw()
        solveButton.draw()
        resetButton.draw()

        # logic checks for objects

        if b1_1:
            box1_1.draw(box1_1.get_num())
        if b1_2:
            box1_2.draw(box1_2.get_num())
        if b1_3:
            box1_3.draw(box1_3.get_num())
        if b1_4:
            box1_4.draw(box1_4.get_num())
        if b1_5:
            box1_5.draw(box1_5.get_num())
        if b1_6:
            box1_6.draw(box1_6.get_num())
        if b1_7:
            box1_7.draw(box1_7.get_num())
        if b1_8:
            box1_8.draw(box1_8.get_num())
        if b1_9:
            box1_9.draw(box1_9.get_num())

        if b2_1:
            box2_1.draw(box2_1.get_num())
        if b2_2:
            box2_2.draw(box2_2.get_num())
        if b2_3:
            box2_3.draw(box2_3.get_num())
        if b2_4:
            box2_4.draw(box2_4.get_num())
        if b2_5:
            box2_5.draw(box2_5.get_num())
        if b2_6:
            box2_6.draw(box2_6.get_num())
        if b2_7:
            box2_7.draw(box2_7.get_num())
        if b2_8:
            box2_8.draw(box2_8.get_num())
        if b2_9:
            box2_9.draw(box2_9.get_num())

        if b3_1:
            box3_1.draw(box3_1.get_num())
        if b3_2:
            box3_2.draw(box3_2.get_num())
        if b3_3:
            box3_3.draw(box3_3.get_num())
        if b3_4:
            box3_4.draw(box3_4.get_num())
        if b3_5:
            box3_5.draw(box3_5.get_num())
        if b3_6:
            box3_6.draw(box3_6.get_num())
        if b3_7:
            box3_7.draw(box3_7.get_num())
        if b3_8:
            box3_8.draw(box3_8.get_num())
        if b3_9:
            box3_9.draw(box3_9.get_num())

        if b4_1:
            box4_1.draw(box4_1.get_num())
        if b4_2:
            box4_2.draw(box4_2.get_num())
        if b4_3:
            box4_3.draw(box4_3.get_num())
        if b4_4:
            box4_4.draw(box4_4.get_num())
        if b4_5:
            box4_5.draw(box4_5.get_num())
        if b4_6:
            box4_6.draw(box4_6.get_num())
        if b4_7:
            box4_7.draw(box4_7.get_num())
        if b4_8:
            box4_8.draw(box4_8.get_num())
        if b4_9:
            box4_9.draw(box4_9.get_num())

        if b5_1:
            box5_1.draw(box5_1.get_num())
        if b5_2:
            box5_2.draw(box5_2.get_num())
        if b5_3:
            box5_3.draw(box5_3.get_num())
        if b5_4:
            box5_4.draw(box5_4.get_num())
        if b5_5:
            box5_5.draw(box5_5.get_num())
        if b5_6:
            box5_6.draw(box5_6.get_num())
        if b5_7:
            box5_7.draw(box5_7.get_num())
        if b5_8:
            box5_8.draw(box5_8.get_num())
        if b5_9:
            box5_9.draw(box5_9.get_num())

        if b6_1:
            box6_1.draw(box6_1.get_num())
        if b6_2:
            box6_2.draw(box6_2.get_num())
        if b6_3:
            box6_3.draw(box6_3.get_num())
        if b6_4:
            box6_4.draw(box6_4.get_num())
        if b6_5:
            box6_5.draw(box6_5.get_num())
        if b6_6:
            box6_6.draw(box6_6.get_num())
        if b6_7:
            box6_7.draw(box6_7.get_num())
        if b6_8:
            box6_8.draw(box6_8.get_num())
        if b6_9:
            box6_9.draw(box6_9.get_num())

        if b7_1:
            box7_1.draw(box7_1.get_num())
        if b7_2:
            box7_2.draw(box7_2.get_num())
        if b7_3:
            box7_3.draw(box7_3.get_num())
        if b7_4:
            box7_4.draw(box7_4.get_num())
        if b7_5:
            box7_5.draw(box7_5.get_num())
        if b7_6:
            box7_6.draw(box7_6.get_num())
        if b7_7:
            box7_7.draw(box7_7.get_num())
        if b7_8:
            box7_8.draw(box7_8.get_num())
        if b7_9:
            box7_9.draw(box7_9.get_num())

        if b8_1:
            box8_1.draw(box8_1.get_num())
        if b8_2:
            box8_2.draw(box8_2.get_num())
        if b8_3:
            box8_3.draw(box8_3.get_num())
        if b8_4:
            box8_4.draw(box8_4.get_num())
        if b8_5:
            box8_5.draw(box8_5.get_num())
        if b8_6:
            box8_6.draw(box8_6.get_num())
        if b8_7:
            box8_7.draw(box8_7.get_num())
        if b8_8:
            box8_8.draw(box8_8.get_num())
        if b8_9:
            box8_9.draw(box8_9.get_num())

        if b9_1:
            box9_1.draw(box9_1.get_num())
        if b9_2:
            box9_2.draw(box9_2.get_num())
        if b9_3:
            box9_3.draw(box9_3.get_num())
        if b9_4:
            box9_4.draw(box9_4.get_num())
        if b9_5:
            box9_5.draw(box9_5.get_num())
        if b9_6:
            box9_6.draw(box9_6.get_num())
        if b9_7:
            box9_7.draw(box9_7.get_num())
        if b9_8:
            box9_8.draw(box9_8.get_num())
        if b9_9:
            box9_9.draw(box9_9.get_num())
        if no_solution:
            solveButton.no_solution()
        if is_pressed_reset:
            isPressed = False
            is_pressed_reset = False
            no_solution = False

            b1_1 = False
            b1_2 = False
            b1_3 = False
            b1_4 = False
            b1_5 = False
            b1_6 = False
            b1_7 = False
            b1_8 = False
            b1_9 = False

            b2_1 = False
            b2_2 = False
            b2_3 = False
            b2_4 = False
            b2_5 = False
            b2_6 = False
            b2_7 = False
            b2_8 = False
            b2_9 = False

            b3_1 = False
            b3_2 = False
            b3_3 = False
            b3_4 = False
            b3_5 = False
            b3_6 = False
            b3_7 = False
            b3_8 = False
            b3_9 = False

            b4_1 = False
            b4_2 = False
            b4_3 = False
            b4_4 = False
            b4_5 = False
            b4_6 = False
            b4_7 = False
            b4_8 = False
            b4_9 = False

            b5_1 = False
            b5_2 = False
            b5_3 = False
            b5_4 = False
            b5_5 = False
            b5_6 = False
            b5_7 = False
            b5_8 = False
            b5_9 = False

            b6_1 = False
            b6_2 = False
            b6_3 = False
            b6_4 = False
            b6_5 = False
            b6_6 = False
            b6_7 = False
            b6_8 = False
            b6_9 = False

            b7_1 = False
            b7_2 = False
            b7_3 = False
            b7_4 = False
            b7_5 = False
            b7_6 = False
            b7_7 = False
            b7_8 = False
            b7_9 = False

            b8_1 = False
            b8_2 = False
            b8_3 = False
            b8_4 = False
            b8_5 = False
            b8_6 = False
            b8_7 = False
            b8_8 = False
            b8_9 = False

            b9_1 = False
            b9_2 = False
            b9_3 = False
            b9_4 = False
            b9_5 = False
            b9_6 = False
            b9_7 = False
            b9_8 = False
            b9_9 = False

            box1_1.num_reset(None)
            box1_2.num_reset(None)
            box1_3.num_reset(None)
            box1_4.num_reset(None)
            box1_5.num_reset(None)
            box1_6.num_reset(None)
            box1_7.num_reset(None)
            box1_8.num_reset(None)
            box1_9.num_reset(None)

            box2_1.num_reset(None)
            box2_2.num_reset(None)
            box2_3.num_reset(None)
            box2_4.num_reset(None)
            box2_5.num_reset(None)
            box2_6.num_reset(None)
            box2_7.num_reset(None)
            box2_8.num_reset(None)
            box2_9.num_reset(None)

            box3_1.num_reset(None)
            box3_2.num_reset(None)
            box3_3.num_reset(None)
            box3_4.num_reset(None)
            box3_5.num_reset(None)
            box3_6.num_reset(None)
            box3_7.num_reset(None)
            box3_8.num_reset(None)
            box3_9.num_reset(None)

            box4_1.num_reset(None)
            box4_2.num_reset(None)
            box4_3.num_reset(None)
            box4_4.num_reset(None)
            box4_5.num_reset(None)
            box4_6.num_reset(None)
            box4_7.num_reset(None)
            box4_8.num_reset(None)
            box4_9.num_reset(None)

            box5_1.num_reset(None)
            box5_2.num_reset(None)
            box5_3.num_reset(None)
            box5_4.num_reset(None)
            box5_5.num_reset(None)
            box5_6.num_reset(None)
            box5_7.num_reset(None)
            box5_8.num_reset(None)
            box5_9.num_reset(None)

            box6_1.num_reset(None)
            box6_2.num_reset(None)
            box6_3.num_reset(None)
            box6_4.num_reset(None)
            box6_5.num_reset(None)
            box6_6.num_reset(None)
            box6_7.num_reset(None)
            box6_8.num_reset(None)
            box6_9.num_reset(None)

            box7_1.num_reset(None)
            box7_2.num_reset(None)
            box7_3.num_reset(None)
            box7_4.num_reset(None)
            box7_5.num_reset(None)
            box7_6.num_reset(None)
            box7_7.num_reset(None)
            box7_8.num_reset(None)
            box7_9.num_reset(None)

            box8_1.num_reset(None)
            box8_2.num_reset(None)
            box8_3.num_reset(None)
            box8_4.num_reset(None)
            box8_5.num_reset(None)
            box8_6.num_reset(None)
            box8_7.num_reset(None)
            box8_8.num_reset(None)
            box8_9.num_reset(None)

            box9_1.num_reset(None)
            box9_2.num_reset(None)
            box9_3.num_reset(None)
            box9_4.num_reset(None)
            box9_5.num_reset(None)
            box9_6.num_reset(None)
            box9_7.num_reset(None)
            box9_8.num_reset(None)
            box9_9.num_reset(None)

        pygame.display.update()
        clock.tick(60)
        continue
pygame.quit()
