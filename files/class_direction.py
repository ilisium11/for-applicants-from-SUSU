from class_abit import Abitur


class Direction:
    def __init__(self,name:str,places:tuple):
        self.name=name
        self.count_target_kvo=int(places[1])
        self.count_special_kvo=int(places[2])
        self.count_separate_kvo=int(places[3])
        self.count_combo_kvo=int(places[4])
        self.count_combo1_kvo=int(places[5])
        self.min_budget=int(places[0])
        self.count_budget=self.min_budget
        self.target_kvo= []
        self.special_kvo=[]
        self.separate_kvo=[]
        self.combo_kvo=[]
        self.combo1_kvo=[]
        self.budget=[]

    @staticmethod
    def processing_applicant(places:list,count:int,score:int,applicant:Abitur):
        if count==0:
            applicant.set_enrollment(False)
            return False
        if len(places)<count:
            places.append((score,applicant))
            applicant.set_enrollment(True)
            places.sort(key=lambda x:x[0])
            return applicant.id
        else:
            if places[0][0]<score:
                places.append((score,applicant))
                applicant.set_enrollment(True)
                places[0][1].set_enrollment(False)
                leave=places[0][1]
                del places[0]
                places.sort(key=lambda x:x[0])
                return applicant.id,leave.id,leave
            else:
                applicant.set_enrollment(False)

    def admission(self,category:str,score:int,applicant:Abitur):
        if 'без экзаменов' in category:
            return self.processing_applicant(self.budget,self.count_budget,score+1000,applicant)
        elif 'Целевая квота' in category:
            return self.processing_applicant(self.target_kvo,self.count_target_kvo,score,applicant)
        elif 'Особая квота' in category:
            return self.processing_applicant(self.special_kvo, self.count_special_kvo, score, applicant)
        elif 'Отдельная квота' in category:
            return self.processing_applicant(self.separate_kvo, self.count_separate_kvo, score, applicant)
        elif 'Совмещенная квота (особая, целевая)' in category:
            return self.processing_applicant(self.combo_kvo, self.count_combo_kvo, score, applicant)
        elif 'Совмещенная квота (отдельная, целевая)' in category:
            return self.processing_applicant(self.combo1_kvo, self.count_combo1_kvo, score, applicant)
        else:
            return self.processing_applicant(self.budget, self.count_budget, score, applicant)

    def contest(self):
        length=len(self.target_kvo)
        if length<self.count_target_kvo:
            self.count_budget+=self.count_target_kvo-length

        length=len(self.special_kvo)
        if length<self.count_special_kvo:
            self.count_budget+=self.count_special_kvo-length

        length=len(self.separate_kvo)
        if length<self.count_separate_kvo:
            self.count_budget+=self.count_separate_kvo-length

        length=len(self.combo_kvo)
        if length<self.count_combo_kvo:
            self.count_budget+=self.count_combo_kvo-length

        length=len(self.combo1_kvo)
        if length<self.count_combo1_kvo:
            self.count_budget+=self.count_combo1_kvo-length

    def get_admission_list(self):
        return self.special_kvo+self.separate_kvo+self.budget+self.combo_kvo+self.combo1_kvo+self.target_kvo

    def get_count_place(self):
        return self.count_special_kvo+self.count_separate_kvo+self.count_budget+self.count_combo_kvo+self.count_combo1_kvo+self.count_target_kvo

