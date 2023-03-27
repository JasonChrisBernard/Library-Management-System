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
        
def edit_books():
    print("Tables in the DataBase:\n\t1-->books\n\t2-->chapters\n\t3-->subjects\n")
    edit_choice = int(input("Which table do you want to edit data from? : "))
    if edit_choice == 1:
        print("Columns in the Book Table\n")
        print("1) Title\n2) Subject_Code\n3) Author\n4) Publisher\n5) Price\n6) Location\n")
        edit_choice = int(input("Enter the column number you want to edit : "))
        print()
        create_db()
        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()
        print("Books Data Table")
        for x in result:
            print(x)
        print()
        if edit_choice == 1:
            edit_choice1 = int(input("Enter the book number you want to edit : "))
            edit_value = input("Enter the new value for the title : ")
            sql = "UPDATE books SET Title = %s WHERE Book_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

        elif edit_choice == 2:
            edit_choice1 = int(input("Enter the book number you want to edit : "))
            edit_value = input("Enter the new value for the subject code : ")
            sql = "UPDATE books SET Subject_Code = %s WHERE Book_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

        elif edit_choice == 3:
            edit_choice1 = int(input("Enter the book number you want to edit : "))
            edit_value = input("Enter the new value for the author : ")
            sql = "UPDATE books SET Author = %s WHERE Book_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

        elif edit_choice == 4:
            edit_choice1 = int(input("Enter the book number you want to edit : "))
            edit_value = input("Enter the new value for the publisher : ")
            sql = "UPDATE books SET Publisher = %s WHERE Book_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

        elif edit_choice == 5:
            edit_choice1 = int(input("Enter the book number you want to edit : "))
            edit_value = input("Enter the new value for the price : ")
            sql = "UPDATE books SET Price = %s WHERE Book_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

        elif edit_choice == 6:
            edit_choice1 = int(input("Enter the book number you want to edit : "))
            edit_value = input("Enter the new value for the location : ")
            sql = "UPDATE books SET Location = %s WHERE Book_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

    elif edit_choice == 2:
        print("Columns in the Chapters Table\n")
        print("1) Chapter_No\n2) Chapter_Title\n3) Starting_Page_No\n4) Ending_Page_No\n")
        edit_choice = int(input("Enter the column number you want to edit : "))
        print()
        create_db()
        cursor.execute("SELECT * FROM chapters")
        result = cursor.fetchall()
        print("Chapters Data Table")
        for x in result:
            print(x)
        print()
        if edit_choice == 1:
            edit_choice1 = int(input("Enter the row number you want to edit : "))
            edit_value = input("Enter the new value for the chapter number : ")
            sql = "UPDATE chapters SET Chapter_No = %s WHERE Row_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

        elif edit_choice == 2:
            edit_choice1 = int(input("Enter the row number you want to edit : "))
            edit_value = input("Enter the new value for the chapter title : ")
            sql = "UPDATE chapters SET Chapter_Title = %s WHERE Row_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

        elif edit_choice == 3:
            edit_choice1 = int(input("Enter the row number you want to edit : "))
            edit_value = input("Enter the new value for the starting page number : ")
            sql = "UPDATE chapters SET Starting_Page_No = %s WHERE Row_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

        elif edit_choice == 4:
            edit_choice1 = int(input("Enter the row number you want to edit : "))
            edit_value = input("Enter the new value for the ending page number : ")
            sql = "UPDATE chapters SET Ending_Page_No = %s WHERE Row_No = %s"
            cursor.execute(sql,(edit_value,edit_choice1))
            db.commit()
            print("New value added")

    elif edit_choice == 3:
        create_db()
        cursor.execute("SELECT * FROM subjects")
        result = cursor.fetchall()
        print("Subjects Data Table")
        for x in result:
            print(x)
        edit_choice1 = int(input("Enter the subject code you want to edit : "))
        edit_value = input("Enter the new value for the subject name : ")
        sql = "UPDATE subjects SET Name = %s WHERE Subject_Code = %s"
        cursor.execute(sql,(edit_value,edit_choice1))
        db.commit()
        print("New value added")


def del_books():
    print("Tables in the DataBase:\n\t1-->books\n\t2-->chapters\n\t3-->subjects\n")
    del_choice = int(input("Which table do you want to delete data from? : "))
    if del_choice == 1:
        create_db()
        cursor.execute("SELECT * FROM books")
        result = cursor.fetchall()
        for x in result:
            print(x)
        print()
        del_choice = int(input("Enter the book number that you want to delete : "))
        sql = "DELETE FROM books WHERE Book_No = %s"
        val = (del_choice,)
        cursor.execute(sql,val)
        db.commit()
        print("Book number",del_choice,"is deleted")

    if del_choice == 2:
        create_db()
        cursor.execute("SELECT * FROM chapters")
        result = cursor.fetchall()
        for x in result:
            print(x)
        print()
        del_choice = int(input("Enter the chapter number that you want to delete : "))
        sql = "DELETE FROM chapters WHERE Chapter_No = %s"
        val = (del_choice,)
        cursor.execute(sql,val)
        db.commit()
        print("Chapter number",del_choice,"is deleted")

    if del_choice == 3:
        create_db()
        cursor.execute("SELECT * FROM subjects")
        result = cursor.fetchall()
        for x in result:
            print(x)
        print()
        del_choice = int(input("Enter the subject code that you want to delete : "))
        sql = "DELETE FROM subjects WHERE Subject_Code = %s"
        val = (del_choice,)
        cursor.execute(sql,val)
        db.commit()
        print("Subject code",del_choice,"is deleted")


