import csv
from enum import Flag
import logging
from parsing.UserData import UserData

class DataParser:
    
    def __init__(self, mandatory_fields = []):
        self.mandatory_fields = mandatory_fields
        

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
            
            #saving the header for better logging and exception handling
            self.headers = reader.__next__()
            self._get_mandatory_field_columns()

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
        data_missing = False        

        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] in (None, '') and j in self.mandatory_fields_index:
                    data_missing = True
                    logging.warning('The row ' + str(row_count) + ' contains invalid ' + self.headers[j].upper() + ' value. DELETING ROW')
                    
            if not data_missing:
                final_data.append(data[i])
            row_count += 1
            data_missing = False
        
        return final_data
    

    #gets the index in the header of the required values in data
    def _get_mandatory_field_columns(self):
        self.mandatory_fields_index = []
        for i in range(len(self.headers)):
            if self.headers[i] in self.mandatory_fields:
                self.mandatory_fields_index.append(i)
        #print(self.mandatory_fields_index)        
        


                
                    
        