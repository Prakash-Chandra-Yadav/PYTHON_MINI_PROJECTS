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
    #add metho to serahc student by their name
    def search_student(self):
        '''search student by their name'''
        name = input("please ente the name of the student").title()
        try:
            students = json.load(r'students.json')
            if name in students:
                print("----student found---")
                print("--HERE ARE THE DETAILS----")
                print(f"\n name: {name}\n 'roll: {students[name]['roll']}")
                print("\n---MARKS---")
                for key,value in students[name]['marks'].items():
                    print(f"{key} : {value}")
            else: 
                print("Student not found")
        except ValueError:
            print("please enter the  name of the student!! number is not allowed")
    #add the method to update the student information
    






