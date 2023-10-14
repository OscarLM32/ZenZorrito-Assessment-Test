from tkinter import TRUE
from data_manipulation.DataManipulator import DataManipulator
from parsing.DataParser import DataParser
from os import listdir
from os.path import isfile, join

####Extra methods####
def set_app_quit(value):
    app_quit = value
#####################


mandatory_fields = ['Street', 'Zip', 'City', 'Last Check-In Date', 'Company']

data_file_path = './data/'
data_files = [f for f in listdir(data_file_path)]
                                 
parser = DataParser(mandatory_fields)

print("Select the dataset file you want to process:\n")
for i in range(len(data_files)):
    print(str(i) + ': ' + data_files[i])
    
selected_dataset = -1
selected_dataset_valid = False

selected_dataset = int(input("\nSelect dataset: "))

if selected_dataset < 0 or selected_dataset >= len(data_files):
    while not selected_dataset_valid:
        if selected_dataset < 0 or selected_dataset >= len(data_files):
            selected_dataset = int(input('\nInvalid dataset selection. Select another one: '))
        else:
            selected_dataset_valid = TRUE   
 
print("\nParsing and checking data integrity...")
dataset = parser.parse_data(data_file_path + data_files[selected_dataset])

#for row in dataset:
#   print(row)

manipulator = DataManipulator(dataset)
app_quit = False

selection_switch = { 1: str(manipulator.get_earliest_check_in_date_customer()), 
                     2: str(manipulator.get_latest_check_in_date_customer()),
                     3: manipulator.get_customer_names(),
                     4: manipulator.get_customer_companies(),
                     5: set_app_quit(True)
                   }

while not app_quit:
    selection = int(input('\nSelect an action: \n 1. Retrieve customer with the earliest check-in date \n 2. Retrieve customer with the latest check-in date \n 3. Retrieve the full name os customers alphabetically ordered \n 4. Retrieve customer\'s company names ordered alphabetically \n 5. Quit\n\n --> '))
    
    #requires python 3.10 or later
    '''match selection:
        case 1:
            manipulator.get_earliest_check_in_date_customer()
        case 2:
            manipulator.get_latest_check_in_date_customer()
        case 3:    
            manipulator.get_customer_names()
        case 4: 
            manipulator.get_customer_companies()
        case 5:
            app_quit = True
        case _:
            print('That is not a valid option\n')'''
            

    if selection == 1:
        print(manipulator.get_earliest_check_in_date_customer())    
    elif selection == 2:
        print(manipulator.get_latest_check_in_date_customer())
    elif selection == 3:
        print(manipulator.get_customer_names())
    elif selection == 4:
        print(manipulator.get_customer_companies())    
    elif selection == 5:
        app_quit = True    
    else:
        print("Invalid operation selected\n")    
            
print('See you next time\n')    
            

            
    