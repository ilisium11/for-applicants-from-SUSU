import pygame as pg


class MenuButton:
    font_size=36
    font=pg.font.Font('font/new_font.ttf',font_size)
    image=pg.image.load('images/menu_button.png').convert()
    image=pg.transform.scale(image,(400,50))
    image.set_colorkey((255,255,255))

    def __init__(self,surface,text,pos):
        self.surface=surface
        self.pos=pos
        self.img=self.image.copy()
        tx=self.font.render(text,1,(200,0,0))
        self.rect=pg.Rect(self.pos[0]-self.img.get_width()/2,self.pos[1]-self.img.get_height()/2,self.img.get_width(),self.img.get_height())
        self.img.blit(tx,tx.get_rect(center=(self.img.get_width()/2,self.img.get_height()/2)))

    def collide(self,mouse):
        if self.rect.collidepoint(mouse):
            return True

    def draw(self):
        self.surface.blit(self.img,self.img.get_rect(center=self.pos))
