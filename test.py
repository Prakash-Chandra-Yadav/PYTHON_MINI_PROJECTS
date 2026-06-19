from student_app import Student 
import json 

def test_add_student():
    std1 = Student()
    std1.add_student('raju','110')
    contents = std1.path.read_text()
    students = json.loads(contents)
    assert 'raju' in students 