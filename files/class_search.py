import sys
import pygame as pg
from class_area_search import AreaSearch
from class_search_button import SearchButton
from class_list_applicant import ListApplicant
from class_menu_button import MenuButton


class Search:
    font= pg.font.Font('font/new_font.ttf', 40)
    font_special=pg.font.Font('font/new_font.ttf',24)

    def __init__(self,surface,directions,applicants):
        self.text=self.font.render('Введите № абитуриента -',1,(30,30,30))
        self.rect_text=self.text.get_rect(center=(surface.get_width()/4,surface.get_height()/7.5))
        self.surface=surface
        width,height=surface.get_width(),surface.get_height()
        self.clock=pg.time.Clock()
        self.area_search=AreaSearch(self.surface,(width/4,height/9),(width/1.7,height/7.5))
        self.search_button=SearchButton(self.surface,(width/1.3,height/7.5))
        size_area_special=(self.surface.get_width()/1.15,self.surface.get_height()/1.5)
        center_area_special=(self.surface.get_width()/2,self.surface.get_height()/1.8)
        self.area_special=ListApplicant(self.surface,applicants,directions,size_area_special,center_area_special)
        self.back_button = MenuButton(self.surface, 'Назад',(self.surface.get_width() * 0.2, self.surface.get_height() * 0.95))

    def run(self):
        r = True
        while r:
            mouse = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type==pg.KEYDOWN:
                    if event.key==pg.K_SPACE:
                        sys.exit()
                    self.area_search.input_text(event.key)
                elif event.type==pg.MOUSEBUTTONDOWN:
                    if self.back_button.collide(mouse):
                        return True
                    if not self.area_search.clicking_mouse(mouse):
                        if self.search_button.clicking_mouse(mouse):
                            text=self.area_search.get_text()
                            self.area_special.search_applicants(text)

            self.search_button.check_mouse(mouse)
            self.surface.blit(self.text,self.rect_text)
            self.area_special.draw()
            self.area_search.draw()
            self.search_button.draw()
            self.back_button.draw()
            self.clock.tick(60)
            pg.display.update()
            self.surface.fill((200, 191, 231))
