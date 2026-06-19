#import the required libraries
from pathlib import Path 
import json

from pytest import mark 

class Student:
    def __init__(self):
        '''initialize the needed attributes'''
        self.path = self._load_path()
    #method to add the student
    def add_student(self,name,roll_no):
        '''add the new student'''
        contents = self.path.read_text()
        students = json.loads(contents)
        students[name] = {'roll_no':roll_no, 'marks':{}}
        contents = json.dumps(students)
        self.path.write_text(contents)
        print("student added")

    #method to view all the student
    def view_all_studnets(self): 
        '''view all the studnet in the system'''
        i = 1
        contents = self.path.read_text()
        students = json.loads(contents)
        for student in students.keys():
            print(f"{i}: {student}")
            i += 1
    #add metho to serahc student by their name
    def search_student(self):
        '''search student by their name'''
        name = input("please ente the name of the student").title()
        try:
            contents = self.path.read_text()
            students = json.loads(contents)
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
            contents = self.path.read_text()
            students = json.loads(contents)
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
                        self.path.write_text(content)
                    case '2':
                        new_roll = input("please ente the new roll_no: ")
                        students[name]['roll_no'] = new_roll
                        content = json.loads(students)
                        self.path.write_text(content)
            else:
                print("student not found!!")
        except ValueError: 
            print("please enter the name of the student not roll number")
    #add method that delets the student record
    def delete_student(self):
        contents = self.path.read_text()
        students = json.load(contents)
        name = input("enter the name of the student: ")
        if name in students:
            confirm = input("please enter the student name again to confirm deletion: ")
            if confirm == name: 
                del students[name]
                content = json.dups(students)
                self.path.write_text(content)
                print("updated the information")
            else: 
                print("not the same name")
        else: 
            print("student not found")
    def _load_path(self):
        '''load the file path'''
        path = Path(r'C:\Users\Envay\Desktop\python_mini_projects\students.json')
        if path.exists():
            return path
        else: 
            students = {}
            contents = json.dumps(students)
            path.write_text(contents)
            return path


    #add method that runs the app 
    def run_student_app(self): 
        '''runs the application'''
        print("----------MAIN--MENU---------\n")
        print("\n1.Add new student\n2.search for the student\n3.update the student informtation")
        choice = input("please select the correct option: ")
        match choice:
            case '1':
                stdn = Student()
                name = input("please enter the student name: ")
                roll_no = input("please ente the roll no: ")
                stdn.add_student(name,roll_no)
def main():
    std2 = Student()
    std2.run_student_app()

if __name__ == "__main__":
    main()





