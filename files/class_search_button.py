import pygame as pg


class SearchButton:
    image_false = pg.image.load('images/search.png').convert()
    image_false.set_colorkey((255, 255, 255))
    image_true = pg.image.load('images/search_mouse.png').convert()
    image_true.set_colorkey((255,255,255))
    width,height=image_false.get_width(),image_false.get_height()

    def __init__(self,surface,pos:tuple):
        self.surface=surface
        self.image_false=SearchButton.image_false.copy()
        self.image_true=SearchButton.image_true.copy()
        self.actual_image=self.image_false.copy()
        self.status=False
        self.rect=pg.Rect(pos[0]-self.width/2,pos[1]-self.height/2,self.width,self.height)

    def check_mouse(self,mouse:tuple):
        if self.rect.collidepoint(mouse):
            if not self.status:
                self.actual_image=self.image_true.copy()
                self.status=True
        else:
            if self.status:
                self.actual_image=self.image_false.copy()
                self.status=False

    def clicking_mouse(self,mouse):
        if self.rect.collidepoint(mouse):
            return True

    def draw(self):
        self.surface.blit(self.actual_image,self.rect)

