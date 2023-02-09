###bookcheckout funtions
from Database import *
from booksearch import *
import matplotlib.pyplot as plt
import datetime

book_for_checkout= (" "+book_for_checkout)
checkoutlist = []
In_Stock_ID = []
temp_database = []
temp_pop_database = []
pop_database = []
book_title_match = []
book_title = []
pop_value = []
log_database = []
date = datetime.datetime.now().strftime("%d-%m-%y") #Creates a date to log the checkout of a book

def logfile_checkout(book_ID,book_name):
    '''
This function, creates a log of the checkout of a book
and saves it to a text file called log_database.txt
'''
    log_database.append([book_ID.replace('[',''),book_name.strip(),date,"22-03-12"])#adds the book ID,Title and dates to the log database
    with open('logfile.txt', "a") as logfile:
        logfile.write(str(log_database).replace('[','').replace(']','').replace("'",'')+"\n")# add the new log string to the text file
                    
    
def pop_show():
    '''
This function is used to display the graph of the popularity
of the books. By matching the ID of the book that has been checkout
with the ID of the book in database
'''
    with open('popularity.txt') as p:
        for line in p:
            pop_database.sort(key = lambda x: int(x[1])) #sorts the pop_database list
            lines = line.split(",")# splits each line in p adds it into the the pop_database list
            add_to_pop(str(lines[0]).replace('[',''),lines[1].replace(']','').strip())
        for data in pop_database: #for data inside of the pop_database list, open the database
            #and add each element in database to a list called book match
            x = data[0] # x is the ID of every book
            book_title_match.clear()
            with open('Database.txt') as f:
                for line in f:
                    line = line.strip()
                    line = line.split(',')
                    book_title_match.append([str(line[0]).replace('[',''),line[1]])
                
                for line in book_title_match:
                    print(line[0])
                    if x == line[0]: # match x with the ID of the books in the database
                        x = line[1]# then switch the ID with the name of the title
            y = data[1]
            pop_value.append(y) # add the popularity to a list called pop_value
            book_title.append(x) # add the title of the book to a list called book_title
                

    plt.figure(figsize=(10, 5)) #created the window for the graph plot to be created to

    plt.subplot(131)#create a bar chart
    plt.subplots_adjust(left=0.12, bottom=0.40, right=1.00, top=0.88, wspace=0.00, hspace=0.20)#adjusts to allow the graph to displayed in the best way
    plt.bar(book_title,pop_value)#plot the book_title for the x values, plot pop_value for the y values
    plt.xticks(
    rotation=45, 
    horizontalalignment='right',
    fontweight='light',
    fontsize='x-small'  
) #adjusts so that the title of the book can be all distinguished and read
    plt.suptitle('Book popularity')
    plt.show() #display the graph plot
def pop_check(book_ID):
    pop_database.clear()
    temp_pop_database.clear()
    with open('popularity.txt') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                temp_pop_database.append([str(line[0]).replace('[',''),line[1].replace(']','').strip("\n").strip()])
            #opens up the popularity txt file and splits each element and adds into a temporary store
            for j in temp_pop_database:
                if j[0] == book_ID: #matches the the ID in the temporary store with the book_ID from the checkout function
                    with open('popularity.txt') as p:
                        for line in p:
                            if book_ID not in line:
                                lines = line.split(",")
                                add_to_pop(str(lines[0]).replace('[',''),lines[1].replace(']','').strip())
                                #opens up the popularity txt file and splits each element and adds into the main store
                                #which will be used to add popularities to the txt file
                            if book_ID in line:
                                for i in temp_pop_database:
                                    if i[0] == book_ID:
                                        newpop=str(line).replace(i[1],str(int(i[1])+1)) #adds one to the value of the popularity
                    
                    with open('popularity.txt', "w") as p:
                             p.write('')
                    with open('popularity.txt', "a") as p:
                        for i in pop_database:
                            p.write((str(i).replace("[",'')).replace("]",'').replace("'",'').replace(" ","")+"\n")
                            #appends all lists in the main store
                        p.write(newpop) #appends the popularity of the changed                        

def add_to_pop(ID,Popularity):
    '''
this function adds the ID and popularity to the main list store for popularity
'''
    pop_database.append([ID,Popularity])

def add_to_temp(ID,title,author,loan_status,purchase_date,Member_ID):
    '''
this function adds the ID and popularity to the temporary list store for popularity
'''
    temp_database.append([ID,title,author,loan_status,purchase_date,Member_ID])
