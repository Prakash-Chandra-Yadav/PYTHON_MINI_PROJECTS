from library import Library 

class LibraryManager:

    def __init__(self):
        '''default attributes'''
        self.mylibrary = Library()
    def Run_app(self):
        '''entry point of the program that runs the program'''
        while True: 
            print('1>Add New Book\n2>View all books\n3>Search Book\n4>update book info\n5>Delete a book\n6>borrow a book\n7>return a book\n8>Generate a report\n9>exit')
            choice = input('please selecte the option: ')
            match choice:
                case '1':
                    self.mylibrary.add_new_book()
                case '2':
                    self.mylibrary.View_all_books()
                case '3':
                    self.mylibrary.search_book()
                case '4':
                    self.mylibrary.update_booK_info()
                case '5':
                    self.mylibrary.delete_book()
                case '6':
                    self.mylibrary.borrow_book()
                case '7':
                    self.mylibrary.return_book()
                case '8':
                    self.mylibrary.generate_report()
                case '9':
                    print('thanks for using the library service ')
                    break
                case '':
                    print('please select the correct option')
                
def main():
    library1 = LibraryManager()
    library1.Run_app()

if __name__ == '__main__':
    main()
