'''
----------------------------------
MENU System for my library system
created by Tobi Akinyemi B921352
----------------------------------
'''
import math
import random
import Database
from bookcheckout import *
from booksearch import *
from tkinter import *
from time import sleep
members_list = [] # This the inital declaration of the list - members_list
reset_items = []

def reset_screen():
    for i in reset_items:
        i.destroy() # destroys the widget on the window
    '''
This fucntion resets the page screen by taking each element in the list reset_items and destroying each of them
'''
def booksearch_submit():
    '''
This function links the submit button to the booksearch function, taking in the bookrequest as input from the entry box 
'''
    bookrequest = Entry5.get() #assigns the entry input from the user to the variable bookrequest
    booksearch(bookrequest) # takes bookrequest and runs it through the boksearch function
def bookreturn_menu():
    '''
This function controls the menu for the bookreturn_b button,
first of all it destroys the tags from the main menu, so that they dont
appear on the screen anymore. Then it creates a tag on the screen, instructions
for the user so that they how to use the system. Then creates a button which allows the user
to run the book return function. Lastly, it adds the widgets on the screen to the reset items list so that
they can be cleared when switching back to the menu.
'''
    BookSearch_b.destroy()
    Bookcheckout_b.destroy()
    Bookreturn_b.destroy()
    pop_check_button.destroy()

    global reset_items
    Tag7=Label(window,text=("%s, To return a book, press the button below: "%(name)),fg="Black",bg="red",relief="solid",font=("arial",13,"bold"))
    Tag7.place(x=90,y=200)

    Tag8=Label(window,text=("%s See Python Shell to continue after pressing return "%(name)),fg="Black",bg="red",relief="solid",font=("arial",13,"bold"))
    Tag8.place(x=80,y=450)

    Bookreturn_submit=Button(window,text="Return",fg="Black",bg="red",relief="groove",height = 3, width = 20,font=("arial",15,"bold"), command = return_book)
    Bookreturn_submit.place(x=180,y=300) # creates the submit button for returning a book and places it onto the screen

    return_to_menu=Button(window,text="Menu",fg="Black",bg="red",relief="groove",height = 2, width = 10,font=("arial",15,"bold"), command = menu)
    return_to_menu.place(x=480,y=0) # creates the menu button to return to the menu and places it onto the screen
    reset_items = [Tag7,Tag8,Bookreturn_submit,return_to_menu]
def bookcheckout_menu():
    '''
This function controls the menu for the bookcheckout_b button,
first of all it destroys the tags from the main menu, so that they dont
appear on the screen anymore. Then it creates a tag on the screen, instructions
for the user so that they how to use the system. Then creates a button which allows the user
to run the book checking out function. Lastly, it adds the widgets on the screen to the reset items list so that
they can be cleared when switching back to the menu.
'''
    BookSearch_b.destroy()
    Bookcheckout_b.destroy()
    Bookreturn_b.destroy()
    pop_check_button.destroy()

    global reset_items
    Tag7=Label(window,text=("%s, To checkout a book, press the button below: "%(name)),fg="Black",bg="orange",relief="solid",font=("arial",13,"bold"))
    Tag7.place(x=90,y=200)

    Tag8=Label(window,text=("%s See Python Shell to continue after pressing checkout "%(name)),fg="Black",bg="orange",relief="solid",font=("arial",13,"bold"))
    Tag8.place(x=80,y=450)

    Bookcheckout_submit=Button(window,text="Checkout",fg="Black",bg="orange",relief="groove",height = 3, width = 20,font=("arial",15,"bold"), command = book_checkout)
    Bookcheckout_submit.place(x=180,y=300)# creates the book checkout button for checking a book and places it onto the screen

    return_to_menu=Button(window,text="Menu",fg="Black",bg="orange",relief="groove",height = 2, width = 10,font=("arial",15,"bold"), command = menu)
    return_to_menu.place(x=480,y=0)
    reset_items = [Tag7,Tag8,Bookcheckout_submit,return_to_menu]
    