#The functions below, use the same split functions to seperate books into a list of string
#and then loan_status with either in stock or Out on loan
def return_book():
    '''
The return book function, checks with the user to see if they would ike to return
a book and then dispalys the books that are currently on loan. the user
must the input the ID of the book that they would like to return to the
library.
'''
    checkoutlist.clear()
    checkoutlist.clear()
    temp_database.clear()
    In_Stock_ID.clear()
    checkout = input("would you like to return a book?: ")
    if checkout.lower() == "yes":
        with open('Database.txt') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                checkoutlist.append([str(line[0]).replace('[',''),line[1],line[2],line[3],line[4],str(line[5]).replace(']','')])
            
            for i in checkoutlist:
                if i[3].strip() == "'Out on Loan'" or i[3].strip() == '"Out on Loan"':
                    #if the loan status of a book is out on loan then the ID is added to list of
                    #available books to return
                    In_Stock_ID.append(i[0])
                    In_Stock_book = (i[1])
                    print(i[0],i[1])
            bookrequest = input("Enter the ID of the book you would like to return: ")
            Id_for_return = "0"
            for i in checkoutlist:
                if i[0].strip() == bookrequest:
                    print("Book has been returned")
                    with open('Database.txt') as f:
                        for line in f:
                            if bookrequest == line[0]+line[1]:
                                lines = line.split(",")
                                add_to_temp((str(lines[0]).replace('[','').strip()),lines[1].replace("'",'').strip(),lines[2].strip(),lines[3].strip(),lines[4].strip(),str(lines[5]).replace('\n','').strip())
                                print((str(lines[0]).replace('[','').strip()),lines[1].replace("'",'').strip(),lines[2].strip(),lines[3].strip(),lines[4].strip(),str(lines[5]).replace('\n','').strip())
                                if i[3].strip() == "'Out on Loan'":
                                    newdatabase=line.replace(" 'Out on Loan'", " 'In Stock'").replace(i[5],Id_for_return)
                                elif i[3].strip() == '"Out on Loan"':
                                    newdatabase=line.replace('"Out on Loan"','"In Stock"').replace(i[5],Id_for_return)
                                    #if the book was out on loan before the code then switches it to In Stock

                    with open('Database.txt', "w") as f:
                             f.write('')
                    with open('Database.txt', "a") as f:
                        for i in temp_database:
                            f.write((str(i).replace("[",'')).replace("]",'').replace("'",'').strip()+"\n")
                        f.write(newdatabase)

def book_checkout():
    '''
The checkout book function, checks with the user to see if they would ike to checkout
a book and then dispalys the books that are currently In Stock. the user
must the input the ID of the book that they would like to checkout of the
library.
'''
    checkoutlist.clear()
    checkoutlist.clear()
    temp_database.clear()
    In_Stock_ID.clear()
    checkout = input("would you like to take out a book?: ")
    if checkout.lower() == "yes":
        with open('Database.txt') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                checkoutlist.append([str(line[0]).replace('[',''),line[1],line[2],line[3],line[4],str(line[5]).replace(']','')])
            
            for i in checkoutlist:
                if i[3].strip() == "'In Stock'" or i[3].strip() == '"In Stock"':
                    #if the loan status of a book is In Stock then the ID is added to list of
                    #available books to check out
                    In_Stock_ID.append(i[0])
                    In_Stock_book = (i[1])
                    print(i[0],i[1])
            bookrequest = input("Enter the ID of one the available books you would like to checkout: ")
            Id_for_checkout = input("Enter the ID of the user checking out the book: ")
            for i in checkoutlist:
                if i[0].strip() == bookrequest:
                    print("Book has been checked out")
                    with open('Database.txt') as f:
                        for line in f:
                            if bookrequest not in line[0]+line[1]:
                                lines = line.split(",")
                                add_to_temp((str(lines[0]).replace('[','').strip()),lines[1].replace("'",'').strip(),lines[2].strip(),lines[3].strip(),
                                            lines[4].strip(),str(lines[5]).replace('\n','').strip())
                            if bookrequest in line[0]+line[1]:
                                if i[3].strip() == "'In Stock'":
                                    newdatabase=line.replace(" 'In Stock'", " 'Out on Loan'").replace(i[5],Id_for_checkout)
                                    book_ID = i[0]
                                    book_name = i[1].strip()
                                elif i[3].strip() == '"In Stock"':
                                    newdatabase=line.replace(' "In Stock"', " 'Out on Loan'").replace(i[5],Id_for_checkout)
                                    book_ID = i[0]
                                    book_name = i[1].strip()
                                #if the book was In Stock before the code then switches it to Out on Loan
                                
                                    
                    with open('Database.txt', "w") as f:
                             f.write('')
                    with open('Database.txt', "a") as f:
                        for i in temp_database:
                            f.write((str(i).replace("[",'')).replace("]",'').replace("'",'').strip()+"\n")
                        f.write(newdatabase)
                    pop_check(book_ID) #sends the ID to the popularity check
                    logfile_checkout(book_ID,book_name) # sends the ID and name to the popularity check
    elif checkout.lower() == "no":
        print("returning to menu")
    else:
        print("Try again. Please enter Yes or No: ")
        book_checkout()
        

