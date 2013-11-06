import pygame
import pygame.mouse

black   = (   0,   0,   0)
white   = ( 255, 255, 255)
red     = ( 255,   0,   0)

pygame.init()

size = [1000,600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TicTacToe")

done = False
fill = []
for row in range(10):
    fill.append([])
    for column in range(10):
        fill[row].append(0)
player = 1

clock = pygame.time.Clock()

def f_draw():
    j = row * 200
    i = column * 200
    if mouse_x > i and mouse_x < i+200 and mouse_y > j and mouse_y < j+200:
        if fill[row][column] == 2:
            print("fill: ", fill[row][column], row, column)
            pygame.draw.line(screen, black, [i+30,j+30], [i+170,j+170], 3)
            pygame.draw.line(screen, black, [i+170,j+30], [i+30,j+170], 3)
        elif fill[row][column] == 1:
            pygame.draw.circle(screen, black, [i+100, j+100], 70, 3)

screen.fill(white)


#------Main Loop------
while done == False:
    draw = False
    #Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                mouse_x = pos[0]
                mouse_y = pos[1]
                row = mouse_y/200
                column = mouse_x/200
                print("Pos, ", pos, "Row, ", row, "Column, ", column)
                if player == 1 and fill[row][column] == 0:
                    fill[row][column] = 2
                    player = 0
                elif player == 0 and fill[row][column] == 0:
                    fill[row][column] = 1
                    player = 1

    #Game Logic

    #Code to draw
    for row in range(3):
        for column in range(3):
            if fill[row][column] == 1 or fill[row][column] == 2:
                f_draw()

    #Draw board
    pygame.draw.rect(screen, black, [0,0,600,600], 5)
    pygame.draw.line(screen, black, [200,0], [200,600], 5)
    pygame.draw.line(screen, black, [400,0], [400,600], 5)
    pygame.draw.line(screen, black, [0,200], [600,200], 5)
    pygame.draw.line(screen, black, [0,400], [600,400], 5)

    #Draw button
    pygame.draw.rect(screen, black, [650, 100, 250, 100], 2)

    #Update screen
    pygame.display.flip()


    #FPS limit
    clock.tick(20)

pygame.quit()

