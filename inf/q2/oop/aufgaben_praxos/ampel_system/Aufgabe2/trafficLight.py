from pygame import Rect, Surface
import pygame
from pygameExt import Circle

class TrafficLight(object):
    def __init__(self, startValueRed:bool, startValueYellow:bool, startValueGreen:bool):
        self.setLights(startValueRed, startValueYellow, startValueGreen)

    def setLights(self, valueRed:bool, valueYellow:bool, valueGreen:bool):
        self.lights = (valueRed, valueYellow, valueGreen)

    def getLights(self) -> tuple: 
        return self.lights

    def shift(self):
        if self.lights == (True, False, False):
            self.lights = (True, True, False)

        elif self.lights == (True, True, False):
            self.lights = (False, False, True)

        elif self.lights == (False, False, True):
            self.lights = (False, True, False)

        elif self.lights == (False, True, False):
            self.lights = (True, False, False)

    def __repr__(self) -> str:
        return str(self.lights)

class TrafficLightPyGame(TrafficLight):
    def __init__(self, startValueRed:bool, startValueYellow:bool, startValueGreen:bool, x:int, y:int, width:int, height:int, colorBackground:tuple = (0, 0, 0), colorRed:tuple = (255, 0, 0), colorYellow:tuple = (255, 255, 0), colorGreen:tuple=(0,255,0)):
        super().__init__(startValueRed, startValueYellow, startValueGreen)
        self.coords = (x, y)
        self.width = width
        self.height = height
        self.colorBG = colorBackground
        self.colorLights = ((10,10,10), colorRed, colorYellow, colorGreen)
        
        self.__initObjects__()

    def __initObjects__(self):
        self.objects = (
                    Rect(self.coords[0], self.coords[1], self.width, self.height),
                    Circle(int(self.coords[0] + self.width/2), int(self.coords[1] + self.height/2 - self.height/3), int(self.width/3)),
                    Circle(int(self.coords[0] + self.width/2), int(self.coords[1] + self.height/2), int(self.width/3)),
                    Circle(int(self.coords[0] + self.width/2), int(self.coords[1] + self.height/2 + self.height/3), int(self.width/3))
                )

    def drawObjects(self, surface:Surface):
        pygame.draw.rect(surface, self.colorBG, self.objects[0])

        pygame.draw.circle(surface, self.colorLights[1 if self.lights[0] else 0], self.objects[1].coords, self.objects[1].radius)
        pygame.draw.circle(surface, self.colorLights[2 if self.lights[1] else 0], self.objects[2].coords, self.objects[2].radius)
        pygame.draw.circle(surface, self.colorLights[3 if self.lights[2] else 0], self.objects[3].coords, self.objects[3].radius)
