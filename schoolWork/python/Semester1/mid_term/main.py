import os
from datetime import datetime
def Menu():
    print('===== Main Meny =====')
    print('1. Financial Operation')
    print('2. Tuple Operations')
    print('3. Coditional Statements')
    print('0. Exit')
    user_Input = int(input("Enter choice : "))
    while True:
        if user_Input == 1 : 
            Logs('Enter choice : 1. Financial Operation')
            Finan()
        elif user_Input == 2:
            Logs('Enter choice : 2. Tuple Operations')
            Tuple_OP()
        elif user_Input == 3:
            Logs('Enter choice : 3. Coditional Statements')
            Condit_Stat()
        else:
            print('invalid input !!!')


def Finan():
    print('0. Back to Main Menu')
    print('1. Calculate Inflation Rate')
    print('2. Calculate Total Equity')
    print('3. Calcuate Annual Growth Rate')
    user_Input = int(input('Enter choice : '))
    while True:
        if user_Input == 0:
            Logs('choice : 0. Back to Main Menu')
            Menu()
        elif user_Input == 1 : 
            Logs('choice : 1. Calculate Inflation Rate')
            initCPI = int(input("Enter Initial CPI : "))
            finCPI = int(input("Enter Final CPI : "))
            inflationRate = ((finCPI-initCPI)/initCPI)*100
            print('Inflation Rate : ',inflationRate)
            Logs(f'Initial CPI : {initCPI} - Final CPI : {finCPI} - Inflation Rate : {inflationRate}')
        elif user_Input == 2:
            Logs('2. Calculate Total Equity')
            total_Asset = int(input("Enter Total Asset : "))
            total_Lia = int(input("Enter Total Liabilities : "))
            total_Equity = total_Asset - total_Lia
            print('Total Equity : ',total_Equity)
            Logs(f'Total Asset : {total_Asset} - Total Liabilities : {total_Lia} - Total Equity : {total_Equity}')
        elif user_Input == 3:
            Logs('3. Calcuate Annual Growth Rate')
            initVal = int(input("Enter Initial Value : "))
            finVal = int(input("Enter Final Value : "))
            numOfYear = int(input("Enter Number of Years : "))
            annualGrowthRate = ((finVal - initVal)/initVal)*100
            print('Annual Growth Rate',annualGrowthRate)
            Logs(f'Initial Value : {initVal} - Final Value : {finVal} - Number of Years : {numOfYear} - Annual Growth Rate : {annualGrowthRate}')
        else:
            Logs(f'User input : {user_Input} - invalid input !!!')
            print('invalid input !!!')

def Tuple_OP():
    print('0. Back to Main Menu')
    print('1. Unpack Tuple Elements')
    print('2. Create a Nested Tuple')
    print('3. Access Elements of a Nested Tuple')
    user_Input = int(input('Enter choice : '))
    while True:
        if user_Input == 0:
            Logs('choice : 0. Back to Main Menu')
            Menu()
        elif user_Input == 1 : 
            me_Tuple = (10, 20, 30)
            x, y, z = me_Tuple
            print(f"x = {x}, y = {y}, z = {z}")
        elif user_Input == 2:
            me_Tuple = ((1,2,3),(4,5,6))
            print(me_Tuple)
        elif user_Input == 3:
            nested_tuple = (
             (1, 2, 3),
             (4, 5, 6),
             (7, 8, 9)
            )
            outer_Index = int(input("Enter index of outer tuple: "))
            inner_Index = int(input("Enter index of inner tuple: "))
            try:
                value = nested_tuple[outer_Index][inner_Index]
                print(f"Value at specified index: {value}")
            except IndexError:
                print("Invalid index!!!")
            else:
                print('invalid input !!!')
    

def Condit_Stat():
    print('0. Back to Main Menu')
    print('1. Determine Day of the Week')
    print('2. Check Password Strength')
    print('3. Simple Calculator')
    user_Input = int(input('Enter choice : '))
    while True:
        if user_Input == 0:
            Menu()
        elif user_Input == 1 : 
            DOW = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            num = int(input("Enter a number (1-7) : "))
            if 1 <= num <= 7:
                print(f"Day of the Week: {DOW[num - 1]}")
            else:
                print("Invalid input!!!")
        elif user_Input == 2:
            passWord = input("Enter a password: ")
            if any(char.isalpha() for char in passWord) and any(char.isdigit() for char in passWord):
                print("Password is Strong!")
            else:
                print("Password is Weak! (Use letter and number.)")
        elif user_Input == 3:
            Condit_Stat()
        else:
            print('invalid input !!!')

def Logs(info):
    
    now = datetime.now()
    current_Datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    file_Name = "logs.txt"
    if not os.path.exists(file_Name):
        with open(file_Name, "w") as file:
            file.write(f"{current_Datetime}{info}\n")
        print(f"{file_Name} created.")
    else:
        with open(file_Name, "r") as file:
            content = file.read()
            print(f"{file_Name} exists. Content:\n{content}")
              
Menu()