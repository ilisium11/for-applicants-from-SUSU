from setup_info import dict_applicants,dict_directions
applicants=dict_applicants
directions=dict_directions
kvo_applicants={}
budget_applicants={}

for app in applicants:
    if applicants[app].count_kvo>0:
        kvo_applicants[app]=applicants[app]
    else:
        budget_applicants[app]=applicants[app]


def processing_entrance(dict_app:dict,status:int):
    applicants_false={}
    while len(dict_app)>0:
        list_delete = []
        dict_add = {}
        for applicant in dict_app:
            list_special=dict_app[applicant].list_special
            priority=dict_app[applicant].actual_prior
            category= list_special[priority][3]
            name= list_special[priority][2]
            score= list_special[priority][1]
            app_id=directions[name].admission(category,score,dict_app[applicant])

            if app_id:
                if type(app_id) == tuple:
                    list_delete.append(app_id[0])
                    if app_id[2].check_prior(status):
                        applicants_false[app_id[1]] = app_id[2]
                    else:
                        dict_add[app_id[1]] = app_id[2]
                else:
                    list_delete.append(app_id)
            elif dict_app[applicant].check_prior(status):
                list_delete.append(applicant)
                applicants_false[applicant]=dict_app[applicant]

        for applicant in list_delete:
            dict_app.pop(applicant)
        for applicant in dict_add:
            dict_app[applicant]=dict_add[applicant]
    return applicants_false


dc={}
kvo=processing_entrance(kvo_applicants,1)
kvo_false={}
for direction in directions:
    directions[direction].contest()

for app in kvo:
    if kvo[app].count_budget>0:
        budget_applicants[app]=kvo[app]
    else:
        kvo_false[app]=kvo[app]
all_applicants_false=processing_entrance(budget_applicants,2)

#print(len(all_applicants_false))
n='02.03.02Высшая школа электроники и компьютерных наук'
#проблема 42796

