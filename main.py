import json 
import math
import pandas as pd
from teacher import Teacher
the_file = pd.read_csv('teachertimetable.csv')
print("This is a Sample Subsitution Program")
for x in range(len(the_file)):
    print(f"{x}.{the_file['Teachers'][x]}")
    the_file['Teachers'][x] = Teacher(the_file['Teachers'][x],the_file['Subjects'][x],eval(f"[{the_file['Class'][x]}]"))
decision = int(input("enter the number used before the name of the teacher absent:"))
the_file['Teachers'][decision].subme(decision)
