# Tic Tac Toe ver.1.0
# By Ridam Shrestha
# https://github.com/robinstark369

import pygame, sys, random, time
from pygame.locals import *

# Initialize
pygame.init()
WIN_SIZE = (640, 480)
main_clock = pygame.time.Clock()
window = pygame.display.set_mode(WIN_SIZE)
pygame.display.set_caption('Tic Tac Toe')
cursor_pos = [100, 85, 100, 100]  # Cursor position
cursor = pygame.Rect(cursor_pos)

# colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (77, 77, 77)

# Font
font = pygame.font.Font('Roboto-Light.ttf', 50)
top_render = font.render('Tic Tac Toe', True, white)

# Images
X = pygame.image.load('X.png').convert()
X.set_colorkey(black)
O = pygame.image.load('O1.png').convert()
O.set_colorkey(black)

board_images = []  # Board images position List
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
particles = []  # particles effect
cubes = []  # flying cube background
turn = 1  # if odd then user input
running = True

# Function to render the board
def can_win(board, i, j):
    b1 = board
    b1[i][j] == 'X'
    if check(board, 'X') == 'X':
        return True

def comp_move(board):
    global board_images
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                if can_win():
                    board[i][j] = 'O'
                    x,y = 100+i*160, 85+j*140
                    board_images.append(x+16, y+16)
          
                
def draw_board():
    board = pygame.image.load('tic_tac_toe.png').convert()
    board.set_colorkey(black)
    window.blit(board, (0, 0))
    for image in board_images:
        if image[1] == 0:
            window.blit(X, image[0])
        elif image[1] == 1:
            window.blit(O, image[0])

def draw_cursor():
    cursor_color = (200, 100, 150, 150)
    pygame.draw.rect(window, cursor_color, cursor, 100, 4)

def draw(player):  # draws X and O in the selected region
    global turn
    draw_player = True
    if player == 'X':
        drawn_pos = (cursor[0] + 16, cursor[1] + 16)
        for image in board_images:
            if image[0] == drawn_pos:
                draw_player = False
        if draw_player:
            window.blit(X, drawn_pos)
            board_images.append([drawn_pos, 0])
            turn += 1
    if player == 'O':
        drawn_pos = (cursor[0] + 16, cursor[1] + 16)
        for image in board_images:
            if image[0] == drawn_pos:
                draw_player = False
        if draw_player:
            window.blit(O, drawn_pos)
            board_images.append([drawn_pos,1])   
            turn += 1  

def board_update(player):
    if player == 'X':
        x = int(cursor_pos[0] / 100) - 1
        y = int(cursor_pos[1] / 85) - 1
        if x == 3:
            x = 2
        if y == 3:
            y = 2

        print(x, y)
        if board[x][y] == 0:
            board[x][y] = player
        print(board)
    
    elif player == 'O':
        x = int(cursor_pos[0] / 100) - 1
        y = int(cursor_pos[1] / 85) - 1
        if x == 3:
            x = 2
        if y == 3:
            y = 2

        print(x, y)
        if board[x][y] == 0:
            board[x][y] = player
        print(board)

def move_cursor(key):
    global turn
    if (key == K_w or key == K_UP) and cursor_pos[1] >= 100:
        cursor_pos[1] -= 140
        cursor.update(cursor_pos)

    if (key == K_a or key == K_LEFT) and cursor_pos[0] > 100:
        cursor_pos[0] -= 160
        cursor.update(cursor_pos)

    if (key == K_s or key == K_DOWN) and cursor_pos[1] <= 300:
        cursor_pos[1] += 140
        cursor.update(cursor_pos)

    if (key == K_d or key == K_RIGHT) and cursor_pos[0] <= 300:
        cursor_pos[0] += 160
        cursor.update(cursor_pos)

    if key == K_RETURN:
        if turn % 2 != 0:
            board_update('X')
            draw('X')
        elif turn % 2 == 0:
            board_update('O')
            draw('O')
        
def background_animation(x, y): #Function for square animation
                                # [x,y,w,h] [x_vel, y_vel] [width]
    width = 50
    height = 50

    cubes.append(
        [
            [x, y, width, height],
            [random.randint(-20, 20) / 10 * -1, random.randint(-20, 20) / 10 * -1],
            random.randint(5, 15),
        ]
    )

def particle_effect(x, y): #Function for particle animation
    particles.append(
        [
            [x, y],
            [random.randint(-20, 20) / 10 * -1, random.randint(-20, 20) / 10 * -1],
            random.randint(50, 60),
        ]
    )

    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.2
        pygame.draw.circle(
            window, gray, [int(particle[0][0]), int(particle[0][1])], int(particle[2])
        )
    if particle[2] <= 0:
        particles.remove(particle)

    for cube in cubes:
        cube[0][0] += cube[1][0]
        cube[0][1] += cube[1][1]
        cube[2] -= 0.05
        pygame.draw.rect(
            window,
            gray,
            [int(cube[0][0]), int(cube[0][1]), int(cube[0][2]), int(cube[0][3])],
            int(cube[2]),
        )
        if cube[2] <= 0:
            cubes.remove(cube)

def draw_end_screen(message):
    global font
    f1 = pygame.font.Font('Roboto-Light.ttf', 100)
    end_screen = f1.render(message, True, white)
    restart = font.render('press Space', True, white)
    window.blit(end_screen, (165, 195))
    window.blit(restart, (180, 400))

def check(board, player): #Checks the board whether for win cases
    winner = ''
    valx = {
        0 : 0,
        1 : 0,
        2 : 0
    }
    valy = {
        0 : 0,
        1 : 0,
        2 : 0
    }
    x = []
    y = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == player:
                x.append(i)
                y.append(j)
    for i in x:
        valx[i] += 1
    for i in y:
        valy[i] += 1

    if valx[0] == 3 or valx[1] == 3 or valx[2] == 3:
        winner = player
    elif valy[0] == 3 or valy[1] == 3 or valy[2] == 3:
        winner = player
    elif board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        winner = board[0][0]
    elif board[2][0] == board[1][1] and board[2][0] == board[0][2]:
        winner = board[2][0]
    return winner

def run():
    global running, board, board_images, turn
    is_full = True
    window.fill(black)
    background_animation(0, WIN_SIZE[1] * 1.5)
    background_animation(WIN_SIZE[0], WIN_SIZE[1] * -0.5)
    particle_effect(0, 0)
    particle_effect(WIN_SIZE[1] + 100, WIN_SIZE[1])
    window.blit(top_render, (185, 15))
    if running:
        draw_board()
        draw_cursor()

    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                is_full = False

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            move_cursor(event.key)

            if event.key == K_SPACE:
                board = [[0,0,0],[0,0,0],[0,0,0]]
                board_images = []
                turn = 1
                running = True


    if check(board,'X') == 'X':
        draw_end_screen('X WINS')
        pygame.display.update()
        running = False

    elif check(board,'O') == 'O':
        draw_end_screen('O WINS')
        pygame.display.update()
        running = False
    
    elif is_full:
        draw_end_screen('DRAW')
        pygame.display.update()
        running = False
    
    pygame.display.update()
    main_clock.tick(60)

# Main game loop:

while True:
    run()
