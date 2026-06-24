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
        title = self._validate_input('Please enter the title of the book: ','Title')
        author = self._validate_input('Please enter the author of the book: ','Author')
        book_id = self._validate_input('Please enter the book ID: ','Book ID')
        try: 
            total_copies = int(input("total copies owned by libraries: "))
            available_copies = int(input("enter the number of the copies available: "))
        except ValueError: 
            print("integere value only allowed")
        else:
            borrower = input("enter the name of the brower: ")

            library[book_id] ={'title': title, 'author': author, 'total_copies':total_copies, 'available_copies': available_copies, 'borrowed_by':[borrower,] }

            self._update_library(library)

    #method to see all the books
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
    
    #created the method to search for the book 
    def search_book(self):
        '''search for the book by id or title'''
        print("please select the option\n1>Search by ID\n2.Search by title")
        choice = input('select your response: ')
        match choice:
            case '1':
                id = self._validate_input('Please enter the book ID: ', 'Book ID')
                self._search_by_book_id(id)  
            case '2':
                self._search_by_title() 
            case '':
                print('please select the correct response!!')
    def borrow_book(self):
        '''method to borrow the book'''
        library = self._load_library()
        id = self._validate_input('Please enter the Book ID: ', 'Book ID')
        if id in library: 
            if library[id]['available_copies'] >=1:
                name = input("please enter the name of the borrower: ")
                library[id]['borrowed_by'].append(name)
                library[id]['available_copies'] -= 1
                self._update_library(library)
                print(f'book is successfully borrowed by {name}')
            else: 
                print('no copies available to borrow')
        else: 
            print('book not found!!')

    
    #create the method to update the book information
    def update_booK_info(self):
        '''this method updates the information of the book'''
        library = self._load_library()
        id = self._validate_input('Please enter the book ID: ', 'Book ID')
        if id in library:
            print('\n--please select the information you wan tto update--')
            print('n1>title\n2>author\n3>Total Copies')
            choice = input('select the option: ')
            self._perform_update(choice,id)

    #create the method to delete the book
    def delete_book(self):
        '''method to delete the book from the libraray'''
        library = self._load_library()
        id = self._validate_input('Please enter the book ID: ', 'Book ID')
        if id in library:
            confirm_id = input('please confirm the book id: ')
            if id == confirm_id:
                #book should nt be borrowed currently
                if (library[id]['total_copies'] - library[id]['available_copies']) >=1:
                    print('sorry the book cant be deletd as it is borrowed wait for them tu return the book!!')
                else: 
                    del library[id]
                    self._update_library(library)
                    print('book deleted')
            else: 
                print('book id didnt match!!')
        else: 
            print('book not found')
    #helper function to validate the input (input cannot be empty)
    def _validate_input(self,prompt,field_name):
        '''check if th einput filed is empty '''
        while True: 
            value = input(prompt)
            if value.strip():
                return value 
            else:
                print(f"{field_name} can't be empty!!")
    #helper method to perform the updated is any restrictions need to be applied in future it can be handeled here
    def _perform_update(self,choice,id):
        '''helper function to perform the update'''
        library = self._load_library()
        match choice:
            case '1':
                new_title = self._validate_input('Please enter the new title','New Title')
                library[id]['title'] = new_title
                self._update_library(library)
                print('information updated')
            case '2':
                new_author = self._validate_input('Please enter the author','New Author')
                library[id]['author'] = new_author
                self._update_library(library)
                print('information updated')
            case '3':
                try:
                    new_total = int(input("enter the total number of compies: "))
                except ValueError:
                    print("integer value is only allowed!!")
                else:
                    #total copy cant be less than the borrowed copy
                    if new_total > (library[id]['total_copies'] - library[id]['available_copies']):
                        library[id]['total_copies']  = new_total 
                        self._update_library(library)
                        print('information updated')
                    else: 
                        print("total compies cant be negative")
  
    #helper function to search for the book by id
    def _search_by_book_id(self,book_id):
        '''searches for the book by using the book id'''
        library = self._load_library()
        if book_id in library:
            title = library[book_id]['title']
            print(f'book found {book_id}\nTitle : {title}')
        else:
            print('book not found')
    #create the helper function to sarch fir the book title
    def _search_by_title(self):
        '''searches for the book by using the book title'''
        #set the flag 
        found = False
        library = self._load_library()
        title = self._validate_input('Please enter the title: ','Title')
        for book_id,book_info in library.items():
            if book_info['title'] == title: 
                print(f'Found: {title}')
                found = True 
                break 
        if found == False:
            print('SOrry book not found!!') 
    
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
    l1.add_new_book()

if __name__ == '__main__':
    main()
        
