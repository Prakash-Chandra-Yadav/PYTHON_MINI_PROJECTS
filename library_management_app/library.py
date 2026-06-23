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
        library = self._load_library()

        title = input("enter the title of the book: ")
        author = input("enter the name of the author: ")
        book_id = input("enter the book id: ")
        try: 
            total_copies = int(input("total copies owned by libraries: "))
            available_copies = int(input("enter the number of the copies available: "))
        except ValueError: 
            print("integere value only allowed")
        else:
            borrower = input("enter the name of the brower: ")

            library[book_id] ={'title': title, 'author': author, 'total_copies':total_copies, 'available_copies': available_copies, 'borrowed_by':[borrower,] }

            self._update_library(library)
    def View_all_books(self):
        '''method to show all the books in the library '''
        library = self._load_library()
        #show all the book titles 
        i = 0
        try: 
            for book in library:
                print(f'{1}->{book}')

        except KeyError:
            print("sorry we dont have books now")


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
    #create the helper function to load the json format 
    def _load_library(self):
        '''load the json strudture of the library'''
        contents = self.path.read_text()
        library = json.loads(contents)
        return library
    #create new method to update the existing library 
    def _update_library(self,library):
        '''updates the existing json file of the library with new information'''
        contents = json.dumps(library)
        self.path.write_text(contents)
        
    
def main():
    l1 = Libraray()
    l1.View_all_books()

if __name__ == '__main__':
    main()
        
