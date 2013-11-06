import pygame

black   = (   0,   0,   0)
white   = ( 255, 255, 255)

pygame.init()

size = [700,500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("TicTacToe")

done = False

clock = pygame.time.Clock()

#------Main Loop------
while done == False:
    #Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #Game Logic

    #Code to draw
    screen.fill(white)
    pygame.draw.line black
    #Update screen
    pygame.display.flip()

    #FPS limit
    clock.tick(20)

pygame.quit()

