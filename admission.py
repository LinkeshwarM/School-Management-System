import main_menu
import admission
import mysql.connector

def ADM_MENU():
    while True:
        admission.clrscreen()
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t * ** * Welcome to School Management System * * * *")
        print("\t\t-------------------------------------------------------------------------")

        print("\n\t\t * * ** A D M I S S I O N  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Admission Details ")
        print("2 :  Show Admin_Details")
        print("3 :  Search ")
        print("4 :  Deletion")
        print("5 :  Update Admission Details")
        print("6 :  Return to MAIN MENU...")
        print("\t\t-------------------------------------------------------------------------")
        choice = int(input("Enter Your Choice 1-6 :"))

        if choice == 1:
            admission.Admin_details()
        elif choice == 2:
            admission.Show_Admin_Details()
        elif choice == 3:
            admission.Search_Admin_Details()
        elif choice == 4:
            admission.delete_Admin_Details()
        elif choice == 5:
            admission.Edit_Admin_Details()
        elif choice == 6:
            return
    else:
        print("Error : Invalid Choice try again....")
        conti = input("Press any key return to MAIN - MENU..")


def Admin_details():
    try:
        mycon = connection.MySQLConnection(user='root', password=' ', host='localhost',database='schoolmgm')
        MyCur = mycon.cursor()


    adno = input("Enter Admission No ")
    rollno = int(input("Enter Rollno :"))
    sname = input("Enter Student Name :")
    address = input("Enter Address :")
    phone = input("Enter Phone No.")
    class1 = input("Enter Class")

    Query = ("Insert into admission values(%s,%d,%s,%s,%s,%s)")
    Record=(adno, rollno, sname, phone,class )
    MyCur.execute(Query, Record)
    MyCur.close()
    myCon.close()
    print("Record has been Saved .. in Admission Data Table....")
    except mysql.connector.error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Oops! Something is invalid ...Re.Check User Name & Password........")

    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Admission /SchoolMgm: DATABASE does not exists...try another DB")
    else:
        print(err)
    MyCon.close()

    from mysql.connector import errorcode
    from mysql.connector import (connection)


def Show_Admin_Details():
    try:
        mycon = connection.MySQLConnection(user='root', password=' ', host='localhost',database='schoolmgm')
    MyCur = mycon.cursor()

    Query = (“Select * from Admission”)
    MyCur.execute(Query)

    for (adno, rollno, name, addres,class ) in cursor:
        print(“Admission Code”, adno)
        print(“Roll Number”, rollno)
        print(“Student Name”, sname)
        print(“Address”, address)
        print(“Phone Number”, phone, “Class”,class )
    Mycur.close()  Con.close()

    except mysql.connector.error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Oops! Something is invalid ...Re.Check User Name & Password........")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Admission /SchoolMgm: DATABASE does not exists...try another DB")
    else:
        print(err)
    mycur.close()
    mycon.close()


# --------------------------------------------------------------------------------
def Search_Admin_Details():


    try:
        mycon = connection.MySQLConnection(user='root', password=' ', host='localhost',database='schoolmgm')

    temp_adno = input(“Enter Admission Number to be Search:”)
    MyCur = mycon.cursor()
    Query = (“Select * from Admission where  temp_adno= “ % s”)
    rec_srch = (temp_adno,)
    MyCur.execute(Query, rec_srch)

    for (adno, rollno, name, addres,class ) in cursor:
        print(“Admission Code”, adno)
        print(“Roll Number”, rollno)
    print(“Student Name”, sname)
    print(“Address”, address)
    print(“Phone Number”, phone, “Class”,class )

    except mysql.connector.error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Oops! Something is invalid ...Re.Check User Name & Password........")
    if err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Admission /SchoolMgm: DATABASE does not exists...try another DB")
    else:
        print(err)
    mycur.close()
    mycon.close()


    # --------------------------------------------------------------------------------------

    # admission.def delete_Admin_Details()

    # --------------------------------------------------------------------------------------

def delete_Admin_Details():
    try:
        mycon = connection.MySQLConnection(user='root', password=' ', host='localhost',database='schoolmgm')

    temp_adno = input(“Enter Admission Number to be Delete:”)
    MyCur = mycon.cursor()
    Query = (“ “ “ Delete from Admission where adno= “ % s”)
    rec_srch = (temp_adno,)
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
    # -------------------------------------------------------------------------------------------------
    # admission.Edit_Admin_Details():    ADM_MENU() Choice=5
    # -------------------------------------------------------------------------------------------------


def Edit_Admin_Details():
    try:
        mycon = connection.MySQLConnection
    (user='root', password=' ', host='localhost',
    database='schoolmgm')


    temp_adno = input(“Enter Admission Number to be Update / Edit:”)

    Query = (“ “ “ Select * from Admission
             where temp_adno= “ % s”)

    MyCur = mycon.cursor()
    rec_srch = (temp_adno,)

    print("Input New Data ")

    sname = input("Enter Student Name :")
    address = input("Enter Address :")
    phone = input("Enter Phone No.")
    class1 = input("Enter Class")

    Q = ("Update admission set sname=" % s",address=" % s",
    phone="%s", class1="%s", where temp_adno="%s")

    D = (sname, address, phone, class1)

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

##--------------------------------------------------------------------------------