import sys

import pygame as pg


class AreaSearch:
    font = pg.font.Font('font/new_font.ttf', 40)

    def __init__(self,surface:pg.Surface,size:tuple,center:tuple):
        self.text=''
        self.color=(150,150,150)
        self.color1=(0,150,0)
        self.actual_color=self.color
        self.surface = surface
        self.surf=pg.Surface(size)
        self.surf.fill(self.color)
        self.rect=self.surf.get_rect(center=center)
        self.mouse=False
        self.dict_key={}
        self.list_key=[j for j in range(48,58)]
        for i in self.list_key:
            self.dict_key[i]=pg.key.name(i)

    def clicking_mouse(self,mouse):
        if self.rect.collidepoint(mouse):
            self.actual_color=self.color1
            self.set_text()
            self.mouse=True
            return True
        else:
            if self.mouse:
                self.actual_color=self.color
                self.set_text()
                self.mouse=False
            return False

    def set_text(self):
        self.surf.fill(self.actual_color)
        text = self.font.render(self.text, 1, (215, 145, 0))
        self.surf.blit(text, text.get_rect(center=(self.surf.get_width() / 2, self.surf.get_height() / 2)))

    def get_text(self):
        return self.text

    def input_text(self,key):
        if self.mouse:
            if key in self.list_key:
                self.text+=self.dict_key[key]
                self.set_text()
            elif key==8:
                self.text=self.text[:-1]
                self.set_text()

    def draw(self):
        self.surface.blit(self.surf,self.rect)