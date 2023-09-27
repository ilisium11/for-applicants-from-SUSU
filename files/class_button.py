import pygame as pg


class Button:
    font_size=24
    font=pg.font.Font('font/new_font.ttf',font_size)
    image=pg.image.load('images/button.png').convert()
    image.set_colorkey((255,255,255))
    width,height=image.get_width(),image.get_height()
    area_text=pg.Surface((image.get_width()*0.96,image.get_height()*0.9))
    area_text.fill((200,191,231))

    def __init__(self,surface,center_x,center_y,name,direction):
        self.pos=[center_x,center_y]
        self.direction=direction
        st=''
        for i in name:
            st+=i
            if len(st)*self.font_size/2>self.area_text.get_width()*1.05:
                st=st[:-1]
                break
        text=self.font.render(st,True,(127,127,127))
        self.area_tx=self.area_text.copy()
        self.img=self.image.copy()
        self.area_tx.blit(text,text.get_rect(center=(self.area_tx.get_width()/2,self.area_tx.get_height()/2)))
        self.img.blit(self.area_tx,self.area_tx.get_rect(center=(self.width/2,self.height/2)))
        self.rect=pg.Rect(center_x-self.width/2,center_y-self.height/2,self.width,self.height)
        surface.blit(self.img,self.img.get_rect(center=(center_x,center_y)))

    def collide(self,mouse):
        if self.rect.collidepoint(mouse):
            return True
