import sys
import pygame as pg

from class_top_directions import TopDirections
from class_top_list import TopList
from class_menu_button import MenuButton


Yellow=(255,255,0)
Red=(255,0,0)
Green=(0,255,0)


class Lists:

    def __init__(self,surface,directions):
        self.surface=surface
        self.clock=pg.time.Clock()
        self.top_directions=TopDirections(self.surface,len(directions),directions)
        self.top_list=None
        self.back_button=MenuButton(self.surface,'Назад',(self.surface.get_width()*0.2,self.surface.get_height()*0.9))

    def run(self):
        run=True
        while run:
            mouse=pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
                elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_SPACE:
                        sys.exit()
                elif event.type==pg.MOUSEBUTTONDOWN:
                    if self.back_button.collide(mouse):
                        return True
                    if not self.top_directions.clicking_wheel(mouse):
                        direction=self.top_directions.clicking_buttons(mouse)
                        if direction:
                            self.top_list=TopList(self.surface,direction)
                        elif self.top_list:
                            self.top_list.clicking_wheel(mouse)

                elif event.type==pg.MOUSEBUTTONUP:
                    self.top_directions.stop_wheel()
                    if self.top_list:
                        self.top_list.stop_wheel()

            if self.top_list:
                self.top_list.moving_wheel(mouse)
                self.top_list.draw()
            self.top_directions.moving_wheel(mouse)
            self.top_directions.draw()
            self.back_button.draw()
            self.clock.tick(60)
            pg.display.update()
            self.surface.fill((230, 230, 230))