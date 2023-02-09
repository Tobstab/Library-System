from random import randint
Member_ID = 0
book_database = []
loan_status = 0
def add_item_txt(title,author,purchase_date,Member_ID):
    '''
This function takes in 4 parameters, which all need to be provided by the librarian
or user using the system. This being the title of a book, its author,
date of purchase and the member ID of the user, which is needed so that
the system knows whether the book is currently in stock or not.
'''
    ID = randint(1,99)# generate a random number between 1 to 99 to use as the books ID
    loan_status = 0 # loan status is inital set to zero meaning that the book is in stock
    newbook = str([ID,title,author,loan_status,purchase_date,Member_ID])# creates a string which will later added to the txt file
    f=open("Database.txt","r")# opens up the txt file so that it can be read and its information can be used
    for line in f:
        line = line.strip()
        line = line.split(',')# each line is split up and stripped of all whitespaces at the front and end of the line
        if Member_ID == 0: # checks the member ID, if its equal to zero it will know the book is in stock
            loan_status = "In Stock" # changes loan status to "In Stock"
            newbook = str([ID,title,author,loan_status,purchase_date,Member_ID]) #written again so that the new loan status is added
            add_item_database(str(ID).replace('[',''),line[1].replace("'",''),line[2],line[3],line[4],str(line[5])) #adds the book to the database
        elif Member_ID > 0:
            loan_status = "Out on Loan" #if the member_ID is non-zero - has a member's ID in it then the loan status is changed to "Out on Loan"
            newbook = str([ID,title,author,loan_status,purchase_date,Member_ID])
            add_item_database((str(ID).replace('[','')),line[1].replace("'",''),line[2],line[3],line[4],str(line[5]))
        IDs = [i[0].replace('[','').replace(']','') for i in book_database]#removes square brackets from ids and creates a list of them
        if str(ID) in IDs: # if the ID is already in the database then replace the ID with another randomly generated one
            ID = randint(1,99)
            newbook = str([ID,title,author,loan_status,purchase_date,Member_ID])
            add_item_database((str(ID).replace('[','')),line[1].replace("'",''),line[2],line[3],line[4],str(line[5]))
        else:
            add_item_database(str(line[0]).replace('[',''),line[1].replace("'",''),line[2],line[3],line[4],str(line[5]))
    f.close()
    f=open("Database.txt","a") #open the database in append mode 
    addbook= str(newbook).replace('[','').replace(']','')#removes the square brackets from the new book string 
    f.write(addbook+"\n")# adds the newbook to the database
    f.close()#safely closes the database
def add_item_database(ID,title,author,loan_status,purchase_date,Member_ID):
    '''
This function takes in the inputs ID,title,author,loan_status,purchase_date,Member_ID
and then appends them to the list book_database
'''
    book_database.append([ID,title,author,loan_status,purchase_date,Member_ID])
def loanbook():
    '''
This function, gets the total amount of books in the database
and outputs all of their titles.
'''
    f=open("Database.txt","r")
    for line in f:
            line = line.strip().split(',')
            book_database.append([str(line[0]).replace('[',''),line[1],line[2],line[3],line[4],str(line[5]).replace(']','')])
    AvailableBooks = [i[1].replace('"',"").replace("'","").strip() for i in book_database]#creates a list of all of the titles of the books in the database txt
    print(AvailableBooks) #prints the list of books
    book_database.clear()#clears the list so that there are no repeats
    AvailableBooks.clear()#clears the list so that there are no repeats


