import main_menu
import lib_details


def LIB_MENU():  # lib_details.py module
    while True:
        lib_details.clrscreen()
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t * ** * Welcome to School Management System * * * *")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** Library  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Book Issue ")
        print("2 :  Book Return")
        print("3 :  return to Main Menu..")
        print("\t\t-------------------------------------------------------------------------")
        choice = int(input("Enter Your Choice 1-3 :"))

        if choice == 1:
            lib_details.book_issue()
        elif choice == 2:
            lib_details.book_return()
        elif choice == 3:
            return
        else:
            print("Error : Invalid Choice try again....")
            conti = input("Press any key to Back to MAIN - MENU..")