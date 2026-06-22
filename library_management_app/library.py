from pathlib import Path 
import json 

#create the library class 

class Libraray:

    def __init__(self):
        '''set the default attributes here'''
        #add the attributes of the path 
        self.path = self._load_path()

    def add_new_book(self):
        '''gets the details about the book and loads on the json file'''
        #laod the json file  first 
        contents = self.path.read_text()
        library = json.loads(contents)

        title = input("enter the title of the book: ")
        author = input("enter the name of the author: ")
        book_id = input("enter the book id: ")
        total_copies = int(input("total copies owned by libraries: "))
        available_copies = int(input("enter the number of the copies available: "))
        borrower = input("enter the name of the brower: ")

        library[book_id] ={'title': title, 'author': author, 'total_copies':total_copies, 'available_copies': available_copies, 'borrowed_by':[borrower,] }

        contents = json.dumps(library)
        self.path.write_text(contents)

    #create the helper function for creating the path
    def _load_path(self):
        '''load the path of the json file'''
        path = Path(__file__).parent/'library.json'
        if path.exists():
            return path 
        else: 
            library = {}
            contents = json.dumps(library)
            path.write_text(contents)
    
    if __name__ == '__main__':
        