def booksearch_menu():
    '''
This function controls the menu for the bookSearch_b button,
first of all it destroys the tags from the main menu, so that they dont
appear on the screen anymore. Then it creates a tag on the screen, instructions
for the user so that they how to use the system. Then creates a button which allows the user
to run the book searching function. Lastly, it adds the widgets on the screen to the reset items list so that
they can be cleared when switching back to the menu.
'''
    BookSearch_b.destroy()
    Bookcheckout_b.destroy()
    Bookreturn_b.destroy()
    pop_check_button.destroy()

    global reset_items
    Tag7=Label(window,text=("%s, Please Enter name of book to search for availability: "%(name)),fg="Black",bg="cyan",relief="solid",font=("arial",13,"bold"))
    Tag7.place(x=70,y=200) 

    Tag8=Label(window,text=("%s See Python Shell to continue after pressing search "%(name)),fg="Black",bg="cyan",relief="solid",font=("arial",13,"bold"))
    Tag8.place(x=80,y=450)

    global Entry5
    Entry5=Entry(window,font=("arial",12,"bold"), width= 100)
    Entry5.place(x=0, y=280) # this creates an entry box for the user so they can search for the book they want

    BookSearch_submit=Button(window,text="Search",fg="Black",bg="cyan",relief="groove",height = 3, width = 20,font=("arial",15,"bold"), command = booksearch_submit)
    BookSearch_submit.place(x=80,y=320)# creates a submit button so that the entry can be saved to a variable

    BookSearch_all=Button(window,text="All Books",fg="Black",bg="cyan",relief="groove",height = 3, width = 10,font=("arial",15,"bold"), command = loanbook)
    BookSearch_all.place(x=400,y=320)# creates a button so that the user can see the total collection of books the library has

    return_to_menu=Button(window,text="Menu",fg="Black",bg="cyan",relief="groove",height = 2, width = 10,font=("arial",15,"bold"), command = menu)
    return_to_menu.place(x=480,y=0)
    reset_items = [Tag7,Tag8,Entry5,BookSearch_submit,BookSearch_all,return_to_menu]

    
    
def menu():
    '''
This is the main menu for the gui, it creates buttons for all of the functions of
the library system. These being the book search button, the book return button and the
book checkout button. There is a popularity of book button which produces a graph,
displaying the popularity of books in the database.
'''
    reset_screen()
    Tag6=Label(window,text=("Welcome %s"%(name)),fg="Black",bg="blue",relief="solid",font=("arial",20,"bold"))
    Tag6.place(x=210,y=100)
    Entry3.destroy()
    Label3.destroy()
    Entry4.destroy()
    Label4.destroy()
    Button4.destroy()

    global BookSearch_b
    BookSearch_b=Button(window,text="Search For A Book",fg="Black",bg="cyan",relief="groove",height = 5, width = 20,font=("arial",15,"bold"), command=booksearch_menu)
    BookSearch_b.place(x=180,y=150) #creates the book search menu button and places it on the screen

    global Bookcheckout_b
    Bookcheckout_b=Button(window,text="Checkout A Book",fg="Black",bg="orange",relief="groove",height = 5, width = 20,font=("arial",15,"bold"), command=bookcheckout_menu)
    Bookcheckout_b.place(x=180,y=300) #creates the book checkout menu button and places it on the screen

    global Bookreturn_b
    Bookreturn_b=Button(window,text="Return a Book",fg="Black",bg="red2",relief="groove",height = 5, width = 20,font=("arial",15,"bold"), command=bookreturn_menu)
    Bookreturn_b.place(x=180,y=450) #creates the book return menu button and places it on the screen

    global pop_check_button
    pop_check_button=Button(window,text="Popularity of books",fg="Black",bg="olivedrab1",relief="groove",height = 1, width = 20,font=("arial",12,"bold"), command=pop_show)
    pop_check_button.place(x=0,y=0) #creates the popularity graph button and places it on the screen
    

def login_check():
    '''
This is the login check function, and it reads the librarians.txt and splits each line
so that each element can be added to a list so that the ID and password can
tested agasint the users input. if they are equal to the users input then the librarian can access
the system.
'''
    f = open("librarians.txt","r")
    librarian_ID = Entry3.get()
    password  = Entry4.get()
    for line in f: #for every line inside of the txt file, each line is split by commas and each value is added to a database
        line = line.strip()
        line = line.replace("'",'')
        line = line.split(',')
        members_list.append([str(line[0]).replace('[',''),line[1].strip(),(str(line[2]).replace(']','')).strip()])
    for i in members_list: # then for every value in members list, the first and second elements are tested agaisn the users input
        if i[0] == librarian_ID and i[2] == password:
            global name
            name = i[1]
            menu() #The user can access the menu if the password is correct
        else:
            print("Please try Again")
                
    members_list.clear() #clears the members list so that there is no repeated data
    
 
