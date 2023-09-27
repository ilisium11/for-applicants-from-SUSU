import pygame as pg
from class_wheel import Wheel
from class_button import Button


class TopDirections:

    def __init__(self,surface,count_button,directions):
        self.height_area_special = 650
        self.area_special = pg.Surface((600, self.height_area_special))
        self.area_special.fill((239, 228, 176))
        self.surface=surface
        height_area_button = (2 * count_button + 1) * 100
        self.area_button = pg.Surface((600, height_area_button))
        self.area_button.fill((239, 228, 176))
        self.buttons = []
        k = 0
        for i in directions:
            self.buttons.append(Button(self.area_button, 300, (150 + k * 200), i, directions[i]))
            k += 1
        self.difference = height_area_button - self.height_area_special
        self.kf = 0
        self.area_special.blit(self.area_button, (0,0))
        self.wheel=Wheel(surface,630,100,700)

    def clicking_buttons(self,mouse):
        dif = -self.kf * self.difference
        for i in self.buttons:
            if i.collide((mouse[0], mouse[1] - dif)):
                return i.direction

    def moving_wheel(self,mouse):
        ret = self.wheel.draw(mouse)
        if ret:
            self.area_special.blit(self.area_button, (0, -ret * self.difference))
            self.kf = ret

    def stop_wheel(self):
        self.wheel.mouse=False

    def clicking_wheel(self,mouse):
        return self.wheel.clicking_mouse(mouse)

    def draw(self):
        self.surface.blit(self.area_special,(0,0))

