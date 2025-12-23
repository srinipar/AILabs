####### Monthly Budget Tracker #######,  SRINIVASAN PARAMASIVAM, 20-Dec-2025 #######
import os
import pandas as pd

expenses = []  # List to store expenses
fileName_Budget = 'budget.txt'  # File to store budget information
fileName_Expenses = 'expenses.csv'  # File to store expenses information
def get_monthly_budget():
    '''This is function to get the monthly budget from the file'''
    #Check for Budget file existence
    if os.path.exists(fileName_Budget):
        file_Budget=open(fileName_Budget, 'r')  #Open the Budget file in read mode
        local_monthly_budget = float(file_Budget.read())  #Read the budget amount from the file
        file_Budget.close()  #Close the Budget file
        return local_monthly_budget
    else:
        input_budget = float(input("**** Your Monthly Budget is not sent, hence please enter your monthly budget amount: ₹"))  #Get the input from user to set the budget
        local_monthly_budget = input_budget #Set the monthly budget
        file_Budget=open(fileName_Budget, 'w')  #Open the Budget file in write mode
        file_Budget.write(str(local_monthly_budget))  #Write the budget amount to the file
        file_Budget.close()  #Close the Budget file
        return local_monthly_budget 
    

if os.path.exists(fileName_Expenses):#check for Expenses file existence
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
    
    file_Expenses.close()  #Close the Expenses file
 
#Function to add the expense
def add_expense()->bool :
    '''This is function to add the expenses. It will get Date of Expenses (YYYY-MM-DD), 
    Category of the Expenses, Amount Spent and breif Description of the Expenses from the user'''
 
    #get the consumed budget
    addexp_consumed_budget = calculate_consumed_amount()
    addexp_monthly_budget=get_monthly_budget()  #Get the monthly budget
    if(addexp_consumed_budget >= addexp_monthly_budget):
        print(f"WARNING : You have already exceeded your monthly budget of ₹{addexp_monthly_budget} !!!!")
    else:
        print(f"INFO : You have consumed ₹{addexp_consumed_budget} out of your monthly budget of ₹{addexp_monthly_budget}. You can spend up to ₹{addexp_monthly_budget - addexp_consumed_budget} more this month.")

    date = input("Enter the date of the expense (YYYY-MM-DD): ")
    #Validation of date format can be added here
    if not date or date.strip() == "" or len(date) != 10 or date[4] != '-' or date[7] != '-' or  not (date[:4]).isdigit()  or not (date[5:7]).isdigit() or not (date[8:]).isdigit(): #validate the input date format
        print("ERROR : Date should be in YYYY-MM-DD format. Please try again.")
        return False

    if(int(date[5:7]) < 1 or int(date[5:7]) > 12 or int(date[8:]) < 1 or int(date[8:]) > 31): #validate the month and day values of the expense date
        print("ERROR : Month should be between 01 and 12 and Day should be between 01 and 31. Please try again.")
        return False

    category = input("Enter the category of the expense (e.g., Food, Transport, Utilities): ")
    if not category or category.strip() == "": #validate the  category
        print("ERROR : Category cannot be empty. Please try again.")
        return False
    
    amount = float(input("Enter the amount spent: ₹"))
    if amount <= 0: #validate the amount
        print("ERROR : Expenses amount should be a positive number. Please try again.")
        return False
    
    description = input("Enter a brief description of the expense: ")
    if not description or description.strip() == "": #validate the description
        print("ERROR : Description cannot be empty. Please try again.")
        return False
    
    #All inputs are validated hence return the expense as a dictionary
    expenses.append({
        'expense_date': date,
        'expense_category': category,
        'expense_amount': amount,
        'expense_description': description
    }) #append the returned expense dictionary to the expenses list
    return   True

#Function to view the expenses
def view_expenses():
    '''This is function to view the expenses recorded by the user'''
    if not expenses:
        print("ERROR : You havent added any expenses yet. Please add some expenses using option 1.")
        return
    
    pd_expenses = pd.DataFrame(expenses)  #load expenses list to pandas DataFrame
    print(pd_expenses)  #Print the expenses DataFrame2
         

