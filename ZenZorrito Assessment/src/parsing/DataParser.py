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
            
            #saving the header for better logging
            self.headers = data[0]
            
            #we don't need the header inside the data
            data.pop(0)  
            
            self.check_data_integrity(data)            
            return data
        

    def check_data_integrity(self, data):
        row_count = 1
        for row in data:
            if not row:
                print("Hola")
                continue
            
            for field in range(len(row)):
                if row[field] in (None, ""):
                    print('Row: ' + str(row_count) + ' Field: ' + self.headers[field] + ' empty')
            
            row_count += 1

                
                    
        