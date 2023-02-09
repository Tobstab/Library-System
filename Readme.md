
## *****************************************************************
This is the Library System ~ Created By Tobi Akinyemi
Version 1
Filename - Menu.py
## *****************************************************************
## ------------------------- Description ---------------------------
The Library system, allows a user with the correct 
creditionals - ID and password to access the library system.
This provides with the ability to Checkout a book, return a book,
search for the availability of the books as well as find the most 
popular book. Which is presented in a graph.
## ------------------------- How to Use -----------------------------
The GUI is only used to make calling functions easier,
however the majority of my library system occurs in the python IDLE.
To access the library system - feel free to create a new log ID
using the GUI. By pressing the no button when the system asks 
whether or not "you have used the library system before". Or use the 
predefined guest login. The ID = 34 and password = 12345, see 
librarians txt file for the Ids that can be used, written in the form
[ID,Name,Password]
The ID for checkout must be a 4 digit ID for future implementation
## --------------------- Highlighted Features -----------------------
One feature that i was most proud of is my function for searching
for books. As it is highly functional and doesnt require the user 
to input the full name of a book but only parts of it are needed 
as a minimum. it takes the users input splits into individual
words and splits every book in the database into words.
They system tries to check for every word in the inputted search
if the word matches with a word in the certain title of a book.
## ----------------------------- Bugs -------------------------------
My log function works, but it doesnt replace the time of return
correctly. This can be fixed but within the constriant i was unable to
get it to work. However everything else works well without fail. Including
the graphing system.
