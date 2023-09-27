import pygame as pg


class ListApplicant:
    font = pg.font.Font('font/new_font.ttf', 24)
    color=(0,0,180)
    color1=(150,0,150)

    def __init__(self,surface,applicants,directions,size,pos):
        self.directions=directions
        self.applicants=applicants
        self.surface=surface
        self.area_special=pg.Surface(size)
        self.rect_area_special=self.area_special.get_rect(center=pos)
        self.text_priority_x=size[0]*0.1
        self.text_score_x=size[0]*0.23
        self.text_direction_x=size[0]*0.43
        self.text_status_x=size[0]*0.77
        self.text_admission_x=size[0]*0.5
        self.first_text_y=size[1]*0.05
        self.last_text_y=size[1]*0.95
        self.difference_text_y=size[1]*0.08
        self.area_special.fill((130, 130, 130))
        self.actual_applicant=''

    def search_applicants(self,applicant_id):
        if self.actual_applicant!=applicant_id:
            self.area_special.fill((130, 130, 130))
            if applicant_id in self.applicants:
                list_special=self.applicants[applicant_id].list_special
                readlines=[('Приоритет','Баллы','Направление','Статус')]
                for special in list_special:
                    readlines.append((special[0],special[1],special[2],special[3]))
                color=self.color
                k=0
                for i in readlines:
                    priority=self.font.render(str(i[0]),1,color)
                    score=self.font.render(str(i[1]),1,color)
                    direction = self.font.render(str(i[2]), 1, color)
                    status = self.font.render(str(i[3]), 1, color)
                    text_y=self.first_text_y+k*self.difference_text_y
                    self.area_special.blit(priority,priority.get_rect(center=(self.text_priority_x,text_y)))
                    self.area_special.blit(score,score.get_rect(center=(self.text_score_x,text_y)))
                    self.area_special.blit(direction, direction.get_rect(center=(self.text_direction_x, text_y)))
                    self.area_special.blit(status, status.get_rect(center=(self.text_status_x, text_y)))
                    k+=1
                    color=self.color1

                self.entrance_applicant(self.applicants[applicant_id])
                self.actual_applicant=applicant_id

    def entrance_applicant(self,applicant):
        text_admission = self.font.render('Поступил на:', 1, (240, 170, 0))
        self.area_special.blit(text_admission, text_admission.get_rect(center=(self.text_priority_x, self.last_text_y)))
        for direction in self.directions:
            list_special=[i[1] for i in self.directions[direction].get_admission_list()]
            if applicant in list_special:
                text=self.font.render(direction,1,(0,240,0))
                self.area_special.blit(text, text.get_rect(center=(self.text_admission_x, self.last_text_y)))
                return True
        text=self.font.render('Не поступил',1,(220,0,0))
        self.area_special.blit(text, text.get_rect(center=(self.text_admission_x, self.last_text_y)))

    def draw(self):
        self.surface.blit(self.area_special,self.rect_area_special)
