import main_menu
import student_data


def STU_MENU():  # student_data.py  module
    while True:
        student_data.clrscreen()
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t * ** * Welcome to School Management System * * * *")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** STUDENT DATA   M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Add Student Record ")
        print("2 :  Show Student Details")
        print("3 :  Search Student Record")
        print("4 :  Delete Student Record ")
        print("5 :  Edit Student Record ")
        print("6 :  Return")
        print("\t\t-------------------------------------------------------------------------")
        choice = int(input("Enter Your Choice 1-6 :"))

        if choice == 1:
            student_data.Add_Records()
        elif choice == 2:
            student_data.Show_Stu_Details()
        elif choice == 3:
            student_data.Search_Stu_Details()
        elif choice == 4:
            student_data.Delete_Stu_Details()
        elif choice == 5:
            student_data.Edit_Stu_Details()
        elif choice == 6:
            return
    else:
        print("Error : Invalid Choice try again....")
        conti = input("Press any key to Back to MAIN - MENU..")


def Add_Records():
    try:
        mycon = connection.MySQLConnection
    (user='root', password=' ', host='localhost',
    database='schoolmgm')
    MyCur = mycon.cursor()


    rollno = int(input("Enter Rollno :"))
    sname = input("Enter Student Name :")
    add = input("Enter Address :")
    Stream = input("Enter Stream:")

    Query = ("Insert into  student_data
             values( % s, % s, % s, % s)
    Record = (rollno, sname, add, stream))
    MyCur.execute(Query, Record)
    MyCur.close()
    MyCon.close()
    print("Record has been Saved .. in Student Data Table....")
    except mysql.connector.error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Oops! Something is invalid ...Re.Check User Name & Password........")

    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Admission /SchoolMgm: DATABASE does not exists...try another DB")
    else:
        print(err)
    MyCon.close()


# ---------------------------------------------------------
#      #2  Show Student Record | def Show_Stu_Details()
# ---------------------------------------------------------

def Show_Stu_Details():
    try:
        mycon = connection.MySQLConnection(user='root', password=' ', host='localhost',
                                           database='schoolmgm')


    MyCur = mycon.cursor()

    Query = (“Select * from Student_Data”)
    MyCur.execute(Query)

    for (rollno, sname, add, stream) in cursor:
        print("Student Rollno ", rollno)
    print("Student Name", name)
    print("Address", add)
    print("Stream", stream)
    Mycur.close()
    Con.close()
    except mysql.connector.error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Oops! Something is invalid ...Re.Check User Name & Password........")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Admission /SchoolMgm: DATABASE does not exists...try another DB")
    else:
        print(err)
        mycur.close()
    mycon.close()


# -------------------------------------------------------------------------
#       #3  Search Student Record | def Search_Stu_Details()
# ---------------------------------------------------------------------

def Search_Stu_Details():
    try:
        mycon = connection.MySQLConnection(user='root', password=' ', host='localhost',
                                           database='schoolmgm')


    temp_rollno = input(“Enter
    Roll
    Number
    to
    be
    Search:”)

    MyCur = mycon.cursor()
    Query = (“Select * from Student_data
             where  temp_rollno= “ % s”)
    rec_srch = (temp_rollno,)

    MyCur.execute(Query, rec_srch)

    for (rollno, sname, add, stream) in cursor:
        print("Student Rollno ", rollno)
        print("Student Name", name)
        print("Address", add)
        print("Stream", stream)

    except mysql.connector.error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Oops! Something is invalid ...Re.Check User Name & Password........")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Admission /SchoolMgm: DATABASE does not exists...try another DB")
        else:
        print(err)

    mycur.close()
    mycon.close()


    # -------------------------------------------------------------------------
    #       #4  Delete Student Record | def Delete_Stu_Details()
    # ---------------------------------------------------------------------

def Delete_Admin_Details():
    try:
        mycon = connection.MySQLConnection
        (user='root', password=' ', host='localhost',
        database='schoolmgm')

    temp_rollno = input(“Enter
    Rollno
    Number
    to
    be
    Delete:”)
    MyCur = mycon.cursor()
    Query = (“ “ “ Delete from Student_Data
             where temp_rollno= “ % s”)
    rec_srch = (temp_rollno,)
    MyCur.execute(Query, rec_srch)

    except mysql.connector.error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Oops! Something is invalid ...Re.Check User Name & Password........")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Admission /SchoolMgm: DATABASE does not exists...try another DB")
    else:
        print(err)
        mycur.close()
        mycon.close()
        print("Record has been deleted Now ")

    # -------------------------------------------------------------------
    #       #5 Edit Student Record | def Edit_Stu_Details()
    # ---------------------------------------------------------------------


def Edit_Admin_Details():
    try:
        mycon = connection.MySQLConnection
    (user='root', password=' ', host='localhost',
    database='schoolmgm')


    temp_rollno = input(“Enter
    Rollno
    Number
    to
    be
    Update / Edit:”)

    Query = (“ “ “ Select * from Student_Data
             where temp_rollno= “ % s”)

    MyCur = mycon.cursor()
    rec_srch = (temp_rollno,)

    print("Input New Data ")

    name = input("Enter  Student Name :")
    add = input("Enter Address :")
    stream = input("Enter Stream")

    Q = ("Update student_data set name=" % s",add=" % s",
    stream="%s" where temp_rollno="%s")

    D = (name, add, stream)

    MyCur.execute(Q, D)
    print("Record has been updated Now")

    except mysql.connector.error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Oops! Something is invalid
        print("Re.Check User Name & Password........")
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Admission /SchoolMgm: DATABASE does not exists...try another DB")
        else:
            print(err)

    mycur.close()
    mycon.close()

    # ------------------end of Student Data Menu ---------------------------------------