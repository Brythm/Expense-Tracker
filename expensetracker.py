import numpy as np
import pandas as pd
from datetime import date

#Create Empty Lists
GOODS_OR_SERVICES = []
PRICES = []
DATES = []
EXPENSE_TYPES = []






#Create a function to add the expenses to the lists and organize the data
def add_expense(goods_or_services, price, date, expense_type):
    GOODS_OR_SERVICES.append(goods_or_services)
    PRICES.append(price)
    DATES.append(date)
    
    

#Main Program
option = -1 #This will be the users option, or choice, or input
while(option != 0):
    #Create the option menu
    print('Welcome to Shared Expense:')
    print('1. Add Food Expense')
    print('2. Add Household Expense')
    print('3. Add Transportation Expense')
    print('4. Show and Save your Shared Expense')
    print('0. Exit')
    option = int(input('Choose an option:\n'))

    #Print a new line
    print()
    #Check for the users choice or option or input
    if option == 0:
        print('Thank you for using Shared Expense!')
        break
    elif option == 1:
        print('Adding Food Expense:')
        expense_type = 'FOOD'
    elif option == 2:
        print('Adding Household Expense:')
        expense_type = 'Household'
    elif option == 3:
        print('Adding Transportation Expense:')
        expense_type = 'Transportation'
    elif option == 4:
        #Create a data frame and add the expenses
        expense_report = pd.DataFrame()
        expense_report['GOODS_OR_SERVICES'] = GOODS_OR_SERVICES
        expense_report['PRICES'] = PRICES
        expense_report['DATES'] = DATES
        #Save the expense report
        expense_report.to_csv('SharedExpense.csv')
        #Show the expense Report
        print(expense_report)
    else:
        print('You chose an invalid option, please choose between 0-4')

        #Allow the user to enter the good or service and the price
    if option == 1 or option == 2 or option == 3:
        good_or_service = input('Enter the good or service for the expense type '+expense_type+':\n')
        price = float(input('Enter the price of the good or service:\n'))
        today = date.today()
        add_expense(good_or_service, price, today, expense_type,)
        

#Print a new line for formatting

    print()
    
    
