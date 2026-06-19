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
    def update_information(self):
        '''updates the student information'''
        try: 
            content = path.read_text(r'student.json')
            students = json.loads(content)
            name = input("enter the name of the student")
            if name in students: 
                print("select the details you want to edit: \n")
                print("\n1.Name\n2.Roll_no")
                choice = input("\nenter the option number: ")

                match choice:
                    case '1':
                        new_name = input("enter the new name: ")
                        students[name] = new_name
                        content = json.dumps(students)
                        path.write_text(content)
                    case '2':
                        new_roll = input("please ente the new roll_no: ")
                        students[name]['roll_no'] = new_roll
                        content = json.loads(students)
                        path.write_text(content)
            else:
                print("student not found!!")
        except ValueError: 
            print("please enter the name of the student not roll number")
    #add method that delets the student record
    def delete_student(self):
        contents = path.read_text(r'students.json')
        students = json.load(contents)
        name = input("enter the name of the student: ")
        if name in students:
            confirm = input("please enter the student name again to confirm deletion: ")
            if confirm == name: 
                del students[name]
                content = json.dups(students)
                path.write_text(content)
                print("updated the information")
            else: 
                print("not the same name")
        else: 
            print("student not found")
    #add method that runs the app 
    def run_student_app(self): 
        '''runs the application'''
        print("----------MAIN--MENU---------\n")
        print("\n1.Add new student\n2.search for the student\n3.update the student informtation")







