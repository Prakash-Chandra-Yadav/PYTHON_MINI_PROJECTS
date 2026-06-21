from student_app import Student

class StudentManager:
    def __init__(self):
        '''set the default attributes'''
        self.manager = Student()
        #add method that runs the app 
    def run_student_app(self): 
        '''runs the application'''
        while True:
            print("----------MAIN--MENU---------\n")
            print("\n1.Add new student\n2.search for the student\n3.update the student informtation\n4.view all students\n5.Delete Student\n6.add marks\n7.generate report")
            choice = input("please select the correct option: ")
            match choice:
                case '1':
                    name = input("please enter the student name: ")
                    roll_no = input("please ente the roll no: ")
                    self.manager.add_student(name,roll_no)
                case '2': 
                    self.manager.search_student()
                case '3':
                    ##update the content 
                    self.manager.update_information()
                case '4':
                    self.manager.view_all_studnets()
                case '5':
                    self.manager.delete_student()
                case '6':
                    self.manager.add_marks()
                case '7':
                    self.manager.generate_report()
def main():
    menu = StudentManager()
    menu.run_student_app()
if __name__ == '__main__':
    main()
        