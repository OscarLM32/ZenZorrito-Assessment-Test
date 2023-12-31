
from datetime import datetime
import logging
import sys


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
        #this is supposedly handled by the parser, but you can never be to sure
        if data[6] in (None, ''):
            self.last_check_in_date = ''
        else:
            try:
                self.last_check_in_date = datetime.strptime(data[6], self.date_format)
            except:
                logging.error("The time date specified for user: " + self.first_name + " " + self.last_name + " is invalid.\n STOPPING PROGRAM")
                sys.exit(0)

        self.job = data[7]
        self.phone = data[8]
        self.company = data[9]
        
    def __str__(self):
        return '['+",".join(str(data) for data in self.data)+']'
    
        
            