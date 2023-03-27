import lib_portal.library_c
import random
import mysql.connector
#Create variables
user_opt = 0
book_no = 0
title = 0
sub_code = 0
author = 0
publisher = 0
price = 0
location = 0
chap_no = 0
chap_title = 0
start_no = 0
end_no = 0
new_chap = 0
table_list = []
del_choice = 0
edit_choice = 0

def create_db():
    global db, cursor
    conDict = {'host':'localhost',
               'database':'abc_book_store',
               'user':'root',
               'password':''}

    db = mysql.connector.connect(**conDict)

    cursor = db.cursor()
    cursor.execute("SHOW TABLES")

    #Storing the available data tables in a list
    for table_name in cursor:
        table_list.append(table_name)

    #Creating a data table, if that data table is not in the table_list
    if ("books",) not in table_list:
        cursor.execute("CREATE TABLE books(Book_No INT AUTO_INCREMENT PRIMARY KEY, Title VARCHAR(200), Subject_Code INT(200), Author VARCHAR(200), Publisher VARCHAR(200), Price INT(200), Location VARCHAR(200))")

    if ("chapters",) not in table_list:
        cursor.execute("CREATE TABLE chapters(Row_No INT AUTO_INCREMENT PRIMARY KEY, Book_No INT(200), Chapter_No INT(200), Chapter_Title VARCHAR(200), Starting_Page_No INT(200), Ending_Page_No INT(200))")
    
    if ("subjects",) not in table_list:
        cursor.execute("CREATE TABLE subjects(Subject_Code INT AUTO_INCREMENT PRIMARY KEY, Name VARCHAR(200))")
    


def menu():
    global user_opt
    print("Menu Options:\n\t1. Direct search to find books\n\t2. Add books\n\t3. Edit books\n\t4. Delete books\n")
    user_opt = int(input("Enter your option number : "))

    
def add_books():
    global book_no,sub_code
    book_no = random.randrange(1,9999)
    print("\nPlease enter the following information for the book number",book_no,"\n")
    title = input("Enter the title of the book : ")
    sub_code = input("Enter the subject code of the book : ")
    author = input("Enter the name of the author : ")
    publisher = input("Enter the name of the publisher : ")
    price = input("Enter the price of the book : ")
    location = input("Enter the location of the book : ")
    print("\nBook number",book_no,"is created successfully!\n")
    print("Please enter the chapter information of the book number",book_no,"\n")
    
    #Storing the data in a DB
    create_db()
    mySQLText = "INSERT INTO books(Book_No, Title, Subject_Code, Author, Publisher, Price, Location) VALUES(%s,%s,%s,%s,%s,%s,%s)"
    myValues = (book_no, title, sub_code, author, publisher, price, location)
    cursor.execute(mySQLText, myValues)
    db.commit()
    db.close()

    
    
def create_chapters():
    global row_no
    while True:
        row_no = random.randrange(1,9999)
        chap_no = input("Enter the chapter number : ")
        chap_title = input("Enter the title of the chapter "+chap_no+" : ")
        start_no = input("Enter the starting page number of chapter "+chap_no+" : ")
        end_no = input("Enter the ending page number of chapter "+chap_no+" : ")
        print("\n")
        new_chap = input("Do you want to enter the information of another chapter? (y/n) : ")
        new_chap = new_chap.lower()

        #Storing the data in a DB
        create_db()
        mySQLText = "INSERT INTO chapters(Row_No, Book_No, Chapter_No, Chapter_Title, Starting_Page_No, Ending_Page_No) VALUES(%s,%s,%s,%s,%s,%s)"
        myValues = (row_no, book_no, chap_no, chap_title, start_no, end_no)
        cursor.execute(mySQLText, myValues)
        db.commit()
        db.close()

        if new_chap == "y":
            continue
        else:
            print("Chapter information of the book number",book_no," is successfully added!")
            break
def subjects():
    sub_code=input("Enter the subject code :")
    name=input("Enter the name : ")

    #Storing the data in a DB
    create_db()
    mySQLText = "INSERT INTO subjects(Subject_Code, Name) VALUES(%s,%s)"
    myValues = (sub_code,name)
    cursor.execute(mySQLText, myValues)
    db.commit()
    db.close()

menu()
def search_books():
    print("Search menu:\n\t1) Book_Number\n\t2) Title\n\t3) Author\n\t4) Publisher\n")
    menu_choice = int(input("From what do you need to search? : "))
    if menu_choice == 1:
        create_db()
        cursor.execute("SELECT Book_No FROM books")
        result = cursor.fetchall()
        for x in result:
            print(x,end=" ")
        print("\n")
        sql = "SELECT * FROM books WHERE Book_No = %s"
        choice = int(input("Enter the book number : "))
        choice = (choice,)
        cursor.execute(sql,choice)
        result = cursor.fetchall()
        for x in result:
            print(x)
        db.commit()

    elif menu_choice == 2:
        create_db()
        cursor.execute("SELECT Title FROM books")
        result = cursor.fetchall()
        for x in result:
            print(x,end=" ")
        print("\n")
        sql = "SELECT * FROM books WHERE Title = %s"
        choice = input("Enter the title : ")
        choice = (choice,)
        cursor.execute(sql,choice)
        result = cursor.fetchall()
        for x in result:
            print(x)
        db.commit()

    elif menu_choice == 3:
        create_db()
        cursor.execute("SELECT Author FROM books")
        result = cursor.fetchall()
        for x in result:
            print(x,end=" ")
        print("\n")
        sql = "SELECT * FROM books WHERE Author = %s"
        choice = input("Enter the author : ")
        choice = (choice,)
        cursor.execute(sql,choice)
        result = cursor.fetchall()
        for x in result:
            print(x)
        db.commit()

    elif menu_choice == 4:
        create_db()
        cursor.execute("SELECT Publisher FROM books")
        result = cursor.fetchall()
        for x in result:
            print(x,end=" ")
        print("\n")
        sql = "SELECT * FROM books WHERE Publisher = %s"
        choice = input("Enter the publisher : ")
        choice = (choice,)
        cursor.execute(sql,choice)
        result = cursor.fetchall()
        for x in result:
            print(x)
        db.commit()

lib_portal.library_c.edit_books()            
lib_portal.library_c.del_books()
   

if user_opt == 1:
    search_books()

elif user_opt == 2:
    add_books()
    create_chapters()
    subjects()

elif user_opt == 3:
    lib_portal.library_c.edit_books()

elif user_opt == 4:
    lib_portal.library_c.del_books()


 
