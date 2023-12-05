import pandas as pd
the_file = pd.read_csv('teachertimetable.csv')
class Teacher():
    def __init__(self,name,subject,clas):
        self.name = name
        self.subject = subject 
        self.clas = clas
    def subme(self,n):
        score = 0 
        subs_possibility = {}
        free_periods_for_potential_teacher = []
        padhai_periods_for_absent_teacher = []
        for z in range(1,9):
            if pd.notnull(the_file[f"{z}"][n]) is True:  
                padhai_periods_for_absent_teacher.append(z)
                subs_possibility[z] = []
        for x in range(len(the_file)):
            free_periods_for_potential_teacher.clear()
            for z in range(len(the_file['Class'][x].split(","))):
                if int(the_file['Class'][x].split(",")[z]) in self.clas:
                    score += 10 
            if (the_file['Subjects'][x]) == self.subject:
                score += 100
            for z in range(1,9):
                if pd.isnull(the_file[f"{z}"][x]) is True:  
                    free_periods_for_potential_teacher.append(z)
            for z in range(len(free_periods_for_potential_teacher)):
                if free_periods_for_potential_teacher[z] in padhai_periods_for_absent_teacher:
                    subs_possibility[free_periods_for_potential_teacher[z]].append([the_file['Teachers'][x],score]) 
        print(subs_possibility)
