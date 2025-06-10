init = True
selUSD = 4020
buyUSD = 4030
def save_to_history(log_entry: str, filename: str = "history.log"):
    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(log_entry + "\n")
    except Exception as e:
        print(f"Error writing to log file: {e}")
    
def Finan():
    user_Input = int(input('0. Back to Main Menu\n1. Calculat Simple Interest\n2. Convert Currency(USD<->Riel)'))
    if user_Input == 0:
        Main_menu()
    elif user_Input == 1:
        print('Calculate Simple Interest')
    elif user_Input == 2:
        print(f'Convert Currency USD=>Riel\nUSD=>Riel = {selUSD}KHR')
        tmp = int(input('Enter USD :'))
        print(f'Converted {tmp} => {tmp * selUSD}')
    elif user_Input == 3:
        print(f'Convert Currency Riel=>USD\nRiel=>USD = {buyUSD}KHR')
        tmp = int(input('Enter Riel :'))
        print(f'Converted {tmp} => {tmp * buyUSD}')
    else:
        print('invalid Input!!!')
        
def List_op():
    user_Input = int(input('0. Back to Main Menu\n1. Append to List\n2. Insert into List\n3. Slice List\n4. Access Item by index'))
    if user_Input == 0:
        Main_menu()
    elif user_Input == 1:
        print('Append to List')
    elif user_Input == 2:
        print('Insert into List')
    elif user_Input == 3:
        print('Access Item by Index')
    else:
        print('Invalid input!!!')
   
def Loop_ex():
    user_Input = int(input('0. Back to Main Menu\n1. One-Dimensional Loop\n2. Two-Dimensional Loop\n3. Condition-Based Loop'))
    if user_Input == 0:
        Main_menu()
    elif user_Input == 1:
        print('One-Dimensional')
    elif user_Input == 2:
        print('Two-Dimensional')
    elif user_Input == 3:
        print('Condition-Based Loop')
    else:
        print('invalid input!!!')
        
def Main_menu():
    user_Input = int(input('1. Financial Calculation\n2. List Operations\n3. Loop Examples\n4. Exit'))
    if user_Input == 1:
        Finan()
    elif user_Input == 2:
        List_op()
    elif user_Input == 3:
        Loop_ex()
    else:
        print("invalid Input!!!")
    
while(init):
    Main_menu()

