
class UserData:

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
        self.job = data[6]
        self.phone = data[7]
        self.last_check_in_date = data[8]
        self.company = data[9]
        
    def __str__(self):
        return '['+",".join(str(data) for data in self.data)+']'
    
        
            