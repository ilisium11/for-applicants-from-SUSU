import sys
import pygame as pg
pg.init()
width_display=1400
height_display=800
screen=pg.display.set_mode((width_display,height_display))
screen.fill((180,180,180))
pg.display.set_caption('Поступление')
f=pg.font.Font('font/new_font.ttf',50)
text=f.render('Сбор данных...',1,(200,10,0))
screen.blit(text,text.get_rect(center=(width_display/2,height_display/2)))
pg.display.update()
from lists import Lists
from class_menu_button import MenuButton
from class_search import Search
from entrance import directions,applicants
from class_stats import Stats
Yellow=(255,255,0)
Red=(255,0,0)
Green=(0,255,0)


class MainMenu:
    def __init__(self):
        self.width_display=width_display
        self.height_display=height_display
        self.screen=screen
        self.screen.fill((180, 180, 180))
        self.clock=pg.time.Clock()
        self.button_lists=MenuButton(self.screen,'Списки',(self.width_display/2,self.height_display*0.5))
        self.button_find=MenuButton(self.screen,'Поиск Абитуриентов',(self.width_display/2,self.height_display*0.65))
        self.button_stats=MenuButton(self.screen,'Поступившие',(self.width_display/2,self.height_display*0.8))
        self.lists=Lists(self.screen,directions)
        self.search=Search(self.screen,directions,applicants)
        self.stats=Stats(self.screen,(width_display/2,height_display*0.45),(width_display*0.95,height_display*0.85),directions)

    def run(self):
        r=True
        while r:
            mouse=pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    sys.exit()
                elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_SPACE:
                        sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if self.button_lists.collide(mouse):
                        self.lists.run()
                    elif self.button_find.collide(mouse):
                        self.search.run()
                    elif self.button_stats.collide(mouse):
                        self.stats.run()
            self.button_lists.draw()
            self.button_find.draw()
            self.button_stats.draw()
            self.clock.tick(60)
            pg.display.update()


menu=MainMenu()
menu.run()