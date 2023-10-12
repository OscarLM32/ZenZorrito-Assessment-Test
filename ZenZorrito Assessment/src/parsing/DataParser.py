import csv
import logging
from parsing.UserData import UserData

class DataParser:
    
    def parse_data(self, file):
        data = self.read_csv(file)
        users = []
        for row in data:
            users.append(UserData(row))
        return users    
            
        
    def read_csv(self, file):
        #with -> try/catch and closes the file
        #I was having trouble with the encoding so I had to specifically define
        with open(file, 'r', encoding='utf_8') as csvfile:
            reader = csv.reader(csvfile)
            data = []
            
            #saving the header for better logging
            self.headers = reader.__next__()

            for row in reader:
                #strip removes leading and trailing whitespaces
                #this line can be read as: "if there are any values left after stripping all string values in the row
                if any(field.strip() for field in row):
                    data.append(row)
                else:
                    logging.warning("Empty line found")
            
            return self.check_data_integrity(data)            
        

    def check_data_integrity(self, data):
        final_data = []
        row_count = 1
        for row in data:
            if not all(row):
                logging.warning('The row ' + str(row_count) + ' contains empty values. DELETING ROW')
            else:
                final_data.append(row)
            row_count += 1
        
        return final_data


                
                    
        