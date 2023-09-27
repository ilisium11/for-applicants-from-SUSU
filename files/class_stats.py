import sys
import pygame as pg
from class_menu_button import MenuButton


class Stats:
    font = pg.font.Font('font/new_font.ttf', 32)

    def __init__(self,surface,pos,size,directions):
        self.surface=surface
        self.clock = pg.time.Clock()
        self.area_directions=pg.Surface(size)
        self.area_directions_rect= self.area_directions.get_rect(center=pos)
        self.area_directions.fill((160, 160, 160))
        self.back_button = MenuButton(self.surface, 'Назад',
                                      (self.surface.get_width() * 0.2, self.surface.get_height() * 0.95))
        dict_directions={}
        for direction in directions:
            name=direction.split()[0]
            if name in dict_directions:
                dict_directions[name][0]+=len(directions[direction].get_admission_list())
                dict_directions[name][1]+=directions[direction].get_count_place()
            else:
                dict_directions[name]=[len(directions[direction].get_admission_list()),directions[direction].get_count_place()]
        center_x=0.25*size[0]
        difference_x=0.35*size[0]
        count = 9
        center_y=(1/(count+1))*size[1]
        difference_y=(1/(count+1))*size[1]
        k=0
        k1=0
        for direction in dict_directions:
            text=self.font.render(direction+' Занято '+str(dict_directions[direction][0])+' / Всего '+str(dict_directions[direction][1]),1,(0,100,100))
            self.area_directions.blit(text,text.get_rect(center=(center_x+k1*difference_x,center_y+k*difference_y)))
            k+=1
            if k>8:
                k=0
                k1+=1

    def run(self):
        r=True
        while r:
            mouse = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.back_button.collide(mouse):
                        return True

            self.back_button.draw()
            self.draw()
            self.clock.tick(60)
            pg.display.update()
            self.surface.fill((200, 191, 231))

    def draw(self):
        self.surface.blit(self.area_directions,self.area_directions_rect)