from pygame.locals import *
import pygame
import numpy as np
import time
import sys

pygame.init()
width, height = 800, 800
bg = 25, 25, 25

screen = pygame.display.set_mode((height, width))
pygame.display.set_caption("Juego de la vida")

screen.fill(bg)

nxC, nyC = 100, 100

gameState = np.zeros((nxC, nyC))

dimCW = width / nxC
dimCH = height/nyC

gameState[38, 20] = 1
gameState[39, 20] = 1
gameState[40, 20] = 1
gameState[60, 20] = 1
gameState[61, 20] = 1
gameState[59, 20] = 1

# Runner 1
gameState[10,5] = 1
gameState[12,5] = 1
gameState[11,6] = 1
gameState[12,6] = 1
gameState[11,7] = 1
#Runner 2
gameState[5,10] = 1
gameState[5,12] = 1
gameState[6,11] = 1
gameState[6,12] = 1
gameState[7,11] = 1
#Box 1
gameState[18,15] = 1
gameState[17,16] = 1
gameState[17,15] = 1
gameState[18,16] = 1
#Serpent 1
gameState[30,20] = 1
gameState[31,20] = 1
gameState[32,20] = 1
gameState[32,19] = 1
gameState[33,19] = 1
gameState[34,19] = 1

pauseExect=False

while True:
    newGameState = np.copy(gameState)
   
    screen.fill(bg)

    ev = pygame.event.get()

    for event in ev:
        #detectamos si se pulsa una tecla

        keys = pygame.key.get_pressed()
        if keys[K_p]:     
            pauseExect = not pauseExect

        if keys[K_ESCAPE]:         
                pygame.quit()
                sys.exit()

        #Detectamos si se presiona el raton

        mouseClick= pygame.mouse.get_pressed()

        if sum(mouseClick)>0:
            posX,posY = pygame.mouse.get_pos()
            celX, celY = int(np.floor(posX/dimCW)), int(np.floor(posY/dimCH))
            newGameState[celX,celY]=1

        for y in range(0,nxC):
            for x in range (0,nyC):

                if not pauseExect:
                    #calculamos los vecinos cercanos
                    n_neigh =   gameState[(x - 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x)     % nxC, (y - 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y - 1)  % nyC] + \
                            gameState[(x - 1) % nxC, (y)      % nyC] + \
                            gameState[(x + 1) % nxC, (y)      % nyC] + \
                            gameState[(x - 1) % nxC, (y + 1)  % nyC] + \
                            gameState[(x)     % nxC, (y + 1)  % nyC] + \
                            gameState[(x + 1) % nxC, (y + 1)  % nyC]
                                      
                    #Regla #1: Una celda muerta con exactamente 4 vecinas vivas,"revive"

                    if gameState[x,y]==0 and n_neigh ==3:
                        newGameState[x,y]=1
                    #Regla #2 : una celda viva con menos de 2 03 vecinas vivas,"muere"
                    elif gameState[x,y] == 1 and (n_neigh<2 or n_neigh>3):
                        newGameState[x,y]=0
                  # Calculamos el polígono que forma la celda.
                poly = [((x)   * dimCW, y * dimCH),
                        ((x+1) * dimCW, y * dimCH),
                        ((x+1) * dimCW, (y+1) * dimCH),
                        ((x)   * dimCW, (y+1) * dimCH)]
                # Si la celda está "muerta" pintamos un recuadro con borde gris
                if newGameState[x, y] == 0:
                    pygame.draw.polygon(screen, (40, 40, 40), poly, 1)
                # Si la celda está "viva" pintamos un recuadro relleno de color
                else:
                    pygame.draw.polygon(screen, (200, 100, 100), poly, 0)
    
        gameState = np.copy(newGameState)
        pygame.display.flip()