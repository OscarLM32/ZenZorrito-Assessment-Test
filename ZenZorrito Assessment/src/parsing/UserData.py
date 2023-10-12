
from datetime import datetime


class UserData:
    date_format = '%d/%m/%Y'
    #Constructors in Python remsemble to those in Ruby. I createthe attributes inside the constructor. If an attribute is
    #declared outside the constructor it will be the same as 'static' in C        
    def __init__(self, data):
        self.data = data        

        self.first_name = data[0]
        self.last_name = data[1]
        self.street = data[2]
        self.zip_code = data[3]
        self.city = data[4]
        self.user_type = data[5]

        #need to check if the field is empty in order for the program not to "crash"
        if data[6] in (None, ''):
            self.last_check_in_date = ''
        else:
            self.last_check_in_date = datetime.strptime(data[6], self.date_format)
            print(self.last_check_in_date)

        self.job = data[7]
        self.phone = data[8]
        self.company = data[9]
        
    def __str__(self):
        return '['+",".join(str(data) for data in self.data)+']'
    
        
            