import locale

class DataManipulator:
    
    def __init__(self, dataset):
        self.dataset = dataset
        self.earliest_check_in_user = None
        self.latest_check_in_user = None
        self.ordered_customer_full_names = None
        self.ordered_company_names = None
        

    def get_earliest_check_in_date_customer(self):
        if self.earliest_check_in_user:
            return self.earliest_check_in_user
        

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


        selected_customer = 0
        latest_date = self.dataset[selected_customer].last_check_in_date
            
        for i in range(1, len(self.dataset)):
            if self.dataset[i].last_check_in_date > latest_date:
                selected_customer = i
                latest_date = self.dataset[i].last_check_in_date
            
        self.latest_check_in_user = self.dataset[selected_customer]        
        return self.latest_check_in_user
    
    
    def get_customer_names(self):
        if self.ordered_customer_full_names:
            return self.ordered_customer_full_names
        

        full_names = []
        for row in self.dataset:
            full_names.append(row.first_name + " " + row.last_name)
        
        #make data more clear by removing unnecessary whitespaces that may have been introduced   
        for i in range(len(full_names)):
            full_names[i] = full_names[i].strip()

        full_names_sorted = self._sort_accent_sensitive(full_names)
        
        self.ordered_customer_full_names = full_names_sorted
        return self.ordered_customer_full_names


    def get_customer_companies(self):
        if self.ordered_company_names:
            return self.ordered_company_names
        

        company_names = []
        for user in self.dataset:
            if not user.company in company_names:
                company_names.append(user.company)
                
        company_names_sorted = self._sort_accent_sensitive(company_names)
        self.ordered_company_names = company_names_sorted
        return self.ordered_company_names
        

    def _sort_accent_sensitive(self, names):
        #I seet locale to accent insensitive locale
        locale.setlocale(locale.LC_COLLATE, 'en_US.UTF-8')
        # key locale.strxfrm sorts the array with keys in the selected locale that represent the real values and then
        # recover the real values
        sorted_names = sorted(names, key=locale.strxfrm)
        # Reset the locale to the default value so it does not conflict with anything else
        locale.setlocale(locale.LC_COLLATE, '')
            
        return sorted_names
            