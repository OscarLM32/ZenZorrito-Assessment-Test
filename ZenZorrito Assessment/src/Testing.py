import array
from parsing.DataParser import DataParser


data_parser = DataParser()
user_data = data_parser.parse_data("./data/data1.csv")

for row in user_data:
    print(row)