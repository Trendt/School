import pygame
from trafficLight import TrafficLightPyGame
from time import sleep

pygame.init()

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)

DIMENSIONS = (800, 800)

screen = pygame.display.set_mode(DIMENSIONS)
screen.fill((60,60,60))

running = True

trafficLight = TrafficLightPyGame(True, False, False, 50, 50, 100, 300)
trafficLight.setNightMode(True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    trafficLight.shift()
    trafficLight.drawObjects(screen)
    pygame.display.flip()

    sleep(1)        
