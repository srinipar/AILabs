####### Monthly Budget Tracker #######,  SRINIVASAN PARAMASIVAM, 20-Dec-2025 #######
import os


#Function to add the expense
def add_expense():
    '''This is function to add the expenses. It will get Date of Expenses (YYYY-MM-DD), 
    Category of the Expenses, Amount Spent and breif Description of the Expenses from the user'''
    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    #Validation of date format can be added here
    if not date or date.strip() == "" or len(date) != 10 or date[4] != '-' or date[7] != '-' or  not (date[:4]).isdigit()  or not (date[5:7]).isdigit() or not (date[8:]).isdigit(): #validate the input date format
        print("ERROR : Date should be in YYYY-MM-DD format. Please try again.")
        return None

    category = input("Enter the category of the expense (e.g., Food, Transport, Utilities): ")
    if not category or category.strip() == "": #validate the  category
        print("ERROR : Category cannot be empty. Please try again.")
        return None
    
    amount = float(input("Enter the amount spent:"))
    if amount <= 0: #validate the amount
        print("ERROR : Expenses amount should be a positive number. Please try again.")
        return None
    
    description = input("Enter a brief description of the expense: ")
    if not description or description.strip() == "": #validate the description
        print("ERROR : Description cannot be empty. Please try again.")
        return None
    
    #All inputs are validated hence return the expense as a dictionary
    return   {
        'expense_date': date,
        'expense_category': category,
        'expense_amount': amount,
        'expense_description': description
    }
def view_expenses():
    '''This is function to view the expenses recorded by the user'''
    if not expenses:
        print("ERROR : You havent added any expenses yet. Please add some expenses using option 1.")
        return
    for expense in expenses:
        print(expense)


expenses = []  # List to store expenses
monthly_budget=0.0  # Variable to store monthly budget amount
remaining_budget=0.0  # Variable to store remaining budget amount

fileName_Budget = 'budget.txt'  # File to store budget information
#Check for Budget file existence
if os.path.exists(fileName_Budget):
    file_Budget=open(fileName_Budget, 'r')  #Open the Budget file in read mode
    monthly_budget = float(file_Budget.read())  #Read the budget amount from the file
    file_Budget.close()  #Close the Budget file
else:
    input_budget = float(input("**** Your Monthly Budget is not sent, hence please enter your monthly budget amount: "))  #Get the input from user to set the budget
    monthly_budget = input_budget #Set the monthly budget
    file_Budget=open(fileName_Budget, 'w')  #Open the Budget file in write mode
    file_Budget.write((monthly_budget))  #Write the budget amount to the file
    file_Budget.close()  #Close the Budget file


#check for Expenses file existence
fileName_Expenses = 'expenses.csv'  # File to store expenses information
if os.path.exists(fileName_Expenses):
    file_Expenses=open(fileName_Expenses, 'r')  #Open the Expenses file in read mode
    lines = file_Expenses.readlines()  #Read all lines from expense file
    consumed_amount = 0.0  #Variable to store the total consumed amount
    for line in lines:
        date, category, amount, description = line.strip().split(',')  #Split the line into respective fields
        expense = {
            'expense_date': date,
            'expense_category': category,
            'expense_amount': float(amount),
            'expense_description': description
        }
        consumed_amount += float(amount)  #Accumulate the consumed amount
        expenses.append(expense)  #Append the expense dictionary to the expenses list
    remaining_budget = monthly_budget - consumed_amount  #Calculate the remaining budget
    file_Expenses.close()  #Close the Expenses file
else: #Means expenses file doesnt exist, so create an empty expenses file
    file_Expenses=open(fileName_Expenses, 'w')  #Open the Expenses file in write mode
    file_Expenses.close()  #Close the Expenses file
    remaining_budget = monthly_budget  #Set the remaining budget as monthly budget, as there are no expenses yet

while True:
    print("################################### Welcome to Monthly Budget Tracker ###################################")
    print(f"1. Add Expense                          |  Your Monthly Budget is ${monthly_budget}")
    print("2. View Expenses                        |  ")
    print(f"3. Track Remaining Budget               |  Your Remaining Budget is ${remaining_budget}")
    print("4. Save the Expenses to a File          |")
    print("5. Exit                                 |")
    print("################################### Welcome to Monthly Budget Tracker ###################################")
    choice = input("Enter your choice: ")
    if choice == '1': #Add Expense Option so call the function to add expense
        expenses.append(add_expense()) #append the returned expense dictionary to the expenses list
        print("Expense added successfully.")
    elif choice == '2': #View Expenses Option so call the function to view expenses
        print("Here are your recorded expenses:")
        view_expenses(); #call the function to view expenses
    elif choice == '3': #Track Remaining Budget Option so call the function to track remaining budget
        pass
    elif choice == '4': #Save the Expenses to a File Option so call the function to save expenses to a file
        pass
    elif choice == '5': #Exit Option
        print("Thanks for using the Monthly Budget Tracker. Goodbye! Have a nice day!") #Exit message
        break
    else:
        print("Invalid choice. Please try again.") #Invalid choice handling

