####### Monthly Budget Tracker #######,  SRINIVASAN PARAMASIVAM, 20-Dec-2025 #######

#Function to add the expense
def add_expense():
    '''This is function to add the expenses. It will get Date of Expenses (YYYY-MM-DD), 
    Category of the Expenses, Amount Spent and breif Description of the Expenses from the user'''

    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    #Validation of date format can be added here
    if not date or date.strip() == "" or len(date) != 10 or date[4] != '-' or date[7] != '-' or type(date[:4]) != int or not type(date[5:7]) != int or type( date[8:])!= int: #validate the input date format
        print("Date should be in YYYY-MM-DD format. Please try again.")
        return None
    category = input("Enter the category of the expense (e.g., Food, Transport, Utilities): ")
    amount = float(input("Enter the amount spent: $"))
    description = input("Enter a brief description of the expense: ")
    return   {
        'expense_date': date,
        'expense_category': category,
        'expense_amount': amount,
        'expense_description': description
    }

while True:
    expenses = []  # List to store expenses
    print("################################### Welcome to Monthly Budget Tracker ###################################")
    print(" **** Your Monthly Budget is $2000 **** ")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Track Remaining Budget")
    print("4. Save the Expenses to a File")
    print("5. Exit")
    print("################################### Welcome to Monthly Budget Tracker ###################################")
    choice = input("Enter your choice: ")
    if choice == '1': #Add Expense Option so call the function to add expense
        expenses.append(add_expense()) #append the returned expense dictionary to the expenses list
    elif choice == '2': #View Expenses Option so call the function to view expenses
        pass
    elif choice == '3': #Track Remaining Budget Option so call the function to track remaining budget
        pass
    elif choice == '4': #Save the Expenses to a File Option so call the function to save expenses to a file
        pass
    elif choice == '5': #Exit Option
        print("Thanks for using the Monthly Budget Tracker. Goodbye! Have a nice day!") #Exit message
        break
    else:
        print("Invalid choice. Please try again.") #Invalid choice handling

