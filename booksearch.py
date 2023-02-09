###booksearch funtions
from Database import *
string_search =[]
book_by_string=[]
Book_found = "None"
def booksearch(bookrequest):
    '''
This function allows the user to search for a book, in the system.
This is through user input by the librarian. The librarian must either
enter the entire name of the book or a phrase e.g. "Lord of the rings","lord" or "rings"
in order to get a match.
'''
    occur = 0
    found = 3
    f=open("Database.txt","r")
    for line in f:
        line = line.strip()
        line = line.split(',')
        #adds books the database so that they can be critique
        book_database.append([str(line[0].replace('[','')),line[1],line[2],line[3],line[4],str(line[5].replace(']','') )])
    Books = [i[1].replace('"',"").strip().lower() for i in book_database] #takes all the book titles and removes the white space
    # and also makes everything lowercase for validation
    search = bookrequest.split(" ") # splits up the users input into a list of individual words
    search =[i.lower() for i in search]# makes each book lowercase
    if "the" in search:
        search.remove("the") #removes the word 'the' from the search as it is a generic word
    if "of" in search:
        search.remove("of") #removes the word 'of' from the search as it is a generic word
        #and slows down the search process
    for book in Books:
        book_by_string.append(book.split(" "))
    for item in book_by_string: #the code checks every element in book_by_String and checks across each word in the search list
        for j in search:
            if j in item:
                occur = occur +1
                if occur == 1:
                    global Book_found
                    Book_found = " ".join(item) #once its found the book it joins the list of words together again but as a sentence
                    confirm =input("Did you mean %s: "%(Book_found))#validates it has found the right book
                    if confirm.lower() == "yes":
                        for i in book_database:
                            if (i[1].lower()).strip() == Book_found  and (i[3].strip() == "'In Stock'" or i[3].strip() == '"In Stock"'):
                                found = 1
                                #if the user inputs yes the book matches with the book in the database
                                # prints that this book is in stock, if the loan_status is equal to "In stock"
                            elif (i[1].lower()).strip() == Book_found  and (i[3].strip() == "'Out on Loan'" or i[3].strip() == '"Out on Loan"'):
                                found = 0
                                #if the user inputs yes the book matches with the book in the database
                                # prints that this book is not in stock, if the loan_status is equal to "In stock"
                        book_by_string.clear()
                        book_database.clear()
                        break
            
                    elif confirm.lower() == "no": #if the user says that it was not the right book
                        print("Try again, please be more precise")
                        book_by_string.remove(item)# the incorrect book is removed from the list so that another book that is similar can be tried
                        bookrequest = input("Please enter the name of the book you like to find: ")
                        booksearch(bookrequest)

                    else:
                        print("Try again, please be more precise")
                        bookrequest = input("Please enter the name of the book you like to find: ")
                        booksearch(bookrequest)# if the input is anything other than yes or no, then user is accessed to reenter their choice
                else:
                    break
                
    if found == 1:
        print("This book is in stock")
    elif found == 0:
        print("This book is not in stock")
                    
                    
    else:
        if found == 3:
            print("Sorry this book is not in stock: %s"%(bookrequest)) #if book title is not found at all then it says the book is not in stock
            Book_found = "None"
    
        book_by_string.clear()
        book_database.clear()

      
book_for_checkout = Book_found

if __name__=="__main__":
     # testing search function
     request = ["harry","harry potter","lord","1"]
     for i in request:
         booksearch(i)
     # results should be as follows
     # Output 1 = This is in Stock
     # Output 2 = This is in Stock
     # Output 3 = This is in Stock
     # Output 4 = Sorry this book is not in stock: 1
