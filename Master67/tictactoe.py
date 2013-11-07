import pygame

black = (   0,   0,   0)
white = ( 255, 255, 255)
red   = ( 255,   0,   0)

pygame.init()

size = [600, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TicTacToe")

playing = True

tot_dim = 600
dim = 200
border = 5

#I'm BAD with multidimensional arrays
fill = []
for row in range(4):
# Add an empty array that will hold each cell
# in this row
    fill.append([])
    for col in range(4):
        fill[row].append(0)  # Append a cell

turn = 0
nr = 0

clock = pygame.time.Clock()


def draw_board():
    pygame.draw.rect(screen, black, [0, 0, 600, 600], border)

    for i in range(1, 3):
        pygame.draw.line(screen, black, [dim*i, 0], [dim*i, tot_dim], border)
        pygame.draw.line(screen, black, [0, dim*i], [tot_dim, dim*i], border)


def draw_marks():
    for i in range(1, 4, 1):
        for j in range(1, 4, 1):
            if fill[j][i] == 1:
                pygame.draw.line(screen, black, [(i-1)*dim+30, (j-1)*dim+30], [i*dim-30, j*dim-30], 3)
                pygame.draw.line(screen, black, [(i-1)*dim+30, j*dim-30], [i*dim-30, (j-1)*dim+30], 3)
            elif fill[j][i] == 2:
                pygame.draw.circle(screen, black, [(i-1)*dim+100, (j-1)*dim+100], 70, 3)


def check_end():
    for i in range(1, 4):
        if fill[i][1] == fill[i][2] == fill[i][3] and fill[i][1] != 0:
            pygame.draw.line(screen, red, [10, i*dim-100], [tot_dim-10, i*dim-100], 7)
            return 1
        if fill[1][i] == fill[2][i] == fill[3][i] and fill[1][i] != 0:
            pygame.draw.line(screen, red, [i*dim-100, 10], [i*dim-100, tot_dim-10], 7)
            return 1
    if fill[1][1] == fill[2][2] == fill[3][3] and fill[1][1] != 0:
        pygame.draw.line(screen, red, [10, 10], [tot_dim-10, tot_dim-10], 7)
        return 1
    if fill[1][3] == fill[2][2] == fill[3][1] and fill[2][2] != 0:
        pygame.draw.line(screen, red, [tot_dim-10, 10], [10, tot_dim-10], 7)
        return 1
    if nr == 9:
        return 1


while playing:
    #Event processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = pos[0] // dim + 1
            row = pos[1] // dim + 1
            if turn % 2 == 0 and fill[row][col] == 0:
                fill[row][col] = 1
                turn += 1
                nr += 1
            elif turn % 2 == 1 and fill[row][col] == 0:
                fill[row][col] = 2
                turn += 1
                nr += 1

    #Code to draw
    screen.fill(white)
    draw_board()
    draw_marks()
    if check_end() or nr == 9:
        pygame.display.flip()
        pygame.time.wait(2000)
        for i in range(4):
            for j in range(4):
                fill[i][j] = 0

    #Update screen
    pygame.display.flip()

    #FPS limit
    clock.tick(20)

pygame.quit()
