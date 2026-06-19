#import the required libraries
from pathlib import path 
import json

from pytest import mark 

class Student:
    def __init__(self,name,roll_no):
        '''initialize the needed attributes'''
        self.name = name
        self.roll_no = roll_no
        self.marks = {}
        self.student = {name:{roll_no:self.roll_no, self.marks:{}}}
        self.students = {}
    #method to add the student
    def add_student(self,name,roll_no):
        '''add the new student'''
        self.student[self.name] = {'roll_no':roll_no, 'marks':{}}
    #method to view all the student
    def view_all_studnets(self): 
        '''view all the studnet in the system'''
        i = 1
        students = json.load(r'students.json')
        for student in students.keys():
            print(f"{i}: {student}")
            i += 1
    



