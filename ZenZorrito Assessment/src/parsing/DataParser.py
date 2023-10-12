import csv
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
            for row in reader:
                data.append(row)
            #this first line inside data contains the header, which we dont care about    
            data.pop(0)        
            return data