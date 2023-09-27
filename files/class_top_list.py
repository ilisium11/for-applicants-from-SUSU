import pygame as pg
from class_wheel import Wheel
Azure=(0,220,220)
Blue=(0,0,255)
Orange=(220,145,0)
Purple=(113,72,154)


class TopList:
    font=pg.font.Font('font/new_font.ttf',21)
    font_kvo = pg.font.Font('font/new_font.ttf', 16)
    font_name=pg.font.Font('font/new_font.ttf', 24)
    width_area_special = 670
    height_area_special = 700

    def __init__(self,surface,direction):
        self.surface=surface
        self.target_kvo=direction.target_kvo
        self.target_kvo.sort(key=lambda x:x[0],reverse=True)
        self.special_kvo=direction.special_kvo
        self.special_kvo.sort(key=lambda x:x[0],reverse=True)
        self.separate_kvo=direction.separate_kvo
        self.separate_kvo.sort(key=lambda x:x[0],reverse=True)
        self.combo_kvo=direction.combo_kvo
        self.combo_kvo.sort(key=lambda x:x[0],reverse=True)
        self.combo1_kvo=direction.combo1_kvo
        self.combo1_kvo.sort(key=lambda x:x[0],reverse=True)
        self.budget=direction.budget
        self.budget.sort(key=lambda x:x[0],reverse=True)
        readlines=[('Порядковый номер','Статус','Номер абитуриента','Баллы')]
        k=1
        for applicant in self.target_kvo:
            readlines.append((str(k),'Цел Квота',str(applicant[1].id),str(applicant[0])))
            k+=1
        for applicant in self.special_kvo:
            readlines.append((str(k),'Особ Квота',str(applicant[1].id),str(applicant[0])))
            k += 1
        for applicant in self.separate_kvo:
            readlines.append((str(k),'Отд Квота',str(applicant[1].id),str(applicant[0])))
            k += 1
        for applicant in self.combo_kvo:
            readlines.append((str(k),'Сов Квота(ос,цел)',str(applicant[1].id),str(applicant[0])))
            k += 1
        for applicant in self.combo1_kvo:
            readlines.append((str(k),'Сов квота(отд,цел)',str(applicant[1].id),str(applicant[0])))
            k += 1
        for applicant in self.budget:
            if applicant[0]>=1000:
                readlines.append((str(k),'БВИ',str(applicant[1].id),str(applicant[0]-1000)))
            else:
                readlines.append((str(k), 'Об Конкурс', str(applicant[1].id), str(applicant[0])))
            k += 1
        self.area_special = pg.Surface((self.width_area_special, self.height_area_special))
        self.area_special.fill((175,175,175))
        count=len(self.target_kvo+self.special_kvo+self.separate_kvo+self.combo_kvo+self.combo1_kvo+self.budget)
        height_area_applicant = 200+(count+1) * 100
        self.area_applicant=pg.Surface((self.width_area_special,height_area_applicant))
        self.area_applicant.fill((175,175,175))
        k=0
        color=Blue
        self.text_name=self.font_kvo.render(direction.name,1,Purple)
        self.text_budget=self.font_kvo.render('Общ конкурс '+str(len(self.budget))+' из '+str(direction.count_budget),1,Purple)
        self.text_target_kvo=self.font_kvo.render('Цел квота '+str(len(self.target_kvo))+' из '+str(direction.count_target_kvo),1,Purple)
        self.text_special_kvo=self.font_kvo.render('Особ квота '+str(len(self.special_kvo))+' из '+str(direction.count_special_kvo),1,Purple)
        self.text_separate_kvo=self.font_kvo.render('Отдел квота '+str(len(self.separate_kvo))+' из '+str(direction.count_separate_kvo),1,Purple)
        self.text_combo_kvo = self.font_kvo.render('Сов квота(особ,цел) ' + str(len(self.combo_kvo)) + ' из ' + str(direction.count_combo_kvo), 1, Purple)
        self.text_combo1_kvo = self.font_kvo.render('Сов квота(отд,цел) ' + str(len(self.combo1_kvo)) + ' из ' + str(direction.count_combo1_kvo), 1, Purple)
        self.area_applicant.blit(self.text_name,self.text_name.get_rect(center=(335,60)))
        self.area_applicant.blit(self.text_budget,self.text_budget.get_rect(center=(90,120)))
        self.area_applicant.blit(self.text_target_kvo, self.text_target_kvo.get_rect(center=(240, 120)))
        self.area_applicant.blit(self.text_special_kvo, self.text_special_kvo.get_rect(center=(380, 120)))
        self.area_applicant.blit(self.text_separate_kvo, self.text_separate_kvo.get_rect(center=(550, 120)))
        self.area_applicant.blit(self.text_combo_kvo, self.text_combo_kvo.get_rect(center=(160, 180)))
        self.area_applicant.blit(self.text_combo1_kvo, self.text_combo1_kvo.get_rect(center=(440, 180)))
        for readline in readlines:
            rect=pg.Surface((self.width_area_special,60))
            rect.fill(Azure)
            self.area_applicant.blit(rect,rect.get_rect(center=(self.width_area_special/2,250 + k * 100)))
            text1 = self.font.render(readline[0], True, color)
            text2 = self.font.render(readline[1], True, color)
            text3 = self.font.render(readline[2], True, color)
            if readline[3]!='Баллы':
                if int(readline[3])>=1000:
                    text4 = self.font.render(str(int(readline[3])-1000), True, color)
                else:
                    text4 = self.font.render(readline[3], True, color)
            else:
                text4 = self.font.render(readline[3], True, color)
            self.area_applicant.blit(text1, text1.get_rect(center=(110, 250 + k * 100)))
            self.area_applicant.blit(text2,text2.get_rect(center=(270,250+k*100)))
            self.area_applicant.blit(text3, text3.get_rect(center=(435, 250 + k * 100)))
            self.area_applicant.blit(text4, text4.get_rect(center=(600, 250 + k * 100)))
            k+=1
            color=Orange
        self.area_special.blit(self.area_applicant, (0, 0))
        self.difference = height_area_applicant - self.height_area_special
        self.kf = 0
        self.wheel = Wheel(surface, 1365, 100, 700)

    def moving_wheel(self,mouse):
        ret = self.wheel.draw(mouse)
        if ret:
            self.area_special.blit(self.area_applicant, (0, -ret * self.difference))
            self.kf = ret

    def stop_wheel(self):
        self.wheel.mouse = False

    def clicking_wheel(self,mouse):
        return self.wheel.clicking_mouse(mouse)

    def draw(self):
        self.surface.blit(self.area_special,(660,0))