
class DataManipulator:
    
    def __init__(self, dataset):
        self.dataset = dataset
        self.earliest_check_in_user = None
        self.latest_check_in_user = None
        

    def get_earliest_check_in_date_customer(self):
        if self.earliest_check_in_user:
            return self.earliest_check_in_user
        else:
            selected_customer = 0
            earliest_date = self.dataset[selected_customer].last_check_in_date
            
            for i in range(1, len(self.dataset)):
                if self.dataset[i].last_check_in_date < earliest_date:
                    selected_customer = i
                    earliest_date = self.dataset[i].last_check_in_date
            
            self.earliest_check_in_user = self.dataset[selected_customer]        
            return self.earliest_check_in_user
    

    def get_latest_check_in_date_customer(self):
        if self.latest_check_in_user:
            return self.latest_check_in_user
        else:
            selected_customer = 0
            latest_date = self.dataset[selected_customer].last_check_in_date
            
            for i in range(1, len(self.dataset)):
                if self.dataset[i].last_check_in_date > latest_date:
                    selected_customer = i
                    latest_date = self.dataset[i].last_check_in_date
            
            self.latest_check_in_user = self.dataset[selected_customer]        
            return self.latest_check_in_user
    
    
    def get_customer_names(self):
        pass
    

    def get_customer_companies(self):
        pass