#Function to read the Consumed Amount from the expenses list
def calculate_consumed_amount():
    '''This is function to calculate the total consumed amount from the expenses list'''
    consumed_amount = 0.0  #Variable to store the total consumed amount
    for expense in expenses:
        consumed_amount += float(expense['expense_amount'] ) #Add the consumed amount
    return consumed_amount

#function to save the expenses to a file
def save_expenses_to_file():
    '''This is function to save the expenses to a file'''
    if not expenses: #means expenses list is empty
        print("ERROR : You havent added any expenses yet. Please add some expenses using option 1.")
        return
    else:
        print(f"INFO : Saving {len(expenses)} expenses to the file {fileName_Expenses}...")
        file_Expenses=open(fileName_Expenses, 'w')  #Open the Expenses file in write mode
        for expense in expenses:
            line = f"{expense['expense_date']},{expense['expense_category']},{expense['expense_amount']},{expense['expense_description']}\n"
            file_Expenses.write(line)  #Write the expense to the file
        print("Expenses saved successfully to the file.")
        file_Expenses.close()  #Close the Expenses file

#function to track remaining budget
def track_remaining_budget():
    '''This is function to track the remaining budget'''
    print(f"You monthly budget is ₹{get_monthly_budget()}")  #Print the monthly budget
    track_consumed_amount = calculate_consumed_amount()  #Get the consumed amount
    track_remaining_budget = get_monthly_budget() - track_consumed_amount  #Calculate the remaining budget
    print(f"Your Remaining Budget is ₹{track_remaining_budget}")
    choice=input("Press 1 to modify the monthly budget or any other key to return to main menu: ")
    if choice == '1':
        new_budget = float(input("Enter the new monthly budget amount: ₹"))
        if new_budget <= 0: #validate the new budget
            print("ERROR : Monthly budget should be a positive number. Please try again.")
            return
        if new_budget < track_consumed_amount:
            print(f"ERROR : New monthly budget ₹{new_budget} cannot be less than the already consumed amount ₹{track_consumed_amount}. Please try again.")
            return
        
        file_Budget=open(fileName_Budget, 'w')  #Open the Budget file in write mode
        file_Budget.write(str(new_budget))  #Write the new budget amount to the file
        file_Budget.close()  #Close the Budget file 
        print(f"INFO : Monthly budget updated successfully to ₹{get_monthly_budget()}.")
        
 
while True:
    print("################################### Welcome to Monthly Budget Tracker ###################################")
    print(f"1. Add Expense                         |")
    print(f"2. View Expenses                       |  Your Monthly Budget is ₹{get_monthly_budget()}  ")
    print(f"3. Track Remaining Budget              |")
    print(f"4. Save the Expenses to a File         |  Your Remaining Budget is ₹{get_monthly_budget() - calculate_consumed_amount()}")
    print(f"5. Exit                                |")
    print("################################### Welcome to Monthly Budget Tracker ###################################")
    choice = input("Enter your choice: ")
    if choice == '1': #Add Expense Option so call the function to add expense
        if(add_expense()): #call the function to add expense
            save_expenses_to_file() #save the expenses to file after adding new expense
            print("Expense added successfully.")
    elif choice == '2': #View Expenses Option so call the function to view expenses
        print("Here are your recorded expenses:")
        view_expenses(); #call the function to view expenses 
    elif choice == '3': #Track Remaining Budget Option so call the function to track remaining budget
        track_remaining_budget(); #call the function to track remaining budget
    elif choice == '4': #Save the Expenses to a File Option so call the function to save expenses to a file
        save_expenses_to_file(); #call the function to save expenses to a file
        #print("Expenses saved successfully to the file.")
    elif choice == '5': #Exit Option
        print("Thanks for using the Monthly Budget Tracker. Goodbye! Have a nice day!") #Exit message
        break
    else:
        print("Invalid choice. Please try again.") #Invalid choice handling