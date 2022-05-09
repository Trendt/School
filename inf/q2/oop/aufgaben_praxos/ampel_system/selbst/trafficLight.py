from pygame import Rect, Surface
import pygame
from pygameExt import Circle




class TrafficLight(object):
    def __init__(self, startValueRed:bool, startValueYellow:bool, startValueGreen:bool):
        self.setLights(startValueRed, startValueYellow, startValueGreen)
        self.shiftOrder = [
                            (True, False, False), # red
                            (True, True, False),  # red-yellow
                            (False, False, True), # green
                            (False, True, False)  # yellow
                        ]
        self.nightShiftOrder = [
                            (False, True, False),
                            (False, False, False)
                            ]
        self.nightMode = False
        self.currentShift = 0

    def setLights(self, valueRed:bool, valueYellow:bool, valueGreen:bool):
        self.lights = (valueRed, valueYellow, valueGreen)

    def getLights(self) -> tuple: 
        return self.lights

    def setNightMode(self, nightMode:bool = True):
        self.nightMode = nightMode
        if self.nightMode:
            self.currentShift = 0

    def shift(self):
        if not self.nightMode:
            self.currentShift = self.currentShift + 1 if self.currentShift != len(self.shiftOrder)-1 else 0 
            self.lights = self.shiftOrder[self.currentShift]
        else:
            self.currentShift = self.currentShift + 1 if self.currentShift != len(self.nightShiftOrder)-1 else 0 
            self.lights = self.nightShiftOrder[self.currentShift]

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

class PedestrianTrafficLight(TrafficLight):
    def __init__(self, startValueRed:bool, startValueGreen:bool):
        self.setLights(startValueRed, startValueGreen)
        self.shiftOrder = [
                    (True, False),
                    (False, True)
                ]
        self.currentShift = 0

    def setLights(self, valueRed:bool, valueGreen:bool):
        self.lights = (valueRed, valueGreen)

    def getLights(self) -> tuple:
        return self.lights

class PedestrianTrafficLightPyGame(PedestrianTrafficLight):
    def __init__(self, startValueRed:bool, startValueGreen:bool, x:int, y:int, widht:int, height:int, colorBackground:tuple =(0,0,0), colorRed:tuple=(255, 0, 0), colorGreen:tuple=(0, 255, 0), colorOff:tuple = (10, 10, 10)):
        super().__init__(startValueRed, startValueGreen)
        self.coords = (x,y)
        self.width = width
        self.height = height
        self.colorBG = colorBackground
        self.colorLights = (colorOff, colorRed, ColorGreen)

        self.__initObjects__()

    def __initObjects__(self):
        # pygame Objects
        self.objects

        pygame.draw.circle(surface, self.colorLights[3 if self.lights[2] else 0], self.objects[3].coords, self.objects[3].radius)
