class Abitur:
    def __init__(self,id_number):
        self.id=id_number
        self.directions=[]
        self.actual_prior=0
        self.count_kvo=0
        self.count_budget=0
        self.list_special=[]
        self.enrollment=False

    def add_direction(self,name:str,category:str,priority:int,score:int):
        self.directions.append((priority,score,name,category))

    def sort_direction(self):
        list_kvo=[]
        list_budget=[]
        for i in self.directions:
            if 'квота' in i[3]:
                list_kvo.append(i)
            else:
                list_budget.append(i)
        list_kvo.sort()
        list_budget.sort()
        self.count_kvo=len(list_kvo)
        self.count_budget=len(list_budget)
        self.list_special=list_kvo+list_budget

    def check_prior(self,status:int):
        if status==1:
            if self.actual_prior>self.count_kvo-1:
                return True
        elif status==2:
            if self.actual_prior>len(self.list_special)-1:
                return True

    def set_enrollment(self,value:bool):
        self.enrollment=value
        if not value:
            self.actual_prior+=1

