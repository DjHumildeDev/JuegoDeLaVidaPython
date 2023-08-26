import pygame
import numpy as np 
import time

pygame.init()
width,height = 400,400
bg = 25,25,25

screen = pygame.display.set_mode((height,width))
screen.fill(bg)

nxC,nyC = 60,60

gameState = np.zeros((nxC, nyC))

dimCW =width /nxC
dimCH =height/nyC