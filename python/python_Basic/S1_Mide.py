import os
from datetime import datetime

def Menu():
    while True:
        print('===== Main Menu =====')
        print('1. Financial Operation')
        print('2. Tuple Operations')
        print('3. Conditional Statements')
        print('0. Exit')

        user_Input = input("Enter choice: ")

        if user_Input == '1': 
            Logs('Enter choice: 1. Financial Operation')
            Finan()
        elif user_Input == '2':
            Logs('Enter choice: 2. Tuple Operations')
            Tuple_OP()
        elif user_Input == '3':
            Logs('Enter choice: 3. Conditional Statements')
            Condit_Stat()
        elif user_Input == '0':
            Logs('User exited the program.')
            break
        else:
            Logs(f'User input: {user_Input} - Invalid input!')
            print('Invalid input!')

def Finan():
    while True:
        print('===== Financial Operations =====')
        print('0. Back to Main Menu')
        print('1. Calculate Inflation Rate')
        print('2. Calculate Total Equity')
        print('3. Calculate Annual Growth Rate')

        user_Input = input('Enter choice: ')

        if user_Input == '0':
            Logs('Choice: 0. Back to Main Menu')
            return
        elif user_Input == '1': 
            Logs('Choice: 1. Calculate Inflation Rate')
            initCPI = float(input("Enter Initial CPI: "))
            finCPI = float(input("Enter Final CPI: "))
            inflationRate = ((finCPI - initCPI) / initCPI) * 100
            print('Inflation Rate:', inflationRate)
            Logs(f'Initial CPI: {initCPI}, Final CPI: {finCPI}, Inflation Rate: {inflationRate}\n')
        elif user_Input == '2':
            Logs('Choice: 2. Calculate Total Equity')
            total_Asset = float(input("Enter Total Asset: "))
            total_Lia = float(input("Enter Total Liabilities: "))
            total_Equity = total_Asset - total_Lia
            print('Total Equity:', total_Equity)
            Logs(f'Total Asset: {total_Asset}, Total Liabilities: {total_Lia}, Total Equity: {total_Equity}\n')
        elif user_Input == '3':
            Logs('Choice: 3. Calculate Annual Growth Rate')
            initVal = float(input("Enter Initial Value: "))
            finVal = float(input("Enter Final Value: "))
            numOfYear = int(input("Enter Number of Years: "))
            annualGrowthRate = ((finVal - initVal) / initVal) * 100
            print('Annual Growth Rate:', annualGrowthRate)
            Logs(f'Initial Value: {initVal}, Final Value: {finVal}, Number of Years: {numOfYear}, Annual Growth Rate: {annualGrowthRate}\n')
        else:
            Logs(f'User input: {user_Input} - Invalid input!')
            print('Invalid input!')

def Tuple_OP():
    while True:
        print('===== Tuple Operations =====')
        print('0. Back to Main Menu')
        print('1. Unpack Tuple Elements')
        print('2. Create a Nested Tuple')
        print('3. Access Elements of a Nested Tuple')

        user_Input = input('Enter choice: ')

        if user_Input == '0':
            Logs('Choice: 0. Back to Main Menu')
            return
        elif user_Input == '1': 
            Logs('Choice: 1. Unpack Tuple Elements')
            my_Tuple = (10, 20, 30)
            x, y, z = my_Tuple
            print(f"x = {x}, y = {y}, z = {z}\n")
        elif user_Input == '2':
            Logs('Choice: 2. Create a Nested Tuple')
            my_Tuple = ((1, 2, 3), (4, 5, 6))
            print(my_Tuple,"\n")
        elif user_Input == '3':
            Logs('Choice: 3. Access Elements of a Nested Tuple')
            nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
            outer_Index = int(input("Enter index of outer tuple: "))
            inner_Index = int(input("Enter index of inner tuple: "))

            try:
                value = nested_tuple[outer_Index][inner_Index]
                print(f"Value at specified index: {value}\n")
                Logs(f"User accessed tuple value: {value}")
            except IndexError:
                print("Invalid index!")
                Logs(f"User entered invalid indexes: {outer_Index}, {inner_Index}")
        else:
            Logs(f'User input: {user_Input} - Invalid input!')
            print('Invalid input!')

def Condit_Stat():
    while True:
        print('===== Conditional Statements =====')
        print('0. Back to Main Menu')
        print('1. Determine Day of the Week')
        print('2. Check Password Strength')
        print('3. Simple Calculator')

        user_Input = input('Enter choice: ')

        if user_Input == '0':
            Logs('Choice: 0. Back to Main Menu')
            return
        elif user_Input == '1': 
            Logs('Choice: 1. Determine Day of the Week')
            days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            num = int(input("Enter a number (1-7): "))
            if 1 <= num <= 7:
                print(f"Day of the Week: {days_of_week[num - 1]}\n")
                Logs(f"User selected day: {days_of_week[num - 1]}")
            else:
                print("Invalid input!\n")
                Logs(f"User entered invalid number: {num}")
        elif user_Input == '2':
            Logs('Choice: 2. Check Password Strength')
            password = input("Enter a password: ")
            if any(char.isalpha() for char in password) and any(char.isdigit() for char in password):
                print("Password is Strong!\n")
                Logs("User entered a strong password.")
            else:
                print("Password is Weak! (Use letters and numbers.)\n")
                Logs("User entered a weak password.")
        elif user_Input == '3':
            Logs('Choice: 3. Simple Calculator')
            first_num = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ")
            second_num = float(input("Enter second number: "))

            if operator == "+":
                result = first_num + second_num
            elif operator == "-":
                result = first_num - second_num
            elif operator == "*":
                result = first_num * second_num
            elif operator == "/":
                if second_num != 0:
                    result = first_num / second_num
                else:
                    print("Error: Division by zero is not allowed!")
                    Logs("Error: Division by zero is not allowed!")
                    return
            else:
                print("Invalid operator!")
                Logs("Invalid operator!")
                return

            print("Result:", result)
            Logs(f"first number: {first_num} - operator : {operator} - second number: {second_num} - result : {result}")
        else:
                    Logs(f'User input: {user_Input} - Invalid input! ')
                    print('Invalid input!\n')

def Logs(info):
    now = datetime.now()
    current_Datetime = now.strftime("%Y-%m-%d %H:%M:%S")
    file_Name = "logs.txt"

    with open(file_Name, "a") as file:
        file.write(f"{current_Datetime} - {info}\n")
    file.close()

Menu()