def login_page1():
    '''
This is the login page for users, who have created a login
This has two entry box one for the librarian ID and the other
for the password of the user. With a submit button which sends
the user input within the entry box to the login check function
'''
    Tag3=Label(window,text="Library System V1",fg="Black",bg="blue",relief="solid",font=("arial",20,"bold"))
    Tag3.place(x=180,y=50)

    Button1.destroy()
    Button2.destroy()
    Tag2.destroy()

    global Entry3
    global Label3
    Label3=Label(window,text="Enter your Librarian_ID: ",fg="Black",bg="blue",relief="solid",font=("arial",12,"bold"))
    Label3.place(x=50,y=250)
    Entry3= Entry(window,font=("arial",12,"bold"))
    Entry3.place(x=350, y=250) #Entry box for the user input for librarian ID

    global Entry4
    global Label4
    Label4=Label(window,text="What is your password?: ",fg="Black",bg="blue",relief="solid",font=("arial",12,"bold"))
    Label4.place(x=50,y=350)
    Entry4= Entry(window,font=("arial",12,"bold"))
    Entry4.place(x=350, y=350) #Entry box for the user's password
    
    global Button4
    Button4=Button(window,text="Log In",fg="Black",bg="blue",relief="groove",command=login_check)
    Button4.place(x=150,y=400) #runs the login_check function so that the inputs can be verified
    

def new_user_submit():
    '''
This function, takes the input for creating a new login and adds
to the librarian txt so that they can use the login menu to access
the library system
'''
    librarians = open("librarians.txt","a")
    username = Entry1.get() # get the entry for the username
    password = Entry2.get() # get the entry for the password
    librarian_details = [str(librarian_ID),username,password] #stores the ID, username and password
    librarians.write(str(librarian_details).strip() + "\n") #writes the information to the txt file
    Button3.destroy()
    Label1.destroy()
    Label2.destroy()
    Tag4.destroy()
    Entry1.destroy()
    Entry2.destroy()
    login_page1()
    
    
    
def new_user_page():
    '''
This function creates the menu for creating a login for a user,
this creates two entry boxes one for the users name and the other for the password
This also creates a random ID for the the user so that they can be uniquely identified
At the end there is a button to submit all this information to the new user submit function
'''
    global librarian_ID
    librarian_ID = random.randint(1,1000) #genrates a random between 1 and 1000
    Tag3=Label(window,text="Library System V1",fg="Black",bg="blue",relief="solid",font=("arial",20,"bold"))
    Tag3.place(x=180,y=50)
    
    Tag2.destroy()
    Button1.destroy()
    Button2.destroy()

    global Entry1
    global Label1
    Label1=Label(window,text="What is your name?: ",fg="Black",bg="blue",relief="solid",font=("arial",12,"bold"))
    Label1.place(x=50,y=250)
    Entry1= Entry(window,font=("arial",12,"bold"))
    Entry1.place(x=350, y=250)

    global Entry2
    global Label2
    Label2=Label(window,text="What is your new password?: ",fg="Black",bg="blue",relief="solid",font=("arial",12,"bold"))
    Label2.place(x=50,y=350)
    Entry2= Entry(window,font=("arial",12,"bold"))
    Entry2.place(x=350, y=350)

    global Tag4
    Tag4=Label(window,text=("Your new ID is: "+ str(librarian_ID)),fg="Black",bg="cyan",relief="solid",font=("arial",15,"bold"))
    Tag4.place(x=50,y=150)
    
    global Button3
    Button3=Button(window,text="Submit",fg="Black",bg="blue",relief="groove",command=new_user_submit)
    Button3.place(x=150,y=400)
    return librarian_ID # returns the librarian ID so that it can be used in the user submit function
    

window=Tk() 
window.geometry("600x600")# The size of the screen of the GUI
window.title("Library System by Tobi")

Tag1=Label(window,text="Library System V1",fg="Black",bg="blue",relief="solid",font=("arial",20,"bold"))
Tag1.place(x=180,y=50)#creates the sub title for the library system

Tag2=Label(window,text="Have you used this system before?: ",fg="Black",bg="blue",relief="solid",font=("arial",20,"bold"))
Tag2.place(x=50,y=250)

Button1=Button(window,text="Yes",fg="Black",bg="blue",relief="groove", command=login_page1)
Button1.place(x=150,y=400) #button to check if the user has used the system before if yes then, it send the user to the login page

Button2=Button(window,text="No",fg="Black",bg="blue",relief="groove",command=new_user_page)
Button2.place(x=380,y=400)#button to check if the user has used the system before if yes then, it send the user to the new user page



