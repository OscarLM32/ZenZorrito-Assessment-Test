import array
from data_manipulation.DataManipulator import DataManipulator
from parsing.DataParser import DataParser


data_parser = DataParser()
user_data = data_parser.parse_data("./data/data1.csv")

#for row in user_data:
    #print(row)

data_manipulator = DataManipulator(user_data)

print(data_manipulator.get_earliest_check_in_date_customer())
