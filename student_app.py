#import the required libraries
from pathlib import Path 
import json

class Student:
    def __init__(self):
        '''initialize the needed attributes'''
        self.path = self._load_path()
    #method to add the student
    def add_student(self,name,roll_no):
        '''add the new student'''
        #loads the json file
        students = self._load_file()
        students[name] = {'roll_no':roll_no, 'marks':{}}
        #saves the json file 
        self._save_file(students)
        print("student added")

    #method to view all the student
    def view_all_studnets(self): 
        '''view all the studnet in the system'''
        i = 1
        #loads the json file 
        students = self._load_file()
        for student in students.keys():
            print(f"{i}: {student}")
            i += 1
    #add metho to serahc student by their name
    def search_student(self):
        '''search student by their name'''
        name = input("please ente the name of the student: ")
        #loads the json file
        students = self._load_file()
        if name in students:
            print("----student found---")
            print("--HERE ARE THE DETAILS----")
            print(f"\n name: {name}\n 'roll: {students[name]['roll_no']}")
            print("\n---MARKS---")
            for key,value in students[name]['marks'].items():
                print(f"{key} : {value}")
        else: 
            print("Student not found")
    #add the method to update the student information
    def update_information(self):
        '''updates the student information'''
        #loads the json files
        students = self._load_file()
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
                    self._save_file(students)
                    print("updated the information")
                case '2':
                    try:
                        new_roll = int(input("please ente the new roll_no: "))
                    except ValueError: 
                        print("please enter the integer value")
                    else: 
                        students[name]['roll_no'] = new_roll
                        #saves the json files
                        self._save_file(students)
                        print("updated the information")
        else:
            print("student not found!!")
    #add method that delets the student record
    def delete_student(self):
        #loads the json files 
        students = self._load_file()
        name = input("enter the name of the student: ")
        if name in students:
            confirm = input("please enter the student name again to confirm deletion: ")
            if confirm == name: 
                del students[name]
                #saves the json files
                self._save_file(students)
                print("updated the information")
            else: 
                print("not the same name")
        else: 
            print("student not found")
    ##add the method to add the marks 
    def add_marks(self):
        #laods the json file
        print("---running add marks function will update the makrs---")
        students = self._load_file()
        name = input("please enter the name of the student: ")
        if name in students: 
            print('\n_____STUDENT MARKS UPDATE________')
            print("\n1.Python\n2.Math\n3.English")
            choice = input("please select the option: ")
            match choice :
                case '1':
                    try:
                        score = float(input("please enter the marks: "))
                    except ValueError: 
                        print("enter number only")
                    else:
                        students[name]['marks']['python'] = score
                        print('marks updated')
                        #saves the json files 
                        self._save_file(students)
                case '2':
                    try: 
                        score =float(input("please enter the marks: "))
                    except ValueError:
                        print("enter number only")
                    else: 
                        students[name]['marks']['math'] = score
                        print('marks updated')
                        #lsaves the json file
                        self._save_file(students)
                case '3':
                    try:
                        score = float(input("please enter the marks: "))
                    except ValueError:
                        print("enter number only")
                    else:
                        students[name]['marks']['english'] = score
                        print('marks updated')
                        #saves the json files
                        self._save_file(students)
        else: 
            print("student not found!!")
    ##add the method to calculate the marks 
    def generate_report(self):
        #laods the json files
        students = self._load_file()
        name = input("please enter the name of the students: ")
        if name in students: 
            python_mark = students[name]['marks'].get('python')
            if python_mark is not None:
                python_grade = self._grade_marks(python_mark)
            else: 
                python_mark = 'N/A'
                python_grade = 'N/A'


            english_mark = students[name]['marks'].get('english')
            if english_mark is not None: 
                english_grade = self._grade_marks(english_mark)
            else: 
                english_mark = 'N/A'
                english_grade = 'N/A'

            math_mark = students[name]['marks'].get('math')
            if math_mark is not None:
                math_grade = self._grade_marks(math_mark)
            else: 
                math_mark = 'N/A'
                math_grade ='N/A'
            
            marks =[python_mark,english_mark,math_mark]
            validated_marks = [m for m in marks if isinstance(m,(int,float))]
            total_marks = sum(validated_marks) if validated_marks else 'N/A'

            if isinstance(total_marks, (int, float)):
                total_grade = self._grade_total(total_marks)
            else:
                total_grade = 'N/A'
            #generate the report
            print(f"-----report of {name} --------")
            print(f"roll_no: {students[name]['roll_no']}")
            print(f"python:{python_mark}, grade: {python_grade}")
            print(f"math:{math_mark}, grade: {math_grade}")
            print(f"english:{english_mark}, grade: {english_grade}")
            print("\nTOTAL: ")
            print(f"total_marks:{total_marks}")
            print(f"final_grade:{total_grade}")
        else: 
            print('student not found')

    def _grade_marks(self,mark):
            if 80 <= mark <= 100:
                grade = 'A'
            elif 70 <= mark < 80:
                grade = 'B'
            elif 60 <= mark < 70: 
                grade = 'C'
            elif 50 <= mark < 60:
                grade = 'D'
            else: 
                grade='fail'
            return grade 
    def _grade_total(self, total):
        if 240 <= total <= 300:
            return 'A'
        elif 210 <= total < 240:
            return 'B'
        elif 180 <= total < 210:
            return 'C'
        elif 150 <= total < 180:
            return 'D'
        else:
            return 'fail'

    def _load_path(self):
        '''load the file path'''
        path = Path(__file__).parent/'students.json'
        if path.exists():
            return path
        else: 
            students = {}
            contents = json.dumps(students)
            path.write_text(contents)
            return path
    def _load_file(self):
        '''loads the json file from the dir'''
        contents = self.path.read_text()
        students = json.loads(contents)
        return students
    def _save_file(self,students):
        content = json.dumps(students)
        self.path.write_text(content)





