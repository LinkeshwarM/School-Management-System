import main_menu
import fee_details


def FEE_MENU():  # fee_details.py module
    while True:
        fee_details.clrscreen()
        print("\t\t-------------------------------------------------------------------------")
        print("\t\t * ** * Welcome to School Management System * * * *")
        print("\t\t-------------------------------------------------------------------------")
        print("\n\t\t * * ** STUDENT FEE  M E N U   * * ** ")
        print("\t\t-------------------------------------------------------------------------")
        print("1 :  Fee Deposit ")
        print("2 :  Fee Details")
        print("3 :  return to Main Menu..")
        print("\t\t-------------------------------------------------------------------------")
        choice = int(input("Enter Your Choice 1-3 :"))
        if choice == 1:
            fee_details.fees_Deposit()
        elif choice == 2:
            fee_details.FDetails()
        elif choice == 3:
            return
        else:
            print("Error : Invalid Choice try again....")
            conti = input("Press any key to Back to MAIN - MENU..")