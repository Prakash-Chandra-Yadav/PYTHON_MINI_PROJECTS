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
        #loads the json file
        contents = self.path.read_text()
        students = json.loads(contents)
        students[name] = {'roll_no':roll_no, 'marks':{}}
        #saves the json file 
        contents = json.dumps(students)
        self.path.write_text(contents)
        print("student added")

    #method to view all the student
    def view_all_studnets(self): 
        '''view all the studnet in the system'''
        i = 1
        #loads the json file 
        contents = self.path.read_text()
        students = json.loads(contents)
        for student in students.keys():
            print(f"{i}: {student}")
            i += 1
    #add metho to serahc student by their name
    def search_student(self):
        '''search student by their name'''
        name = input("please ente the name of the student: ")
        try:
            #loads the json file
            contents = self.path.read_text()
            students = json.loads(contents)
            if name in students:
                print("----student found---")
                print("--HERE ARE THE DETAILS----")
                print(f"\n name: {name}\n 'roll: {students[name]['roll_no']}")
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
            #loads the json files
            students = self.load_file()
            name = input("enter the name of the student")
            if name in students: 
                print("select the details you want to edit: \n")
                print("\n1.Name\n2.Roll_no")
                choice = input("\nenter the option number: ")

                match choice:
                    case '1':
                        new_name = input("enter the new name: ")
                        students[new_name] = students.pop(name)
                        #saves the json files 
                        content = json.dumps(students)
                        self.path.write_text(content)
                        print("updated the information")
                    case '2':
                        new_roll = input("please ente the new roll_no: ")
                        students[name]['roll_no'] = new_roll
                        #saves the json files
                        content = json.loads(students)
                        self.path.write_text(content)
                        print("updated the information")
            else:
                print("student not found!!")
        except ValueError: 
            print("please enter the name of the student not roll number")
    #add method that delets the student record
    def delete_student(self):
        #loads the json files 
        students = self._laod_file()
        name = input("enter the name of the student: ")
        if name in students:
            confirm = input("please enter the student name again to confirm deletion: ")
            if confirm == name: 
                del students[name]
                #saves the json files
                content = json.dumps(students)
                self.path.write_text(content)
                print("updated the information")
            else: 
                print("not the same name")
        else: 
            print("student not found")
    ##add the method to add the marks 
    def add_marks(self):
        #laods the json file
        students = self._laod_file()
        name = input("please enter the name of the student: ")
        if name in students: 
            print('\n_____STUDENT MARKS UPDATE________')
            print("\n1.Python\n2.Math\n3.English")
            choice = input("please select the option: ")
            match choice :
                case '1':
                    score = float(input("please enter the marks: "))
                    students[name]['marks']['python'] = score
                    print('marks updated')
                    #saves the json files 
                    content = json.dumps(students)
                    self.path.write_text(content)
                case '2':
                    score =float(input("please enter the marks: "))
                    students[name]['marks']['math'] = score
                    print('marks updated')
                    #lsaves the json file
                    content = json.dumps(students)
                    self.path.write_text(content)
                case '3':
                    score = float(input("please enter the marks: "))
                    students[name]['marks']['english'] = score
                    print('marks updated')
                    #saves the json files
                    content = json.dumps(students)
                    self.path.write_text(content)
        else: 
            print("student not found!!")
    ##add the method to calculate the marks 
    def generate_report(self):
        #laods the json files
        students = self._laod_file()
        name = input("please enter the name of the students: ")
        if name in students: 
            python_mark = students[name]['marks']['python']
            if 80 <= python_mark <= 100:
                python_grade = 'A'
            elif 70 <= python_mark < 80:
                python_grade = 'B'
            elif 60 <= python_mark < 70: 
                python_grade = 'C'
            elif 50 <= python_mark < 60:
                python_grade = 'D'
            else: 
                python_grade='fail'
            english_mark = students[name]['marks']['english']
            if 80 <= english_mark <= 100:
                english_grade = 'A'
            elif 70 <= english_mark < 80:
                english_grade = 'B'
            elif 60 <= english_mark < 70: 
                english_grade = 'C'
            elif 50 <= english_mark < 60:
                english_grade = 'D'
            else: 
                english_grade = 'fail'
            math_mark = students[name]['marks']['math']
            if 80 <= math_mark <= 100:
                math_grade = 'A'
            elif 70 <= math_mark < 80:
                math_grade = 'B'
            elif 60 <= math_mark < 70: 
                math_grade = 'C'
            elif 50 <= math_mark < 60:
                math_grade = 'D'
            else: 
                math_grade = 'fail'
            total_marks = python_mark + english_mark + math_mark
            if 80 <= total_marks <= 100:
                total_grade = 'A'
            elif 70 <= total_marks < 80:
                total_grade = 'B'
            elif 60 <= total_marks < 70: 
                total_grade = 'C'
            elif 50 <= total_marks < 60:
                total_grade = 'D'
            else: 
                total_grade = 'fail'
        #generate the report
        print(f"-----report of {name} --------")
        print(f"roll_no: {students[name]['roll_no']}")
        print(f"python:{python_mark}, grade: {python_grade}")
        print(f"math:{math_mark}, grade: {math_grade}")
        print(f"english:{english_mark}, grade: {english_grade}")
        print("\nTOTAL: ")
        print(f"total_marks:{total_marks}")
        print(f"final_grade:{total_grade}")

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
    def _laod_file(self):
        '''loads the json file from the dir'''
        contents = self.path.read_text()
        students = json.loads(contents)
        return students




    #add method that runs the app 
    def run_student_app(self): 
        '''runs the application'''
        print("----------MAIN--MENU---------\n")
        print("\n1.Add new student\n2.search for the student\n3.update the student informtation\n4.view all students\n5.Delete Student\n6.add marks\n7.generate report")
        choice = input("please select the correct option: ")
        match choice:
            case '1':
                stdn = Student()
                name = input("please enter the student name: ")
                roll_no = input("please ente the roll no: ")
                stdn.add_student(name,roll_no)
            case '2': 
                std1 = Student()
                std1.search_student()
            case '3':
                ##update the content 
                std2 = Student()
                std2.update_information()
            case '4':
                std3 =Student()
                std3.view_all_studnets()
            case '5':
                std4 = Student()
                std4.delete_student()
            case '6':
                std5 = Student()
                std5.add_marks()
            case '7':
                std6 = Student()
                std6.generate_report()
def main():
    std2 = Student()
    std2.run_student_app()

if __name__ == "__main__":
    main()





