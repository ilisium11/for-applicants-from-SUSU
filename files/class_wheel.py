import pygame as pg


class Wheel:
    image=pg.image.load('images/wheel.png').convert()
    image=image.convert()
    image.set_colorkey((255,255,255))
    width=image.get_width()
    height=image.get_height()

    def __init__(self,surface:pg.Surface,center_x,low_border,high_border):
        self.surface=surface
        self.low_border=low_border
        self.high_border=high_border
        self.len_path=abs(high_border-low_border)
        self.pos_center=[center_x,low_border]
        self.rect=pg.Rect(self.pos_center[0]-self.width/2,self.pos_center[1]-self.height/2,self.width,self.height)
        self.mouse=False

    def clicking_mouse(self,mouse:tuple):
        if self.rect.collidepoint(mouse):
            self.mouse=True
            return True

    def change_pos(self,mouse):
        if mouse[1]<self.low_border:
            self.pos_center[1]=self.low_border
        elif mouse[1]>self.high_border:
            self.pos_center[1]=self.high_border
        else:
            self.pos_center[1]=mouse[1]
        self.rect.y=self.pos_center[1]-self.height/2

    def draw(self,mouse):
        if self.mouse:
            self.change_pos(mouse)
            self.surface.blit(self.image, (self.image.get_rect(center=self.pos_center)))
            kf=(self.pos_center[1]-self.low_border)/self.len_path
            return kf
        self.surface.blit(self.image,(self.image.get_rect(center=self.pos_center)))


