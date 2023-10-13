import array
from parsing.DataParser import DataParser

mandatory_fields = ['Street', 'Zip', 'City', 'Last Check-In Date', 'Company']

data_parser = DataParser(mandatory_fields)
user_data = data_parser.parse_data("./data/data1.csv")

for row in user_data:
    print(row)