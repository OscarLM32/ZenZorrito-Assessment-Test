import array
from data_manipulation.DataManipulator import DataManipulator
from parsing.DataParser import DataParser

mandatory_fields = ['Street', 'Zip', 'City', 'Last Check-In Date', 'Company']

data_parser = DataParser(mandatory_fields)
user_data = data_parser.parse_data("./data/data1.csv")

for row in user_data:
    print(row)
print('\n')

data_manipulator = DataManipulator(user_data)

print(data_manipulator.get_earliest_check_in_date_customer())
print(data_manipulator.get_latest_check_in_date_customer())

print(data_manipulator.get_customer_names())
print(data_manipulator.get_customer_companies())